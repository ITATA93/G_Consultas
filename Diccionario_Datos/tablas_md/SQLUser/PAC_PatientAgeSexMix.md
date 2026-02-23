# SQLUser.PAC_PatientAgeSexMix

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PASM_RowId | bigint | PK |  | NO | - |
| PASM_Code | varchar |  |  | NO | Code |
| PASM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PASM_CreatedDate | date |  |  | SI | Created Date |
| PASM_CreatedTime | time |  |  | SI | Created Time |
| PASM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PASM_Desc | varchar |  |  | NO | Description |
| PASM_Owner | varchar |  |  | SI | Owner |
| PASM_UpdatedDate | date |  |  | SI | Updated Date |
| PASM_UpdatedTime | time |  |  | SI | Updated Time |
| PASM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Prior history |
| Q04 | - |  |  | SI | Cardiovascular |
| Q05 | - |  |  | SI | Postpartum haemorrhage |
| Q06 | - |  |  | SI | Medication |
| Q07 | - |  |  | SI | Neurofunction / Anaesthesia |
| Q08 | - |  |  | SI | Motor / Activity |
| Q09 | - |  |  | SI | Score |
| Q10 | - |  |  | SI | Classification |
| Q11 | - |  |  | SI | 0 - 2 |
| Q12 | - |  |  | SI | Low Fall Risk |
| Q13 | - |  |  | SI | 3 - 4 |
| Q14 | - |  |  | SI | Moderate Fall Risk |
| Q15 | - |  |  | SI | > 4 |
| Q16 | - |  |  | SI | High Fall Risk |
| Q17 | - |  |  | SI | A scoring tool for the assessment of fall risk for... |
| Q18 | - |  |  | SI | 0 - 2: Low Fall Risk |
| Q19 | - |  |  | SI | 3 - 4: Moderate Fall Risk |
| Q20 | - |  |  | SI | > 4: High Fall Risk |
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