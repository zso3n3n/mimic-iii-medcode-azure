# Medical Coding with AI

This repository provides a comprehensive survey and implementation of various AI techniques for to medical coding — a crucial task in healthcare for translating clinical documentation into standardized codes used for billing, treatment tracking, and medical research.


---
### 📒 Notebooks

┣ **00 EDA** - Get familiar with the MIMIC-III / ICD9 dataset. Explore the challenges with AI based medical coding via the MIMIC-III dataset  
┣  **01 Azure Text Analytics for Health**  - Parse medical notes into medical concepts. Supplement medical concepts with synonyms and definitions  
┣  **02 LLM Extraction**  - Use an LLM to extract _only_ the relevant components of a medical note  
┣  **03 Heirarchical Medical Coding** - Model ICD9 codes as a tree to limit the code label space. Use an SLM (small language model) to do many small classifications recursively  
┣  **04 Fine-Tuning** - Prepare a dataset for supervised fine-tuning. Fine-tune a GPT model for multi-label medical coding    

---
### ⚕️ Data
Data for this analysis is from the semi-open [MIMIC-III Clinical Dataset](https://physionet.org/content/mimiciii/1.4/). **The data is not permenantly stored in this repository.** To access the data, follow the steps on the linked website and complete the necessary trainings. This data is for research purposes only.

To run the repository code download the data to a data/ in the home directory. The following files are used:
<small>
- D_ICD_DIAGNOSES.csv.gz
- DIAGNOSES_ICD.csv.gz
- DRGCODES.csv.gz
- NOTEEVENTS.csv.gz
</small>  

Once you have accessed the MIMIC-III data set, prepare the data using the [prepare_mimic_iii.py](./src/prepare_mimic_iii.py) script provided in this repo.   
  
The ICD9 Code heirarchy is represented in the [icd9_codes_full.json](./icd9_codes_full.json) file. This file is permenantly stored in the repo.  

---
### 🔧 Setup
To run this repository, follow the steps below to setup dependencies and environment variables.

1. Follow the steps in the above "Data" section to get access to the MIMIC-III dataset.

2. Follow the steps linked here to get access to the [UMLS API](https://documentation.uts.nlm.nih.gov/rest/home.html)

3. Setup the required resources in Azure:
    - [Azure Open AI Resource](https://azure.microsoft.com/en-us/products/ai-services/openai-service?msockid=359b98bc5ab160c83b508c325bd061fd)
    - [Azure AI Language Resource](https://azure.microsoft.com/en-us/products/ai-services/ai-language?msockid=359b98bc5ab160c83b508c325bd061fd)

4. Setup conda virtual environment
    ```bash
    conda env create --file=./conda.yml
    conda activate med_code 
    ```

5. Create a .env file, and populate according to the [.env.sample](.env.sample) example provided.

    ```bash
    AZURE_OPENAI_BASE=your-endpoint
    AZURE_OPENAI_KEY=your-key
    AOAI_MINI_DEPLOYMENT_NAME=gpt-4o-mini-deployment-name
    AOAI_MAIN_DEPLOYMENT_NAME=gpt-4o-deployment-name
    LANGUAGE_KEY=your-key
    LANGUAGE_ENDPOINT=your-endpoint
    UMLS_API_KEY=your-key
    ```

