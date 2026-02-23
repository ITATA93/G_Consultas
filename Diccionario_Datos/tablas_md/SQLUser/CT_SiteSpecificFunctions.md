# SQLUser.CT_SiteSpecificFunctions

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSF_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Sitting to standing |
| Q02 | - |  |  | SI | Standing unsupported |
| Q03 | - |  |  | SI | Sitting unsupported |
| Q04 | - |  |  | SI | Standing to sitting |
| Q05 | - |  |  | SI | Transfers |
| Q06 | - |  |  | SI | Standing with eyes closed |
| Q07 | - |  |  | SI | Standing with feet together |
| Q08 | - |  |  | SI | Reaching forward with outstretched arm |
| Q09 | - |  |  | SI | Retrieving object from floor |
| Q10 | - |  |  | SI | Turning to look behind |
| Q10a | - |  |  | SI | Turn to look directly behind you over your left sh... |
| Q11 | - |  |  | SI | Turning 360 degrees |
| Q11a | - |  |  | SI | Turn completely around in a full circle. Pause. Th... |
| Q12 | - |  |  | SI | Placing alternate foot on stool |
| Q12a | - |  |  | SI | Place each foot alternately on step. Continue unti... |
| Q13 | - |  |  | SI | Standing with one foot in front |
| Q13a | - |  |  | SI | Place one foot directly in front of the other |
| Q14 | - |  |  | SI | Standing on one foot |
| Q14a | - |  |  | SI | Stand on one leg as long as you can without holdin... |
| Q15 | - |  |  | SI | Berg Balance Scale (BBS) was developed to measure ... |
| Q16 | - |  |  | SI | A five-point scale, ranging from 0-4. 0 indicates ... |
| Q17 | - |  |  | SI | 41-56: low fall risk |
| Q18 | - |  |  | SI | 21-40: medium fall risk |
| Q19 | - |  |  | SI | 0–20: high fall risk |
| Q1a | - |  |  | SI | Please stand up. Try not to use your hands for sup... |
| Q2a | - |  |  | SI | Please stand for 2 minutes without holding |
| Q3a | - |  |  | SI | Please sit with arms folded for 2 minutes (back un... |
| Q4a | - |  |  | SI | Please sit down |
| Q5a | - |  |  | SI | Transfer between bed and chair |
| Q6a | - |  |  | SI | Please close your eyes and stand still for 10 seco... |
| Q7a | - |  |  | SI | Place your feet together and stand without holding |
| Q8a | - |  |  | SI | Lift arms to 90 degrees. Reach forward as far as y... |
| Q9a | - |  |  | SI | Please pick up shoe / slipper that is placed in fr... |
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
| SSF_Code | varchar |  |  | NO | Code |
| SSF_CreatedDate | date |  |  | SI | Created Date |
| SSF_CreatedTime | time |  |  | SI | Created Time |
| SSF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSF_Desc | varchar |  |  | NO | Description |
| SSF_UpdatedDate | date |  |  | SI | Updated Date |
| SSF_UpdatedTime | time |  |  | SI | Updated Time |
| SSF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*