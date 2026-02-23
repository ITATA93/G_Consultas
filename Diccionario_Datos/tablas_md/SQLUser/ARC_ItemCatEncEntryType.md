# SQLUser.ARC_ItemCatEncEntryType

**Schema:** SQLUser
**Columnas:** 59
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ETYPE_ParRef | bigint | PK |  | NO | ARC_ItemCat Parent Reference |
| ETYPE_Childsub | double |  |  | NO | Childsub |
| ETYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ETYPE_CreatedDate | date |  |  | SI | Created Date |
| ETYPE_CreatedTime | time |  |  | SI | Created Time |
| ETYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ETYPE_DateFrom | date |  |  | SI | Date From |
| ETYPE_DateTo | date |  |  | SI | Date To |
| ETYPE_EncEntryType_DR | bigint |  | FK | SI | Des Ref EncEntryType |
| ETYPE_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| ETYPE_RowId | varchar |  |  | NO | - |
| ETYPE_UpdatedDate | date |  |  | SI | Updated Date |
| ETYPE_UpdatedTime | time |  |  | SI | Updated Time |
| ETYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QAPPTID | - |  |  | SI | Appointment ID |
| QATENTMPODEF | - |  |  | SI | Atención Establecido en Tiempo de Protocolo |
| QCONDCLI | - |  |  | SI | Consulta Pertinente según Condición Clínica |
| QPERTINENCIA | - |  |  | SI | Pertinencia |
| QREFSEGPROT | - |  |  | SI | Referencia según Protocolo |
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