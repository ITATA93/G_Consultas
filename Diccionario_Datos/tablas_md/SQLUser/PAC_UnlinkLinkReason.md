# SQLUser.PAC_UnlinkLinkReason

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LINKR_RowId | bigint | PK |  | NO | - |
| LINKR_Code | varchar |  |  | NO | Code |
| LINKR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LINKR_CreatedDate | date |  |  | SI | Created Date |
| LINKR_CreatedTime | time |  |  | SI | Created Time |
| LINKR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LINKR_DateFrom | date |  |  | SI | Date From |
| LINKR_DateTo | date |  |  | SI | Date To |
| LINKR_Desc | varchar |  |  | NO | Description |
| LINKR_LinkReason | varchar |  |  | SI | Reason for Linking |
| LINKR_Owner | varchar |  |  | SI | Owner |
| LINKR_UnlinkReason | varchar |  |  | SI | Reason for Unlinking |
| LINKR_UpdatedDate | date |  |  | SI | Updated Date |
| LINKR_UpdatedTime | time |  |  | SI | Updated Time |
| LINKR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | White Blood Cell (WBC) count &gt |
| Q04 | - |  |  | SI | Age &gt |
| Q05 | - |  |  | SI | Blood glucose &gt |
| Q06 | - |  |  | SI | Aspartate transaminase (AST) &gt |
| Q07 | - |  |  | SI | Lactate dehydrogenase (LDH) &gt |
| Q08 | - |  |  | SI | Haematocrit drop &gt |
| Q09 | - |  |  | SI | Blood urea nitrogen increase &gt |
| Q10 | - |  |  | SI | Calcium &lt |
| Q11 | - |  |  | SI | Arterial PO2 &lt |
| Q12 | - |  |  | SI | Base deficit &gt |
| Q13 | - |  |  | SI | Positive fluid balance &gt |
| Q14 | - |  |  | SI | The Ranson criteria can only be calculated once th... |
| Q15 | - |  |  | SI | Score |
| Q16 | - |  |  | SI | Classification |
| Q17 | - |  |  | SI | 0 - 2 |
| Q18 | - |  |  | SI | 0 - 2: Mortality 0% to 3% |
| Q19 | - |  |  | SI | 3 - 4 |
| Q20 | - |  |  | SI | 3 - 4: 15% predicted mortality |
| Q21 | - |  |  | SI | 5 - 6 |
| Q22 | - |  |  | SI | 5 - 6: 40% predicted mortality |
| Q23 | - |  |  | SI | 7 - 11 |
| Q24 | - |  |  | SI | 7 - 11: 100% predicted mortality |
| Q25 | - |  |  | SI | Consider ICU admission if score is 3 or greater. |
| Q26 | - |  |  | SI | 1% predicted mortality |
| Q27 | - |  |  | SI | 15% predicted mortality |
| Q28 | - |  |  | SI | 40% predicted mortality |
| Q29 | - |  |  | SI | 100% predicted mortality |
| Q30 | - |  |  | SI | Ranson's criteria is one of the earliest scoring s... |
| Q31 | - |  |  | SI | It consists of 11 indices measured at two time sta... |
| Q32 | - |  |  | SI | White blood cell count &gt |
| Q33 | - |  |  | SI | 1.&nbsp |
| Q34 | - |  |  | SI | 2.&nbsp |
| Q35 | - |  |  | SI | 3.&nbsp |
| Q36 | - |  |  | SI | 4.&nbsp |
| Q37 | - |  |  | SI | 5.&nbsp |
| Q38 | - |  |  | SI | 6.&nbsp |
| Q39 | - |  |  | SI | 7.&nbsp |
| Q40 | - |  |  | SI | 8.&nbsp |
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