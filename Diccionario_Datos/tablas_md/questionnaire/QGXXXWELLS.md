# questionnaire.QGXXXWELLS

> Wells DVT Prediction Rule

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wells DVT Prediction Rule

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | bit |  |  | SI | 1 - Active cancer (treatment ongoing, within 6 mon... |
| Q02 | bit |  |  | SI | 1 - Paralysis, paresis or recent plaster immobilis... |
| Q03 | bit |  |  | SI | 1 - Recently bedridden for longer than 3 days or m... |
| Q04 | bit |  |  | SI | 1 - Localised tenderness along the distribution of... |
| Q05 | bit |  |  | SI | 1 - Entire leg swollen |
| Q06 | bit |  |  | SI | 1 - Calf swelling >3 cm compared with the asymptom... |
| Q07 | bit |  |  | SI | 1 - Unilateral pitting edema |
| Q08 | bit |  |  | SI | -2 - Alternative diagnosis as likely or greater th... |
| Q09 | varchar |  |  | SI | >=3: High probability, about 75% risk of DVT |
| Q10 | varchar |  |  | SI | 1–2: Moderate probability, about 17% risk of DVT |
| Q11 | varchar |  |  | SI | -2 - 0: Low probability, about 3% risk of DVT |
| Q12 | varchar |  |  | SI | The Wells prediction score for deep vein thrombosi... |
| Q13 | bit |  |  | SI | 1 - Collateral (nonvaricose) superficial veins pre... |
| Q14 | bit |  |  | SI | 1 - Previously documented DVT |
| Q15 | varchar |  |  | SI | <=0: Low probability, about 3% risk of DVT |
| Q16 | varchar |  |  | SI | 1–2: Moderate probability, about 17% risk of DVT |
| Q17 | varchar |  |  | SI | >=3: High probability, about 75% risk of DVT |
| Q18 | date |  |  | SI | Date |
| Q19 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Score |
| Q21 | varchar |  |  | SI | Classification |
| Q22 | varchar |  |  | SI | 1 - Active cancer (treatment ongoing, within 6 mon... |
| Q23 | varchar |  |  | SI | 1 - Paralysis, paresis or recent plaster immobilis... |
| Q24 | varchar |  |  | SI | 1 - Recently bedridden for longer than 3 days or m... |
| Q25 | varchar |  |  | SI | 1 - Localised tenderness along the distribution of... |
| Q26 | varchar |  |  | SI | 1 - Entire leg swollen |
| Q27 | varchar |  |  | SI | 1 - Calf swelling >3 cm compared with the asymptom... |
| Q28 | varchar |  |  | SI | 1 - Unilateral pitting edema |
| Q29 | varchar |  |  | SI | -2 - Alternative diagnosis as likely or greater th... |
| Q30 | varchar |  |  | SI | 1 - Collateral (nonvaricose) superficial veins pre... |
| Q31 | varchar |  |  | SI | 1 - Previously documented DVT |
| Q32 | varchar |  |  | SI | ≤0 |
| Q33 | varchar |  |  | SI | Low probability, about 3% risk of DVT |
| Q34 | varchar |  |  | SI | 1 – 2 |
| Q35 | varchar |  |  | SI | Moderate probability, about 17% risk of DVT |
| Q36 | varchar |  |  | SI | ≥3 |
| Q37 | varchar |  |  | SI | High probability, about 75% risk of DVT |
| Q38 | varchar |  |  | SI | Active cancer (treatment ongoing, within 6 months ... |
| Q39 | varchar |  |  | SI | Paralysis, paresis or recent plaster immobilisatio... |
| Q40 | varchar |  |  | SI | Recently bedridden for longer than 3 days or major... |
| Q41 | varchar |  |  | SI | Localised tenderness along the distribution of the... |
| Q42 | varchar |  |  | SI | Entire leg swollen |
| Q43 | varchar |  |  | SI | Calf swelling >3 cm compared with the asymptomatic... |
| Q44 | varchar |  |  | SI | Unilateral pitting edema |
| Q45 | varchar |  |  | SI | Alternative diagnosis as likely or greater than th... |
| Q46 | varchar |  |  | SI | Collateral (nonvaricose) superficial veins present |
| Q47 | varchar |  |  | SI | Previously documented DVT |
| Q48 | varchar |  |  | SI | Primary References |
| Q49 | varchar |  |  | SI | Wells PS, Hirsh J, Anderson DR, Lensing AW, Foster... |
| Q50 | varchar |  |  | SI | Wells PS, Anderson DR, Bormanis J, et al. Value of... |
| Q51 | varchar |  |  | SI | Wells PS, Anderson DR, Rodger M, Forgie M, Kearon ... |
| Q52 | varchar |  |  | SI | Tool Validation |
| Q53 | varchar |  |  | SI | Scarvelis D, Wells PS. Diagnosis and treatment of ... |
| Q54 | varchar |  |  | SI | Author endorsed tool: |
| Q55 | varchar |  |  | SI | https://www.mdcalc.com/calc/362/wells-criteria-dvt... |
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