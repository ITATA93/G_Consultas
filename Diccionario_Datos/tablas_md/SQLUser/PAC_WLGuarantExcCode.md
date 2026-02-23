# SQLUser.PAC_WLGuarantExcCode

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLGEC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Rasmsay Sedation Score |
| Q02 | - |  |  | SI | Observe patient, if awake score 1 or 2 depending o... |
| Q03 | - |  |  | SI | Give voice command, score 3 or 4 depending on spee... |
| Q04 | - |  |  | SI | Guidelines for RSS Assessment |
| Q05 | - |  |  | SI | If no response to voice, give louder voice command... |
| Q06 | - |  |  | SI | If no response to stimuli, score 6 |
| Q07 | - |  |  | SI | The Ramsay Sedation Scale (RSS) scores sedation at... |
| Q08 | - |  |  | SI | It is an intuitively obvious scale and therefore l... |
| Q09 | - |  |  | SI | It can be added to the pain score and be considere... |
| Q10 | - |  |  | SI | not only in the ICU, but wherever sedative drugs o... |
| Q11 | - |  |  | SI | Date |
| Q12 | - |  |  | SI | Time |
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
| WLGEC_Code | varchar |  |  | NO | Code |
| WLGEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLGEC_CreatedDate | date |  |  | SI | Created Date |
| WLGEC_CreatedTime | time |  |  | SI | Created Time |
| WLGEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLGEC_Desc | varchar |  |  | NO | Description |
| WLGEC_Owner | varchar |  |  | SI | Owner |
| WLGEC_UpdatedDate | date |  |  | SI | Updated Date |
| WLGEC_UpdatedTime | time |  |  | SI | Updated Time |
| WLGEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*