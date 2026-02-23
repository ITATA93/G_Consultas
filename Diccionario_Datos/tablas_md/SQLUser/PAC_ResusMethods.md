# SQLUser.PAC_ResusMethods

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESUSMTH_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Incubation time |
| Q04 | - |  |  | SI | Site of infection |
| Q05 | - |  |  | SI | State of protection |
| Q06 | - |  |  | SI | Complicating factors |
| Q07 | - |  |  | SI | 0 - 30 |
| Q08 | - |  |  | SI | Higher scores are indicative of worse prognosis. |
| Q09 | - |  |  | SI | 0 - 30: Higher scores are indicative of worse prog... |
| Q10 | - |  |  | SI | Score |
| Q11 | - |  |  | SI | Classification |
| Q12 | - |  |  | SI | The Phillip Score is a prognostic scoring for grad... |
| Q13 | - |  |  | SI | A score > 14 was noted to be associated with ‘seve... |
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
| RESUSMTH_Active | varchar |  |  | SI | Active flag |
| RESUSMTH_Code | varchar |  |  | NO | Code |
| RESUSMTH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESUSMTH_CreatedDate | date |  |  | SI | Created Date |
| RESUSMTH_CreatedTime | time |  |  | SI | Created Time |
| RESUSMTH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESUSMTH_DateFrom | date |  |  | SI | Date From |
| RESUSMTH_DateTo | date |  |  | SI | Date To |
| RESUSMTH_Desc | varchar |  |  | NO | Description |
| RESUSMTH_NationalCode | varchar |  |  | SI | National Code |
| RESUSMTH_Owner | varchar |  |  | SI | Owner |
| RESUSMTH_UpdatedDate | date |  |  | SI | Updated Date |
| RESUSMTH_UpdatedTime | time |  |  | SI | Updated Time |
| RESUSMTH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*