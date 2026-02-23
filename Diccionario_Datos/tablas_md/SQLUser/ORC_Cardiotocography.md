# SQLUser.ORC_Cardiotocography

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CARDI_RowId | bigint | PK |  | NO | - |
| CARDI_Code | varchar |  |  | NO | Code |
| CARDI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CARDI_CreatedDate | date |  |  | SI | Created Date |
| CARDI_CreatedTime | time |  |  | SI | Created Time |
| CARDI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CARDI_DateFrom | date |  |  | SI | Date From |
| CARDI_DateTo | date |  |  | SI | Date To |
| CARDI_Desc | varchar |  |  | NO | Description |
| CARDI_Owner | varchar |  |  | SI | Owner |
| CARDI_UpdatedDate | date |  |  | SI | Updated Date |
| CARDI_UpdatedTime | time |  |  | SI | Updated Time |
| CARDI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Edad |
| Q04 | - |  |  | SI | Puntaje por Edad |
| Q05 | - |  |  | SI | Condiciones |
| Q06 | - |  |  | SI | Índice de comorbilidad de Charlson (ICC) |
| Q07 | - |  |  | SI | Los datos de enfermedad hepática y diabetes son mu... |
| Q08 | - |  |  | SI | Puntaje |
| Q09 | - |  |  | SI | Clasificación |
| Q10 | - |  |  | SI | Un ICC más alto indica un mayor riesgo de muerte |
| Q11 | - |  |  | SI | 0 - 41 |
| Q12 | - |  |  | SI | El índice de comorbilidad de Charlson (ICC) predic... |
| Q13 | - |  |  | SI | 0-41: Un ICC más alto indica un mayor riesgo de mu... |
| Q14 | - |  |  | SI | Age Hidden |
| Q15 | - |  |  | SI | Puntaje ICC |
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