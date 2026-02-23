# SQLUser.ARC_PackageGroupType

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PKGRTYPE_RowId | bigint | PK |  | NO | - |
| PKGRTYPE_Code | varchar |  |  | NO | Code |
| PKGRTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PKGRTYPE_CreatedDate | date |  |  | SI | Created Date |
| PKGRTYPE_CreatedTime | time |  |  | SI | Created Time |
| PKGRTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PKGRTYPE_DateFrom | date |  |  | SI | Date From |
| PKGRTYPE_DateTo | date |  |  | SI | Date To |
| PKGRTYPE_Desc | varchar |  |  | NO | Description |
| PKGRTYPE_Owner | varchar |  |  | SI | Owner |
| PKGRTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| PKGRTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| PKGRTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Profesional de Registro |
| Q02 | - |  |  | SI | Fecha Llamada |
| Q03 | - |  |  | SI | Hora Llamada |
| Q04 | - |  |  | SI | Detalles de la Cirugía |
| Q05 | - |  |  | SI | Cirugía Principal |
| Q06 | - |  |  | SI | Cirugía Secundaria |
| Q07 | - |  |  | SI | Fecha Cirugía |
| Q08 | - |  |  | SI | Nombre Cirujano |
| Q09 | - |  |  | SI | Nombre Anestesista |
| Q10 | - |  |  | SI | Tipo de Cirugía |
| Q11 | - |  |  | SI | Es laparoscópica? |
| Q12 | - |  |  | SI | Otros antecedentes relevantes de la Intervención Q... |
| Q13 | - |  |  | SI | Detalles de la Entrevista |
| Q14 | - |  |  | SI | Estado General Referido por el Paciente |
| Q15 | - |  |  | SI | Comentarios Estado General |
| Q16 | - |  |  | SI | Fiebre Referida por el Paciente |
| Q17 | - |  |  | SI | Comentarios Fiebre Referida |
| Q18 | - |  |  | SI | Dificultad Respiratoria |
| Q19 | - |  |  | SI | Comentarios Dificultad Respiratoria |
| Q20 | - |  |  | SI | Movilidad y Desplazamiento |
| Q21 | - |  |  | SI | Comentarios Movilidad y Desplazamiento |
| Q22 | - |  |  | SI | Náuseas y Vómitos |
| Q22ObsDR | - |  |  | SI | Náuseas y Vómitos DR |
| Q23 | - |  |  | SI | Comentarios Náuseas y Vómitos |
| Q24 | - |  |  | SI | Adherencia al Régimen Alimentario Indicado |
| Q25 | - |  |  | SI | Comentarios Adherencia Régimen Alimentario |
| Q26 | - |  |  | SI | Tolerancia a la Alimentación |
| Q27 | - |  |  | SI | Comentarios Tolerancia Alimentación |
| Q28 | - |  |  | SI | Eliminación de Gases |
| Q29 | - |  |  | SI | Comentarios Eliminación de Gases |
| Q30 | - |  |  | SI | Deposiciones |
| Q31 | - |  |  | SI | Comentarios Deposiciones |
| Q32 | - |  |  | SI | Diuresis |
| Q33 | - |  |  | SI | Comentarios Diuresis |
| Q34 | - |  |  | SI | Sangramiento |
| Q35 | - |  |  | SI | Comentarios Sangramiento |
| Q36 | - |  |  | SI | Estado Zona Operatoria |
| Q37 | - |  |  | SI | Comentarios Zona Operatoria |
| Q38 | - |  |  | SI | Instrucciones sobre Administración de Medicamentos |
| Q39 | - |  |  | SI | Comentarios Instrucciones Medicamentos |
| Q40 | - |  |  | SI | Observaciones Generales |
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