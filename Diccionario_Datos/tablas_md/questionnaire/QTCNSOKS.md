# questionnaire.QTCNSOKS

> Oxford Knee Score

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Oxford Knee Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Please specify the type of visit |
| Q02 | varchar |  |  | SI | How would you describe the pain you usually have i... |
| Q03 | varchar |  |  | SI | Have you had any trouble washing and drying yourse... |
| Q04 | varchar |  |  | SI | Have you had any trouble getting in and out of the... |
| Q05 | varchar |  |  | SI | For how long are you able to walk before the pain ... |
| Q06 | varchar |  |  | SI | After a meal (sat at a table), how painful has it ... |
| Q07 | varchar |  |  | SI | Have you been limping when walking, because of you... |
| Q08 | varchar |  |  | SI | Could you kneel down and get up again afterwards? |
| Q09 | varchar |  |  | SI | Are you troubled by pain in your knee at night in ... |
| Q10 | varchar |  |  | SI | How much has pain from your knee interfered with y... |
| Q11 | varchar |  |  | SI | Have you felt that your knee might suddenly give a... |
| Q12 | varchar |  |  | SI | Could you do household shopping on your own? |
| Q13 | varchar |  |  | SI | Could you walk down a flight of stairs? |
| Q14 | varchar |  |  | SI | 0 - 19: Severe knee arthritis |
| Q15 | varchar |  |  | SI | 20 - 29: Moderate to severe knee arthritis |
| Q16 | varchar |  |  | SI | 30 - 39: Mild to moderate knee arthritis |
| Q17 | varchar |  |  | SI | 40 - 48: Satisfactory joint function |
| Q18 | varchar |  |  | SI | The OKS consists of 12 questions covering function... |
| Q19 | varchar |  |  | SI | Each question was scored from 1 to 5, with 1 repre... |
| Q20 | varchar |  |  | SI | Score |
| Q21 | varchar |  |  | SI | Classification |
| Q22 | varchar |  |  | SI | 0 - 19 |
| Q23 | varchar |  |  | SI | Severe knee arthritis |
| Q24 | varchar |  |  | SI | 20 - 29 |
| Q25 | varchar |  |  | SI | Moderate to severe knee arthritis |
| Q26 | varchar |  |  | SI | 30 - 39 |
| Q27 | varchar |  |  | SI | Mild to moderate knee arthritis |
| Q28 | varchar |  |  | SI | 40 - 48 |
| Q29 | varchar |  |  | SI | Satisfactory joint function |
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