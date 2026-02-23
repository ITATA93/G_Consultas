# SQLUser.PAC_EmailValidationStatus

**Schema:** SQLUser
**Columnas:** 105
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EMVST_RowId | bigint | PK |  | NO | - |
| EMVST_Code | varchar |  |  | NO | Code |
| EMVST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EMVST_CreatedDate | date |  |  | SI | Created Date |
| EMVST_CreatedTime | time |  |  | SI | Created Time |
| EMVST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EMVST_DateFrom | date |  |  | SI | Date From |
| EMVST_DateTo | date |  |  | SI | Date To |
| EMVST_Desc | varchar |  |  | NO | Description |
| EMVST_Owner | varchar |  |  | SI | Owner |
| EMVST_UpdatedDate | date |  |  | SI | Updated Date |
| EMVST_UpdatedTime | time |  |  | SI | Updated Time |
| EMVST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Clinical context |
| Q04 | - |  |  | SI | Social worker contacted |
| Q05 | - |  |  | SI | Notes |
| Q06 | - |  |  | SI | Dummy1 |
| Q07 | - |  |  | SI | Dummy2 |
| Q08 | - |  |  | SI | Chaplain / Religious delegate contacted |
| Q09 | - |  |  | SI | Notes |
| Q10 | - |  |  | SI | Clinical photographs |
| Q11 | - |  |  | SI | Notes |
| Q12 | - |  |  | SI | Consent for clinical photos, if applicable |
| Q13 | - |  |  | SI | Notes |
| Q14 | - |  |  | SI | Parent's wishes |
| Q15 | - |  |  | SI | Notes |
| Q16 | - |  |  | SI | Memento photographs downloaded to USB |
| Q17 | - |  |  | SI | Notes |
| Q18 | - |  |  | SI | USB given to parents |
| Q19 | - |  |  | SI | Notes |
| Q20 | - |  |  | SI | Memory booklet |
| Q21 | - |  |  | SI | Notes |
| Q22 | - |  |  | SI | Follow up organised |
| Q23 | - |  |  | SI | Follow up details |
| Q24 | - |  |  | SI | Additional notes |
| Q25 | - |  |  | SI | Stillbirth |
| Q26 | - |  |  | SI | Discussion with parents |
| Q27 | - |  |  | SI | Notes |
| Q28 | - |  |  | SI | Midwifery care and documentation |
| Q29 | - |  |  | SI | Notes |
| Q30 | - |  |  | SI | Medical officer responsibilities |
| Q31 | - |  |  | SI | Additional notes |
| Q32 | - |  |  | SI | Neonatal Death |
| Q33 | - |  |  | SI | Discussion with parents |
| Q34 | - |  |  | SI | Notes |
| Q35 | - |  |  | SI | Midwifery care and documentation |
| Q36 | - |  |  | SI | Notes |
| Q37 | - |  |  | SI | Medical officer responsibilities |
| Q38 | - |  |  | SI | Additional notes |
| Q39 | - |  |  | SI | Second Trimester Termination (Registerable) |
| Q40 | - |  |  | SI | Discussion with parents |
| Q41 | - |  |  | SI | Notes |
| Q42 | - |  |  | SI | Midwifery care and documentation |
| Q43 | - |  |  | SI | Midwifery care and documentation notes |
| Q44 | - |  |  | SI | Medical officer responsibilities |
| Q45 | - |  |  | SI | Additional notes |
| Q46 | - |  |  | SI | Second Trimester Miscarriage / Termination (Non-Re... |
| Q47 | - |  |  | SI | Discussion with parents |
| Q48 | - |  |  | SI | Notes |
| Q49 | - |  |  | SI | Midwifery care and documentation |
| Q50 | - |  |  | SI | Notes |
| Q51 | - |  |  | SI | Medical officer responsibilities |
| Q52 | - |  |  | SI | Additional notes |
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