# questionnaire.QGXXXMNA

> Cribaje MNA (Mini Nutritional Assessment)

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cribaje MNA (Mini Nutritional Assessment)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Complete el cuestionario llenando con los valores ... |
| Q02 | varchar |  |  | SI | Peso (kg) |
| Q02ObsDR | varchar |  | FK | SI | Peso (kg) DR |
| Q03 | varchar |  |  | SI | Talla (cm)  |
| Q03ObsDR | varchar |  | FK | SI | Talla (cm)  DR |
| Q04 | date |  |  | SI | Fecha |
| Q05 | varchar |  |  | SI |  A. Ha comido menos por falta de apetito, problema... |
| Q06 | varchar |  |  | SI | B. Pérdida reciente de peso (últimos 3 meses) |
| Q07 | varchar |  |  | SI | C. Movilidad |
| Q08 | varchar |  |  | SI | D. Ha tenido una enfermedad aguda o situación de e... |
| Q09 | varchar |  |  | SI | E. Problemas neuropsicológicos |
| Q11 | varchar |  |  | SI | IMC |
| Q12 | varchar |  |  | SI | F1. Índice de masa corporal (IMC) |
| Q13 | varchar |  |  | SI | F2. Circunferencia de la Pantorilla |
| Q14 | varchar |  |  | SI | Puntaje Screening  (max. 14 puntos) |
| Q15 | varchar |  |  | SI | 12 - 14 puntos: Estado Nutricional Normal |
| Q16 | varchar |  |  | SI | 8-11 puntos: Riesgo de Malnutrición |
| Q17 | varchar |  |  | SI | 0-7 puntos: Malnutrición |
| Q18 | varchar |  |  | SI | IMC |
| Q19 | date |  |  | SI | Date |
| Q20 | varchar |  |  | SI | El formulario de evaluación mini-nutricional es un... |
| Q21 | time |  |  | SI | Time |
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