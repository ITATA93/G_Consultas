# SQLUser.DTC_FluidVolumeRestr

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FLVLR_RowId | bigint | PK |  | NO | - |
| FLVLR_Code | varchar |  |  | NO | Code |
| FLVLR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FLVLR_CreatedDate | date |  |  | SI | Created Date |
| FLVLR_CreatedTime | time |  |  | SI | Created Time |
| FLVLR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FLVLR_DateFrom | date |  |  | SI | Date From |
| FLVLR_DateTo | date |  |  | SI | Date To |
| FLVLR_Desc | varchar |  |  | NO | Description |
| FLVLR_Owner | varchar |  |  | SI | Owner |
| FLVLR_UpdatedDate | date |  |  | SI | Updated Date |
| FLVLR_UpdatedTime | time |  |  | SI | Updated Time |
| FLVLR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Consultant's name	 |
| Q02 | - |  |  | SI | Reference |
| Q03 | - |  |  | SI | First operator's name	 |
| Q04 | - |  |  | SI | Procedure |
| Q05 | - |  |  | SI | Indications for procedure 	 |
| Q06 | - |  |  | SI | Techniques used 	 |
| Q07 | - |  |  | SI | Catheter number	 |
| Q08 | - |  |  | SI | Left main stem	 |
| Q09 | - |  |  | SI | Left anterior descending coronary artery	 |
| Q10 | - |  |  | SI | Left circumflex coronary artery	 |
| Q11 | - |  |  | SI | Right coronary artery	 |
| Q12 | - |  |  | SI | Catheter number |
| Q13 | - |  |  | SI | Left main stem |
| Q14 | - |  |  | SI | Left anterior descending coronary artery |
| Q15 | - |  |  | SI | Left circumflex coronary artery |
| Q16 | - |  |  | SI | Right coronary artery |
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