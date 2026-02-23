# web_Msg.LBCAppEventRuleList

**Schema:** web_Msg
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCAER_AdmType | varchar |  |  | SI | Patient / Episode
-------------
Admission Type |
| LBCAER_Age | varchar |  |  | SI | Age (format [yy].mmdd , mmdd is 0-1231)
Not in us... |
| LBCAER_AgeFrom | double |  |  | SI | Age Range From (format [yy].mmdd , ddd is 0-1231)... |
| LBCAER_AgeTo | double |  |  | SI | Age Range To (format [yy].mmdd , mmdd is 0-1231)
... |
| LBCAER_AnatomicalSiteQualifiers | varchar |  |  | SI | Anatomical Site Qualifier |
| LBCAER_AnatomicalSites | varchar |  |  | SI | Anatomical Site |
| LBCAER_CareProvGroup_DR | bigint |  | FK | SI | Care Provider Group |
| LBCAER_CareProvSpeciality_DR | bigint |  | FK | SI | Care Provider Speciality |
| LBCAER_CareProv_DR | varchar |  | FK | SI | Care Provider |
| LBCAER_ClinicalConditions | varchar |  |  | SI | Clinical Conditions |
| LBCAER_ClinicalInterpretations | varchar |  |  | SI | Actions
------------
Clinical Interpretations |
| LBCAER_CodeTableTags | varchar |  |  | SI | Code Table
--------
List of code table Tags |
| LBCAER_CreatedDate | date |  |  | SI | Created Date |
| LBCAER_CreatedTime | time |  |  | SI | Created Time |
| LBCAER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAER_DateFrom | date |  |  | SI | Effective date for the record |
| LBCAER_DateTo | date |  |  | SI | Last day the record is active  |
| LBCAER_Description | varchar |  |  | SI | General Properties
--------------
Description
R... |
| LBCAER_Group | numeric |  |  | SI | Group |
| LBCAER_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBCAER_Instrument_DR | bigint |  | FK | SI | Instrument |
| LBCAER_Lesions | varchar |  |  | SI | Lesion |
| LBCAER_PatType_DR | bigint |  | FK | SI | Patient Type |
| LBCAER_PatientFlags | varchar |  |  | SI | Patient Flags |
| LBCAER_PatientLocation_DR | bigint |  | FK | SI | Patient Location DR. |
| LBCAER_PerformedAtLabSite_DR | bigint |  | FK | SI | Performed at Lab Site |
| LBCAER_Pregnant | varchar |  |  | SI | Pregnant. |
| LBCAER_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| LBCAER_RowID | varchar |  |  | SI | - |
| LBCAER_Sequence | numeric |  |  | SI | Sequence within the group
Required by User.LBCApp... |
| LBCAER_Sex_DR | bigint |  | FK | SI | Sex
Compared with LBEPSexDR |
| LBCAER_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCAER_Species_DR | bigint |  | FK | SI | Species |
| LBCAER_SpecimenGroups | varchar |  |  | SI | Specimen
-------------
Specimen Group |
| LBCAER_Specimens | varchar |  |  | SI | Specimen |
| LBCAER_SubjectType_DR | bigint |  | FK | SI | SubjectType |
| LBCAER_TSClinicalReview | varchar |  |  | SI | Clinical Review |
| LBCAER_TSConfidential | varchar |  |  | SI | Test Set Confidental. |
| LBCAER_TSExpiredSpcValidity | varchar |  |  | SI | Test Set Expired Specimen Validity
Compared with ... |
| LBCAER_TSIExpiredSpcValidity | varchar |  |  | SI | Test Set Item
--------------
Test Set Item Expri... |
| LBCAER_TSLabSite_DR | bigint |  | FK | SI | Test Set Lab Site |
| LBCAER_TSPriority_DR | bigint |  | FK | SI | Test Set
-----------
Test Priority |
| LBCAER_TSSignificantResult | varchar |  |  | SI | Significant Result. |
| LBCAER_TestMethod_DR | bigint |  | FK | SI | Test Method |
| LBCAER_TestSetItem_DR | varchar |  | FK | SI | Test Set Revision Reference |
| LBCAER_Type | varchar |  |  | SI | Type
Required by User.LBCAppEventRule. |
| LBCAER_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAER_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCTestSetRevisionID | varchar |  |  | SI | - |
| LBCTestSetRevisionItemID | varchar |  |  | SI | - |
| LBTestSetID | varchar |  |  | SI | - |
| LBTestSetItemID | varchar |  |  | SI | - |
| LBTestSetItemMsgID | varchar |  |  | SI | - |
| LBTestSetMsgID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*