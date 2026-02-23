# questionnaire.QCLXXTACV

> Tele ACV

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario Regional Chile**. Formulario de evaluación clínica adaptado para Chile. *(Tele ACV)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Lugar Inicio Síntomas |
| Q02 | varchar |  |  | SI | Hubo Llamdo a Ambulancia |
| Q03 | varchar |  |  | SI | Se contactó a hospital antes de la llegada del pac... |
| Q04 | varchar |  |  | SI | ¿Se activó código ACV? |
| Q05 | varchar |  |  | SI | Medio de transporte en que paciente llega al hospi... |
| Q06 | time |  |  | SI | Hora Inicio de Síntomas |
| Q07 | varchar |  |  | SI | Hora Ingreso Admisión |
| Q08 | time |  |  | SI | Hora Triage Enfermería |
| Q09 | varchar |  |  | SI | Valor triage enfermería |
| Q10 | time |  |  | SI | Hora en que se solicitan los exámenes de laborator... |
| Q11 | time |  |  | SI | Hora en que los exámenes de sangre llegan al labor... |
| Q12 | time |  |  | SI | Hora atención médico urgencias |
| Q13 | time |  |  | SI | Hora inicio contacto telefónico neurólogo |
| Q14 | varchar |  |  | SI | Médico Urgenciólogo que presenta al paciente |
| Q15 | time |  |  | SI | Hora Inicio Teleconsulta Tele- ACV |
| Q16 | time |  |  | SI | Hora TAC Cerebral |
| Q17 | time |  |  | SI | Hora de Visualización TAC por Tele ACV |
| Q18 | varchar |  |  | SI | Diagnóstico de la Teleconsulta |
| Q19 | time |  |  | SI | Hora de la Decisión Terapéutica |
| Q20 | time |  |  | SI | Hora Inicio Trombolisis |
| Q201 | bit |  |  | SI | No Aplica |
| Q21 | varchar |  |  | SI | ¿Se logra el tiempo puerta aguja menor a 60 minuto... |
| Q22 | varchar |  |  | SI | NIHSS Ingreso  |
| Q23 | varchar |  |  | SI | NIHSS al Final de Trombolisis |
| Q24 | varchar |  |  | SI | NIHSS 24 Horas Post Trombolisis |
| Q25 | numeric |  |  | SI | RANKIN Estimado de Ingreso |
| Q26 | numeric |  |  | SI | RANKIN Estimado de Alta |
| Q28 | numeric |  |  | SI | NIHSS Ingreso Valor |
| Q29 | numeric |  |  | SI | NIHSS al Final de Trombolisis Valor |
| Q30 | numeric |  |  | SI | NIHSS 24 Horas Post Trombolisis Valor |
| Q31 | varchar |  |  | SI | Comentarios |
| Q32 | time |  |  | SI | Hora de resultado de examenes de laboratorio |
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