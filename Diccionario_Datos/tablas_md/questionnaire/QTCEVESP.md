# questionnaire.QTCEVESP

> VE Seguridad y Protección

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* VE Seguridad y Protección

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Objetivo Registro |
| Q02 | bit |  |  | SI | Total |
| Q03 | bit |  |  | SI | Parcial (Incapacidad de Autorecuperacion) |
| Q04 | bit |  |  | SI | Incapacidad de solicitar ayuda |
| Q05 | bit |  |  | SI | Alergias |
| Q06 | varchar |  |  | SI | Detalle |
| Q07 | bit |  |  | SI | Riesgo Caida |
| Q08 | bit |  |  | SI | Riesgo Infeccion |
| Q09 | varchar |  |  | SI | Riesgo de Ulcera-Escala de Bradem |
| Q10 | bit |  |  | SI | No maneja adecuadamente el regimenterapeutico |
| Q11 | bit |  |  | SI | Conductas de Riesgo |
| Q12 | varchar |  |  | SI | Detalle |
| Q13 | bit |  |  | SI | Toxicos |
| Q14 | varchar |  |  | SI | Detalle |
| Q15 | bit |  |  | SI | Automedicacion |
| Q16 | bit |  |  | SI | Afrontamiento |
| Q17 | bit |  |  | SI | Negacion |
| Q18 | bit |  |  | SI | Minimizacion |
| Q19 | bit |  |  | SI | Proyeccion |
| Q20 | bit |  |  | SI | Ansiedad |
| Q21 | bit |  |  | SI | Dolor |
| Q22 | varchar |  |  | SI | En |
| Q23 | bit |  |  | SI | A la movilizacion |
| Q24 | bit |  |  | SI | Agudo |
| Q25 | bit |  |  | SI | Cronico |
| Q26 | numeric |  |  | SI | Intensidad del Dolor EVA |
| Q27 | bit |  |  | SI | Vacunacion |
| Q28 | varchar |  |  | SI | Detalle |
| Q29 | bit |  |  | SI | Implantes |
| Q30 | varchar |  |  | SI | Detalle |
| Q31 | bit |  |  | SI | Realiza medidas de prevencion en salud |
| Q32 | varchar |  |  | SI | Detalle |
| Q33 | varchar |  |  | SI | Diagnostico 1 |
| Q34 | varchar |  |  | SI | Diagnostico 2 |
| Q35 | varchar |  |  | SI | Conclusion |
| Q36 | bit |  |  | SI | Rieso |
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