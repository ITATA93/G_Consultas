# questionnaire.QTCMST

> Malnutrition Screening Tool (MST)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Malnutrition Screening Tool (MST)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Have you/the patient lost weight recently (i.e. in... |
| Q02 | varchar |  |  | SI | How much?	 |
| Q03 | varchar |  |  | SI | Have you/the patient been eating poorly because of... |
| Q04 | varchar |  |  | SI | Score |
| Q05 | varchar |  |  | SI | Classification |
| Q06 | varchar |  |  | SI | ≥ 2 |
| Q07 | varchar |  |  | SI | Positive for nutrition risk |
| Q08 | varchar |  |  | SI | < 2 |
| Q09 | varchar |  |  | SI | Negative for nutrition risk	 |
| Q10 | varchar |  |  | SI | Nutrition screening tool assesses whether an adult... |
| Q11 | varchar |  |  | SI | ≥ 2: Positive for nutrition risk	 |
| Q12 | varchar |  |  | SI | < 2: Negative for nutrition risk |
| Q13 | varchar |  |  | SI | 2 - 5 |
| Q14 | varchar |  |  | SI | Indicates risk of malnutrition |
| Q15 | varchar |  |  | SI | 0 - 1 |
| Q16 | varchar |  |  | SI | Indicates no risk of malnutrition |
| Q17 | varchar |  |  | SI | 2 - 5: Indicates risk of malnutrition |
| Q18 | varchar |  |  | SI | 0 - 1: Indicates no risk of malnutrition |
| Q19 | varchar |  |  | SI | • Patients who are not at risk of malnutrition (MS... |
| Q20 | varchar |  |  | SI | • Patients who are at risk of malnutrition (MST sc... |
| Q21 | varchar |  |  | SI | appropriate form of nutrition support. |
| Q22 | varchar |  |  | SI | • Note: overweight / obese clients who have unexpl... |
| Q23 | varchar |  |  | SI | The following question(s) related to swallowing ar... |
| Q24 | varchar |  |  | SI | Does the patient have difficulty swallowing? |
| Q25 | varchar |  |  | SI | Speech pathology referral required |
| Q26 | varchar |  |  | SI | Queensland Health, Royal Brisbane and Women's Hosp... |
| Q27 | varchar |  |  | SI | https://www.health.qld.gov.au/__data/assets/pdf_fi... |
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