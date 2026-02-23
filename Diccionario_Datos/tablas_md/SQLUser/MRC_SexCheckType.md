# SQLUser.MRC_SexCheckType

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SEXCHK_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Dolor |
| Q02 | - |  |  | SI | Función Distancia Caminada |
| Q03 | - |  |  | SI | Función Apoyos |
| Q04 | - |  |  | SI | Movilidad y Potencia Muscular, Capacidad de Movili... |
| Q05 | - |  |  | SI | Cuidado de los Pies. Ej. Lavar y Secar los Pies |
| Q06 | - |  |  | SI | Claudicación |
| Q07 | - |  |  | SI | Escaleras |
| Q08 | - |  |  | SI | Resultado Evaluación Cadera Harris Modificado |
| Q08ObsDR | - |  |  | SI | Resultado Evaluación Cadera Harris Modificado DR |
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
| SEXCHK_Code | varchar |  |  | NO | Code |
| SEXCHK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SEXCHK_CreatedDate | date |  |  | SI | Created Date |
| SEXCHK_CreatedTime | time |  |  | SI | Created Time |
| SEXCHK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SEXCHK_DateFrom | date |  |  | SI | Date From |
| SEXCHK_DateTo | date |  |  | SI | Date To |
| SEXCHK_Desc | varchar |  |  | NO | Description |
| SEXCHK_Owner | varchar |  |  | SI | Owner |
| SEXCHK_UpdatedDate | date |  |  | SI | Updated Date |
| SEXCHK_UpdatedTime | time |  |  | SI | Updated Time |
| SEXCHK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*