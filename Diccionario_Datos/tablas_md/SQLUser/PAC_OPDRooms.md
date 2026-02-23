# SQLUser.PAC_OPDRooms

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPD_RowId | bigint | PK |  | NO | - |
| OPD_Code | varchar |  |  | NO | Code |
| OPD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OPD_CreatedDate | date |  |  | SI | Created Date |
| OPD_CreatedTime | time |  |  | SI | Created Time |
| OPD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPD_DateFrom | date |  |  | SI | DateFrom |
| OPD_DateTo | date |  |  | SI | DateTo |
| OPD_Desc | varchar |  |  | NO | Description |
| OPD_Owner | varchar |  |  | SI | Owner |
| OPD_UpdatedDate | date |  |  | SI | Updated Date |
| OPD_UpdatedTime | time |  |  | SI | Updated Time |
| OPD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Please specify the type of visit |
| Q02 | - |  |  | SI | How would you describe the pain you usually have i... |
| Q03 | - |  |  | SI | Have you had any trouble washing and drying yourse... |
| Q04 | - |  |  | SI | Have you had any trouble getting in and out of the... |
| Q05 | - |  |  | SI | For how long are you able to walk before the pain ... |
| Q06 | - |  |  | SI | After a meal (sat at a table), how painful has it ... |
| Q07 | - |  |  | SI | Have you been limping when walking, because of you... |
| Q08 | - |  |  | SI | Could you kneel down and get up again afterwards? |
| Q09 | - |  |  | SI | Are you troubled by pain in your knee at night in ... |
| Q10 | - |  |  | SI | How much has pain from your knee interfered with y... |
| Q11 | - |  |  | SI | Have you felt that your knee might suddenly give a... |
| Q12 | - |  |  | SI | Could you do household shopping on your own? |
| Q13 | - |  |  | SI | Could you walk down a flight of stairs? |
| Q14 | - |  |  | SI | 0 - 19: Severe knee arthritis |
| Q15 | - |  |  | SI | 20 - 29: Moderate to severe knee arthritis |
| Q16 | - |  |  | SI | 30 - 39: Mild to moderate knee arthritis |
| Q17 | - |  |  | SI | 40 - 48: Satisfactory joint function |
| Q18 | - |  |  | SI | The OKS consists of 12 questions covering function... |
| Q19 | - |  |  | SI | Each question was scored from 1 to 5, with 1 repre... |
| Q20 | - |  |  | SI | Score |
| Q21 | - |  |  | SI | Classification |
| Q22 | - |  |  | SI | 0 - 19 |
| Q23 | - |  |  | SI | Severe knee arthritis |
| Q24 | - |  |  | SI | 20 - 29 |
| Q25 | - |  |  | SI | Moderate to severe knee arthritis |
| Q26 | - |  |  | SI | 30 - 39 |
| Q27 | - |  |  | SI | Mild to moderate knee arthritis |
| Q28 | - |  |  | SI | 40 - 48 |
| Q29 | - |  |  | SI | Satisfactory joint function |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*