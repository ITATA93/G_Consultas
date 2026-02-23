# SQLUser.PAC_SutureType

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUTRTYPE_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Any unusual events occur during the course of this... |
| Q04 | - |  |  | SI | Unusual event notes |
| Q05 | - |  |  | SI | Any alcoholic drinks yesterday |
| Q06 | - |  |  | SI | Amount of alcohol (approx number of glasses) |
| Q07 | - |  |  | SI | Any naps yesterday |
| Q08 | - |  |  | SI | What time did you nap (approx) |
| Q09 | - |  |  | SI | Approximately how long did you nap (min) |
| Q10 | - |  |  | SI | Nap notes |
| Q11 | - |  |  | SI | Any sleeping medication on the night of the study |
| Q12 | - |  |  | SI | Medication notes |
| Q13 | - |  |  | SI | Lights off time (approx) |
| Q14 | - |  |  | SI | Bed time (approx) |
| Q15 | - |  |  | SI | Awake time (approx) |
| Q16 | - |  |  | SI | Perception of Sleep Quality |
| Q17 | - |  |  | SI | How long do you think it took you to fall asleep l... |
| Q18 | - |  |  | SI | How long do you think you slept last night (approx... |
| Q19 | - |  |  | SI | Did you wake during the night |
| Q20 | - |  |  | SI | How many times do you think you woke up (approx) |
| Q21 | - |  |  | SI | What is the total time you think you were awake (a... |
| Q22 | - |  |  | SI | How would you describe the quality of your sleep l... |
| Q23 | - |  |  | SI | How did your sleep last night compared to a usual ... |
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
| SUTRTYPE_Active | varchar |  |  | SI | Active flag |
| SUTRTYPE_Code | varchar |  |  | NO | Code |
| SUTRTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUTRTYPE_CreatedDate | date |  |  | SI | Created Date |
| SUTRTYPE_CreatedTime | time |  |  | SI | Created Time |
| SUTRTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUTRTYPE_DateFrom | date |  |  | SI | Date From |
| SUTRTYPE_DateTo | date |  |  | SI | Date To |
| SUTRTYPE_Desc | varchar |  |  | NO | Description |
| SUTRTYPE_NationalCode | varchar |  |  | SI | National Code |
| SUTRTYPE_Owner | varchar |  |  | SI | Owner |
| SUTRTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| SUTRTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| SUTRTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*