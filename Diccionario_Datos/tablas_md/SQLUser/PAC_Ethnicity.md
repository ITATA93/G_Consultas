# SQLUser.PAC_Ethnicity

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ETHNIC_RowId | bigint | PK |  | NO | - |
| ETHNIC_Code | varchar |  |  | NO | Code |
| ETHNIC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ETHNIC_CreatedDate | date |  |  | SI | Created Date |
| ETHNIC_CreatedTime | time |  |  | SI | Created Time |
| ETHNIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ETHNIC_DateFrom | date |  |  | SI | Date From |
| ETHNIC_DateTo | date |  |  | SI | Date To |
| ETHNIC_Desc | varchar |  |  | NO | Description |
| ETHNIC_Owner | varchar |  |  | SI | Owner |
| ETHNIC_Rank | integer |  |  | SI | Ethnicity Rank |
| ETHNIC_UpdatedDate | date |  |  | SI | Updated Date |
| ETHNIC_UpdatedTime | time |  |  | SI | Updated Time |
| ETHNIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | MDT Date |
| Q02 | - |  |  | SI | Meeting ID |
| Q03 | - |  |  | SI | Report ID |
| Q04 | - |  |  | SI | Reference Doctor |
| Q05 | - |  |  | SI | Reference Nurse |
| Q06 | - |  |  | SI | Clinical Pathway Protocol |
| Q07 | - |  |  | SI | Stages of the Protocol discussed |
| Q08 | - |  |  | SI | Decisions as per the Guidelines |
| Q09 | - |  |  | SI | Reason for Variance |
| Q10 | - |  |  | SI | Variance Notes |
| Q11 | - |  |  | SI | Therapeutic Options |
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