# questionnaire.QCLXXDBURKE

> Escala de Evaluación de Distonía Burke Fahn Marsden

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Evaluación de Distonía Burke Fahn Marsden

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Fecha de Evaluación |
| Q02 | varchar |  |  | SI | 1. Ojos Provocación |
| Q03 | varchar |  |  | SI | 1. Ojos Severidad |
| Q04 | numeric |  |  | SI | 1. Ojos Po |
| Q05 | varchar |  |  | SI | 1. Ojos Total E.M. |
| Q06 | varchar |  |  | SI | 2. Boca Provocación |
| Q07 | varchar |  |  | SI | 2. Boca Severidad |
| Q08 | numeric |  |  | SI | 2. Boca Po |
| Q09 | varchar |  |  | SI | 2. Boca Total E.M. |
| Q10 | varchar |  |  | SI | 3. Habla y Deglución Provocación |
| Q11 | varchar |  |  | SI | 3. Habla y Deglución Severidad |
| Q12 | numeric |  |  | SI | 3. Habla y Deglución Po |
| Q13 | varchar |  |  | SI | 3. Habla y Deglución Total E.M. |
| Q14 | varchar |  |  | SI | 4. Cuello Provocación  |
| Q15 | varchar |  |  | SI | 4. Cuello Severidad |
| Q16 | numeric |  |  | SI | 4. Cuello Po |
| Q17 | varchar |  |  | SI | 4. Cuello Total E.M. |
| Q18 | varchar |  |  | SI | 5. Brazo Derecho Provocación |
| Q19 | varchar |  |  | SI | 5. Brazo Derecho Severidad |
| Q20 | numeric |  |  | SI | 5. Brazo Derecho Po |
| Q21 | varchar |  |  | SI | 5. Brazo Derecho Total  E.M. |
| Q22 | varchar |  |  | SI | 6. Brazo Izquierdo Provocación |
| Q23 | varchar |  |  | SI | 6. Brazo Izquierdo Severidad |
| Q24 | numeric |  |  | SI | 6. Brazo Izquierdo Po |
| Q25 | varchar |  |  | SI | 6. Brazo Izquierdo Total  E.M. |
| Q26 | varchar |  |  | SI | 7. Tronco Provocación |
| Q27 | varchar |  |  | SI | 7. Tronco Severidad |
| Q28 | numeric |  |  | SI | 7. Tronco Severidad Po |
| Q29 | varchar |  |  | SI | 7. Tronco Severidad Total E.M. |
| Q30 | varchar |  |  | SI | 8. Pierna Derecha Provocación |
| Q31 | varchar |  |  | SI | 8. Pierna Derecha Severidad |
| Q32 | numeric |  |  | SI | 8. Pierna Derecha Po |
| Q33 | varchar |  |  | SI | 8. Pierna Derecha Total E.M. |
| Q34 | varchar |  |  | SI | 9. Pierna Izquierda Provocación |
| Q35 | varchar |  |  | SI | 9. Pierna Izquierda Severidad |
| Q36 | numeric |  |  | SI | 9. Pierna Izquierda Po |
| Q37 | varchar |  |  | SI | 9. Pierna Izquierda Total E.M. |
| Q38 | varchar |  |  | SI | SUMA PUNTAJE TOTAL  E.M |
| Q39 | varchar |  |  | SI | CÁLCULO DE PUNTAJE POR ESCALA |
| Q40 | varchar |  |  | SI | A.ESCALA DE MOVIMIENTO |
| Q41 | varchar |  |  | SI | B.ESCALA DE DISCAPACIDAD |
| Q42 | varchar |  |  | SI | 1. Habla |
| Q43 | varchar |  |  | SI | 2. Escritura |
| Q44 | varchar |  |  | SI | 3. Alimentación |
| Q45 | varchar |  |  | SI | 4. Comer/Tragar |
| Q46 | varchar |  |  | SI | 5. Higiene |
| Q47 | varchar |  |  | SI | 6. Vestirse |
| Q48 | varchar |  |  | SI | 7. Caminar |
| Q49 | varchar |  |  | SI | SUMA PUNTAJE TOTAL  E.D. |
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