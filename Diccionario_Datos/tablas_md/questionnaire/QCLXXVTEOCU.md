# questionnaire.QCLXXVTEOCU

> Ingreso Valoración de Terapia Ocupacional

**Schema:** questionnaire
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Valoración de Terapia Ocupacional

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Ingreso |
| Q02 | time |  |  | SI | Hora de Ingreso |
| Q03 | varchar |  |  | SI | Contextualización |
| Q04 | varchar |  |  | SI | Higiene |
| Q05 | varchar |  |  | SI | Vestuario |
| Q06 | varchar |  |  | SI | Arreglo Personal |
| Q07 | varchar |  |  | SI | Uso de Medicamento |
| Q08 | varchar |  |  | SI | Observación (Autocuidado) |
| Q09 | varchar |  |  | SI | Preparación de Alimento |
| Q10 | varchar |  |  | SI | Uso Medios de Comunicación |
| Q11 | varchar |  |  | SI | Cuidado de Hijos |
| Q12 | varchar |  |  | SI | Gestión y Movilidad en la Comunidad |
| Q13 | varchar |  |  | SI | Administración del Dinero |
| Q14 | varchar |  |  | SI | Gestión y Mantenimiento de Salud |
| Q15 | varchar |  |  | SI | Observación (Actividades Instrumentales) |
| Q16 | varchar |  |  | SI | Recreación |
| Q17 | varchar |  |  | SI | Observaciones (Recreación) |
| Q18 | varchar |  |  | SI | Trabajo |
| Q19 | varchar |  |  | SI | Observaciones (Trabajo) |
| Q20 | varchar |  |  | SI | Educación |
| Q21 | varchar |  |  | SI | Educación (Finalización) |
| Q22 | varchar |  |  | SI | Capacitaciones |
| Q23 | varchar |  |  | SI | Observaciones (Educaciones) |
| Q24 | varchar |  |  | SI | Participación Social |
| Q25 | varchar |  |  | SI | Observaciones (Participación Social) |
| Q26 | varchar |  |  | SI | Roles |
| Q27 | varchar |  |  | SI | Rutina |
| Q29 | varchar |  |  | SI | Rutina Diaria  Mañana (Lunes a Viernes) |
| Q30 | varchar |  |  | SI | Rutina Diaria Tarde (Lunes a Viernes) |
| Q31 | varchar |  |  | SI | Rutina Diaria Manaña (Sábado y Domingo) |
| Q32 | varchar |  |  | SI | Rutina Diaria Tarde (Sábado y Domingo) |
| Q33 | varchar |  |  | SI | Movilidad Global |
| Q34 | varchar |  |  | SI | Tolerancia al Esfuerzo |
| Q35 | varchar |  |  | SI | Destreza Fina |
| Q36 | varchar |  |  | SI | Ritmo y Fluidez de Movimiento |
| Q37 | varchar |  |  | SI | Visoperceptuales |
| Q38 | varchar |  |  | SI | Equilibrio |
| Q39 | varchar |  |  | SI | Orientación |
| Q40 | varchar |  |  | SI | Memoria |
| Q41 | varchar |  |  | SI | Atención y Concentración |
| Q42 | varchar |  |  | SI | Resolución de Problemas |
| Q43 | varchar |  |  | SI | Contacto Social |
| Q44 | varchar |  |  | SI | Participación Grupal |
| Q45 | varchar |  |  | SI | Comunicación |
| Q46 | varchar |  |  | SI | Tolerancia Frustración |
| Q47 | varchar |  |  | SI | Respuesta a Crítica |
| Q48 | varchar |  |  | SI | Autocontrol |
| Q49 | varchar |  |  | SI | Motivación de Logro |
| Q50 | varchar |  |  | SI | Social Comunitario |
| Q51 | varchar |  |  | SI | Familia |
| Q52 | varchar |  |  | SI | Amigos |
| Q53 | varchar |  |  | SI | Trabajo / Estudio |
| Q54 | varchar |  |  | SI | Comunidad |
| Q55 | varchar |  |  | SI | Intereses |
| Q56 | varchar |  |  | SI | Proyecto Vital |
| Q57 | varchar |  |  | SI | Áreas Ocupacionales Exitosas |
| Q58 | varchar |  |  | SI | Áreas Ocupacionales en Riesgo |
| Q59 | varchar |  |  | SI | Objetivos |
| Q60 | varchar |  |  | SI | Estrategias |
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