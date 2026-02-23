# questionnaire.QTCEREQX

> Reintervención Quirúrgica

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Reintervención Quirúrgica

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit |  |  | SI | Paciente Reintervenido |
| Q02 | varchar |  |  | SI | Cirugia Principal |
| Q03 | date |  |  | SI | Fecha Inicio Cirugia |
| Q04 | time |  |  | SI | Hora Inicio Cirugia |
| Q05 | varchar |  |  | SI | Arsenalera |
| Q06 | numeric |  |  | SI | Duración Cirugia |
| Q07 | varchar |  |  | SI | Razón de Reintervención |
| Q08 | varchar |  |  | SI | Anestesiólogo |
| Q09 | varchar |  |  | SI | Cirugia Secundaria |
| Q10 | varchar |  |  | SI | Pabellonera |
| Q11 | varchar |  |  | SI | Enfermera Pabellón |
| Q12 | varchar |  |  | SI | Primer Cirujano |
| Q13 | date |  |  | SI | Fecha Término Cirugia |
| Q14 | time |  |  | SI | Hora Término Cirugia |
| Q15 | varchar |  |  | SI | Primer Ayudante (Cirujano) |
| Q16 | varchar |  |  | SI | N° Episodio |
| Q17 | varchar |  |  | SI | ANAOP |
| Q18 | varchar |  |  | SI | Cirugías secundarias 2 |
| Q18hidden | varchar |  |  | SI | Cirugías secundarias 2 - oculto |
| Q19 | varchar |  |  | SI | Se reinterviene por:  |
| Q20 | varchar |  |  | SI | Reintervención Secundaria |
| Q20hidden | varchar |  |  | SI | Reintervención Secundaria - oculto |
| Q23 | varchar |  |  | SI | Comentarios |
| Q24 | varchar |  |  | SI | Tipo de Reintervención |
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