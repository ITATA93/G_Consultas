# questionnaire.QTCOTSA

> Oral Trials / Swallow Assessment

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Oral Trials / Swallow Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q04 | varchar |  |  | SI | Respiratory sufficiency and coordination during or... |
| Q04ObsDR | varchar |  | FK | SI | Respiratory sufficiency and coordination during or... |
| Q05 | varchar |  |  | SI | Respiratory sufficiency and coordination comments |
| Q06 | varchar |  |  | SI | Oral trial finding |
| Q07 | varchar |  |  | SI | Phase of dysphagia |
| Q08 | varchar |  |  | SI | Severity of dysphagia |
| Q09 | varchar |  |  | SI | Contributing factors |
| Q10 | varchar |  |  | SI | Contributing factors comments |
| Q11 | varchar |  |  | SI | Impression |
| Q13 | varchar |  |  | SI | Overall impression |
| Q14 | varchar |  |  | SI | Diet |
| Q15 | varchar |  |  | SI | Recommended diet |
| Q16 | varchar |  |  | SI | Texture |
| Q17 | varchar |  |  | SI | Fluids |
| Q18 | varchar |  |  | SI | Diet comments |
| Q19 | varchar |  |  | SI | Precautions |
| Q20 | varchar |  |  | SI | Diet safety precautions |
| Q21 | varchar |  |  | SI | Diet safety precautions notes |
| Q22 | varchar |  |  | SI | Review |
| Q23 | varchar |  |  | SI | Review in |
| Q24 | varchar |  |  | SI | Ear Nose and Throat (ENT) investigation indicated? |
| Q25 | varchar |  |  | SI | Videofluoroscopy indicated? |
| Q26 | varchar |  |  | SI | Plan comments |
| Q27 | varchar |  |  | SI | Intervention program |
| Q28 | varchar |  |  | SI | Referrals |
| Q29 | varchar |  |  | SI | Referral orders placed in TrakCare? |
| Q30 | varchar |  |  | SI | Referral(s) external to TrakCare comment |
| Q31 | varchar |  |  | SI | Referral(s) external to TrakCare completed? |
| Q32 | varchar |  |  | SI | Referral detail |
| Q33 | varchar |  |  | SI | Education provided to |
| Q34 | varchar |  |  | SI | Type of education provided |
| Q35 | varchar |  |  | SI | Education details |
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