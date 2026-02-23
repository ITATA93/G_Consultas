# questionnaire.QCLXXDUFFY

> Escala de Inteligibilidad DUFFY

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Escala de Inteligibilidad DUFFY

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Nivel |
| Q02 | varchar |  |  | SI | 10 |
| Q03 | varchar |  |  | SI | 9 |
| Q04 | varchar |  |  | SI | 8 |
| Q05 | varchar |  |  | SI | 7 |
| Q06 | varchar |  |  | SI | 6 |
| Q07 | varchar |  |  | SI | 5 |
| Q08 | varchar |  |  | SI | 4 |
| Q09 | varchar |  |  | SI | 3 |
| Q10 | varchar |  |  | SI | 2 |
| Q11 | varchar |  |  | SI | 1 |
| Q12 | varchar |  |  | SI | Eficiencia (***) |
| Q13 | varchar |  |  | SI | Ambiente (*) |
| Q14 | varchar |  |  | SI | Contenido (**) |
| Q15 | varchar |  |  | SI | Eficiencia |
| Q16 | varchar |  |  | SI | Ambiente |
| Q17 | varchar |  |  | SI | Contenido |
| Q18 | varchar |  |  | SI | Eficiencia |
| Q19 | varchar |  |  | SI | Ambiente |
| Q20 | varchar |  |  | SI | Contenido |
| Q21 | varchar |  |  | SI | Eficiencia |
| Q22 | varchar |  |  | SI | Ambiente |
| Q23 | varchar |  |  | SI | Contenido |
| Q24 | varchar |  |  | SI | Eficiencia |
| Q25 | varchar |  |  | SI | Ambiente |
| Q26 | varchar |  |  | SI | Contenido |
| Q27 | varchar |  |  | SI | Eficiencia |
| Q28 | varchar |  |  | SI | Ambiente |
| Q29 | varchar |  |  | SI | Contenido |
| Q30 | varchar |  |  | SI | Eficiencia |
| Q31 | varchar |  |  | SI | Ambiente |
| Q32 | varchar |  |  | SI | Contenido |
| Q33 | varchar |  |  | SI | Eficiencia |
| Q34 | varchar |  |  | SI | Ambiente |
| Q35 | varchar |  |  | SI | Contenido |
| Q36 | varchar |  |  | SI | Eficiencia |
| Q37 | varchar |  |  | SI | Ambiente |
| Q38 | varchar |  |  | SI | Contenido |
| Q39 | varchar |  |  | SI | Normal en todos los ambientes sin restricciones de... |
| Q40 | varchar |  |  | SI | A veces (#) reducida frente a condiciones adversas... |
| Q41 | varchar |  |  | SI | A veces reducida frente a condiciones ideales cuan... |
| Q42 | varchar |  |  | SI | A veces reducida frente a condiciones adversas aún... |
| Q43 | varchar |  |  | SI | A veces reducida en condiciones ideales cuando no ... |
| Q44 | varchar |  |  | SI | Usualmente (##) reducida bajo condiciones adversas... |
| Q45 | varchar |  |  | SI | Usualmente reducida bajo condiciones ideales, aún ... |
| Q46 | varchar |  |  | SI | Usualmente reducida bajo condiciones adversas aún ... |
| Q47 | varchar |  |  | SI | Usualmente reducida en condiciones ideales aún cua... |
| Q48 | varchar |  |  | SI | El habla no es un medio viable de comunicación en ... |
| Q49 | varchar |  |  | SI | Eficiencia |
| Q50 | varchar |  |  | SI | Estado de la Inteligibilidad |
| Q51 | varchar |  |  | SI | Nivel |
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