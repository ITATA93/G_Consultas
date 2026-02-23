# questionnaire.QTCCSVT

> Caprini Score for Venous Thromboembolism

**Schema:** questionnaire
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Caprini Score for Venous Thromboembolism

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Age (years) |
| Q02 | varchar |  |  | SI | Type of surgery |
| Q03 | varchar |  |  | SI | Recent (<1 month) event |
| Q04 | varchar |  |  | SI | Venous disease or clotting disorder |
| Q05 | varchar |  |  | SI | Mobility |
| Q06 | varchar |  |  | SI | Other present and past history |
| Q07 | varchar |  |  | SI | 0: Risk Category: Lowest |
| Q08 | varchar |  |  | SI | Risk Percent: Minimal |
| Q09 | varchar |  |  | SI | Recommended Prophylaxis: |
| Q10 | varchar |  |  | SI | Early frequent ambulation only, OR at discretion o... |
| Q11 | varchar |  |  | SI | Pneumatic compression devices OR graduated compres... |
| Q12 | varchar |  |  | SI | Duration of Chemoprophylaxis: |
| Q13 | varchar |  |  | SI | During hospitalization |
| Q14 | varchar |  |  | SI | 1 - 2: Risk Category: Low |
| Q15 | varchar |  |  | SI | Risk Percent: Minimal |
| Q16 | varchar |  |  | SI | Recommended Prophylaxis: |
| Q17 | varchar |  |  | SI | Pneumatic compression devices ± graduated compress... |
| Q18 | varchar |  |  | SI | Duration of Chemoprophylaxis: |
| Q19 | varchar |  |  | SI | During hospitalization |
| Q20 | varchar |  |  | SI | 3 - 4: Risk Category: Moderate |
| Q21 | varchar |  |  | SI | Risk Percent: 0.7% |
| Q22 | varchar |  |  | SI | Recommended Prophylaxis: |
| Q23 | varchar |  |  | SI | Pneumatic compression devices ± graduated compress... |
| Q24 | varchar |  |  | SI | Duration of Chemoprophylaxis: |
| Q25 | varchar |  |  | SI | During hospitalization |
| Q26 | varchar |  |  | SI | 5 - 6: Risk Category: High |
| Q27 | varchar |  |  | SI | Risk Percent: 1.8% |
| Q28 | varchar |  |  | SI | Recommended Prophylaxis: |
| Q29 | varchar |  |  | SI | Pneumatic compression devices AND low dose heparin... |
| Q30 | varchar |  |  | SI | Duration of Chemoprophylaxis: |
| Q31 | varchar |  |  | SI | 7–10 days total |
| Q32 | varchar |  |  | SI | 7–10 days total |
| Q33 | varchar |  |  | SI | Risk Percent: 4.0% |
| Q34 | varchar |  |  | SI | Recommended Prophylaxis: |
| Q35 | varchar |  |  | SI | Pneumatic compression devices AND low dose heparin... |
| Q36 | varchar |  |  | SI | Duration of Chemoprophylaxis: |
| Q37 | varchar |  |  | SI | 7–10 days total |
| Q38 | varchar |  |  | SI | ≥ 9: Risk Category: Highest |
| Q39 | varchar |  |  | SI | Risk Percent: 10.7%la |
| Q40 | varchar |  |  | SI | Recommended Prophylaxis: |
| Q41 | varchar |  |  | SI | Pneumatic compression devices AND low dose heparin... |
| Q42 | varchar |  |  | SI | Duration of Chemoprophylaxis: |
| Q43 | varchar |  |  | SI | 30 days total |
| Q44 | varchar |  |  | SI | Caprini Score for Venous Thromboembolism Stratifie... |
| Q45 | varchar |  |  | SI | Score |
| Q46 | varchar |  |  | SI | Classification	 |
| Q47 | varchar |  |  | SI | 0 |
| Q48 | varchar |  |  | SI | Risk Category: Lowest |
| Q49 | varchar |  |  | SI | Risk Percent: Minimal |
| Q50 | varchar |  |  | SI | 1 - 2 |
| Q51 | varchar |  |  | SI | Risk Category: Low |
| Q52 | varchar |  |  | SI | Risk Percent: Minimal |
| Q53 | varchar |  |  | SI | 3 - 4 |
| Q54 | varchar |  |  | SI | Risk Category: Moderate |
| Q55 | varchar |  |  | SI | Risk Percent: 0.7% |
| Q56 | varchar |  |  | SI | 5- 6 |
| Q57 | varchar |  |  | SI | Risk Category: High |
| Q58 | varchar |  |  | SI | Risk Percent: 1.8% |
| Q59 | varchar |  |  | SI | 7 - 8 |
| Q60 | varchar |  |  | SI | Risk Category: High |
| Q61 | varchar |  |  | SI | Risk Percent: 4.0% |
| Q62 | varchar |  |  | SI | ≥ 9 |
| Q63 | varchar |  |  | SI | Risk Category: Highest |
| Q64 | varchar |  |  | SI | Risk Percent: 10.7% |
| Q65 | varchar |  |  | SI | 0: Risk Category: Lowest, Risk Percent: Minimal |
| Q66 | varchar |  |  | SI | 1 - 2: Risk Category: Low, Risk Percent: Minimal |
| Q67 | varchar |  |  | SI | 3 - 4: Risk Category: Moderate, Risk Percent: 0.7% |
| Q68 | varchar |  |  | SI | 5 - 6: Risk Category: High, Risk Percent: 1.8% |
| Q69 | varchar |  |  | SI | 7 - 8: Risk Category: High, Risk Percent: 4.0% |
| Q70 | varchar |  |  | SI | >= 9: Risk Category: Highest, Risk Percent: 10.7% |
| Q71 | date |  |  | SI | Date |
| Q72 | time |  |  | SI | Time |
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