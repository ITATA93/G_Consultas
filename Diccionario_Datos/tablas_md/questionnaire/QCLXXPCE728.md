# questionnaire.QCLXXPCE728

> Pauta CERO 72 a 83 Meses

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pauta CERO 72 a 83 Meses

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Resultado |
| Q01ObsDR | varchar |  | FK | SI | Resultado DR |
| Q02 | varchar |  |  | SI | I. Anamnesis |
| Q03 | varchar |  |  | SI | ¿El niño(a) presenta una condición que disminuya s... |
| Q04 | varchar |  |  | SI | ¿El niño(a) presenta situación de discapacidad? |
| Q05 | varchar |  |  | SI | II. Condición Clínica |
| Q06 | varchar |  |  | SI | ¿Cuál es la historia de caries del niño(a)? |
| Q07 | varchar |  |  | SI | ¿Cuál es el estado de las encias del niño(a)? |
| Q08 | varchar |  |  | SI | III. Dieta |
| Q09 | varchar |  |  | SI | ¿Cuántas veces al día el niño(a) ingiere alimentos... |
| Q10 | varchar |  |  | SI | ¿En qué momento el niño(a) realiza la ingesta de a... |
| Q11 | varchar |  |  | SI | Si el niño(a) toma mamadera, ¿Cuántas veces se que... |
| Q12 | varchar |  |  | SI | IV. Higiene |
| Q13 | varchar |  |  | SI | ¿Cuántas veces al día el niño(a) se lava los dient... |
| Q14 | varchar |  |  | SI | ¿El niño o niña, se lava los dientes antes de ir a... |
| Q15 | varchar |  |  | SI | Los padres y/o cuidadores, ¿Ayudan al niño(a) a la... |
| Q16 | varchar |  |  | SI | V. Fluoruros |
| Q17 | varchar |  |  | SI | Luego de las preguntas anteriores, según usted (de... |
| Q18 | varchar |  |  | SI | VI. Motivación de los Padres / Cuidadores |
| Q19 | varchar |  |  | SI | ¿Utiliza el niño o niña pasta con flúor de más de ... |
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