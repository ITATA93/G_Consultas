# questionnaire.QTCEAPACHE2

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Score APACHE**. Evaluación de severidad en pacientes críticos (UCI).

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQ1 | varchar | PK |  | SI | - |
| CQ10 | varchar | PK |  | SI | - |
| CQ11 | varchar | PK |  | SI | - |
| CQ12 | varchar | PK |  | SI | - |
| CQ13 | varchar | PK |  | SI | - |
| CQ18 | varchar | PK |  | SI | - |
| CQ19 | varchar | PK |  | SI | - |
| CQ2 | varchar | PK |  | SI | - |
| CQ3 | varchar | PK |  | SI | - |
| CQ4 | varchar | PK |  | SI | - |
| CQ5 | varchar | PK |  | SI | - |
| CQ6 | varchar | PK |  | SI | - |
| CQ8 | varchar | PK |  | SI | - |
| CQ9 | varchar | PK |  | SI | - |
| CQAaDO2 | varchar | PK |  | SI | - |
| CQEdad | varchar | PK |  | SI | - |
| CQPaO2 | varchar | PK |  | SI | - |
| CQVg | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| Q1 | varchar | PK |  | SI | Frecuencia Cardiaca |
| Q10 | varchar | PK |  | SI | Temperatura Rectal |
| Q11 | varchar | PK |  | SI | Sodio Serico |
| Q12 | varchar | PK |  | SI | Potasio Serico |
| Q13 | varchar | PK |  | SI | Creatinina Plasmatica mg/dl (con o sin IRA) |
| Q18 | varchar | PK |  | SI | Bicarbonato Sérico |
| Q19 | varchar | PK |  | SI | Gases en Sangre Arterial |
| Q2 | varchar | PK |  | SI | Presion Arterial Media |
| Q3 | varchar | PK |  | SI | pH Arterial |
| Q4 | varchar | PK |  | SI | Insuficiencia Orgánica Severa |
| Q5 | varchar | PK |  | SI | Frecuencia Respiratoria |
| Q6 | varchar | PK |  | SI | FIO2  |
| Q8 | varchar | PK |  | SI | Hematocrito (%) |
| Q9 | varchar | PK |  | SI | Leucocitos (total/mm3 en miles) |
| QAaDO2 | varchar | PK |  | SI | A-aDO2 |
| QEdad | varchar | PK |  | SI | Edad |
| QPaO2 | varchar | PK |  | SI | PaO2 |
| QUESAnaDR | varchar | PK | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar | PK | FK | SI | Operation |
| QUESConsultDR | varchar | PK | FK | SI | Consult |
| QUESCopiedComments | varchar | PK |  | SI | Copied Comments |
| QUESCopiedDate | date | PK |  | SI | Copied Date |
| QUESCopiedEpDR | bigint | PK | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint | PK | FK | SI | Copied Source DR |
| QUESCopiedTime | time | PK |  | SI | Copied Time |
| QUESCopiedUserDR | bigint | PK | FK | SI | Copied User |
| QUESCreateDate | date | PK |  | SI | Creation Date |
| QUESCreateTime | time | PK |  | SI | Creation Time |
| QUESCreateUserDR | bigint | PK | FK | SI | Creation User |
| QUESDate | date | PK |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint | PK | FK | SI | Error Reason |
| QUESFHResidentDR | bigint | PK | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar | PK | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar | PK | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar | PK | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint | PK | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar | PK | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint | PK | FK | SI | Operating Room |
| QUESPAAdmDR | bigint | PK | FK | SI | Admission |
| QUESPAPatMasDR | bigint | PK | FK | SI | Patient |
| QUESPAPregnancyDR | bigint | PK | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint | PK | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar | PK | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar | PK | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar | PK | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar | PK | FK | SI | Appointment Outcome |
| QUESReasonForCorrectionDR | bigint | PK | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint | PK | FK | SI | Questionnaire |
| QUESScore | varchar | PK |  | SI | Score |
| QUESStatusDR | bigint | PK | FK | SI | Status |
| QUESTextResultDR | bigint | PK | FK | SI | Text Result |
| QUESTime | time | PK |  | SI | Last Update Time |
| QUESTransactionDR | varchar | PK | FK | SI | Transaction |
| QUESUserDR | bigint | PK | FK | SI | Last Update User |
| QVg | varchar | PK |  | SI | Glasgow |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*