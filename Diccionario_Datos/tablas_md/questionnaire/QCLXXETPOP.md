# questionnaire.QCLXXETPOP

> Encuesta Telefónica Post Alta Paciente Quirúrgico

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Encuesta Telefónica Post Alta Paciente Quirúrgico

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Profesional de Registro |
| Q02 | date |  |  | SI | Fecha Llamada |
| Q03 | time |  |  | SI | Hora Llamada |
| Q04 | varchar |  |  | SI | Detalles de la Cirugía |
| Q05 | varchar |  |  | SI | Cirugía Principal |
| Q06 | varchar |  |  | SI | Cirugía Secundaria |
| Q07 | date |  |  | SI | Fecha Cirugía |
| Q08 | varchar |  |  | SI | Nombre Cirujano |
| Q09 | varchar |  |  | SI | Nombre Anestesista |
| Q10 | varchar |  |  | SI | Tipo de Cirugía |
| Q11 | varchar |  |  | SI | Es laparoscópica? |
| Q12 | varchar |  |  | SI | Otros antecedentes relevantes de la Intervención Q... |
| Q13 | varchar |  |  | SI | Detalles de la Entrevista |
| Q14 | varchar |  |  | SI | Estado General Referido por el Paciente |
| Q15 | varchar |  |  | SI | Comentarios Estado General |
| Q16 | varchar |  |  | SI | Fiebre Referida por el Paciente |
| Q17 | varchar |  |  | SI | Comentarios Fiebre Referida |
| Q18 | varchar |  |  | SI | Dificultad Respiratoria |
| Q19 | varchar |  |  | SI | Comentarios Dificultad Respiratoria |
| Q20 | varchar |  |  | SI | Movilidad y Desplazamiento |
| Q21 | varchar |  |  | SI | Comentarios Movilidad y Desplazamiento |
| Q22 | varchar |  |  | SI | Náuseas y Vómitos |
| Q22ObsDR | varchar |  | FK | SI | Náuseas y Vómitos DR |
| Q23 | varchar |  |  | SI | Comentarios Náuseas y Vómitos |
| Q24 | varchar |  |  | SI | Adherencia al Régimen Alimentario Indicado |
| Q25 | varchar |  |  | SI | Comentarios Adherencia Régimen Alimentario |
| Q26 | varchar |  |  | SI | Tolerancia a la Alimentación |
| Q27 | varchar |  |  | SI | Comentarios Tolerancia Alimentación |
| Q28 | varchar |  |  | SI | Eliminación de Gases |
| Q29 | varchar |  |  | SI | Comentarios Eliminación de Gases |
| Q30 | varchar |  |  | SI | Deposiciones |
| Q31 | varchar |  |  | SI | Comentarios Deposiciones |
| Q32 | varchar |  |  | SI | Diuresis |
| Q33 | varchar |  |  | SI | Comentarios Diuresis |
| Q34 | varchar |  |  | SI | Sangramiento |
| Q35 | varchar |  |  | SI | Comentarios Sangramiento |
| Q36 | varchar |  |  | SI | Estado Zona Operatoria |
| Q37 | varchar |  |  | SI | Comentarios Zona Operatoria |
| Q38 | varchar |  |  | SI | Instrucciones sobre Administración de Medicamentos |
| Q39 | varchar |  |  | SI | Comentarios Instrucciones Medicamentos |
| Q40 | varchar |  |  | SI | Observaciones Generales |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*