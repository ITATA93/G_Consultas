# SQLUser.PAC_ServiceAgreementHAR

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HAR_ParRef | bigint | PK |  | NO | PAC_ServiceAgreement Parent Reference |
| HAR_Childsub | double |  |  | NO | Childsub |
| HAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HAR_CreatedDate | date |  |  | SI | Created Date |
| HAR_CreatedTime | time |  |  | SI | Created Time |
| HAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HAR_HCR_DR | bigint |  | FK | SI | Des Ref HCR |
| HAR_RowId | varchar |  |  | NO | - |
| HAR_UpdatedDate | date |  |  | SI | Updated Date |
| HAR_UpdatedTime | time |  |  | SI | Updated Time |
| HAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Gestational age |
| Q02 | - |  |  | SI | Alertness |
| Q03 | - |  |  | SI | Heart rate maximum |
| Q04 | - |  |  | SI | Oxygen saturation minimum |
| Q05 | - |  |  | SI | Brow bulge |
| Q06 | - |  |  | SI | Eye squeeze |
| Q07 | - |  |  | SI | Nasolabial furrow |
| Q08 | - |  |  | SI | Minimum score : 0 |
| Q09 | - |  |  | SI | Maximum score : 21 |
| Q10 | - |  |  | SI | Score above 6 indicates pain |
| Q11 | - |  |  | SI | Premature Infant Pain Profile (PIPP) is used to as... |
| Q12 | - |  |  | SI | Absent: is defined as 0% to 9% of the observation ... |
| Q13 | - |  |  | SI | Minimal: 10% to 39% of the time |
| Q14 | - |  |  | SI | Moderate: 40% to 69% of the time |
| Q15 | - |  |  | SI | Maximal: 70% or more of the time |
| Q16 | - |  |  | SI | Date |
| Q17 | - |  |  | SI | Time |
| Q18 | - |  |  | SI | Score |
| Q19 | - |  |  | SI | Classification |
| Q20 | - |  |  | SI | ≤ 6 |
| Q21 | - |  |  | SI | Minimal or no pain |
| Q22 | - |  |  | SI | 7 - 12 |
| Q23 | - |  |  | SI | Slight to moderate pain |
| Q24 | - |  |  | SI | ≥ 13 |
| Q25 | - |  |  | SI | Severe pain |
| Q26 | - |  |  | SI | ≤ 6: Minimal or no pain |
| Q27 | - |  |  | SI | 7 - 12: Slight to moderate pain |
| Q28 | - |  |  | SI | ≥ 13: Severe pain |
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