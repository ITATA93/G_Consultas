# SQLUser.ARC_PostOffice

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| POSTOFC_RowId | bigint | PK |  | NO | - |
| ChildQ27DR | - |  |  | SI | Child Reference: Firma de profesionales |
| POSTOFC_Code | varchar |  |  | NO | Code |
| POSTOFC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| POSTOFC_CreatedDate | date |  |  | SI | Created Date |
| POSTOFC_CreatedTime | time |  |  | SI | Created Time |
| POSTOFC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| POSTOFC_DateFrom | date |  |  | SI | Date From |
| POSTOFC_DateTo | date |  |  | SI | Date To |
| POSTOFC_Desc | varchar |  |  | NO | Description |
| POSTOFC_InterfaceCoding_DR | bigint |  | FK | SI | Des Ref CTInterfaceCodingSystem |
| POSTOFC_Owner | varchar |  |  | SI | Owner |
| POSTOFC_UpdatedDate | date |  |  | SI | Updated Date |
| POSTOFC_UpdatedTime | time |  |  | SI | Updated Time |
| POSTOFC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora de Evaluación |
| Q03 | - |  |  | SI | Fisiatra que deriva |
| Q04 | - |  |  | SI | Impresión General |
| Q05 | - |  |  | SI | Habilidades Motoras |
| Q06 | - |  |  | SI | Actividades de la vida diaria |
| Q07 | - |  |  | SI | Cognición, Comunicación y Lenguaje |
| Q08 | - |  |  | SI | Área Servicio Social |
| Q09 | - |  |  | SI | Área Psicología |
| Q10 | - |  |  | SI | Enfermería |
| Q11 | - |  |  | SI | Dental |
| Q12 | - |  |  | SI | Ayuda Técnica |
| Q13 | - |  |  | SI | Situación Educativa |
| Q14 | - |  |  | SI | ¿Cuáles son los problemas principales que le dific... |
| Q15 | - |  |  | SI | Recibe o ha recibido rehabilitación en otro centro |
| Q16 | - |  |  | SI | Modalidad de Atención Sugerida |
| Q17 | - |  |  | SI | Objetivos Funcionales |
| Q18 | - |  |  | SI | Indicaciones |
| Q19 | - |  |  | SI | Registros Médicos |
| Q20 | - |  |  | SI | Citaciones Especialista |
| Q21 | - |  |  | SI | Citación Médico |
| Q22 | - |  |  | SI | Comentarios Citación |
| Q23 | - |  |  | SI | Diagnóstico |
| Q24 | - |  |  | SI | I Datos Personales |
| Q25 | - |  |  | SI | II Evaluación Integral |
| Q26 | - |  |  | SI | III Asistencia Profesionales Firmada |
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