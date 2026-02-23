# questionnaire.QTCDFS

> Diabetic Foot Screening

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Diabetic Foot Screening

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Amputation |
| Q04 | varchar |  |  | SI | Right foot amputation |
| Q05 | date |  |  | SI | Amputation date |
| Q06 | varchar |  |  | SI | Left foot amputation |
| Q07 | date |  |  | SI | Amputation date |
| Q08 | varchar |  |  | SI | Diabetic related amputation |
| Q09 | varchar |  |  | SI | Risk factor |
| Q10 | varchar |  |  | SI | Significant structural abnormality foot |
| Q11 | varchar |  |  | SI | Significant callus |
| Q12 | varchar |  |  | SI | Active ulceration |
| Q13 | varchar |  |  | SI | Previous ulceration |
| Q14 | varchar |  |  | SI | Able to or help to self care |
| Q15 | varchar |  |  | SI | Other risks |
| Q16 | varchar |  |  | SI | Vascular Assessment |
| Q17 | varchar |  |  | SI | Right peripheral pulse posterior tibial present |
| Q18 | varchar |  |  | SI | Right peripheral pulse dorsalis pedis present |
| Q19 | varchar |  |  | SI | Right intermittent claudication |
| Q20 | varchar |  |  | SI | Right previous vascular intervention |
| Q21 | varchar |  |  | SI | Left peripheral pulse posterior tibial present |
| Q22 | varchar |  |  | SI | Left peripheral pulse dorsalis pedis present |
| Q23 | varchar |  |  | SI | Left intermittent claudication |
| Q24 | varchar |  |  | SI | Left previous vascular intervention |
| Q25 | varchar |  |  | SI | Others |
| Q26 | varchar |  |  | SI | Neurological Assessment |
| Q27 | varchar |  |  | SI | Feet |
| Q28 | varchar |  |  | SI | (10 gram monofilament site) |
| Q29 | numeric |  |  | SI | Neurothesiometer assessment right |
| Q30 | numeric |  |  | SI | Neurothesiometer assessment left |
| Q31 | varchar |  |  | SI | Painful neuropathy (i.e. pain, paresthesia, burnin... |
| Q32 | varchar |  |  | SI | Risk Category |
| Q33 | varchar |  |  | SI | Risk category |
| Q34 | varchar |  |  | SI | Recommendation |
| Q35 | varchar |  |  | SI | Recommendation |
| Q36 | varchar |  |  | SI | Currently attending podiatrist |
| Q37 | varchar |  |  | SI | Referral to |
| Q38 | varchar |  |  | SI | Education |
| Q39 | varchar |  |  | SI | Other comments |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*