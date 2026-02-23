# questionnaire.QCLXXMCPRA

> Medidas de contención en Pacientes en Riesgo de Auto o Heterolesión

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Medidas de contención en Pacientes en Riesgo de Auto o Heterolesión

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1.- ¿Se utilizó previamente Contención Emocional?  |
| Q02 | varchar |  |  | SI | 2.- ¿Se utilizó previamente Contención Ambiental?  |
| Q03 | varchar |  |  | SI | 3.- ¿Se utilizó previamente Contención Farmacológi... |
| Q05 | varchar |  |  | SI | Contención Mecánica |
| Q06 | varchar |  |  | SI | 4. Existe Indicación Médica de Contención Mecánica |
| Q07 | varchar |  |  | SI | 5. Médico quien realiza Indicación  |
| Q08 | date |  |  | SI | Fecha y Hora Indicación Médica de Contención Mecán... |
| Q09 | time |  |  | SI | Hora Indicación Médica de Contención Mecánica  |
| Q10 | varchar |  |  | SI | 7. ¿Se inicia Contención Mecánica?  |
| Q11 | varchar |  |  | SI | 8. Motivo de la Contención |
| Q12 | varchar |  |  | SI | Otro |
| Q13 | varchar |  |  | SI | 9. Tipo de Contención Utilizada  |
| Q14 | varchar |  |  | SI | 10. Se educa a Paciente y/o Familia sobre medidas ... |
| Q15 | varchar |  |  | SI | 11. Persona quien recibe Educación  |
| Q16 | date |  |  | SI | Fecha de Información a Familiar |
| Q17 | varchar |  |  | SI | Aceptación de Medidas |
| Q18 | varchar |  |  | SI | 14. Nombre de quien Acepta o Rechaza Medidas de Co... |
| Q19 | varchar |  |  | SI | 15. Relación con el paciente de Quien Acepta o Rec... |
| Q20 | varchar |  |  | SI | Otro |
| Q21 | varchar |  |  | SI | 16.  Medidas Adoptadas ante Rechazo Contención Mec... |
| Q22 | varchar |  |  | SI | Otros |
| Q24 | date |  |  | SI | 17. Fecha y Hora de término de contención  |
| Q25 | time |  |  | SI | 17. Hora de término de contención  |
| Q26 | varchar |  |  | SI | 18. Responsable del término de contención |
| Q27 | varchar |  |  | SI | 19. Estado de Término  |
| Q28 | varchar |  |  | SI | 20. Motivo de la suspensión anticipada  |
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