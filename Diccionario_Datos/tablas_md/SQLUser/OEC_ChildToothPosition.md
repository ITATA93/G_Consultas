# SQLUser.OEC_ChildToothPosition

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registros hijos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CHTP_RowId | bigint | PK |  | NO | - |
| CHTP_Code | varchar |  |  | NO | Code |
| CHTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CHTP_CreatedDate | date |  |  | SI | Created Date |
| CHTP_CreatedTime | time |  |  | SI | Created Time |
| CHTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CHTP_Desc | varchar |  |  | NO | Description |
| CHTP_Owner | varchar |  |  | SI | Owner |
| CHTP_UpdatedDate | date |  |  | SI | Updated Date |
| CHTP_UpdatedTime | time |  |  | SI | Updated Time |
| CHTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Entered retrospectively |
| Q01ObsDR | - |  |  | SI | Entered retrospectively DR |
| Q02 | - |  |  | SI | Assistance requested - time |
| Q03 | - |  |  | SI | Assistance arrived - time |
| Q04 | - |  |  | SI | Episiotomy done |
| Q04ObsDR | - |  |  | SI | Episiotomy done DR |
| Q05 | - |  |  | SI | Episiotomy time |
| Q06 | - |  |  | SI | McRoberts position - time |
| Q07 | - |  |  | SI | Suprapubic pressure applied - time |
| Q08 | - |  |  | SI | Woods' screw manoeuvre - time |
| Q09 | - |  |  | SI | Delivery of posterior shoulder - time |
| Q10 | - |  |  | SI | Moved onto all fours - time |
| Q11 | - |  |  | SI | Other manoeuvres |
| Q12 | - |  |  | SI | Midwife countersigning |
| Q13 | - |  |  | SI | Help requested - time |
| Q14 | - |  |  | SI | Emergency call - time |
| Q15 | - |  |  | SI | Delivery of head - date |
| Q16 | - |  |  | SI | Delivery of head - time |
| Q17 | - |  |  | SI | Delivery of rest of baby - date |
| Q18 | - |  |  | SI | Delivery of rest of baby - time |
| Q19 | - |  |  | SI | Delivery notes |
| Q20 | - |  |  | SI | Mothers position before and during birth |
| Q21 | - |  |  | SI | Time from emergency call to delivery (mins) |
| Q22 | - |  |  | SI | Direction head facing |
| Q22ObsDR | - |  |  | SI | Direction head facing DR |
| Q23 | - |  |  | SI | Any sign of arm weakness |
| Q24 | - |  |  | SI | Any sign of potential bony fracture |
| Q25 | - |  |  | SI | Assessed by |
| Q26 | - |  |  | SI | Shoulder |
| Q27 | - |  |  | SI | Rubin 2 manoeuvre - time |
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