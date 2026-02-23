# SQLUser.PAC_LabourMethod

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBMTH_RowId | bigint | PK |  | NO | - |
| LBMTH_Code | varchar |  |  | NO | Labour Method Code |
| LBMTH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBMTH_CreatedDate | date |  |  | SI | Created Date |
| LBMTH_CreatedTime | time |  |  | SI | Created Time |
| LBMTH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBMTH_DateFrom | date |  |  | SI | DateFrom |
| LBMTH_DateTo | date |  |  | SI | DateTo |
| LBMTH_Desc | varchar |  |  | NO | Labour Method Description |
| LBMTH_NationalCode | varchar |  |  | SI | National code |
| LBMTH_Owner | varchar |  |  | SI | Owner |
| LBMTH_RcFlag | varchar |  |  | SI | Archived Flag |
| LBMTH_Type | varchar |  |  | SI | Labour Method Type |
| LBMTH_UpdatedDate | date |  |  | SI | Updated Date |
| LBMTH_UpdatedTime | time |  |  | SI | Updated Time |
| LBMTH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Have you/the patient lost weight recently (i.e. in... |
| Q02 | - |  |  | SI | How much?	 |
| Q03 | - |  |  | SI | Have you/the patient been eating poorly because of... |
| Q04 | - |  |  | SI | Score |
| Q05 | - |  |  | SI | Classification |
| Q06 | - |  |  | SI | ≥ 2 |
| Q07 | - |  |  | SI | Positive for nutrition risk |
| Q08 | - |  |  | SI | < 2 |
| Q09 | - |  |  | SI | Negative for nutrition risk	 |
| Q10 | - |  |  | SI | Nutrition screening tool assesses whether an adult... |
| Q11 | - |  |  | SI | ≥ 2: Positive for nutrition risk	 |
| Q12 | - |  |  | SI | < 2: Negative for nutrition risk |
| Q13 | - |  |  | SI | 2 - 5 |
| Q14 | - |  |  | SI | Indicates risk of malnutrition |
| Q15 | - |  |  | SI | 0 - 1 |
| Q16 | - |  |  | SI | Indicates no risk of malnutrition |
| Q17 | - |  |  | SI | 2 - 5: Indicates risk of malnutrition |
| Q18 | - |  |  | SI | 0 - 1: Indicates no risk of malnutrition |
| Q19 | - |  |  | SI | • Patients who are not at risk of malnutrition (MS... |
| Q20 | - |  |  | SI | • Patients who are at risk of malnutrition (MST sc... |
| Q21 | - |  |  | SI | appropriate form of nutrition support. |
| Q22 | - |  |  | SI | • Note: overweight / obese clients who have unexpl... |
| Q23 | - |  |  | SI | The following question(s) related to swallowing ar... |
| Q24 | - |  |  | SI | Does the patient have difficulty swallowing? |
| Q25 | - |  |  | SI | Speech pathology referral required |
| Q26 | - |  |  | SI | Queensland Health, Royal Brisbane and Women's Hosp... |
| Q27 | - |  |  | SI | https://www.health.qld.gov.au/__data/assets/pdf_fi... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*