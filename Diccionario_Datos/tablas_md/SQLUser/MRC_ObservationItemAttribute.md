# SQLUser.MRC_ObservationItemAttribute

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ATTR_ParRef | bigint | PK |  | NO | MRC_ObservationItem Parent Reference |
| ATTR_BottleCount | varchar |  |  | SI | - |
| ATTR_Childsub | double |  |  | NO | Childsub |
| ATTR_Code | varchar |  |  | NO | Code |
| ATTR_CreatedDate | date |  |  | SI | Created Date |
| ATTR_CreatedTime | time |  |  | SI | Created Time |
| ATTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ATTR_DateFrom | date |  |  | SI | Active Date From for new Observation Entries |
| ATTR_DateTo | date |  |  | SI | Active Date To for new Observation Entries |
| ATTR_Deprecated | bit |  |  | SI | Deprecated |
| ATTR_DeprecatedReason | varchar |  |  | SI | Deprecated |
| ATTR_Desc | varchar |  |  | NO | Description |
| ATTR_Generated | varchar |  |  | SI | Response has been used in previous data - Code/Typ... |
| ATTR_InputType | varchar |  |  | SI | Input Type |
| ATTR_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| ATTR_RowId | varchar |  |  | NO | - |
| ATTR_Sequence | double |  |  | SI | - |
| ATTR_UpdatedDate | date |  |  | SI | Updated Date |
| ATTR_UpdatedTime | time |  |  | SI | Updated Time |
| ATTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Mes |
| Q02 | - |  |  | SI | Año |
| Q03 | - |  |  | SI | Edad |
| Q04 | - |  |  | SI | Abortos |
| Q05 | - |  |  | SI | Partos |
| Q06 | - |  |  | SI | Causal |
| Q07 | - |  |  | SI | Beneficiarias |
| Q08 | - |  |  | SI | Pueblos Originarios |
| Q09 | - |  |  | SI | Migrantes |
| QHR | - |  |  | SI | Establecimiento de Salud |
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