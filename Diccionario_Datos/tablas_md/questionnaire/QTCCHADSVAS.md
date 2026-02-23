# questionnaire.QTCCHADSVAS

> CHA₂DS₂-VASc Score for Atrial Fibrillation Stroke Risk

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CHA₂DS₂-VASc Score for Atrial Fibrillation Stroke Risk

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Age |
| Q02 | varchar |  |  | SI | Sex |
| Q03 | varchar |  |  | SI | Congestive heart failure history	 |
| Q04 | varchar |  |  | SI | Hypertension history	 |
| Q05 | varchar |  |  | SI | Stroke / Transient Ischemic Attack (TIA) / Thrombo... |
| Q06 | varchar |  |  | SI | Vascular disease history	 |
| Q07 | varchar |  |  | SI | Diabetes history	 |
| Q08 | varchar |  |  | SI | Stroke or Thromboembolism (TE) / 100 years at risk... |
| Q09 | varchar |  |  | SI | STROKE OR TE/100 PERSON-YEARS |
| Q10 | varchar |  |  | SI | Score	 |
| Q11 | varchar |  |  | SI | Ischemic Stroke	 |
| Q12 | varchar |  |  | SI | Stroke / TIA / TE |
| Q13 | varchar |  |  | SI | 0 |
| Q14 | varchar |  |  | SI | 1 |
| Q15 | varchar |  |  | SI | 2 |
| Q16 | varchar |  |  | SI | 3 |
| Q17 | varchar |  |  | SI | 4 |
| Q18 | varchar |  |  | SI | 5 |
| Q19 | varchar |  |  | SI | 6 |
| Q20 | varchar |  |  | SI | 7 |
| Q21 | varchar |  |  | SI | 8 |
| Q22 | varchar |  |  | SI | 9 |
| Q23 | varchar |  |  | SI | 0.2	 |
| Q24 | varchar |  |  | SI | 0.6 |
| Q25 | varchar |  |  | SI | 2.2 |
| Q26 | varchar |  |  | SI | 3.2	 |
| Q27 | varchar |  |  | SI | 4.8 |
| Q28 | varchar |  |  | SI | 7.2 |
| Q29 | varchar |  |  | SI | 9.7 |
| Q30 | varchar |  |  | SI | 11.2	 |
| Q31 | varchar |  |  | SI | 10.8	 |
| Q32 | varchar |  |  | SI | 12.23	 |
| Q33 | varchar |  |  | SI | 0.3 |
| Q34 | varchar |  |  | SI | 0.9 |
| Q35 | varchar |  |  | SI | 2.9 |
| Q36 | varchar |  |  | SI | 4.6 |
| Q37 | varchar |  |  | SI | 6.7 |
| Q38 | varchar |  |  | SI | 10.0 |
| Q39 | varchar |  |  | SI | 13.6 |
| Q40 | varchar |  |  | SI | 15.7 |
| Q41 | varchar |  |  | SI | 15.2 |
| Q42 | varchar |  |  | SI | 17.4 |
| Q43 | varchar |  |  | SI | Score        |
| Q44 | varchar |  |  | SI | Classification	 |
| Q45 | varchar |  |  | SI | 0 |
| Q46 | varchar |  |  | SI | “Low” risk and may not require anticoagulation |
| Q47 | varchar |  |  | SI | 1 |
| Q48 | varchar |  |  | SI | “Low-moderate” risk and should consider anti-plate... |
| Q49 | varchar |  |  | SI | ≥2 |
| Q50 | varchar |  |  | SI | “Moderate-high” risk and should otherwise be an an... |
| Q51 | varchar |  |  | SI | The CHA2DS2-VASc score is one of several risk stra... |
| Q52 | varchar |  |  | SI | 1 year risk of a Thromboembolism (TE) event in a n... |
| Q53 | varchar |  |  | SI | 0: “Low” risk and may not require anticoagulation |
| Q54 | varchar |  |  | SI | 1: “Low-moderate” risk and should consider anti-pl... |
| Q55 | varchar |  |  | SI | >=2: “Moderate-high” risk and should otherwise be ... |
| Q56 | date |  |  | SI | Date |
| Q57 | time |  |  | SI | Time |
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