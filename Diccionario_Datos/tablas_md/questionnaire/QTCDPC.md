# questionnaire.QTCDPC

> Discharge Planning Checklist

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Discharge Planning Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Admission date |
| Q04 | varchar |  |  | SI | Admission time |
| Q05 | date |  |  | SI | Date of initial screening |
| Q06 | time |  |  | SI | Time of initial screening |
| Q07 | varchar |  |  | SI | a. Use of discharge medications |
| Q08 | varchar |  |  | SI | b. Post discharge care |
| Q09 | varchar |  |  | SI | c. Nutritional discharge instructions |
| Q10 | varchar |  |  | SI | d. Use of medical equipment |
| Q11 | varchar |  |  | SI | e. Instructions on activity of daily living |
| Q12 | varchar |  |  | SI | f. How to seek medical services when emergency rel... |
| Q13 | varchar |  |  | SI | g. Patient's booking for appointment including tes... |
| Q14 | varchar |  |  | SI | Interventions carried out to achieve educational n... |
| Q15 | varchar |  |  | SI | The patient or family member has need to have educ... |
| Q16 | varchar |  |  | SI | The patient needs transportation: |
| Q17 | varchar |  |  | SI | a. Ambulance / Car |
| Q18 | varchar |  |  | SI | b. Medivac |
| Q19 | varchar |  |  | SI | c. Private car |
| Q20 | varchar |  |  | SI | Interventions carried out to achieve transportatio... |
| Q21 | varchar |  |  | SI | Patient is in need of referral to: |
| Q22 | varchar |  |  | SI | a. Social worker / psychologist counselling, for c... |
| Q23 | varchar |  |  | SI | b. Home healthcare services |
| Q24 | varchar |  |  | SI | c. Other post-discharge agencies |
| Q25 | varchar |  |  | SI | Interventions carried out to achieve referral need... |
| Q26 | varchar |  |  | SI | • Discharge planning screening shall be documented... |
| Q27 | varchar |  |  | SI | • Physician shall use this checklist during patien... |
| Q28 | varchar |  |  | SI | • If any box checked yes, physician shall carry ou... |
| Q29 | varchar |  |  | SI | • The primary nurse shall coordinate the referral ... |
| Q30 | varchar |  |  | SI | Patient needs support with: |
| Q31 | varchar |  |  | SI | a. Financial needs expected after discharge |
| Q32 | varchar |  |  | SI | b. Other discharge planning problems identified at... |
| Q33 | varchar |  |  | SI | Interventions carried out to achieve financial and... |
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