# questionnaire.QCLXXFUEXSU

> Funcionalidad de Extremidades Superiores

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Funcionalidad de Extremidades Superiores

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha Evaluación |
| Q02 | time |  |  | SI | Hora Evaluación |
| Q03 | varchar |  |  | SI | I. Movimiento Grueso |
| Q04 | varchar |  |  | SI | 1. Abducción hombros hasta la altura de los hombro... |
| Q05 | varchar |  |  | SI | 1. Abducción hombros hasta la altura de los hombro... |
| Q06 | varchar |  |  | SI | 2. Abducción hombro sobre la altura de los hombros... |
| Q07 | varchar |  |  | SI | 2. Abducción hombro sobre la altura de los hombros... |
| Q08 | varchar |  |  | SI | 3. Flexión de hombros hasta altura de los hombros ... |
| Q09 | varchar |  |  | SI | 3. Flexión de hombros hasta altura de los hombros ... |
| Q10 | varchar |  |  | SI | 4. Flexión de hombros sobre altura de los hombros ... |
| Q11 | varchar |  |  | SI | 4. Flexión de hombros sobre altura de los hombros ... |
| Q12 | varchar |  |  | SI | 5. Colocar mano a la boca (Derecha) |
| Q13 | varchar |  |  | SI | 5. Colocar mano a la boca (Izquierda) |
| Q14 | varchar |  |  | SI | 6. Colocar mano en la nuca (Derecha) |
| Q15 | varchar |  |  | SI | 6. Colocar mano en la nuca (Izquierda) |
| Q16 | varchar |  |  | SI | 7. Trasladar un objetivo desde los muslos a mesa a... |
| Q17 | varchar |  |  | SI | 7. Trasladar un objetivo desde los muslos a mesa a... |
| Q18 | varchar |  |  | SI | 8. Levantar y trasladar botella de agua 500 cc. (D... |
| Q19 | varchar |  |  | SI | 8. Levantar y trasladar botella de agua 500 cc. (I... |
| Q20 | varchar |  |  | SI | II. Pinzas |
| Q21 | varchar |  |  | SI | 1. Cortar papel en dos (Derecha) |
| Q22 | varchar |  |  | SI | 1. Cortar papel en dos (Izquierda) |
| Q23 | varchar |  |  | SI | 2. Destapar una botella (Derecha) |
| Q24 | varchar |  |  | SI | 2. Destapar una botella (Izquierda) |
| Q25 | varchar |  |  | SI | 3. Trazar trayecto en una hoja (Derecha) |
| Q26 | varchar |  |  | SI | 3. Trazar trayecto en una hoja (Izquierda) |
| Q27 | varchar |  |  | SI | 4. Sostener tapa de vía roja entre pulgar y dedo a... |
| Q28 | varchar |  |  | SI | 4. Sostener tapa de vía roja entre pulgar y dedo a... |
| Q29 | varchar |  |  | SI | 5. Sostener tapa de vía roja entre pulgar y dedo m... |
| Q30 | varchar |  |  | SI | 5. Sostener tapa de vía roja entre pulgar y dedo m... |
| Q31 | varchar |  |  | SI | 6. Sostener tapa de vía roja entre pulgar y dedo í... |
| Q32 | varchar |  |  | SI | 6. Sostener tapa de vía roja entre pulgar y dedo í... |
| Q33 | varchar |  |  | SI | Total Evaluación Derecha |
| Q34 | varchar |  |  | SI | Total Evaluación Izquierda |
| Q35 | varchar |  |  | SI | ALTA (3) |
| Q36 | varchar |  |  | SI | MEDIANA (2) |
| Q37 | varchar |  |  | SI | BAJA (1) |
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