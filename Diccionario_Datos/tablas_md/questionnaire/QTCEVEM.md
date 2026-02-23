# questionnaire.QTCEVEM

> VE Movilizacion y mantencion de posturas adecuadas

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* VE Movilizacion y mantencion de posturas adecuadas

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit |  |  | SI | Autonomo |
| Q02 | bit |  |  | SI | Total |
| Q03 | bit |  |  | SI | Parcial |
| Q04 | bit |  |  | SI | Requiere uso de dispositivo |
| Q05 | varchar |  |  | SI | Detalle |
| Q06 | bit |  |  | SI | Requiere ayuda de otra persona, supervision o ense... |
| Q07 | bit |  |  | SI | Requiere ayuda de otra persona y dispositivo |
| Q08 | bit |  |  | SI | Dependiente, no participa en la actividad |
| Q09 | bit |  |  | SI | Deambulacion |
| Q10 | bit |  |  | SI | Sedestacion |
| Q11 | bit |  |  | SI | Movilidad cama |
| Q12 | varchar |  |  | SI | Limitacion a la movilizacion |
| Q13 | bit |  |  | SI | Intolerancia a la actividad fisica |
| Q14 | varchar |  |  | SI | Detalle |
| Q15 | varchar |  |  | SI | Ejercicio fisico habitual |
| Q16 | varchar |  |  | SI | Adecuado para la edad |
| Q17 | varchar |  |  | SI | Especifique |
| Q18 | varchar |  |  | SI | Diagnostico 1 |
| Q19 | varchar |  |  | SI | Diagnostico 2 |
| Q20 | varchar |  |  | SI | Conclusion |
| Q21 | varchar |  |  | SI | Objetivo Registro |
| Q22 | varchar |  |  | SI | Actividad Física |
| Q23 | varchar |  |  | SI | Movilidad |
| Q24 | varchar |  |  | SI | Tipo de Asistencia |
| Q25 | varchar |  |  | SI | Detalle Requier Uso Dispositivo |
| Q26 | varchar |  |  | SI | Detalle Requiere ayuda de otra persona y dispositi... |
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