# SQLUser.CT_HealthCareProvider

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HCP_RowId | bigint | PK |  | NO | - |
| HCP_Code | varchar |  |  | NO | Code |
| HCP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HCP_CreatedDate | date |  |  | SI | Created Date |
| HCP_CreatedTime | time |  |  | SI | Created Time |
| HCP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HCP_Desc | varchar |  |  | NO | Description |
| HCP_HCA_DR | bigint |  | FK | SI | Des Ref HCA |
| HCP_InternAgreem_DR | bigint |  | FK | SI | Des Ref InternAgreem |
| HCP_Owner | varchar |  |  | SI | Owner |
| HCP_Region_DR | bigint |  | FK | SI | Des Ref Region |
| HCP_UpdatedDate | date |  |  | SI | Updated Date |
| HCP_UpdatedTime | time |  |  | SI | Updated Time |
| HCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Type of referral |
| Q02 | - |  |  | SI | Comments	 |
| Q03 | - |  |  | SI | Booking Information	 |
| Q04 | - |  |  | SI | Transport	 |
| Q05 | - |  |  | SI | Gait aid	 |
| Q06 | - |  |  | SI | Weight bearing status	 |
| Q07 | - |  |  | SI | Precautions 	 |
| Q08 | - |  |  | SI | Fluid restriction	 |
| Q09 | - |  |  | SI | Dysphagia precautions	 |
| Q10 | - |  |  | SI | Reason for referral	 |
| Q11 | - |  |  | SI | Anticipated length of stay	 |
| Q12 | - |  |  | SI | Length of time	 |
| Q14 | - |  |  | SI | Bed mobility 	 |
| Q15 | - |  |  | SI | Transfers	 |
| Q16 | - |  |  | SI | Ambulation (Include endurance)	 |
| Q17 | - |  |  | SI | Comments |
| Q18 | - |  |  | SI | Additional Information	 |
| Q19 | - |  |  | SI | Referrer	 |
| Q20 | - |  |  | SI | Date of Referral	 |
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