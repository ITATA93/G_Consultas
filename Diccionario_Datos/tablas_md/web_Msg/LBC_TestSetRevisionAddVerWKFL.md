# web_Msg.LBC_TestSetRevisionAddVerWKFL

**Schema:** web_Msg
**Columnas:** 52
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AnatomicalSiteList | varchar |  |  | SI | - |
| AnatomicalSiteQualifierList | varchar |  |  | SI | - |
| ClinicalConditionList | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| LBCTSRAVW_AdmType | varchar |  |  | SI | Admission Type |
| LBCTSRAVW_Age | double |  |  | SI | - |
| LBCTSRAVW_AgeFrom | double |  |  | SI | Age Range From (format [yy].mmdd , ddd is 0-1231)... |
| LBCTSRAVW_AgeTo | double |  |  | SI | Age Range To (format [yy].mmdd , mmdd is 0-1231)
... |
| LBCTSRAVW_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTSRAVW_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRAVW_CareProv_DR | varchar |  | FK | SI | Care Provider |
| LBCTSRAVW_ClinicalCondition_DR | bigint |  | FK | SI | Clinical Condition DR |
| LBCTSRAVW_ClinicalReview | varchar |  |  | SI | Clinical Review |
| LBCTSRAVW_Code | varchar |  |  | SI | Code
Required by User.LBCTestSetRevisionAddVerWKF... |
| LBCTSRAVW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRAVW_CreatedDate | date |  |  | SI | Created Date |
| LBCTSRAVW_CreatedTime | time |  |  | SI | Created Time |
| LBCTSRAVW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTSRAVW_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRAVW_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRAVW_Desc | varchar |  |  | SI | Description
Required by User.LBCTestSetRevisionAd... |
| LBCTSRAVW_ExpiredSpcValidity | varchar |  |  | SI | Expired Specimen Validity
Compared with LBTSSpeci... |
| LBCTSRAVW_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRAVW_ParRef | bigint |  |  | SI | - |
| LBCTSRAVW_PatientLocation_DR | bigint |  | FK | SI | Patient Location DR. |
| LBCTSRAVW_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCTSRAVW_Queues | varchar |  |  | SI | Queue List Workflow |
| LBCTSRAVW_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBCTSRAVW_RowID | varchar |  |  | SI | - |
| LBCTSRAVW_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCTSRAVW_Sex_DR | bigint |  | FK | SI | Sex
Compared with LBEPSexDR |
| LBCTSRAVW_SignificantResult | varchar |  |  | SI | Significant Result. |
| LBCTSRAVW_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTSRAVW_Species_DR | bigint |  | FK | SI | Species |
| LBCTSRAVW_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRAVW_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRAVW_SubjectType_DR | bigint |  | FK | SI | SubjectType |
| LBCTSRAVW_TSConfidential | varchar |  |  | SI | Test Set Confidental. |
| LBCTSRAVW_TSLabSite_DR | bigint |  | FK | SI | Test Set Lab Site |
| LBCTSRAVW_TSPriority_DR | bigint |  | FK | SI | Test Priority |
| LBCTSRAVW_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTSRAVW_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTSRAVW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBTestSetID | varchar |  |  | SI | The Row ID of the test set being evaluated |
| LesionList | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenGroupList | varchar |  |  | SI | - |
| SpecimenList | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*