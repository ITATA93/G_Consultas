# SQLUser.OEC_ConcOverideReason

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COR_RowId | bigint | PK |  | NO | - |
| COR_Code | varchar |  |  | NO | Code |
| COR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COR_CreatedDate | date |  |  | SI | Created Date |
| COR_CreatedTime | time |  |  | SI | Created Time |
| COR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COR_DateFrom | date |  |  | SI | Date From |
| COR_DateTo | date |  |  | SI | Date To |
| COR_Desc | varchar |  |  | NO | Description |
| COR_Owner | varchar |  |  | SI | Owner |
| COR_UpdatedDate | date |  |  | SI | Updated Date |
| COR_UpdatedTime | time |  |  | SI | Updated Time |
| COR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of Referral |
| Q02 | - |  |  | SI | Referring Physician |
| Q03 | - |  |  | SI | Referral |
| Q04 | - |  |  | SI | Symptoms |
| Q05 | - |  |  | SI | Symptom - Other |
| Q06 | - |  |  | SI | Gross Appearance |
| Q07 | - |  |  | SI | Gross Appearance - Other |
| Q08 | - |  |  | SI | Previous Therapy |
| Q09 | - |  |  | SI | Previous Therapy - Other |
| Q11 | - |  |  | SI | Colposcopic Findings |
| Q12 | - |  |  | SI | Cytological Result |
| Q13 | - |  |  | SI | Colposcopic Result |
| Q14 | - |  |  | SI | Histological Diagnosis |
| Q15 | - |  |  | SI | Results |
| Q16 | - |  |  | SI | Referral Details |
| Q17 | - |  |  | SI | Final Diagnosis |
| Q18 | - |  |  | SI | Final Diagnosis - Other |
| Q19 | - |  |  | SI | Recommended Treatment |
| Q20 | - |  |  | SI | Clinical Indications |
| Q21 | - |  |  | SI | Findings |
| Q30 | - |  |  | SI | Vulvoscopy Diagram |
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