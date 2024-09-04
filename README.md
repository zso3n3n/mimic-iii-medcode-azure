# Medical Coding with AI

Overview here

### 📒 Notebooks
---
┣  **00 EDA**   
- Get familiar with the MIMIC-III / ICD9 dataset
- Explore the challenges with AI based medical coding via the MIMIC-III dataset

┣  **01 Azure Text Analytics for Health** 
- Parse medical notes into medical concepts
- Supplement medical concepts with synonyms and definitions

┣  **02 LLM Extraction**  
- Use an LLM to extract _only_ the relevant components of a medical note  

┣  **03 Heirarchical Medical Coding**
- Model ICD9 codes as a tree to limit the code label space  
- Use an SLM (small language model) to do many small classifications recursively 
   
┣  **04 Fine-Tuning**
- Prepare a dataset for supervised fine-tuning
- Fine-tune a GPT model for multi-label medical coding    

### ⚕️ Data
---
Data for this analysis is from the semi-open [MIMIC-III Clinical Dataset](https://physionet.org/content/mimiciii/1.4/). **The data is not permenantly stored in this repository.** To access the data, follow the steps on the linked website and complete the necessary trainings. This data is for research purposes only.

To run the repository code download the data to a data/ in the home directory. The following files are used:
```
- D_ICD_DIAGNOSES.csv.gz
- DIAGNOSES_ICD.csv.gz
- DRGCODES.csv.gz
- NOTEEVENTS.csv.gz
```

### 🔧 Setup
---
1. Setup conda virtual environment
    ```bash
    conda env create --file=./conda.yml
    conda activate med_code 
    ```

2. Create a .env file, and populate according to the [.env.sample](.env.sample) example provided. You will need access to [UMLS API](https://documentation.uts.nlm.nih.gov/rest/home.html), an [Azure Open AI Resource](https://azure.microsoft.com/en-us/products/ai-services/openai-service?msockid=359b98bc5ab160c83b508c325bd061fd), and an [Azure AI Language Resource](https://azure.microsoft.com/en-us/products/ai-services/ai-language?msockid=359b98bc5ab160c83b508c325bd061fd)

    ```bash
    AZURE_OPENAI_BASE=your-endpoint
    AZURE_OPENAI_KEY=your-key
    AZURE_DEPLOYMENT_NAME=gpt-4o-mini
    LANGUAGE_KEY=your-key
    LANGUAGE_ENDPOINT=your-endpoint
    UMLS_API_KEY=your-key
    ```

