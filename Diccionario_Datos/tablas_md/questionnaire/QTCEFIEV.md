# questionnaire.QTCEFIEV

> Ficha de Evaluación: Columna

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Ficha de Evaluación: Columna

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Postura General |
| Q02 | varchar |  |  | SI | Posterior |
| Q03 | varchar |  |  | SI | Anterior |
| Q04 | varchar |  |  | SI | Lateral |
| Q05 | varchar |  |  | SI | Ubicación e Intensidad |
| Q06 | varchar |  |  | SI | Palpitación |
| Q07 | varchar |  |  | SI | Factores que lo inducen |
| Q08 | varchar |  |  | SI | Factores que lo aminoran |
| Q09 | varchar |  |  | SI | Flexión cabeza 35-45 al Ingreso |
| Q10 | varchar |  |  | SI | Extensión cabeza 35-45 al Ingreso |
| Q11 | varchar |  |  | SI | Inclinación Lateral cabeza 60-80 al Ingreso |
| Q12 | varchar |  |  | SI | Rotación en Flexión 45-0-45 al Ingreso |
| Q13 | varchar |  |  | SI | Rotación en Extensión 60-0-60 al Ingreso |
| Q14 | varchar |  |  | SI | Extensión Columna 0-30 al Ingreso |
| Q15 | varchar |  |  | SI | Flexión Columna 75 al Ingreso |
| Q16 | varchar |  |  | SI | Inclinación Lateral al Ingreso |
| Q17 | varchar |  |  | SI | Rotación Tronco al Ingreso |
| Q18 | varchar |  |  | SI | Ingreso A/P |
| Q19 | varchar |  |  | SI | Flexión cabeza 35-45 al Alta |
| Q20 | varchar |  |  | SI | Pruebas Funcionales |
| Q21 | varchar |  |  | SI | Examen Radiológico |
| Q22 | varchar |  |  | SI | Medición |
| Q23 | varchar |  |  | SI | Miembro Inferior Derecho |
| Q24 | varchar |  |  | SI | Miembro Inferior Izquierdo |
| Q25 | varchar |  |  | SI | Anteversión |
| Q26 | varchar |  |  | SI | Retroversión |
| Q27 | varchar |  |  | SI | Extensión cabeza 35-45 al Alta |
| Q28 | varchar |  |  | SI | Inclinación Lateral cabeza 60-80 al Alta |
| Q29 | varchar |  |  | SI | Rotación en Flexión 45-0-45 al Alta |
| Q30 | varchar |  |  | SI | Rotación en Extensión 60-0-60 al Alta |
| Q31 | varchar |  |  | SI | Extensión Columna 0-30 al Alta |
| Q32 | varchar |  |  | SI | Flexión Columna 75 al Alta |
| Q33 | varchar |  |  | SI | Inclinación Lateral al Alta |
| Q34 | varchar |  |  | SI | Rotación Tronco al Alta |
| Q35 | varchar |  |  | SI | Observación |
| Q36 | varchar |  |  | SI | Dolor (EVA) |
| Q37 | varchar |  |  | SI | Rangos Articulares |
| Q38 | varchar |  |  | SI | Medición |
| Q39 | varchar |  |  | SI | A/P |
| Q40 | varchar |  |  | SI | A/P |
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