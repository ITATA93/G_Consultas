# SQLUser.ARC_ReasonWriteOff

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RW_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Frecuencia Cardiaca Máxima |
| Q03 | - |  |  | SI | % de Frecuencia Cardiaca Máxima |
| Q04 | - |  |  | SI | Presión Arterial Sistólica |
| Q04ObsDR | - |  |  | SI | Presión Arterial Sistólica DR |
| Q05 | - |  |  | SI | Presión Arterial Diastólica |
| Q05ObsDR | - |  |  | SI | Presión Arterial Diastólica DR |
| Q06 | - |  |  | SI | Presión Arterial Media |
| Q07 | - |  |  | SI | Frecuencia Cardiaca |
| Q07ObsDR | - |  |  | SI | Frecuencia Cardiaca DR |
| Q08 | - |  |  | SI | Saturación O2 |
| Q08ObsDR | - |  |  | SI | Saturación O2 DR |
| Q09 | - |  |  | SI | Escala de Borg |
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
| RW_Code | varchar |  |  | NO | Code |
| RW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RW_CreatedDate | date |  |  | SI | Created Date |
| RW_CreatedTime | time |  |  | SI | Created Time |
| RW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RW_CreditAdjFlag | varchar |  |  | SI | Credit Adjustment Flag |
| RW_DateFrom | date |  |  | SI | Date From |
| RW_DateTo | date |  |  | SI | Date To |
| RW_Desc | varchar |  |  | NO | Description |
| RW_Owner | varchar |  |  | SI | Owner |
| RW_UpdatedDate | date |  |  | SI | Updated Date |
| RW_UpdatedTime | time |  |  | SI | Updated Time |
| RW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| RW_WOReasonGroup_DR | bigint |  | FK | SI | Des Ref WOReasonGroup |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*