# SQLUser.CT_PayMode

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPM_RowId | bigint | PK |  | NO | - |
| CTPM_ChangeGiven | varchar |  |  | SI | ChangeGiven |
| CTPM_Code | varchar |  |  | NO | Payment Mode |
| CTPM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTPM_CodeTranslated | varchar |  |  | SI | - |
| CTPM_CreatedDate | date |  |  | SI | Created Date |
| CTPM_CreatedTime | time |  |  | SI | Created Time |
| CTPM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTPM_DateFrom | date |  |  | SI | Date From |
| CTPM_DateTo | date |  |  | SI | Date To |
| CTPM_DefaultPaymentLocation_DR | bigint |  | FK | SI | Default Payment Location |
| CTPM_Desc | varchar |  |  | NO | Payment Mode Description |
| CTPM_DescTranslated | varchar |  |  | SI | - |
| CTPM_GrpCode | varchar |  |  | SI | Payment Group  |
| CTPM_NotUseFlag | varchar |  |  | NO | Not Used Flag |
| CTPM_Owner | varchar |  |  | SI | Owner |
| CTPM_UpdatedDate | date |  |  | SI | Updated Date |
| CTPM_UpdatedTime | time |  |  | SI | Updated Time |
| CTPM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Pure-tone audiogram |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Right ear |
| Q05 | - |  |  | SI | Right ear |
| Q06 | - |  |  | SI | Left ear |
| Q07 | - |  |  | SI | Left ear |
| Q08 | - |  |  | SI | Reliability |
| Q09 | - |  |  | SI | Masking type |
| Q10 | - |  |  | SI | Masking level |
| Q11 | - |  |  | SI | Ear |
| Q12 | - |  |  | SI | Speech audiometry results |
| Q13 | - |  |  | SI | Right ear |
| Q14 | - |  |  | SI | Left ear |
| Q15 | - |  |  | SI | Speech Reception Threshold Level |
| Q16 | - |  |  | SI | Speech Disc. Score % |
| Q17 | - |  |  | SI | Intensity of Speech Disc. |
| Q18 | - |  |  | SI | Masking Level of Speech Reception Threshold |
| Q19 | - |  |  | SI | Masking Level of Speech Disc. |
| Q20 | - |  |  | SI | Aided Speech Disc. Scores |
| Q21 | - |  |  | SI | Speech Reception Threshold Level |
| Q22 | - |  |  | SI | Speech Disc. Score % |
| Q23 | - |  |  | SI | Intensity of Speech Disc. |
| Q24 | - |  |  | SI | Masking Level of Speech Reception Threshold |
| Q25 | - |  |  | SI | Masking Level of Speech Disc. |
| Q26 | - |  |  | SI | Aided Speech Disc. Scores |
| Q27 | - |  |  | SI | Remarks & comments |
| Q28 | - |  |  | SI | Recommendations |
| Q29 | - |  |  | SI | Left Ear |
| Q30 | - |  |  | SI | Right Ear |
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