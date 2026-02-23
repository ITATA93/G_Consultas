# SQLUser.PAC_ReasonForUnmerging

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REAUNM_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Location |
| Q02 | - |  |  | SI | Examiner |
| Q03 | - |  |  | SI | Sitting to standing |
| Q04 | - |  |  | SI | “Hold your arms up and stand up” |
| Q05 | - |  |  | SI | Sitting to standing Time (seconds) |
| Q06 | - |  |  | SI | Standing to sitting |
| Q08 | - |  |  | SI | “Sit down slowly without using your hands” |
| Q09 | - |  |  | SI | Standing to sitting Time (seconds) |
| Q10 | - |  |  | SI | Transfers |
| Q11 | - |  |  | SI | Transfer Time (seconds) |
| Q12 | - |  |  | SI | Standing unsupported |
| Q13 | - |  |  | SI | Standing unsupported Time (seconds) |
| Q14 | - |  |  | SI | Sitting unsupported |
| Q15 | - |  |  | SI | “Sit with your arms folded on your chest for 30 se... |
| Q16 | - |  |  | SI | Sitting unsupported Time (seconds) |
| Q17 | - |  |  | SI | Standing with eyes closed |
| Q18 | - |  |  | SI | “When I say close your eyes, I want you to stand s... |
| Q19 | - |  |  | SI | Standing with eyes closed Time (seconds) |
| Q20 | - |  |  | SI | Standing with feet together |
| Q21 | - |  |  | SI | Standing with feet together Time (seconds) |
| Q22 | - |  |  | SI | Standing with one foot in front |
| Q23 | - |  |  | SI | Standing with one foot in front Time (seconds) |
| Q24 | - |  |  | SI | Standing on one foot |
| Q25 | - |  |  | SI | Standing on one foot Time (seconds) |
| Q26 | - |  |  | SI | Turning 360 degrees |
| Q27 | - |  |  | SI | “Turn completely around in a full circle, STOP, an... |
| Q28 | - |  |  | SI | Turning 360 degrees Time (seconds) |
| Q29 | - |  |  | SI | Turning to look behind |
| Q30 | - |  |  | SI | “Follow this object as I move it. Keep watching it... |
| Q31 | - |  |  | SI | Turning to look behind Time (seconds) |
| Q32 | - |  |  | SI | Retrieving object from floor |
| Q33 | - |  |  | SI | Retrieving object from floor Time (seconds) |
| Q34 | - |  |  | SI | Placing alternate foot on stool |
| Q35 | - |  |  | SI | Placing alternate foot on stool Time (seconds) |
| Q36 | - |  |  | SI | Reaching forward with outstretched arm |
| Q37 | - |  |  | SI | “Stretch out your fingers, make a fist, and reach ... |
| Q38 | - |  |  | SI | Reaching forward with outstretched arm Distance (i... |
| Q39 | - |  |  | SI | Range = 0 - 56. The higher the patient score the g... |
| Q40 | - |  |  | SI | Score |
| Q41 | - |  |  | SI | Classification |
| Q42 | - |  |  | SI | 0 - 56 |
| Q43 | - |  |  | SI | The higher the patient score the greater the indep... |
| Q44 | - |  |  | SI | The Pediatric Balance Scale is a balance measure f... |
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
| REAUNM_Code | varchar |  |  | NO | Code |
| REAUNM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REAUNM_CreatedDate | date |  |  | SI | Created Date |
| REAUNM_CreatedTime | time |  |  | SI | Created Time |
| REAUNM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REAUNM_DateFrom | date |  |  | SI | Date From |
| REAUNM_DateTo | date |  |  | SI | Date To |
| REAUNM_Desc | varchar |  |  | NO | Description |
| REAUNM_Owner | varchar |  |  | SI | Owner |
| REAUNM_UpdatedDate | date |  |  | SI | Updated Date |
| REAUNM_UpdatedTime | time |  |  | SI | Updated Time |
| REAUNM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*