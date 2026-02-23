# SQLUser.OEC_Sentence

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SENT_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Location |
| Q02 | - |  |  | SI | Swelling |
| Q02N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Fever |
| Q03N | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Chills |
| Q04N | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Drainage |
| Q05N | - |  |  | SI | Note |
| Q06 | - |  |  | SI | History of diabetes mellitus |
| Q06N | - |  |  | SI | Note |
| Q07 | - |  |  | SI | History of diabetes mellitus checkbox |
| Q08 | - |  |  | SI | History of peripheral vascular disease |
| Q08N | - |  |  | SI | Note |
| Q09 | - |  |  | SI | History of gangrene / amputations |
| Q09N | - |  |  | SI | Note |
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
| SENT_ARCIM_DR | varchar |  | FK | NO | Order Item |
| SENT_AdminRouteIVType | varchar |  |  | SI | Administration IV Type |
| SENT_AdminRoute_DR | bigint |  | FK | SI | Administration Route |
| SENT_AgeFrom | integer |  |  | SI | Lower Age Boundary (inclusive) |
| SENT_AgeFromUnit | varchar |  |  | SI | Lower Age Boundary Unit |
| SENT_AgeTo | integer |  |  | SI | Upper Age Boundary (inclusive) |
| SENT_AgeToUnit | varchar |  |  | SI | Upper Age Boundary Unit |
| SENT_BSAFormula | varchar |  |  | SI | BSA Formula |
| SENT_BSAFrom | double |  |  | SI | Lower BSA Boundary (inclusive) |
| SENT_BSATo | double |  |  | SI | Upper BSA Boundary (inclusive) |
| SENT_Code | varchar |  |  | SI | Code
Required attribute removed, currently not ap... |
| SENT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SENT_CreatedDate | date |  |  | SI | Created Date |
| SENT_CreatedTime | time |  |  | SI | Created Time |
| SENT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SENT_DateFrom | date |  |  | SI | Date From |
| SENT_DateTo | date |  |  | SI | Date To |
| SENT_Desc | varchar |  |  | NO | Description |
| SENT_Owner | varchar |  |  | SI | Owner |
| SENT_Params_DR | bigint |  | FK | SI | Order Item Details - Default Parameters |
| SENT_Sequence | integer |  |  | SI | Sequence Sort Order |
| SENT_Sex_DR | bigint |  | FK | SI | Sex restriction |
| SENT_UpdatedDate | date |  |  | SI | Updated Date |
| SENT_UpdatedTime | time |  |  | SI | Updated Time |
| SENT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SENT_WeightFrom | integer |  |  | SI | Lower Weight Boundary (inclusive) |
| SENT_WeightFromUnit | varchar |  |  | SI | Lower Weight Boundary Unit |
| SENT_WeightTo | integer |  |  | SI | Upper Weight Boundary (inclusive) |
| SENT_WeightToUnit | varchar |  |  | SI | Upper Weight Boundary Unit |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*