# questionnaire.QTCEESCMC

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CQ1 | varchar | PK |  | SI | - |
| CQ10 | varchar | PK |  | SI | - |
| CQ11 | varchar | PK |  | SI | - |
| CQ12 | varchar | PK |  | SI | - |
| CQ13 | varchar | PK |  | SI | - |
| CQ14 | varchar | PK |  | SI | - |
| CQ15 | varchar | PK |  | SI | - |
| CQ2 | varchar | PK |  | SI | - |
| CQ3 | varchar | PK |  | SI | - |
| CQ4 | varchar | PK |  | SI | - |
| CQ5 | varchar | PK |  | SI | - |
| CQ6 | varchar | PK |  | SI | - |
| CQ7 | varchar | PK |  | SI | - |
| CQ8 | varchar | PK |  | SI | - |
| CQ9 | varchar | PK |  | SI | - |
| ID | bigint | PK |  | NO | - |
| Q1 | varchar | PK |  | SI | Relación del acompañante o cuidador |
| Q10 | varchar | PK |  | SI | Vocalización cuidador |
| Q11 | varchar | PK |  | SI | Tocando (a) cuidador |
| Q12 | varchar | PK |  | SI | Tocado (b) cuidador |
| Q13 | varchar | PK |  | SI | Sosteniendo cuidador |
| Q14 | varchar | PK |  | SI | Afecto cuidador |
| Q15 | varchar | PK |  | SI | Proximidad o cercanía cuidador |
| Q17 | varchar | PK |  | SI | En caso de existir, describa la Conducta Problemát... |
| Q18 | varchar | PK |  | SI | Nombre del cuidador (a)	 |
| Q2 | varchar | PK |  | SI | Mirada niño |
| Q3 | varchar | PK |  | SI | Vocalización niño |
| Q4 | varchar | PK |  | SI | Tocando (a) niño |
| Q5 | varchar | PK |  | SI | Tocado (b) niño |
| Q6 | varchar | PK |  | SI | Sosteniendo niño |
| Q7 | varchar | PK |  | SI | Afecto niño |
| Q8 | varchar | PK |  | SI | Proximidad o cercanía niño   |
| Q9 | varchar | PK |  | SI | Mirada cuidador |
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
| Qqr | varchar | PK |  | SI | Resultado Escala Massie-Campbel |
| QqrObsDR | varchar | PK | FK | SI | Resultado Escala Massie-Campbel DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*