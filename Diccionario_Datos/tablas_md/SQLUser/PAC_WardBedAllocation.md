# SQLUser.PAC_WardBedAllocation

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WBALL_ParRef | bigint | PK |  | NO | PAC_Ward Parent Reference |
| Q1 | - |  |  | SI | Anthropometrics |
| Q13 | - |  |  | SI | Comments |
| Q14 | - |  |  | SI | Fatigue |
| Q15 | - |  |  | SI | Fatigue |
| Q16 | - |  |  | SI | Comments |
| Q17 | - |  |  | SI | Joint pain |
| Q18 | - |  |  | SI | Joint pain |
| Q19 | - |  |  | SI | Details |
| Q20 | - |  |  | SI | Comments |
| Q21 | - |  |  | SI | Peripheral neuropathy |
| Q22 | - |  |  | SI | Comments |
| Q23 | - |  |  | SI | Insomnia |
| Q24 | - |  |  | SI | Insomnia |
| Q25 | - |  |  | SI | Details |
| Q26 | - |  |  | SI | Comments |
| Q27 | - |  |  | SI | Hot flashes |
| Q28 | - |  |  | SI | Hot flashes |
| Q29 | - |  |  | SI | Avg number per day |
| Q3 | - |  |  | SI | Waist measurement (cm) |
| Q30 | - |  |  | SI | Comments |
| Q31 | - |  |  | SI | Lymphoedema |
| Q32 | - |  |  | SI | Lymphoedema |
| Q33 | - |  |  | SI | Comments |
| Q34 | - |  |  | SI | Scar tissue retraction |
| Q35 | - |  |  | SI | Scar tissue retraction |
| Q36 | - |  |  | SI | Comments |
| Q37 | - |  |  | SI | Average steps per day |
| Q38 | - |  |  | SI | Average steps per day |
| Q39 | - |  |  | SI | Comments |
| Q4 | - |  |  | SI | Hips measurement (cm) |
| Q40 | - |  |  | SI | Peripheral neuropathy |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Time |
| Q5 | - |  |  | SI | Waist-to-hip ratio (WHR) |
| Q6 | - |  |  | SI | % FAT (Body Fat Percentage) |
| Q7 | - |  |  | SI | % FFM (Fat Free Mass Percentage) |
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
| WBALL_AllocReason_DR | bigint |  | FK | SI | Des Ref AllocReason |
| WBALL_Beds | double |  |  | NO | Number of Beds |
| WBALL_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WBALL_Childsub | double |  |  | NO | Childsub |
| WBALL_CreatedDate | date |  |  | SI | Created Date |
| WBALL_CreatedTime | time |  |  | SI | Created Time |
| WBALL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WBALL_Date | date |  |  | NO | Date |
| WBALL_DateTo | date |  |  | SI | DateTo |
| WBALL_RowId | varchar |  |  | NO | - |
| WBALL_UpdatedDate | date |  |  | SI | Updated Date |
| WBALL_UpdatedTime | time |  |  | SI | Updated Time |
| WBALL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*