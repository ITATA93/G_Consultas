# SQLUser.DTC_Energy

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ENE_RowId | bigint | PK |  | NO | - |
| ENE_Code | varchar |  |  | NO | Code |
| ENE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ENE_CreatedDate | date |  |  | SI | Created Date |
| ENE_CreatedTime | time |  |  | SI | Created Time |
| ENE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ENE_DateFrom | date |  |  | SI | DateFrom |
| ENE_DateTo | date |  |  | SI | DateTo |
| ENE_Desc | varchar |  |  | NO | Description |
| ENE_Owner | varchar |  |  | SI | Owner |
| ENE_UpdatedDate | date |  |  | SI | Updated Date |
| ENE_UpdatedTime | time |  |  | SI | Updated Time |
| ENE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Pulses |
| Q02 | - |  |  | SI | Spontaneous |
| Q03 | - |  |  | SI | With CPR only |
| Q04 | - |  |  | SI | By doppler |
| Q05 | - |  |  | SI | Measurable BP |
| Q06 | - |  |  | SI | Systolic |
| Q06ObsDR | - |  |  | SI | Systolic DR |
| Q07 | - |  |  | SI | Diastolic |
| Q07ObsDR | - |  |  | SI | Diastolic DR |
| Q08 | - |  |  | SI | Responsiveness |
| Q08N | - |  |  | SI | Note |
| Q10a | - |  |  | SI | Pupil reaction (L) |
| Q10aN | - |  |  | SI | Note |
| Q10aObsDR | - |  |  | SI | Pupil reaction (L) DR |
| Q10b | - |  |  | SI | Pupil reaction (R) |
| Q10bN | - |  |  | SI | Note |
| Q10bObsDR | - |  |  | SI | Pupil reaction (R) DR |
| Q12a | - |  |  | SI | Pupil size (L) |
| Q12aN | - |  |  | SI | Note |
| Q12aObsDR | - |  |  | SI | Pupil size (L) DR |
| Q12b | - |  |  | SI | Pupil size (R) |
| Q12bN | - |  |  | SI | Note |
| Q12bObsDR | - |  |  | SI | Pupil size (R) DR |
| Q15 | - |  |  | SI | Cardiac rhythm (initial) |
| Q15N | - |  |  | SI | Note |
| Q17 | - |  |  | SI | Heart sounds |
| Q17N | - |  |  | SI | Note |
| Q19 | - |  |  | SI | Cardioversion / Countershock |
| Q20 | - |  |  | SI | Response |
| Q20N | - |  |  | SI | Note |
| Q20SPN | - |  |  | SI | See procedure notes |
| Q23 | - |  |  | SI | Respiratory effort |
| Q23N | - |  |  | SI | Note |
| Q25 | - |  |  | SI | Bag-mask ventilation |
| Q26 | - |  |  | SI | Endotracheal tube placed |
| Q27 | - |  |  | SI | Successful |
| Q28 | - |  |  | SI | Position verified |
| Q28CG | - |  |  | SI | If yes |
| Q28N | - |  |  | SI | Note |
| Q28SPN | - |  |  | SI | See procedure notes |
| Q32 | - |  |  | SI | Lung sounds |
| Q32N | - |  |  | SI | Note |
| Q34 | - |  |  | SI | Patient deceased |
| Q36 | - |  |  | SI | Spontaneous circulation restored |
| Q37 | - |  |  | SI | Spontaneous respiration |
| Q38 | - |  |  | SI | On ventilator |
| Q39 | - |  |  | SI | Patient requires circulatory support |
| Q39CBG | - |  |  | SI | If yes |
| Q39N | - |  |  | SI | Note |
| Q42 | - |  |  | SI | Neurological status |
| Q42N | - |  |  | SI | Note |
| Q46 | - |  |  | SI | Cardiac rhythm (initial) |
| Q47 | - |  |  | SI | Heart sounds |
| Q48 | - |  |  | SI | Respiratory effort |
| Q49 | - |  |  | SI | Lung sounds |
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