# SQLUser.PAC_WaitingTimeStandard

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WTST_RowId | bigint | PK |  | NO | - |
| ChildQ10DR | - |  |  | SI | Child Reference: Staff present |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Fetus number |
| Q04 | - |  |  | SI | Maternal position when shoulder dystocia identifie... |
| Q05 | - |  |  | SI | If other, please specify |
| Q06 | - |  |  | SI | Call for help time |
| Q07 | - |  |  | SI | Obstetric emergency called time |
| Q08 | - |  |  | SI | (this is different from initial call for help) |
| Q09 | - |  |  | SI | Neonatologist / Paediatrician called time |
| Q11 | - |  |  | SI | Slow advancement of fetal head |
| Q12 | - |  |  | SI | Difficult delivery of fetal face |
| Q13 | - |  |  | SI | Slow or no restitution of fetal head |
| Q14 | - |  |  | SI | Turtle sign / Fetal chin retraction onto perineum |
| Q15 | - |  |  | SI | Other signs of shoulder dystocia |
| Q16 | - |  |  | SI | If other, please specify |
| Q17 | - |  |  | SI | Time of birth of fetal head |
| Q18 | - |  |  | SI | Birth of head mode |
| Q19 | - |  |  | SI | Fetal position during dystocia |
| Q20 | - |  |  | SI | Episiotomy for manoeuvres |
| Q22 | - |  |  | SI | Overall comments |
| Q23 | - |  |  | SI | Time of shoulder dystocia resolution (birth of bab... |
| Q24 | - |  |  | SI | Head to body delivery interval (mins) |
| Q25 | - |  |  | SI | Shoulder dystocia explained to parents |
| Q26 | - |  |  | SI | Explained by |
| Q27 | - |  |  | SI | Leaflet given |
| Q28 | - |  |  | SI | Incident number |
| Q29 | - |  |  | SI | Signature |
| Q30 | - |  |  | SI | Counter signature |
| Q31 | - |  |  | SI | Head to body delivery interval (mins) |
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
| WTST_Code | varchar |  |  | NO | Code |
| WTST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WTST_CreatedDate | date |  |  | SI | Created Date |
| WTST_CreatedTime | time |  |  | SI | Created Time |
| WTST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WTST_DateFrom | date |  |  | SI | DateFrom |
| WTST_DateTo | date |  |  | SI | DateTo |
| WTST_Desc | varchar |  |  | NO | Description |
| WTST_NewWays | varchar |  |  | SI | New Ways |
| WTST_Owner | varchar |  |  | SI | Owner |
| WTST_RefPathwayStageType_DR | bigint |  | FK | SI | Default Stage Type DR |
| WTST_TTG | varchar |  |  | SI | TTG |
| WTST_UpdatedDate | date |  |  | SI | Updated Date |
| WTST_UpdatedTime | time |  |  | SI | Updated Time |
| WTST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*