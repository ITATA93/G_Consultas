# SQLUser.LB_Request

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRQ_RowID | bigint | PK |  | NO | - |
| LBRQ_CollectionDate | date |  |  | SI | Collection Date of Request |
| LBRQ_CollectionTime | time |  |  | SI | Collection Time of Request |
| LBRQ_EntryDate | date |  |  | SI | Request Date |
| LBRQ_EntryTime | time |  |  | SI | Request Time |
| LBRQ_Number | varchar |  |  | NO | Lab Request Number  |
| LBRQ_ReceivedDate | date |  |  | SI | Received Date of Request |
| LBRQ_ReceivedTime | time |  |  | SI | Received Time of Request |
| LBRQ_User_DR | bigint |  | FK | SI | User Id
User who created the record |
| Q01 | - |  |  | SI | Orientación Temporal |
| Q02 | - |  |  | SI | Orientación Espacial |
| Q03 | - |  |  | SI | Fijación  - Recuerdo Inmediato |
| Q03a | - |  |  | SI | N° de Repeticiones Necesarias |
| Q04 | - |  |  | SI | Atención - Cálculo |
| Q05 | - |  |  | SI | Recuerdo Diferido |
| Q07 | - |  |  | SI | Denominación |
| Q08 | - |  |  | SI | Repetición |
| Q09 | - |  |  | SI | Órdenes |
| Q10 | - |  |  | SI | Lectura |
| Q11 | - |  |  | SI | Escritura |
| Q12 | - |  |  | SI | Copia |
| Q13 | - |  |  | SI | Link a Pentágonos |
| Q14 | - |  |  | SI | Resultado MMSE |
| Q14ObsDR | - |  |  | SI | Resultado MMSE DR |
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