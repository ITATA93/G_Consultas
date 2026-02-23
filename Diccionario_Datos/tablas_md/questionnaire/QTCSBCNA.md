# questionnaire.QTCSBCNA

> Specialty Breast Care Nurse Assessment

**Schema:** questionnaire
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Specialty Breast Care Nurse Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Surgeon |
| Q04 | varchar |  |  | SI | Surgeon (public) |
| Q05 | varchar |  |  | SI | Surgeon (private) |
| Q06 | varchar |  |  | SI | Medical oncologist&nbsp; |
| Q07 | varchar |  |  | SI | Medical oncologist (public) |
| Q08 | varchar |  |  | SI | Medical oncologist (private) |
| Q09 | varchar |  |  | SI | Medical officer |
| Q10 | varchar |  |  | SI | Medical officer (public) |
| Q11 | varchar |  |  | SI | Medical officer (private) |
| Q12 | varchar |  |  | SI | Referral from&nbsp; |
| Q13 | varchar |  |  | SI | Other referral details |
| Q14 | varchar |  |  | SI | Notes |
| Q15 | varchar |  |  | SI | Core biopsy |
| Q16 | varchar |  |  | SI | Estrogen receptor (ER) |
| Q17 | varchar |  |  | SI | Progesterone receptor (PR) |
| Q18 | varchar |  |  | SI | Human epidermal growth factor receptor 2 (HER2) |
| Q19 | varchar |  |  | SI | Ki-67 nuclear antigen |
| Q20 | varchar |  |  | SI | Notes |
| Q21 | varchar |  |  | SI | ER |
| Q22 | varchar |  |  | SI | PR |
| Q23 | varchar |  |  | SI | HER2 |
| Q24 | varchar |  |  | SI | Ki67 |
| Q25 | varchar |  |  | SI | Family history of breast cancer |
| Q26 | varchar |  |  | SI | BReast CAncer gene (BRCA) mutation |
| Q27 | varchar |  |  | SI | Referral to |
| Q28 | varchar |  |  | SI | Other referral to |
| Q29 | varchar |  |  | SI | Notes |
| Q30 | varchar |  |  | SI | Operation |
| Q31 | varchar |  |  | SI | Chemotherapy (Adjuvant / Neo-adjuvant) |
| Q32 | varchar |  |  | SI | Herceptin |
| Q33 | varchar |  |  | SI | Radiotherapy&nbsp; |
| Q34 | varchar |  |  | SI | Hormone |
| Q35 | varchar |  |  | SI | Supportive medicine |
| Q36 | varchar |  |  | SI | Metastatic work up |
| Q37 | varchar |  |  | SI | Metastatic disease |
| Q38 | varchar |  |  | SI | Other site details |
| Q39 | varchar |  |  | SI | Notes |
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