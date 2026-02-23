# SQLUser.PAC_MenstrualHistoryProbs

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MENHP_RowId | bigint | PK |  | NO | - |
| ChildQ08DR | - |  |  | SI | Child Reference: Exam |
| MENHP_Code | varchar |  |  | NO | Code |
| MENHP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MENHP_CreatedDate | date |  |  | SI | Created Date |
| MENHP_CreatedTime | time |  |  | SI | Created Time |
| MENHP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MENHP_DateFrom | date |  |  | SI | DateFrom |
| MENHP_DateTo | date |  |  | SI | DateTo |
| MENHP_Desc | varchar |  |  | NO | Description |
| MENHP_Owner | varchar |  |  | SI | Owner |
| MENHP_UpdatedDate | date |  |  | SI | Updated Date |
| MENHP_UpdatedTime | time |  |  | SI | Updated Time |
| MENHP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Gestation (Weeks) |
| Q02 | - |  |  | SI | Birth weight (Grams) |
| Q03 | - |  |  | SI | Risks |
| Q04 | - |  |  | SI | Postmenstrual age |
| Q04ObsDR | - |  |  | SI | Postmenstrual age DR |
| Q05 | - |  |  | SI | Zone I is a circle, the radius of which extends fr... |
| Q06 | - |  |  | SI | Zone II extends centrifugally from the edge of zon... |
| Q07 | - |  |  | SI | Zone III is the residual crescent of retina anteri... |
| Q09 | - |  |  | SI | Comments |
| Q10 | - |  |  | SI | Follow-up |
| Q11 | - |  |  | SI | Diagram of the retina for annotation |
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