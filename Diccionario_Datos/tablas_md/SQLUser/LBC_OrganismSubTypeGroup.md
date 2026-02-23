# SQLUser.LBC_OrganismSubTypeGroup

**Schema:** SQLUser
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCOSTG_RowID | bigint | PK |  | NO | - |
| LBCOSTG_Code | varchar |  |  | NO | Code
Collation exception to support k,K |
| LBCOSTG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCOSTG_CreatedDate | date |  |  | SI | Created Date |
| LBCOSTG_CreatedTime | time |  |  | SI | Created Time |
| LBCOSTG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCOSTG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCOSTG_DateTo | date |  |  | SI | Last day the record is active |
| LBCOSTG_Desc | varchar |  |  | NO | Description
Collation exception to support k,K
H... |
| LBCOSTG_Owner | varchar |  |  | SI | Owner |
| LBCOSTG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCOSTG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCOSTG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Amputation |
| Q04 | - |  |  | SI | Right foot amputation |
| Q05 | - |  |  | SI | Amputation date |
| Q06 | - |  |  | SI | Left foot amputation |
| Q07 | - |  |  | SI | Amputation date |
| Q08 | - |  |  | SI | Diabetic related amputation |
| Q09 | - |  |  | SI | Risk factor |
| Q10 | - |  |  | SI | Significant structural abnormality foot |
| Q11 | - |  |  | SI | Significant callus |
| Q12 | - |  |  | SI | Active ulceration |
| Q13 | - |  |  | SI | Previous ulceration |
| Q14 | - |  |  | SI | Able to or help to self care |
| Q15 | - |  |  | SI | Other risks |
| Q16 | - |  |  | SI | Vascular Assessment |
| Q17 | - |  |  | SI | Right peripheral pulse posterior tibial present |
| Q18 | - |  |  | SI | Right peripheral pulse dorsalis pedis present |
| Q19 | - |  |  | SI | Right intermittent claudication |
| Q20 | - |  |  | SI | Right previous vascular intervention |
| Q21 | - |  |  | SI | Left peripheral pulse posterior tibial present |
| Q22 | - |  |  | SI | Left peripheral pulse dorsalis pedis present |
| Q23 | - |  |  | SI | Left intermittent claudication |
| Q24 | - |  |  | SI | Left previous vascular intervention |
| Q25 | - |  |  | SI | Others |
| Q26 | - |  |  | SI | Neurological Assessment |
| Q27 | - |  |  | SI | Feet |
| Q28 | - |  |  | SI | (10 gram monofilament site) |
| Q29 | - |  |  | SI | Neurothesiometer assessment right |
| Q30 | - |  |  | SI | Neurothesiometer assessment left |
| Q31 | - |  |  | SI | Painful neuropathy (i.e. pain, paresthesia, burnin... |
| Q32 | - |  |  | SI | Risk Category |
| Q33 | - |  |  | SI | Risk category |
| Q34 | - |  |  | SI | Recommendation |
| Q35 | - |  |  | SI | Recommendation |
| Q36 | - |  |  | SI | Currently attending podiatrist |
| Q37 | - |  |  | SI | Referral to |
| Q38 | - |  |  | SI | Education |
| Q39 | - |  |  | SI | Other comments |
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