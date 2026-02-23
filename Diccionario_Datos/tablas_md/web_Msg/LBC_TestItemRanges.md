# web_Msg.LBC_TestItemRanges

**Schema:** web_Msg
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AnatomicalSiteList | varchar |  |  | SI | - |
| AnatomicalSiteQualifierList | varchar |  |  | SI | - |
| ContainerList | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBCTIR_Age | double |  |  | SI | Actual age |
| LBCTIR_AgeFrom | double |  |  | SI | Age Range From (format [yy].mmdd , ddd is 0-1231)... |
| LBCTIR_AgeTo | double |  |  | SI | Age Range To (format [yy].mmdd , mmdd is 0-1231)
... |
| LBCTIR_Altitude_DR | bigint |  | FK | SI | Altitude
Optinal, Indicates any altitude-related ... |
| LBCTIR_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTIR_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTIR_AutoHighRange | double |  |  | SI | (Auto) High Range (maximum 'auto-authorise' value ... |
| LBCTIR_AutoLowRange | double |  |  | SI | (Auto) Low Range (minimum 'auto-authorise' value f... |
| LBCTIR_CareProv_DR | varchar |  | FK | SI | Care Provider |
| LBCTIR_ClinicalConditionList | varchar |  |  | SI | List of Clinical Condition IDs per LBEpisode |
| LBCTIR_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition DR. Optional
Compared with LBE... |
| LBCTIR_ClinicalReviewFlag | bit |  |  | SI | Clinical Review Flag |
| LBCTIR_ClinicalReviewHighRange | double |  |  | SI | (Clinical Review High Range 
If present, must be ... |
| LBCTIR_ClinicalReviewLowRange | double |  |  | SI | Clinical Review Low Range  |
| LBCTIR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTIR_Comments | varchar |  |  | SI | Comments |
| LBCTIR_Container_DR | bigint |  | FK | SI | Container |
| LBCTIR_Date | date |  |  | SI | Date of collection |
| LBCTIR_DateFrom | date |  |  | SI | Effective date for the record
Required by User.LB... |
| LBCTIR_DateTo | date |  |  | SI | DateTo
Last day the record is active
Optional.  ... |
| LBCTIR_DisplayText | varchar |  |  | SI | Display Text
Show instead of numerical ranges.
N... |
| LBCTIR_Ethinicity_DR | bigint |  | FK | SI | Ethnicity.  Optional
Compared with PAPERIndigStat... |
| LBCTIR_Fasting | varchar |  |  | SI | Patient Fasting |
| LBCTIR_HighRange | double |  |  | SI | (Normal) High Range (maximum normal value)
Option... |
| LBCTIR_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBCTIR_Instrument_DR | bigint |  | FK | SI | Instrument |
| LBCTIR_Interpretation_DR | bigint |  | FK | SI | Clinical Interpretation for the range |
| LBCTIR_LabSite_DR | bigint |  | FK | SI | Lab Site Location.  Optional
This is the Location... |
| LBCTIR_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTIR_LowRange | double |  |  | SI | (Normal) Low Range (minimum normal value)
Optiona... |
| LBCTIR_PanicHighRange | double |  |  | SI | (Panic) High Range (values above PathHighRange up ... |
| LBCTIR_PanicLowRange | double |  |  | SI | (Panic) Low Range (values below PathLowRange down ... |
| LBCTIR_ParRef | bigint |  |  | SI | Parent TestItem DR |
| LBCTIR_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBCTIR_PatientLocation_DR | bigint |  | FK | SI | Patient Location DR.  Optional |
| LBCTIR_Pregnant | varchar |  |  | SI | Pregnant.
Should be set '' unless Sex='F'.
For f... |
| LBCTIR_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBCTIR_RowID | varchar |  |  | SI | - |
| LBCTIR_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCTIR_Sex_DR | bigint |  | FK | SI | Sex
Optional, Compared with LBEPSexDR |
| LBCTIR_SpeciesBreed_DR | varchar |  | FK | SI | Species Breeds |
| LBCTIR_Species_DR | bigint |  | FK | SI | Species
Optional, Compared with (future) PAPERSpe... |
| LBCTIR_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTIR_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTIR_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCTIR_TestMethod_DR | bigint |  | FK | SI | Test Method |
| LBCTIR_Type | varchar |  |  | SI | Ranges Type
AdmType Code Table  
Compared with t... |
| LBCTIR_UnacceptableHighRange | double |  |  | SI | (Unacceptable) High Range (values above PanicHighR... |
| LBCTIR_UnacceptableLowRange | double |  |  | SI | (Unacceptable) Low Range (values below PanicLowRan... |
| LBCTIR_WeeksOfPregnancy | double |  |  | SI | Actual number weeks of pregnancy |
| LBCTIR_WeeksOfPregnancyFrom | integer |  |  | SI | Weeks Of Pregnancy Range From
Optional.  Must onl... |
| LBCTIR_WeeksOfPregnancyTo | integer |  |  | SI | Weeks Of Pregnancy Range To
Optional.  Must only ... |
| LesionList | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenGroupList | varchar |  |  | SI | - |
| SpecimenList | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*