# questionnaire.QTCEPQL3

> Instrumento Medición Calidad de Vida Pacientes con Asma (8-12 Años): Informe de Padres

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Instrumento Medición Calidad de Vida Pacientes con Asma (8-12 Años): Informe de Padres

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Caminar más de 1 cuadra |
| Q02 | varchar |  |  | SI | 2. Correr |
| Q03 | varchar |  |  | SI | 3. Participar en deportes o ejercicio |
| Q04 | varchar |  |  | SI | 4. Levantar algo pesado |
| Q05 | varchar |  |  | SI | 5. Bañarse o ducharse sólo |
| Q06 | varchar |  |  | SI | 6. Realizar actividades alrededor de la casa |
| Q07 | varchar |  |  | SI | 7. Presencia de dolor |
| Q08 | varchar |  |  | SI | 8. Bajo nivel de energía |
| Q09 | varchar |  |  | SI | 1. Preocupado o asustado |
| Q10 | varchar |  |  | SI | 2. Triste o deprimido |
| Q11 | varchar |  |  | SI | 3. Sentirse enojado |
| Q12 | varchar |  |  | SI | 4. Dificultad para dormir |
| Q13 | varchar |  |  | SI | 5. Preocupado por su futuro |
| Q14 | varchar |  |  | SI | 1. Entenderse con otros niños |
| Q15 | varchar |  |  | SI | 2. Otros niños no quieren ser sus amigos |
| Q16 | varchar |  |  | SI | 3. Otros niños se burlan de él |
| Q17 | varchar |  |  | SI | 4. No puede hacer las cosas que hacen otros niños ... |
| Q18 | varchar |  |  | SI | 5. No  puede mantener las actividades de juego con... |
| Q19 | varchar |  |  | SI | 1. Poner atención en clases |
| Q20 | varchar |  |  | SI | 2. Olvidarse de cosas |
| Q21 | varchar |  |  | SI | 3. Estar al día con sus obligaciones escolares |
| Q22 | varchar |  |  | SI | 4. Ausencias a clases por no sentirse bien  |
| Q23 | varchar |  |  | SI | 5. Falta a clases por tener que ir al médico o al ... |
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