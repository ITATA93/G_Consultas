# SQLUser.MRC_BodySystemProbStatus

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STAT_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Mes |
| Q02 | - |  |  | SI | Año |
| Q03 | - |  |  | SI | Reevaluación Médico SS |
| Q04 | - |  |  | SI | Reevaluación Médico Municipal |
| Q05 | - |  |  | SI | Reevaluación Enfermera SS |
| Q06 | - |  |  | SI | Reevaluación Enfermera Municipal |
| Q07 | - |  |  | SI | Reevaluación Nutricionista SS |
| Q08 | - |  |  | SI | Reevaluación Nutricioinista Municipal |
| Q09 | - |  |  | SI | Reevaluación Matrona SS |
| Q10 | - |  |  | SI | Reevaluación Matrona Municipal |
| Q11 | - |  |  | SI | Reevaluación Auxiliar SS |
| Q12 | - |  |  | SI | Reevaluación Auxiliar Municipal |
| QHR | - |  |  | SI | Establecimiento |
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
| STAT_Code | varchar |  |  | NO | Code |
| STAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| STAT_CreatedDate | date |  |  | SI | Created Date |
| STAT_CreatedTime | time |  |  | SI | Created Time |
| STAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| STAT_DateFrom | date |  |  | SI | Date from |
| STAT_DateTo | date |  |  | SI | Date To |
| STAT_Desc | varchar |  |  | NO | Description |
| STAT_Owner | varchar |  |  | SI | Owner |
| STAT_UpdatedDate | date |  |  | SI | Updated Date |
| STAT_UpdatedTime | time |  |  | SI | Updated Time |
| STAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*