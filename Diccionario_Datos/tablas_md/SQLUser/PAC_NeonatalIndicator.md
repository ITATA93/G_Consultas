# SQLUser.PAC_NeonatalIndicator

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NEOIND_RowId | bigint | PK |  | NO | - |
| NEOIND_Active | varchar |  |  | SI | Active flag |
| NEOIND_Code | varchar |  |  | NO | Code |
| NEOIND_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NEOIND_CreatedDate | date |  |  | SI | Created Date |
| NEOIND_CreatedTime | time |  |  | SI | Created Time |
| NEOIND_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NEOIND_DateFrom | date |  |  | SI | Date from |
| NEOIND_DateTo | date |  |  | SI | Date To |
| NEOIND_Desc | varchar |  |  | NO | Description |
| NEOIND_NationalCode | varchar |  |  | SI | National Code |
| NEOIND_Owner | varchar |  |  | SI | Owner |
| NEOIND_UpdatedDate | date |  |  | SI | Updated Date |
| NEOIND_UpdatedTime | time |  |  | SI | Updated Time |
| NEOIND_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Signs / Symptoms |
| Q02 | - |  |  | SI | Please select one of the following |
| Q03 | - |  |  | SI | Score 1: Grade I (have an approximate 30% mortalit... |
| Q04 | - |  |  | SI | Score 2: Grade II (have an approximate 40% mortali... |
| Q05 | - |  |  | SI | Score 3: Grade III (have an approximate 50% mortal... |
| Q06 | - |  |  | SI | Score 4: Grade IV (have an approximate 80% mortali... |
| Q07 | - |  |  | SI | Score 5: Grade V (have an approximate 90% mortalit... |
| Q08 | - |  |  | SI | The scale is used to classify the severity of a su... |
| Q09 | - |  |  | SI | A higher grade predicts a poor outcome and lower l... |
| Q10 | - |  |  | SI | 1 |
| Q11 | - |  |  | SI | Grade I (have an approximate 30% mortality) |
| Q12 | - |  |  | SI | 2 |
| Q13 | - |  |  | SI | Grade II (have an approximate 40% mortality) |
| Q14 | - |  |  | SI | 3 |
| Q15 | - |  |  | SI | Grade III (have an approximate 50% mortality) |
| Q16 | - |  |  | SI | 4 |
| Q17 | - |  |  | SI | Grade IV (have an approximate 80% mortality) |
| Q18 | - |  |  | SI | 5 |
| Q19 | - |  |  | SI | Grade V (have an approximate 90% mortality) |
| Q20 | - |  |  | SI | Score |
| Q21 | - |  |  | SI | Classification |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Time |
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