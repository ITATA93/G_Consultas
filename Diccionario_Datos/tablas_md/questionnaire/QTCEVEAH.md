# questionnaire.QTCEVEAH

> VE Alimentación e Hidratación

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* VE Alimentación e Hidratación

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Objetivo Registro |
| Q02 | bit |  |  | SI | Autonomo (OLD) |
| Q03 | bit |  |  | SI | Total (OLD) |
| Q04 | bit |  |  | SI | Parcial (OLD) |
| Q05 | bit |  |  | SI | Protesis Dental |
| Q06 | bit |  |  | SI | Dificultad al Masticar o Deglutir |
| Q07 | varchar |  |  | SI | Detalle |
| Q08 | bit |  |  | SI | Nauseas |
| Q09 | bit |  |  | SI | Vomitos |
| Q10 | varchar |  |  | SI | Detalle |
| Q11 | bit |  |  | SI | Dispepsia |
| Q12 | numeric |  |  | SI | Hidratacion |
| Q13 | varchar |  |  | SI | Dieta Habitual |
| Q14 | bit |  |  | SI | Dieta Desequilibrada |
| Q15 | bit |  |  | SI | Intolerancia y/o alergias alimentarias |
| Q16 | varchar |  |  | SI | Detalle |
| Q17 | bit |  |  | SI | Dieta Prescrita |
| Q18 | varchar |  |  | SI | Detalle |
| Q19 | bit |  |  | SI | N. Parenteral |
| Q20 | bit |  |  | SI | N. Enteral |
| Q21 | bit |  |  | SI | Suplementos |
| Q22 | varchar |  |  | SI | Diagnostico 1 |
| Q23 | varchar |  |  | SI | Diagnostico 2 |
| Q24 | varchar |  |  | SI | Conclusion |
| Q25 | varchar |  |  | SI | Pecho Materno |
| Q26 | varchar |  |  | SI | Alimentación |
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