# SQLUser.ORC_USTechnique

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| USTE_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Situation |
| Q02 | - |  |  | SI | Chance of dozing |
| Q03 | - |  |  | SI | Sitting and reading |
| Q04 | - |  |  | SI | Watching TV |
| Q05 | - |  |  | SI | Sitting inactive in a public place (e.g a theater ... |
| Q06 | - |  |  | SI | As a passenger in a car for an hour without a brea... |
| Q07 | - |  |  | SI | Lying down to rest in the afternoon when circumsta... |
| Q08 | - |  |  | SI | Sitting and talking to someone |
| Q09 | - |  |  | SI | Sitting quietly after a lunch without alcohol |
| Q10 | - |  |  | SI | In a car, while stopped for a few minutes in traff... |
| Q11 | - |  |  | SI | Score |
| Q12 | - |  |  | SI | Classification |
| Q13 | - |  |  | SI | How likely are you to doze off or fall asleep in t... |
| Q14 | - |  |  | SI | This refers to your usual way of life in recent ti... |
| Q15 | - |  |  | SI | number for each situation |
| Q16 | - |  |  | SI | The Epworth Sleepiness Scale (ESS) score can range... |
| Q17 | - |  |  | SI | 0-5 |
| Q18 | - |  |  | SI | Lower Normal Daytime Sleepiness |
| Q19 | - |  |  | SI | 6-10 |
| Q20 | - |  |  | SI | Higher Normal Daytime Sleepiness |
| Q21 | - |  |  | SI | 11-12 |
| Q22 | - |  |  | SI | Mild Excessive Daytime Sleepiness |
| Q23 | - |  |  | SI | 13-15 |
| Q24 | - |  |  | SI | Moderate Excessive Daytime Sleepiness |
| Q25 | - |  |  | SI | 16-24 |
| Q26 | - |  |  | SI | Severe Excessive Daytime Sleepiness |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Time |
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
| USTE_Code | varchar |  |  | NO | Code |
| USTE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| USTE_CreatedDate | date |  |  | SI | Created Date |
| USTE_CreatedTime | time |  |  | SI | Created Time |
| USTE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| USTE_DateFrom | date |  |  | SI | Date From |
| USTE_DateTo | date |  |  | SI | Date To |
| USTE_Desc | varchar |  |  | NO | Description |
| USTE_Owner | varchar |  |  | SI | Owner |
| USTE_UpdatedDate | date |  |  | SI | Updated Date |
| USTE_UpdatedTime | time |  |  | SI | Updated Time |
| USTE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*