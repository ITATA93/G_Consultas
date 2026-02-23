# SQLUser.PAC_WLStatusListStat

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STAT_ParRef | bigint | PK |  | NO | PAC_WLStatusList Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Strength |
| Q04 | - |  |  | SI | How much difficulty do you have in lifting and car... |
| Q05 | - |  |  | SI | Assistance in walking |
| Q06 | - |  |  | SI | How much difficulty do you have walking across a r... |
| Q07 | - |  |  | SI | Rise from a chair |
| Q08 | - |  |  | SI | How much difficulty do you have transferring from ... |
| Q09 | - |  |  | SI | Climb stairs |
| Q10 | - |  |  | SI | How much difficulty do you have climbing a flight ... |
| Q11 | - |  |  | SI | Falls |
| Q12 | - |  |  | SI | How many times have you fallen in the past year? |
| Q13 | - |  |  | SI | References |
| Q14 | - |  |  | SI | • Malmstrom TK, Morley JE. SARC-F: A Simple Questi... |
| Q15 | - |  |  | SI | • Woo J, Leung J, Morley JE. Validating the SARC-F... |
| Q16 | - |  |  | SI | The SARC-F questionnaire was developed as a possib... |
| Q17 | - |  |  | SI | The scores range from 0 to 10, with 0 to 2 points ... |
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
| STAT_Childsub | double |  |  | NO | Childsub |
| STAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STAT_CreatedDate | date |  |  | SI | Created Date |
| STAT_CreatedTime | time |  |  | SI | Created Time |
| STAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STAT_RowId | varchar |  |  | NO | - |
| STAT_UpdatedDate | date |  |  | SI | Updated Date |
| STAT_UpdatedTime | time |  |  | SI | Updated Time |
| STAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| STAT_WLStatus_DR | bigint |  | FK | SI | Des Ref WLStatus |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*