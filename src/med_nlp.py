from zensols.mednlp import ApplicationFactory
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def parse_note(note:str) -> str:
    
    doc_parser = ApplicationFactory.get_doc_parser()
    doc = doc_parser(note)

    new_note = set([])
    for tok in doc.tokens:
        logger.info(f"{tok}, {tok.detected_name_}, {tok.sub_names}, {tok.pref_name_}, {tok.tuis_}, {tok.tui_descs_}")
        if tok.is_concept and tok.tuis_ in ['T184', 'T047', 'T046', 'T033', 'T037','T191','T005', 'T004', 'T007', 'T008']:
            
            new_note.add(tok.detected_name_.replace("~"," "))
            new_note.add(tok.pref_name_.lower())

    logger.info(f"Note Parsing Complete.")
    
    return " ".join(new_note)

if __name__ == "__main__":
    print(parse_note("History Present Illness INDICATIONS SURGERY year old woman noted bruising mild abdominal pain large incisional hernia site . came emergency room developed profound sepsis"))

'''
List of TUIS:

T001: Organism
T002: Plant
T003: Alga
T004: Fungus
T005: Virus
T007: Bacterium
T008: Rickettsia or Chlamydia
T009: Animal
T010: Amphibian
T011: Bird
T012: Fish
T013: Reptile
T014: Mammal
T015: Human
T016: Group
T017: Anatomical Structure
T018: Embryonic Structure
T019: Congenital Abnormality
T020: Acquired Abnormality
T021: Fully Formed Anatomical Structure
T022: Body Part, Organ, or Organ Component
T023: Tissue
T024: Cell
T025: Cell Component
T026: Gene or Genome
T028: Body Location or Region
T029: Body Space or Junction
T030: Body Substance
T031: Substance
T032: Element, Ion, or Isotope
T033: Chemical
T034: Organic Chemical
T035: Inorganic Chemical
T036: Eicosanoid
T037: Hormone
T038: Enzyme
T039: Vitamin
T040: Immunologic Factor
T041: Receptor
T042: Nucleic Acid, Nucleoside, or Nucleotide
T043: Amino Acid, Peptide, or Protein
T044: Carbohydrate
T045: Lipid
T046: Biomedical or Dental Material
T047: Pharmacologic Substance
T048: Antibiotic
T049: Biomedical Material
T050: Chemical Viewed Structurally
T051: Chemical Viewed Functionally
T052: Chemical Viewed Functionally and Structurally
T053: Biologically Active Substance
T054: Research Device
T055: Clinical Drug
T056: Hazardous or Poisonous Substance
T057: Indicator, Reagent, or Diagnostic Aid
T058: Pharmacologic Substance
T059: Laboratory Procedure
T060: Diagnostic Procedure
T061: Therapeutic or Preventive Procedure
T062: Research Activity
T063: Educational Activity
T064: Governmental or Regulatory Activity
T065: Legal Activity
T066: Administrative Activity
T067: Financial Activity
T068: Machine Activity
T069: Human-caused Phenomenon or Process
T070: Natural Phenomenon or Process
T071: Entity
T072: Group Attribute
T073: Intellectual Product
T074: Language
T075: Occupation or Discipline
T077: Conceptual Entity
T078: Idea or Concept
T079: Temporal Concept
T080: Qualitative Concept
T081: Quantitative Concept
T082: Spatial Concept
T083: Geographic Area
T085: Fully Formed Anatomical Structure
T086: Body Part, Organ, or Organ Component
T087: Tissue
T088: Cell
T089: Cell Component
T090: Gene or Genome
T091: Body Location or Region
T092: Body Space or Junction
T093: Body Substance
T094: Substance
T095: Element, Ion, or Isotope
T096: Chemical
T097: Organic Chemical
T098: Inorganic Chemical
T099: Eicosanoid
T100: Hormone
T101: Enzyme
T102: Vitamin
T103: Immunologic Factor
T104: Receptor
T105: Nucleic Acid, Nucleoside, or Nucleotide
T106: Amino Acid, Peptide, or Protein
T107: Carbohydrate
T108: Lipid
T109: Biomedical or Dental Material
T110: Pharmacologic Substance
T111: Antibiotic
T112: Biomedical Material
T113: Chemical Viewed Structurally
T114: Chemical Viewed Functionally
T115: Chemical Viewed Functionally and Structurally
T116: Biologically Active Substance
T117: Research Device
T118: Clinical Drug
T119: Hazardous or Poisonous Substance
T120: Indicator, Reagent, or Diagnostic Aid
T121: Pharmacologic Substance
T122: Laboratory Procedure
T123: Diagnostic Procedure
T124: Therapeutic or Preventive Procedure
T125: Research Activity
T126: Educational Activity
T127: Governmental or Regulatory Activity
T128: Legal Activity
T129: Administrative Activity
T130: Financial Activity
T131: Machine Activity
T132: Human-caused Phenomenon or Process
T133: Natural Phenomenon or Process
T134: Entity
T135: Group Attribute
T136: Intellectual Product
T137: Language
T138: Occupation or Discipline
T139: Conceptual Entity
T140: Idea or Concept
T141: Temporal Concept
T142: Qualitative Concept
T143: Quantitative Concept
T144: Spatial Concept
T145: Geographic Area
'''