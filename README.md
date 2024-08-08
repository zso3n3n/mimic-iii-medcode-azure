# Medical Coding with Language Models

### Data

Data for this analysis is from the semi-open [MIMIC-III Clinical Dataset](https://physionet.org/content/mimiciii/1.4/). **The data is not permenantly stored in this repository.** To access the data, follow the steps on the linked website and complete the necessary trainings. This data is for research purposes only.

To run the repository code download the data to a data/ in the home directory. The following files are used:
- D_ICD_DIAGNOSES.csv.gz
- DIAGNOSES_ICD.csv.gz
- DRGCODES.csv.gz
- NOTEEVENTS.csv.gz

### Approach

The approach is the leverage small language model(s) to traverse a heirarchy of ICD-9 codes and ask many small questions to classify a Note Event from the MIMI-III dataset.

For example, the image below is a representation of a small portion of the ICD9 code tree. The branch in the picture below shows a subset of the 'Infectious and Parasitic Disease' Chapter of the ICD9 code tree. [View a full json representation of the taxonomy here.](./icd9_full.json)  
  
The coding algorithm recursively walks the tree, starting at the top level and continuing down any branch(es) directed by the mini model until the final codes is returned.

0        Infectious and Parasitic Diseases  
├── 00   Intestinal infectious diseases  
│   ├── 001 Cholera  
│   ├── 002 Typhoid and paratyphoid fevers  
│   ├── 003 Salmonella  
│   ├── 004 Shigellosis  
│   ├── 005 Other poisoning (bacterial)  
│   ├── 006 Amebiasis  
│   ├── 007 Other protozoal intestinal diseases  
│   ├── 008 Intestinal infections due to other organisms  
│   └── 009 Ill-defined intestinal infections  
├── 01   Tuberculosis  
│   ├── 010 Primary tuberculous infection  
│   ├── 011 Pulmonary tuberculosis  
│   ├── 012 Other respiratory tuberculosis  
│   ├── 013 Tuberculosis of meninges and central nervous system  
│   ├── 014 Tuberculosis of intestines, peritoneum, and mesenteric glands  
│   ├── 015 Tuberculosis of bones and joints  
│   ├── 016 Tuberculosis of genitourinary system  
│   ├── 017 Tuberculosis of other organs  
│   ├── 018 Miliary tuberculosis  
│   └── 019 Respiratory tuberculosis unspecified  
...  
├── 09   Rickettsioses and other arthropod-borne diseases  
│   ├── ...   
│   ├── 087 Relapsing fever  
│   └── 088 Other arthropod-borne diseases   

  
### Results

