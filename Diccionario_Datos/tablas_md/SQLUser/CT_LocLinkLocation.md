# SQLUser.CT_LocLinkLocation

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINK_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| LINK_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| LINK_Childsub | double |  |  | NO | Childsub |
| LINK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LINK_CreatedDate | date |  |  | SI | Created Date |
| LINK_CreatedTime | time |  |  | SI | Created Time |
| LINK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LINK_RowId | varchar |  |  | NO | - |
| LINK_UpdatedDate | date |  |  | SI | Updated Date |
| LINK_UpdatedTime | time |  |  | SI | Updated Time |
| LINK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Discharge Summary Completed and Given |
| Q02 | - |  |  | SI | Discharge Information Sheet Explained and Given |
| Q03 | - |  |  | SI | Lines Removed |
| Q04 | - |  |  | SI | Wound Inspected |
| Q05 | - |  |  | SI | No Bleeding / Haematoma |
| Q06 | - |  |  | SI | Medication Prescription Given |
| Q07 | - |  |  | SI | Follow-up Appointment Arranged or Patient Aware to... |
| Q08 | - |  |  | SI | Valuables / Belongings Returned |
| Q09 | - |  |  | SI | Escort to Accompany Patient |
| Q10 | - |  |  | SI | GP Copy |
| Q11 | - |  |  | SI | Patient Copy |
| Q12 | - |  |  | SI | Patient's own X-Rays returned to patient |
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