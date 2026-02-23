# SQLUser.OE_FilmExecute

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEFE_RowId | bigint | PK |  | NO | - |
| OEFE_Comment1 | varchar |  |  | SI | Comment1 |
| OEFE_Comment2 | varchar |  |  | SI | Comment2 |
| OEFE_Comment3 | varchar |  |  | SI | Comment3 |
| OEFE_Date | date |  |  | SI | Date |
| OEFE_Personnel | varchar |  |  | SI | Personnel |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age |
| Q04 | - |  |  | SI | years |
| Q05 | - |  |  | SI | Albumin |
| Q06 | - |  |  | SI | g/L |
| Q07 | - |  |  | SI | Bilirubin (initial) |
| Q08 | - |  |  | SI | mg/dL |
| Q09 | - |  |  | SI | Bilirubin (day 7) |
| Q10 | - |  |  | SI | mg/dL |
| Q11 | - |  |  | SI | Creatinine (Cr) |
| Q12 | - |  |  | SI | mg/dL |
| Q13 | - |  |  | SI | Prothrombin Time (PT) |
| Q14 | - |  |  | SI | sec |
| Q15 | - |  |  | SI | Score |
| Q16 | - |  |  | SI | Lille Score Item |
| Q17 | - |  |  | SI | Albumin |
| Q18 | - |  |  | SI | Bilirubin (initial) |
| Q19 | - |  |  | SI | Bilirubin (day 7) |
| Q20 | - |  |  | SI | Creatinine |
| Q21 | - |  |  | SI | Prothrombin Time |
| Q22 | - |  |  | SI | Normal Range |
| Q23 | - |  |  | SI | 35 - 55 |
| Q24 | - |  |  | SI | 0.3 - 1.9 |
| Q25 | - |  |  | SI | 0.3 - 1.9 |
| Q26 | - |  |  | SI | 0.7 - 1.3 |
| Q27 | - |  |  | SI | 11 – 13 |
| Q28 | - |  |  | SI | Unit of Measure |
| Q29 | - |  |  | SI | g/L |
| Q30 | - |  |  | SI | mg/dL |
| Q31 | - |  |  | SI | mg/dL |
| Q32 | - |  |  | SI | mg/dL |
| Q33 | - |  |  | SI | seconds |
| Q34 | - |  |  | SI | Score |
| Q35 | - |  |  | SI | Classification |
| Q36 | - |  |  | SI | ≤ 0.45 |
| Q37 | - |  |  | SI | > 0.45 |
| Q38 | - |  |  | SI | Predict a 6-month survival of 85% |
| Q39 | - |  |  | SI | Predict a 6-month survival of 25% |
| Q40 | - |  |  | SI | ≤ 0.45: Predict a 6-month survival of 85% |
| Q41 | - |  |  | SI | > 0.45: Predict a 6-month survival of 25% |
| Q42 | - |  |  | SI | The Lille Model Score risk stratifies patients alr... |
| Q43 | - |  |  | SI | It should be used for the identification of patien... |
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