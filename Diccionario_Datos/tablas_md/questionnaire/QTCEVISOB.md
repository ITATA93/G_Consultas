# questionnaire.QTCEVISOB

> Visita de Sobrevivencia

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Visita de Sobrevivencia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Antecedentes Del Paciente |
| Q02 | varchar |  |  | SI | Aseo Personal Observación |
| Q03 | varchar |  |  | SI | Alimentación Observación |
| Q04 | varchar |  |  | SI | Examen Físico General |
| Q05 | varchar |  |  | SI | Lesiones por Presión |
| Q06 | varchar |  |  | SI | Ubicación(es) |
| Q07 | varchar |  |  | SI | Dimension(es) |
| Q08 | varchar |  |  | SI | Aspecto |
| Q09 | varchar |  |  | SI | Evolución |
| Q10 | varchar |  |  | SI | Acciones a Realizar |
| Q11 | varchar |  |  | SI | Movilidad |
| Q12 | varchar |  |  | SI | Realiza Ejercicios Pasivos |
| Q13 | varchar |  |  | SI | Se Levanta al Paciente |
| Q14 | varchar |  |  | SI | Usa Silla de Ruedas |
| Q15 | varchar |  |  | SI | Se realizan cambios de posición |
| Q16 | varchar |  |  | SI | Observaciones |
| Q17 | varchar |  |  | SI | Antecedentes del Cuidador |
| Q18 | varchar |  |  | SI | Administración de Medicamentos por Parte del Cuida... |
| Q19 | varchar |  |  | SI | Se realiza Capacitación a Cuidador |
| Q20 | varchar |  |  | SI | Contenido de la Capacitación |
| Q21 | varchar |  |  | SI | Recepción de Pago de Estipendio |
| Q22 | date |  |  | SI | Fecha Último Retiro |
| Q23 | varchar |  |  | SI | Mes Cancelado Correspondiente |
| Q24 | varchar |  |  | SI | Comentarios |
| Q25 | varchar |  |  | SI | Cuidados de la Piel Observación |
| Q26 | varchar |  |  | SI | Uso de ayudas técnicas u ortesis |
| Q27 | varchar |  |  | SI | Resultado Dependencia Indice Barthel |
| Q27ObsDR | varchar |  | FK | SI | Resultado Dependencia Indice Barthel DR |
| Q28 | varchar |  |  | SI | Oncológico |
| Q29 | varchar |  |  | SI | Aseo Personal  |
| Q30 | varchar |  |  | SI | Estado de Uñas |
| Q31 | varchar |  |  | SI | Estado de Uñas Observación |
| Q32 | varchar |  |  | SI | Alimentación |
| Q33 | varchar |  |  | SI | Incontinencia |
| Q34 | varchar |  |  | SI | Incontinencia Observación |
| Q35 | varchar |  |  | SI | Formas de Apoyo a Incontinencia |
| Q36 | varchar |  |  | SI | Tendencia a Fecalomas |
| Q37 | varchar |  |  | SI | Cuidados de la Piel |
| Q38 | varchar |  |  | SI | Factores de Riesgo mas Importantes |
| Q39 | varchar |  |  | SI | Formas de Apoyo a Incontinencia Obs |
| Q40 | varchar |  |  | SI | Tendencia a Fecalomas Obs. |
| Q41 | varchar |  |  | SI | En espera de apoyo monetario |
| Q43 | varchar |  |  | SI | Se realiza evaluación de sobrecarga anual |
| Q44 | varchar |  |  | SI | EMPAM Vigente |
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