# SQLUser.LB_QCBatchLevel

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCBL_ParRef | bigint | PK |  | NO | Parent Batch |
| LBQCBL_Comments | varchar |  |  | SI | Comments |
| LBQCBL_Description | varchar |  |  | SI | Description |
| LBQCBL_ExpiryDate | date |  |  | SI | Expiry Date
This expiry date will overwrite the d... |
| LBQCBL_ExpiryWarningDays | integer |  |  | SI | Expiry Warning Days
A warning will be produced a ... |
| LBQCBL_Level | integer |  |  | SI | Level
Unique level identifier within the batch |
| LBQCBL_MaxExtensionDays | integer |  |  | SI | Maximum Extension Days
Maximum number of days the... |
| LBQCBL_RowID | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | 1. Caminar más de 1 cuadra |
| Q02 | - |  |  | SI | 2. Correr |
| Q03 | - |  |  | SI | 3. Participar en deportes o ejercicio |
| Q04 | - |  |  | SI | 4. Levantar algo pesado |
| Q05 | - |  |  | SI | 5. Bañarse o ducharse sólo |
| Q06 | - |  |  | SI | 6. Realizar actividades alrededor de la casa |
| Q07 | - |  |  | SI | 7. Presencia de dolor |
| Q08 | - |  |  | SI | 8. Bajo nivel de energía |
| Q09 | - |  |  | SI | 1. Preocupado o asustado |
| Q10 | - |  |  | SI | 2. Triste o deprimido |
| Q11 | - |  |  | SI | 3. Sentirse enojado |
| Q12 | - |  |  | SI | 4. Dificultad para dormir |
| Q13 | - |  |  | SI | 5. Preocupado por su futuro |
| Q14 | - |  |  | SI | 1. Entenderse con otros niños |
| Q15 | - |  |  | SI | 2. Otros niños no quieren ser sus amigos |
| Q16 | - |  |  | SI | 3. Otros niños se burlan de él |
| Q17 | - |  |  | SI | 4. No puede hacer las cosas que hacen otros niños ... |
| Q18 | - |  |  | SI | 5. No  puede mantener las actividades de juego con... |
| Q19 | - |  |  | SI | 1. Poner atención en clases |
| Q20 | - |  |  | SI | 2. Olvidarse de cosas |
| Q21 | - |  |  | SI | 3. Estar al día con sus obligaciones escolares |
| Q22 | - |  |  | SI | 4. Ausencias a clases por no sentirse bien |
| Q23 | - |  |  | SI | 5. Falta a clases por tener que ir al médico o al ... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*