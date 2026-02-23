# questionnaire.QTCENUTREQ

> Requerimientos Nutricionales

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Requerimientos Nutricionales

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | KCAL Total  |
| Q02 | varchar |  |  | SI | Peso |
| Q02ObsDR | varchar |  | FK | SI | Peso DR |
| Q03 | numeric |  |  | SI | Proteínas % Molécula Calórica |
| Q04 | numeric |  |  | SI | Carbohidratos % Molécula Calórica  |
| Q05 | numeric |  |  | SI | Lípidos % Molécula Calórica  |
| Q06 | varchar |  |  | SI | Proteínas Gramos / Día |
| Q07 | varchar |  |  | SI | Carbohidratos Gramos / Día |
| Q08 | varchar |  |  | SI | Lípidos Gramos / Día |
| Q09 | varchar |  |  | SI | Proteína GR. Por Kg de Peso |
| Q10 | varchar |  |  | SI | Carbohidratos GR. Por Kg de Peso |
| Q11 | varchar |  |  | SI | Lípidos GR. Por Kg de Peso |
| Q12 | numeric |  |  | SI | Proteínas Gramos / Día (A)  |
| Q13 | varchar |  |  | SI | Proteínas % Molécula Calórica (A) |
| Q14 | varchar |  |  | SI | Proteína GR. Por Kg de Peso (A) |
| Q15 | numeric |  |  | SI | Carbohidratos Gramos / Día (A)  |
| Q16 | varchar |  |  | SI | Carbohidratos % Molécula Calórica (A) |
| Q17 | varchar |  |  | SI | Carbohidratos GR. Por Kg de Peso (A)  |
| Q18 | numeric |  |  | SI | Lípidos Gramos / Día (A) |
| Q19 | varchar |  |  | SI | Lípidos % Molécula Calórica (A) |
| Q20 | varchar |  |  | SI | Lípidos GR. Por kg de peso |
| Q21 | varchar |  |  | SI | Proteínas % |
| Q22 | varchar |  |  | SI | Carbohidratos % |
| Q23 | varchar |  |  | SI | Lípidos % |
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