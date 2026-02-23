# SQLUser.PAC_DelivPlanManag

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DELPM_RowId | bigint | PK |  | NO | - |
| DELPM_Code | varchar |  |  | NO | Code |
| DELPM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DELPM_CreatedDate | date |  |  | SI | Created Date |
| DELPM_CreatedTime | time |  |  | SI | Created Time |
| DELPM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DELPM_DateFrom | date |  |  | SI | Date From |
| DELPM_DateTo | date |  |  | SI | Date To |
| DELPM_Desc | varchar |  |  | NO | Description |
| DELPM_NationalCode | varchar |  |  | SI | National Code |
| DELPM_Owner | varchar |  |  | SI | Owner |
| DELPM_UpdatedDate | date |  |  | SI | Updated Date |
| DELPM_UpdatedTime | time |  |  | SI | Updated Time |
| DELPM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Knee Pain and Symptoms |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Onset date |
| Q05 | - |  |  | SI | Knee pain - affected side |
| Q06 | - |  |  | SI | Knee pain characteristics |
| Q07 | - |  |  | SI | Knee pain location |
| Q08 | - |  |  | SI | Knee pain aggravating factors |
| Q09 | - |  |  | SI | Other knee symptoms |
| Q10 | - |  |  | SI | Additional symptom details |
| Q11 | - |  |  | SI | Follow up information |
| Q12 | - |  |  | SI | Knee symptoms progress |
| Q13 | - |  |  | SI | Additional follow up details |
| Q14 | - |  |  | SI | Knee History |
| Q15 | - |  |  | SI | History of |
| Q16 | - |  |  | SI | Other relevant surgical history or therapy |
| Q17 | - |  |  | SI | Knee trauma details |
| Q18 | - |  |  | SI | Previous knee surgical details |
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