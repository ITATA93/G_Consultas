# questionnaire.QTCEEDIM

> Escala de Edimburgo

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Edimburgo

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ1 | varchar |  |  | SI | - |
| CQ10 | varchar |  |  | SI | - |
| CQ2 | varchar |  |  | SI | - |
| CQ3 | varchar |  |  | SI | - |
| CQ4 | varchar |  |  | SI | - |
| CQ5 | varchar |  |  | SI | - |
| CQ6 | varchar |  |  | SI | - |
| CQ7 | varchar |  |  | SI | - |
| CQ8 | varchar |  |  | SI | - |
| CQ9 | varchar |  |  | SI | - |
| CQEV | varchar |  |  | SI | - |
| CQTEV | varchar |  |  | SI | - |
| Q1 | varchar |  |  | SI | ¿Ha sido capaz de reírse y ver el lado divertido d... |
| Q10 | varchar |  |  | SI | ¿Se le ha ocurrido la idea de hacerse daño? |
| Q13 | varchar |  |  | SI | Condición |
| Q14 | varchar |  |  | SI | Resultado de la Evaluación |
| Q14ObsDR | varchar |  | FK | SI | Resultado de la Evaluación DR |
| Q17 | varchar |  |  | SI | ¿Se deriva a programa de Salud Mental? |
| Q18 | varchar |  |  | SI | 0-12: Normal |
| Q19 | varchar |  |  | SI | 13 o más: Probablilidad de depresión |
| Q2 | varchar |  |  | SI | ¿Ha disfrutado mirar hacia delante? |
| Q20 | varchar |  |  | SI | Puérpera |
| Q21 | varchar |  |  | SI | 0-10: Normal |
| Q22 | varchar |  |  | SI | 11 o más: Probabilidad de depresión |
| Q23 | varchar |  |  | SI | ¿Se deriva a programa de Salud Mental? old |
| Q24 | varchar |  |  | SI | Gestante |
| Q3 | varchar |  |  | SI | ¿Cuándo las cosas le han salido mal se ha culpado ... |
| Q4 | varchar |  |  | SI | ¿Ha estado nerviosa o inquieta sin tener motivo? |
| Q5 | varchar |  |  | SI | ¿Ha sentido miedo o ha estado asustada sin motivo? |
| Q6 | varchar |  |  | SI | ¿Las cosas le han estado abrumando o agobiando? |
| Q7 | varchar |  |  | SI | ¿Se ha sentido tan desdichada que ha tenido dificu... |
| Q8 | varchar |  |  | SI | ¿Se ha sentido triste o desgraciada? |
| Q9 | varchar |  |  | SI | ¿Se ha sentido tan desdichada que ha estado lloran... |
| QEV | varchar |  |  | SI | Tipo de Evaluación |
| QTEV | varchar |  |  | SI | Tipo de Evaluación |
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
| Qder | varchar |  |  | SI | Derivación inmediata a Médico |
| Qqr | varchar |  |  | SI | Resultado Edimburgo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*