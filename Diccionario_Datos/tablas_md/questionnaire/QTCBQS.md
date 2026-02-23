# questionnaire.QTCBQS

> Escala de Braden Q

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Braden Q

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | INTENSIDAD Y DURACIÓN DE LA PRESIÓN |
| Q02 | varchar |  |  | SI | Condición física general |
| Q03 | varchar |  |  | SI | MOVILIDAD |
| Q04 | varchar |  |  | SI | ACTIVIDAD |
| Q05 | varchar |  |  | SI | PERCEPCIÓN SENSORIAL  |
| Q06 | varchar |  |  | SI | TOLERANCIA DE LA PIEL Y LA ESTRUCTURA DE SOPORTE |
| Q07 | varchar |  |  | SI | HUMEDAD |
| Q08 | varchar |  |  | SI | FRICCIÓN Y CIZALLA |
| Q09 | varchar |  |  | SI | NUTRICIÓN |
| Q10 | varchar |  |  | SI | Perfusión tisular y oxigenación |
| Q11 | varchar |  |  | SI | Comentarios |
| Q12 | varchar |  |  | SI | > 16 |
| Q13 | varchar |  |  | SI | Riesgo bajo |
| Q14 | varchar |  |  | SI | ≤ 16 |
| Q15 | varchar |  |  | SI | En riesgo |
| Q16 | varchar |  |  | SI | La escala Braden Q para predecir el riesgo de úlce... |
| Q17 | varchar |  |  | SI | Puntaje |
| Q18 | varchar |  |  | SI | Clasificación |
| Q19 | varchar |  |  | SI | > 16: riesgo bajo |
| Q20 | varchar |  |  | SI | ≤ 16: riesgo alto |
| Q21 | varchar |  |  | SI | Revise la interpretación de la puntuación a contin... |
| Q22 | date |  |  | SI | Fecha |
| Q23 | time |  |  | SI | Hora |
| Q24 | varchar |  |  | SI | Comentarios |
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