# questionnaire.QTCGSR

> GRACE Score V1.0

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* GRACE Score V1.0

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Age |
| Q02 | varchar |  |  | SI | Systolic Blood Pressure (SBP) |
| Q03 | varchar |  |  | SI | Heart Rate (HR) |
| Q04 | varchar |  |  | SI | Serum Creatinine (sCr) |
| Q05 | varchar |  |  | SI | Congestive Heart Failure (CHF) killip class |
| Q06 | varchar |  |  | SI | Other risk factors |
| Q07 | varchar |  |  | SI | Score |
| Q08 | varchar |  |  | SI | Classification |
| Q09 | varchar |  |  | SI | Total GRACE Score (1 to 372 points) |
| Q10 | varchar |  |  | SI | Score predicts in hospital and 6 month risk of dea... |
| Q11 | varchar |  |  | SI | Non-ST Elevation Acute Coronary Syndrome |
| Q12 | varchar |  |  | SI | <109 |
| Q13 | varchar |  |  | SI | Low risk - Mortality <1% (Mortality in the hospita... |
| Q14 | varchar |  |  | SI | 109 - 140 |
| Q15 | varchar |  |  | SI | Intermediate risk - Mortality 1-3% (Mortality in t... |
| Q16 | varchar |  |  | SI |  >140 |
| Q17 | varchar |  |  | SI | High risk - Mortality >3% (Mortality in the hospit... |
| Q18 | varchar |  |  | SI | <89 |
| Q19 | varchar |  |  | SI | Low risk - Mortality <3% (Mortality at 6 months) |
| Q20 | varchar |  |  | SI | 89 - 118 |
| Q21 | varchar |  |  | SI | Intermediate risk - Mortality 3-8% (Mortality at 6... |
| Q22 | varchar |  |  | SI | >118 |
| Q23 | varchar |  |  | SI | High risk - Mortality >8% (Mortality at 6 months) |
| Q24 | varchar |  |  | SI | ST-Elevation Acute Coronary Syndrome |
| Q25 | varchar |  |  | SI | <126 |
| Q26 | varchar |  |  | SI | Low risk - Mortality <2% (Mortality in the hospita... |
| Q27 | varchar |  |  | SI | 126 - 154 |
| Q28 | varchar |  |  | SI | Intermediate risk - Mortality 2-5% (Mortality in t... |
| Q29 | varchar |  |  | SI | >154 |
| Q30 | varchar |  |  | SI | High risk - Mortality >5% (Mortality in the hospit... |
| Q31 | varchar |  |  | SI | <100 |
| Q32 | varchar |  |  | SI | Low risk - Mortality <4.5% (Mortality at 6 months) |
| Q33 | varchar |  |  | SI | 100 - 127 |
| Q34 | varchar |  |  | SI | Intermediate risk - Mortality 4.5-11% (Mortality a... |
| Q35 | varchar |  |  | SI | >127 |
| Q36 | varchar |  |  | SI | High risk -Mortality >11% (Mortality at 6 months) |
| Q37 | varchar |  |  | SI | <109: Low risk - Mortality <1% (Mortality in the h... |
| Q38 | varchar |  |  | SI | 109 - 140: Intermediate risk - Mortality 1-3% (Mor... |
| Q39 | varchar |  |  | SI | >140: High risk - Mortality >3% (Mortality in the ... |
| Q40 | varchar |  |  | SI | <89: Low risk - Mortality <3% (Mortality at 6 mont... |
| Q41 | varchar |  |  | SI | 89 - 118: Intermediate risk - Mortality 3-8% (Mort... |
| Q42 | varchar |  |  | SI | >118: High risk - Mortality >8% (Mortality at 6 mo... |
| Q43 | varchar |  |  | SI | <126: Low risk - Mortality <2% (Mortality in the h... |
| Q44 | varchar |  |  | SI | 126 - 154: Intermediate risk - Mortality 2-5% (Mor... |
| Q45 | varchar |  |  | SI | >154: High risk - Mortality >5% (Mortality in the ... |
| Q46 | varchar |  |  | SI | <100: Low risk - Mortality <4.5% (Mortality at 6 m... |
| Q47 | varchar |  |  | SI | 100 - 127: Intermediate risk - Mortality 4.5-11% (... |
| Q48 | varchar |  |  | SI | >127: High risk -Mortality >11% (Mortality at 6 mo... |
| Q49 | varchar |  |  | SI | Global Registry of Acute Coronary Events (GRACE) V... |
| Q50 | varchar |  |  | SI | The total GRACE Score is from 1 to 372 points. The... |
| Q51 | varchar |  |  | SI | Please find the interpretation of the score below |
| Q52 | date |  |  | SI | Date |
| Q53 | time |  |  | SI | Time |
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