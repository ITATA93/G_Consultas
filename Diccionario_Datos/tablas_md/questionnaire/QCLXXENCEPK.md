# questionnaire.QCLXXENCEPK

> Encuesta de Salud para la Ejecución de Procedimientos de Kinesioterapia Motora

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Encuesta de Salud para la Ejecución de Procedimientos de Kinesioterapia Motora

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Edad |
| Q02 | varchar |  |  | SI | Paciente |
| Q03 | varchar |  |  | SI | Apoderado |
| Q04 | varchar |  |  | SI | Médico Responsable |
| Q05 | varchar |  |  | SI | Diagnóstico Médico |
| Q06 | varchar |  |  | SI | Indicación Médica |
| Q07 | varchar |  |  | SI | ¿Es Hipertenso (a)? |
| Q08 | varchar |  |  | SI | Si es Hipertenso (a) ¿está controlado (a)? |
| Q09 | varchar |  |  | SI | ¿Es paciente con patología cardíaca? |
| Q10 | varchar |  |  | SI | ¿Utiliza marcapasos? |
| Q11 | varchar |  |  | SI | Sexo |
| Q12 | varchar |  |  | SI | ¿Está embarazada? |
| Q13 | varchar |  |  | SI | ¿Es Diabético (a)? |
| Q14 | varchar |  |  | SI | Si es Diabético (a) ¿está controlado (a)? |
| Q15 | varchar |  |  | SI | ¿Se ha sometido a alguna intervención quirúrgica e... |
| Q16 | varchar |  |  | SI | ¿Cuál/es? |
| Q17 | varchar |  |  | SI | ¿Utiliza algún tipo de prótesis traumatológica? |
| Q18 | varchar |  |  | SI | ¿Padece alguna enfermedad crónica? |
| Q19 | varchar |  |  | SI | ¿Cuál/es? |
| Q20 | varchar |  |  | SI | ¿Ingiere alguno de estos medicamentos? (Medicament... |
| Q21 | varchar |  |  | SI | Nombre/s |
| Q22 | varchar |  |  | SI | ¿Recibió indicaciones escritas antes de iniciar su... |
| Q23 | varchar |  |  | SI | ¿Ha presentado o presenta alguna alteración de sen... |
| Q24 | varchar |  |  | SI | ¿Ha presentado caídas en los últimos 3 meses? |
| Q25 | varchar |  |  | SI | ¿Presenta o ha presentado alguna enfermedad o cond... |
| Q26 | varchar |  |  | SI | ¿Utiliza alguna ayuda técnica? como bastones, sill... |
| Q27 | varchar |  |  | SI | ¿Cual? |
| Q28 | varchar |  |  | SI | ¿Presenta alguna alteración visual o auditiva? |
| Q29 | varchar |  |  | SI | Medicamentos |
| Q30 | varchar |  |  | SI | Otros Medicamentos |
| Q31 | varchar |  |  | SI | Comentarios Adicionales |
| Q32 | varchar |  |  | SI | Nombre Kinesiologo (a) |
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