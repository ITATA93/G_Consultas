# questionnaire.QCLXXIR

> Ingreso Recuperación Procedimiento / Cirugía Menor / Endoscopia

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ingreso Recuperación Procedimiento / Cirugía Menor / Endoscopia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | time |  |  | SI | Hora Ingreso |
| Q02 | varchar |  |  | SI | Valoración General |
| Q03 | varchar |  |  | SI | Temporalidad Recuperación |
| Q04 | varchar |  |  | SI | Estado mental / Emocional |
| Q05 | varchar |  |  | SI | Otro |
| Q06 | varchar |  |  | SI | Nivel Sedación |
| Q07 | varchar |  |  | SI | Vía Aérea |
| Q08 | varchar |  |  | SI | Otro |
| Q09 | varchar |  |  | SI | Respiración |
| Q10 | varchar |  |  | SI | Otro |
| Q11 | varchar |  |  | SI | Cardiaco |
| Q12 | varchar |  |  | SI | Otro |
| Q13 | varchar |  |  | SI | Estado de la Piel |
| Q14 | varchar |  |  | SI | Prevención Caídas |
| Q15 | varchar |  |  | SI | Cama Baja |
| Q16 | varchar |  |  | SI | Comentarios |
| Q17 | varchar |  |  | SI | Barandas en Alto |
| Q18 | varchar |  |  | SI | Comentarios |
| Q19 | varchar |  |  | SI | Paciente Vigilado |
| Q20 | varchar |  |  | SI | Comentarios |
| Q21 | varchar |  |  | SI | Freno Activado |
| Q22 | varchar |  |  | SI | Comentarios |
| Q23 | varchar |  |  | SI | Timbre a Mano |
| Q24 | varchar |  |  | SI | Comentarios |
| Q25 | varchar |  |  | SI | Observaciones Generales |
| Q26 | varchar |  |  | SI | Uso de Medidas de Sujeción |
| Q27 | varchar |  |  | SI | Comentarios |
| Q28 | varchar |  |  | SI | Levantar Asistido |
| Q29 | varchar |  |  | SI | Comentarios |
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