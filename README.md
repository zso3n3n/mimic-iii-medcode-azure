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

For example, the image below is a representation of a small portion of the ICD9 code tree. The branch pictured shows codes 001 - 009 which are contained under the 00-Intestinal Infection Disease sub-category. Furthermore, the 00 category can be contained under 'Chapter 1' (Infectious and Parasitic Diseases). [View a full json representation of the taxonomy here.](./icd9_full.json)

![alt text](images/image.png)  
  

### Results

