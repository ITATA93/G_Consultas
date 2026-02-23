# SQLUser.PAC_NWPatientType

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NWPTYPE_RowId | bigint | PK |  | NO | - |
| NWPTYPE_Code | varchar |  |  | NO | Code |
| NWPTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NWPTYPE_CreatedDate | date |  |  | SI | Created Date |
| NWPTYPE_CreatedTime | time |  |  | SI | Created Time |
| NWPTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NWPTYPE_DateFrom | date |  |  | SI | DateFrom |
| NWPTYPE_DateTo | date |  |  | SI | DateTo |
| NWPTYPE_Desc | varchar |  |  | NO | Description |
| NWPTYPE_Owner | varchar |  |  | SI | Owner |
| NWPTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| NWPTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| NWPTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Walk |
| Q04 | - |  |  | SI | Stand up from chair |
| Q05 | - |  |  | SI | Stand on one leg - Right |
| Q06 | - |  |  | SI | Stand on one leg - Left |
| Q07 | - |  |  | SI | Climb box step - Right |
| Q08 | - |  |  | SI | Climb box step - Left |
| Q09 | - |  |  | SI | Descend box step - Right |
| Q10 | - |  |  | SI | Descend box step - Left |
| Q11 | - |  |  | SI | Lifts head |
| Q12 | - |  |  | SI | Gets to sitting |
| Q13 | - |  |  | SI | Rise from the floor |
| Q14 | - |  |  | SI | Stands on heels |
| Q15 | - |  |  | SI | Jump |
| Q16 | - |  |  | SI | Hop right leg |
| Q17 | - |  |  | SI | Hop left leg |
| Q18 | - |  |  | SI | Run (10m) |
| Q19 | - |  |  | SI | Notes |
| Q20 | - |  |  | SI | Seconds |
| Q21 | - |  |  | SI | Seconds |
| Q22 | - |  |  | SI | Stand |
| Q23 | - |  |  | SI | Time to raise from floor (Timed RFF): |
| Q24 | - |  |  | SI | Time to run/walk 10 meters |
| Q25 | - |  |  | SI | The North Star Ambulatory Assessment is a function... |
| Q26 | - |  |  | SI | Score |
| Q27 | - |  |  | SI | Classification |
| Q28 | - |  |  | SI | 0 - 34 |
| Q29 | - |  |  | SI | Lower scores correspond to higher levels of disabi... |
| Q30 | - |  |  | SI | 0 - 34: Lower scores correspond to higher levels o... |
| Q31 | - |  |  | SI | Time to raise from floor (Timed RFF) |
| Q32 | - |  |  | SI | Time to run/walk 10 meters |
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