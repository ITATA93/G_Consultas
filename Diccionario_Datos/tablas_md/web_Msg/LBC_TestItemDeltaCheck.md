# web_Msg.LBC_TestItemDeltaCheck

**Schema:** web_Msg
**Columnas:** 52
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
| LBCTIDC_AbsoluteValue | double |  |  | SI | Absolute Value  |
| LBCTIDC_AbsoluteValueComments | varchar |  |  | SI | Absolute Value Comments |
| LBCTIDC_AdmType | varchar |  |  | SI | Admission Type
AdmType Standard Type   |
| LBCTIDC_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTIDC_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTIDC_ClinicalConditionList | varchar |  |  | SI | List of Clinical Condition IDs per LBEpisode |
| LBCTIDC_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition |
| LBCTIDC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTIDC_Container_DR | bigint |  | FK | SI | Container |
| LBCTIDC_Date | date |  |  | SI | Date of collection |
| LBCTIDC_DateFrom | date |  |  | SI | Effective date from for the record
Required by Us... |
| LBCTIDC_DateTo | date |  |  | SI | Effective date to for the record |
| LBCTIDC_Direction | varchar |  |  | SI | Direction of Change
LabResultDirection Standard T... |
| LBCTIDC_Interpretation_DR | bigint |  | FK | SI | Delta Check Interpretation |
| LBCTIDC_IntervalFrom | integer |  |  | SI | Interval From  |
| LBCTIDC_IntervalFromUnit | varchar |  |  | SI | Interval From Unit  |
| LBCTIDC_IntervalTo | integer |  |  | SI | Interval To |
| LBCTIDC_IntervalToUnit | varchar |  |  | SI | Interval From Unit  |
| LBCTIDC_LastResultInterval | varchar |  |  | SI | Interval to previous result |
| LBCTIDC_LastTestSetItem_DR | varchar |  | FK | SI | temporary previous LBTSI Link  |
| LBCTIDC_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTIDC_ParRef | bigint |  |  | SI | Parent TestItem DR |
| LBCTIDC_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBCTIDC_PatientLocation_DR | bigint |  | FK | SI | Patient Location |
| LBCTIDC_Percentage | double |  |  | SI | Percentage Value  |
| LBCTIDC_PercentageComments | varchar |  |  | SI | Percentage Comments |
| LBCTIDC_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCTIDC_RateOfChange | double |  |  | SI | Rate of Change |
| LBCTIDC_RateOfChangeComments | varchar |  |  | SI | Rate Of Change Comments |
| LBCTIDC_RateOfChangeUnit | varchar |  |  | SI | Rate of Change Unit |
| LBCTIDC_RowID | varchar |  |  | SI | - |
| LBCTIDC_Sequence | double |  |  | SI | Priority  Sequence |
| LBCTIDC_Sex_DR | bigint |  | FK | SI | Sex |
| LBCTIDC_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTIDC_Species_DR | bigint |  | FK | SI | Species |
| LBCTIDC_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTIDC_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTIDC_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCTIDC_TextChange | varchar |  |  | SI | Text Change |
| LBCTIDC_TextChangeComments | varchar |  |  | SI | Text Change Comments |
| LesionList | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenGroupList | varchar |  |  | SI | - |
| SpecimenList | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*