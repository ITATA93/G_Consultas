# SQLUser.MRC_CancerType

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANT_RowId | bigint | PK |  | NO | - |
| CANT_Code | varchar |  |  | NO | Code |
| CANT_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CANT_CreatedDate | date |  |  | SI | Created Date |
| CANT_CreatedTime | time |  |  | SI | Created Time |
| CANT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANT_DateFrom | date |  |  | SI | Date From |
| CANT_DateTo | date |  |  | SI | Date To |
| CANT_Desc | varchar |  |  | NO | Description |
| CANT_Owner | varchar |  |  | SI | Code Table Owner |
| CANT_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept [DEPRECATED] TC-123322 Re... |
| CANT_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms 	[DEPRECATED] TC-123322 Rep... |
| CANT_UpdatedDate | date |  |  | SI | Updated Date |
| CANT_UpdatedTime | time |  |  | SI | Updated Time |
| CANT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Confirmación Diagnóstica GES |
| Q02 | - |  |  | SI | Constancia |
| Q03 | - |  |  | SI | Importante |
| Q04 | - |  |  | SI | Fecha de Notificación |
| Q05 | - |  |  | SI | Hora de Notificación |
| Q06 | - |  |  | SI | Nombre |
| Q07 | - |  |  | SI | RUN |
| Q08 | - |  |  | SI | Teléfono Celular |
| Q09 | - |  |  | SI | Correo Electrónico |
| Q10 | - |  |  | SI | Nombre Profesional |
| Q11 | - |  |  | SI | Diagnóstico Ges |
| Q12 | - |  |  | SI | Observaciones |
| Q13 | - |  |  | SI | Nombre Institución |
| Q14 | - |  |  | SI | Rut Profesional |
| Q15 | - |  |  | SI | Nombre Paciente |
| Q16 | - |  |  | SI | Apellido Paterno Paciente |
| Q17 | - |  |  | SI | Apellido Materno Paciente |
| Q18 | - |  |  | SI | Rut Paciente |
| Q19 | - |  |  | SI | Previsión |
| Q20 | - |  |  | SI | Telefono Fijo Paciente |
| Q21 | - |  |  | SI | Celular |
| Q22 | - |  |  | SI | Correo Paciente |
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