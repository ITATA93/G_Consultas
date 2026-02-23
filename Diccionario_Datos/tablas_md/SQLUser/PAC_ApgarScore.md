# SQLUser.PAC_ApgarScore

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APGS_RowId | bigint | PK |  | NO | - |
| APGS_Code | varchar |  |  | NO | Code |
| APGS_Count | double |  |  | SI | Apgar Count |
| APGS_CreatedDate | date |  |  | SI | Created Date |
| APGS_CreatedTime | time |  |  | SI | Created Time |
| APGS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APGS_Desc | varchar |  |  | NO | Description |
| APGS_NationalCode | varchar |  |  | SI | National code |
| APGS_UpdatedDate | date |  |  | SI | Updated Date |
| APGS_UpdatedTime | time |  |  | SI | Updated Time |
| APGS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Nursing end of life care |
| Q11 | - |  |  | SI | Immobility: bedbound or uncommunicative |
| Q12 | - |  |  | SI | If any of the above is yes, do not remove urinary ... |
| Q13 | - |  |  | SI | If not removed , reason |
| Q14 | - |  |  | SI | Trovillion EW, Hopkins-Broyles D, Recktenwald A, e... |
| Q15 | - |  |  | SI | April 1-4, 2011, Dallas, Texas. Accessed February ... |
| Q16 | - |  |  | SI | Yatim J, Wong K, Ling M, Tan S, Tan K, Hockenberry... |
| Q17 | - |  |  | SI | Paper presented at: SHEA (Society of Healthcare Ep... |
| Q2 | - |  |  | SI | Time |
| Q3 | - |  |  | SI | Indwelling urinary catheter day |
| Q4 | - |  |  | SI | Tick each of the indications for catheterization b... |
| Q5 | - |  |  | SI | Haematuria, gross |
| Q6 | - |  |  | SI | Obstruction |
| Q7 | - |  |  | SI | Urology, abdominal, gynaecological or perineal sur... |
| Q8 | - |  |  | SI | Decubitus ulcer |
| Q9 | - |  |  | SI | Input and output measurement |
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