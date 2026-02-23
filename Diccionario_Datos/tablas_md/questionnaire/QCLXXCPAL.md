# questionnaire.QCLXXCPAL

> Chequeo Al Alta

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Chequeo Al Alta

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Realización Chequeo |
| Q02 | time |  |  | SI | Hora Realización Chequeo |
| Q03 | varchar |  |  | SI | Chequeo Salida Recuperación |
| Q04 | varchar |  |  | SI | Puntaje Escala Aldrete >= 9 puntos |
| Q05 | varchar |  |  | SI | Comentarios |
| Q06 | varchar |  |  | SI | Retiro Dispositivos Invasivos |
| Q07 | varchar |  |  | SI | Comentarios |
| Q08 | varchar |  |  | SI | Evolución Médica previa al alta |
| Q09 | varchar |  |  | SI | Comentarios |
| Q10 | varchar |  |  | SI | Chequeo entrega de pertenencias al Paciente / Acom... |
| Q11 | varchar |  |  | SI | Comentarios |
| Q12 | varchar |  |  | SI | Retiro en Silla de Ruedas |
| Q13 | varchar |  |  | SI | Comentarios |
| Q14 | varchar |  |  | SI | Informe del Procedimiento / Intervención |
| Q15 | varchar |  |  | SI | Comentarios |
| Q16 | varchar |  |  | SI | Indicaciones al Alta (Verbal o Escrita) |
| Q17 | varchar |  |  | SI | Comentarios |
| Q18 | varchar |  |  | SI | Paciente Recibe Conforme y se retira acompañado po... |
| Q19 | varchar |  |  | SI | Nombre |
| Q20 | varchar |  |  | SI | RUN |
| Q21 | varchar |  |  | SI | Observaciones Egreso Recuperación |
| Q22 | varchar |  |  | SI | Enfermera / Matrona Responsable |
| Q23 | varchar |  |  | SI | TENS / TONS Responsable |
| Q24 | varchar |  |  | SI | Indicaciones para el retiro de Biopsias |
| Q25 | varchar |  |  | SI | Comentarios |
| Q26 | varchar |  |  | SI | Entrega de Exámenes Previos al Paciente/Acompañant... |
| Q27 | varchar |  |  | SI | Comentarios |
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