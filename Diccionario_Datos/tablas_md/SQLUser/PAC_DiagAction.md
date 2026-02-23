# SQLUser.PAC_DiagAction

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIAA_RowId | bigint | PK |  | NO | - |
| DIAA_Code | varchar |  |  | NO | Code |
| DIAA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DIAA_CreatedDate | date |  |  | SI | Created Date |
| DIAA_CreatedTime | time |  |  | SI | Created Time |
| DIAA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DIAA_DateFrom | date |  |  | SI | Date From |
| DIAA_DateTo | date |  |  | SI | Date To |
| DIAA_Desc | varchar |  |  | NO | Description |
| DIAA_Owner | varchar |  |  | SI | Owner |
| DIAA_UpdatedDate | date |  |  | SI | Updated Date |
| DIAA_UpdatedTime | time |  |  | SI | Updated Time |
| DIAA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Hepatomegaly |
| Q04 | - |  |  | SI | Splenomegaly |
| Q05 | - |  |  | SI | Spider naevi |
| Q06 | - |  |  | SI | Gynaecomastia |
| Q07 | - |  |  | SI | Palmer erythema |
| Q08 | - |  |  | SI | Notes |
| Q09 | - |  |  | SI | Signs of Decompensated Liver Disease	 |
| Q10 | - |  |  | SI | Known or suspected encephalopathy |
| Q11 | - |  |  | SI | Peripheral oedema |
| Q12 | - |  |  | SI | Ascites |
| Q13 | - |  |  | SI | Jaundice |
| Q14 | - |  |  | SI | Notes |
| Q15 | - |  |  | SI | Signs of Compensated Liver Disease |
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