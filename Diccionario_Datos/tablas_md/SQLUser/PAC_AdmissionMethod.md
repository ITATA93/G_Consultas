# SQLUser.PAC_AdmissionMethod

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMETH_RowId | bigint | PK |  | NO | - |
| ADMETH_Code | varchar |  |  | NO | Code |
| ADMETH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMETH_CreatedDate | date |  |  | SI | Created Date |
| ADMETH_CreatedTime | time |  |  | SI | Created Time |
| ADMETH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMETH_DateFrom | date |  |  | SI | Date from |
| ADMETH_DateTo | date |  |  | SI | Date To |
| ADMETH_Desc | varchar |  |  | NO | Description |
| ADMETH_EpisodeType | varchar |  |  | SI | Episode Type |
| ADMETH_NationalCode | varchar |  |  | SI | National Code |
| ADMETH_Owner | varchar |  |  | SI | Owner |
| ADMETH_RefType | varchar |  |  | SI | Referrer Type |
| ADMETH_TransferSource | varchar |  |  | SI | Transfer Source |
| ADMETH_UpdatedDate | date |  |  | SI | Updated Date |
| ADMETH_UpdatedTime | time |  |  | SI | Updated Time |
| ADMETH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Delivery location |
| Q04 | - |  |  | SI | Location delivery address |
| Q05 | - |  |  | SI | Patient delivery address |
| Q06 | - |  |  | SI | Other location and delivery address |
| Q07 | - |  |  | SI | Requested delivery from |
| Q08 | - |  |  | SI | to |
| Q09 | - |  |  | SI | Requested delivery to |
| Q10 | - |  |  | SI | Date community informed |
| Q11 | - |  |  | SI | Person to contact in community regarding delivery |
| Q12 | - |  |  | SI | Community contact phone number |
| Q13 | - |  |  | SI | Equipment requested |
| Q14 | - |  |  | SI | HD machine type requested |
| Q15 | - |  |  | SI | Other equipment |
| Q16 | - |  |  | SI | Notes to supplier |
| Q17 | - |  |  | SI | Equipment received and installed |
| Q18 | - |  |  | SI | Serial number - haemodialysis machine |
| Q19 | - |  |  | SI | Serial number - RO |
| Q20 | - |  |  | SI | Serial number - chair |
| Q21 | - |  |  | SI | Other serial numbers |
| Q22 | - |  |  | SI | Community contact phone number |
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