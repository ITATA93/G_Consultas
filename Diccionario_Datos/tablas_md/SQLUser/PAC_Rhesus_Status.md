# SQLUser.PAC_Rhesus_Status

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RHSSTS_RowId | bigint | PK |  | NO | - |
| ChildQ03DR | - |  |  | SI | Child Reference: Sources of medicine list |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Prescription medicines |
| Q05 | - |  |  | SI | Sleeping tablets |
| Q06 | - |  |  | SI | Inhalers, puffers, sprays, sublingual tablets |
| Q07 | - |  |  | SI | Oral contraceptives, hormone replacement therapy |
| Q08 | - |  |  | SI | Over-the-counter medicines |
| Q09 | - |  |  | SI | Analgesics |
| Q10 | - |  |  | SI | Gastrointestinal drugs (for reflux, heartburn, con... |
| Q11 | - |  |  | SI | Complementary medicines (e.g. vitamins, herbal or ... |
| Q12 | - |  |  | SI | Topical medicines (e.g. creams, ointments, lotions... |
| Q13 | - |  |  | SI | Inserted medicines (e.g. nose / ear / eye drops, p... |
| Q14 | - |  |  | SI | Injected medicines |
| Q15 | - |  |  | SI | Recently completed courses of medicine |
| Q16 | - |  |  | SI | Other people’s medicine |
| Q17 | - |  |  | SI | Social and recreational drugs |
| Q18 | - |  |  | SI | Intermittent medicines (e.g. weekly or twice weekl... |
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
| RHSSTS_Active | varchar |  |  | SI | Active |
| RHSSTS_Code | varchar |  |  | NO | Code |
| RHSSTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RHSSTS_CreatedDate | date |  |  | SI | Created Date |
| RHSSTS_CreatedTime | time |  |  | SI | Created Time |
| RHSSTS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RHSSTS_DateFrom | date |  |  | SI | Date From |
| RHSSTS_DateTo | date |  |  | SI | Date To |
| RHSSTS_Desc | varchar |  |  | NO | Description |
| RHSSTS_NationalCode | varchar |  |  | SI | National Code |
| RHSSTS_Owner | varchar |  |  | SI | Owner |
| RHSSTS_RhesusNeg | varchar |  |  | SI | Rhesus Negative |
| RHSSTS_UpdatedDate | date |  |  | SI | Updated Date |
| RHSSTS_UpdatedTime | time |  |  | SI | Updated Time |
| RHSSTS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*