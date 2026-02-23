# SQLUser.MRC_ICDDxExtRef

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ExtRef_ParRef | bigint | PK |  | NO | MRC_ICDDx Parent Reference |
| ExtRef_Childsub | double |  |  | NO | Childsub |
| ExtRef_Code | varchar |  |  | SI | Code |
| ExtRef_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| ExtRef_Comment | varchar |  |  | SI | Comments |
| ExtRef_DateFrom | date |  |  | SI | Date from |
| ExtRef_DateTo | date |  |  | SI | Date to |
| ExtRef_Description | varchar |  |  | SI | Description |
| ExtRef_Hospital_DR | bigint |  | FK | SI | Hospital |
| ExtRef_RowId | varchar |  |  | NO | - |
| ExtRef_Trust_DR | bigint |  | FK | SI | Trust |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Servicio o Unidad |
| Q04 | - |  |  | SI | Diagnóstico Ingreso |
| Q05 | - |  |  | SI | Condición Actual del Paciente |
| Q06 | - |  |  | SI | Información del Lugar en qeu se Realizó la Atenció... |
| Q07 | - |  |  | SI | Descripción de lo Sucedido Detallando Hora de Ocur... |
| Q08 | - |  |  | SI | Intervenciones Realizadas con Fecha y Hora |
| Q09 | - |  |  | SI | Definición del Tipo de Evento |
| Q10 | - |  |  | SI | Nombre del Funcionario que Detecta el Evento Adver... |
| Q11 | - |  |  | SI | Nombre del Profesional que Realiza la Notificación |
| Q12 | - |  |  | SI | Jefatura que Recepciona la Notificación |
| Q13 | - |  |  | SI | Recepción Oficina de Calidad |
| Q14 | - |  |  | SI | Fecha 02 |
| Q15 | - |  |  | SI | Hora 02 |
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