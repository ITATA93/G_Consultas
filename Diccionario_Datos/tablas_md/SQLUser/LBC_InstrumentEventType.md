# SQLUser.LBC_InstrumentEventType

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCIET_RowID | bigint | PK |  | NO | - |
| LBCIET_Code | varchar |  |  | NO | Instrument Code |
| LBCIET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCIET_CreatedDate | date |  |  | SI | Created Date |
| LBCIET_CreatedTime | time |  |  | SI | Created Time |
| LBCIET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCIET_DateFrom | date |  |  | SI | Date From |
| LBCIET_DateTo | date |  |  | SI | Date To |
| LBCIET_Desc | varchar |  |  | NO | Instrument Description |
| LBCIET_DisplayInSummary | varchar |  |  | SI | Display in QC Summary |
| LBCIET_Notes | varchar |  |  | SI | Notes |
| LBCIET_Owner | varchar |  |  | SI | Owner |
| LBCIET_UpdatedDate | date |  |  | SI | Updated Date |
| LBCIET_UpdatedTime | time |  |  | SI | Updated Time |
| LBCIET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Deceased Patient Information |
| Q10 | - |  |  | SI | Place of origin of the deceased body |
| Q11 | - |  |  | SI | Observation time (h) |
| Q12 | - |  |  | SI | Reason for a shorter observation period |
| Q13 | - |  |  | SI | Annotation |
| Q14 | - |  |  | SI | Clothes and medical devices removal |
| Q15 | - |  |  | SI | Pacemaker removed |
| Q16 | - |  |  | SI | Other medical devices removed |
| Q17 | - |  |  | SI | Clothes removal date / time |
| Q18 | - |  |  | SI | Clothes removal time |
| Q19 | - |  |  | SI | Removed clothes in charge to |
| Q2 | - |  |  | SI | Referral person to contact |
| Q20 | - |  |  | SI | Information provided and activities performed by t... |
| Q21 | - |  |  | SI | Funeral home name |
| Q22 | - |  |  | SI | Material of the coffin |
| Q23 | - |  |  | SI | Dressing date / time |
| Q24 | - |  |  | SI | Dressing time |
| Q25 | - |  |  | SI | Dressing in charge to |
| Q26 | - |  |  | SI | Assembly date / time |
| Q27 | - |  |  | SI | Assembly time |
| Q28 | - |  |  | SI | Assembly in charge to |
| Q29 | - |  |  | SI | Viewing date / time |
| Q3 | - |  |  | SI | Phone contact |
| Q30 | - |  |  | SI | Viewing time |
| Q31 | - |  |  | SI | Conservation treatments used |
| Q32 | - |  |  | SI | Judicial Authority |
| Q33 | - |  |  | SI | Available to judicial authority |
| Q34 | - |  |  | SI | Available to judicial authority on |
| Q35 | - |  |  | SI | Available to judicial authority at |
| Q36 | - |  |  | SI | Authorized on the day |
| Q37 | - |  |  | SI | Autopsy |
| Q38 | - |  |  | SI | Specify |
| Q39 | - |  |  | SI | Annotation |
| Q4 | - |  |  | SI | Death Information |
| Q40 | - |  |  | SI | Specify |
| Q41 | - |  |  | SI | Date / Time of device removal |
| Q42 | - |  |  | SI | Time of device removal |
| Q43 | - |  |  | SI | In charge to |
| Q44 | - |  |  | SI | Type of the removed device |
| Q45 | - |  |  | SI | Date / Time of device removal |
| Q46 | - |  |  | SI | Time of device removal |
| Q47 | - |  |  | SI | In charge to |
| Q48 | - |  |  | SI | Date |
| Q49 | - |  |  | SI | Time |
| Q5 | - |  |  | SI | Place of death |
| Q50 | - |  |  | SI | Observation time (hh:mm) |
| Q6 | - |  |  | SI | Cause of death |
| Q7 | - |  |  | SI | Infection is out of death reason |
| Q8 | - |  |  | SI | Management of Deceased Body |
| Q9 | - |  |  | SI | Eligible to donate tissues |
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