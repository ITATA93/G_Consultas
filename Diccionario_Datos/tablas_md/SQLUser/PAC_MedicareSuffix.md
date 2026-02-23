# SQLUser.PAC_MedicareSuffix

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MEDSUF_RowId | bigint | PK |  | NO | - |
| MEDSUF_Code | varchar |  |  | NO | Code |
| MEDSUF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MEDSUF_CreatedDate | date |  |  | SI | Created Date |
| MEDSUF_CreatedTime | time |  |  | SI | Created Time |
| MEDSUF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEDSUF_DateFrom | date |  |  | SI | Date From |
| MEDSUF_DateTo | date |  |  | SI | Date To |
| MEDSUF_Default | varchar |  |  | SI | Default |
| MEDSUF_Desc | varchar |  |  | NO | Description |
| MEDSUF_Owner | varchar |  |  | SI | Owner |
| MEDSUF_UpdatedDate | date |  |  | SI | Updated Date |
| MEDSUF_UpdatedTime | time |  |  | SI | Updated Time |
| MEDSUF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient is able to get about the house (indoor wal... |
| Q04 | - |  |  | SI | Patient is able to get out of the house (outdoor w... |
| Q05 | - |  |  | SI | Patient is able to go shopping (walking during sho... |
| Q06 | - |  |  | SI | Score |
| Q07 | - |  |  | SI | Classification |
| Q08 | - |  |  | SI | 0 - 9 |
| Q09 | - |  |  | SI | A higher score indicates a better level of mobilit... |
| Q10 | - |  |  | SI | 0 - 9: A higher score indicates a better level of ... |
| Q11 | - |  |  | SI | The New Mobility Score (NMS) is a valid and easily... |
| Q12 | - |  |  | SI | and discharge status |
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