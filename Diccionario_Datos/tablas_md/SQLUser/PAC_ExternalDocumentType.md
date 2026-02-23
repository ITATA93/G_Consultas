# SQLUser.PAC_ExternalDocumentType

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXTDOCT_RowId | bigint | PK |  | NO | - |
| EXTDOCT_Code | varchar |  |  | NO | Code |
| EXTDOCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EXTDOCT_CreatedDate | date |  |  | SI | Created Date |
| EXTDOCT_CreatedTime | time |  |  | SI | Created Time |
| EXTDOCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXTDOCT_DateFrom | date |  |  | SI | Date From |
| EXTDOCT_DateTo | date |  |  | SI | Date To |
| EXTDOCT_Desc | varchar |  |  | NO | Description |
| EXTDOCT_Owner | varchar |  |  | SI | Owner |
| EXTDOCT_StyleSheetPath | varchar |  |  | SI | Style Sheet File Path |
| EXTDOCT_UpdatedDate | date |  |  | SI | Updated Date |
| EXTDOCT_UpdatedTime | time |  |  | SI | Updated Time |
| EXTDOCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Currently receiving renal replacement therapy |
| Q04 | - |  |  | SI | Serum creatinine |
| Q05 | - |  |  | SI | mg/dL |
| Q06 | - |  |  | SI | Serum total bilirubin |
| Q07 | - |  |  | SI | mg/dL |
| Q08 | - |  |  | SI | International Normalised Ratio (INR) |
| Q09 | - |  |  | SI | Sodium |
| Q10 | - |  |  | SI | mmol/L |
| Q11 | - |  |  | SI | MELD-Na Score |
| Q12 | - |  |  | SI | MELD Score |
| Q13 | - |  |  | SI | Score Interpretation |
| Q14 | - |  |  | SI | Meld-Na Score |
| Q15 | - |  |  | SI | Score Interpretation |
| Q16 | - |  |  | SI | Meld-Na Score |
| Q17 | - |  |  | SI | 90-day mortality |
| Q18 | - |  |  | SI | ≤14 |
| Q19 | - |  |  | SI | 15 - 16 |
| Q20 | - |  |  | SI | 17 - 20 |
| Q21 | - |  |  | SI | 21 - 22 |
| Q22 | - |  |  | SI | 23 - 26 |
| Q23 | - |  |  | SI | 27 - 31 |
| Q24 | - |  |  | SI | ≥ 32 |
| Q25 | - |  |  | SI | 1% |
| Q26 | - |  |  | SI | 1% - 2% |
| Q27 | - |  |  | SI | 3 - 4 % |
| Q28 | - |  |  | SI | 7 - 10% |
| Q29 | - |  |  | SI | 14 - 15% |
| Q30 | - |  |  | SI | 27 - 32% |
| Q31 | - |  |  | SI | 65 - 66% |
| Q32 | - |  |  | SI | This score was adapted for estimating the 90-day r... |
| Q33 | - |  |  | SI | MELD-Na Score Interpretation |
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