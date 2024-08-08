import pandas as pd
import re
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def remove_evm_codes(df: pd.DataFrame) -> pd.DataFrame:
    # Drop E, V, and M codes
    df['ICD9_CODE'] = df['ICD9_CODE'].apply(lambda x: str(x))
    output = df[~df['ICD9_CODE'].str.startswith("E")]
    output = output[~output['ICD9_CODE'].str.startswith("V")]   
    output = output[~output['ICD9_CODE'].str.startswith("M")]
    return output

# TODO
def clean_note_text(text: str) -> str:
    # Remove newline characters
    text = text.strip()
    text = text.replace('\n', '').replace('\"','')
    text = text.replace('[','').replace(']','').replace('{','').replace('}','').replace('*','')
    text = text.replace(',','').replace(';','').replace('/','').replace('\\','').replace('(','').replace(')','')
    text = re.sub('\s+',' ', text)

    return text

def transform_data(data_folder: str, subset:float = 1) -> None:
    
    
    max_notes = 1
    max_icd_class = 279
    logger.info(f"Data Parameters:\n max_notes: {max_notes}\n max_icd9_class: {max_icd_class}")

    # Read in data
    # drg = pd.read_csv(data_folder + 'DRGCODES.csv.gz')
    # d_icd = pd.read_csv(data_folder + 'D_ICD_DIAGNOSES.csv.gz')
    diagnoses = pd.read_csv(data_folder + 'raw/DIAGNOSES_ICD.csv.gz', usecols=['HADM_ID', 'ICD9_CODE'], dtype={'ICD9_CODE':str, 'HADM_ID':'Int64'})
    diagnoses = diagnoses[diagnoses['ICD9_CODE'].notna()]
    
    # Get NOTEEVENTS for HADM_IDs with only <max_notes>
    note_events = pd.DataFrame()
    logger.info("Reading in NOTEEVENTS.csv.gz")
    for reader in pd.read_csv(data_folder + 'raw/NOTEEVENTS.csv.gz', usecols=['HADM_ID','TEXT'], dtype={'text':str,'HADM_ID':'Int64'}, chunksize=400000):
        # Get HADM_IDs with only one note
        sub_df = reader[reader['HADM_ID'].map(reader['HADM_ID'].value_counts()) <= max_notes]
        note_events = pd.concat([note_events, sub_df])
        sub_df.iloc[0:0]
        reader.iloc[0:0]


    note_events = note_events[note_events['HADM_ID'].map(note_events['HADM_ID'].value_counts()) <= max_notes]

    # Drop codes that start with E, V, and M
    diagnoses = remove_evm_codes(diagnoses)

    # Shorten codes to 3 digits (for now)
    diagnoses['ICD9_CODE'] = diagnoses['ICD9_CODE'].str.slice(0, 3)

    # Convert code column to int
    diagnoses['ICD9_CODE'] = diagnoses['ICD9_CODE'].apply(lambda x: int(x))

    # Start with just the 001-279 classes
    diagnoses = diagnoses[diagnoses['ICD9_CODE'] <= max_icd_class]

    # Clean Note Text
    logger.info("Cleaning note text")
    note_events['TEXT'] = note_events['TEXT'].apply(clean_note_text) # TODO - improve

    # Join datasets
    logger.info("Joining datasets")
    joined = note_events.join(diagnoses.set_index("HADM_ID"), on=['HADM_ID'], how='inner').groupby(['HADM_ID']).agg(tuple).map(set).map(list).reset_index()

    # write dataframe
    output_path = "joined/dataset_single_001_279.csv.gz"
    joined.to_csv(data_folder + 'joined/dataset_single_001_279.csv.gz', index=False, compression='gzip')
    logger.info(f"Write dataframe to {data_folder + output_path}")

    return joined


if __name__ == "__main__":
    df = transform_data('/home/zacksoenen/Projects/mimic-iii-medcode-azure/data/')
    print(df.head(10))
    print(df.shape)