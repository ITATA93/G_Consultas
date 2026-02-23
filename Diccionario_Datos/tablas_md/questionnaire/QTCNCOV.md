# questionnaire.QTCNCOV

> Coronavirus Disease 2019 (COVID-19) Screening Tool

**Schema:** questionnaire
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Coronavirus Disease 2019 (COVID-19) Screening Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Does the patient have a fever of 38C or above? |
| Q04 | varchar |  |  | SI | Does the patient have any symptoms of lower respir... |
| Q05 | varchar |  |  | SI | Has the patient travelled to Wuhan, Hubei Province... |
| Q06 | varchar |  |  | SI | Has the patient had any close contact with a perso... |
| Q07 | varchar |  |  | SI | Contact is defined as: |
| Q08 | varchar |  |  | SI | • Providing direct care for COVID-19 patients, wor... |
| Q09 | varchar |  |  | SI | • Working together in proximity or sharing the sam... |
| Q10 | varchar |  |  | SI | • Traveling together with a COVID-19 patient in an... |
| Q11 | varchar |  |  | SI | Has the patient had any close contact with a perso... |
| Q12 | varchar |  |  | SI | WHO Infection Prevention and Control measures at t... |
| Q13 | varchar |  |  | SI | • Give suspect patient a medical mask and direct p... |
| Q14 | varchar |  |  | SI | • Keep at least 1 meter distance between suspected... |
| Q15 | varchar |  |  | SI | • Instruct all patients to cover nose and mouth du... |
| Q16 | varchar |  |  | SI | • Perform hand hygiene after contact with respirat... |
| Q17 | varchar |  |  | SI | Score |
| Q18 | varchar |  |  | SI | Classification |
| Q19 | varchar |  |  | SI | ≤ 20 |
| Q20 | varchar |  |  | SI | This patient does NOT meet the WHO clinical criter... |
| Q21 | varchar |  |  | SI | ≥ 21 |
| Q22 | varchar |  |  | SI | This patient meets the WHO clinical criteria for a... |
| Q23 | varchar |  |  | SI | <= 20: This patient does NOT meet the WHO clinical... |
| Q24 | varchar |  |  | SI | >= 21: This patient meets the WHO clinical criteri... |
| Q25 | varchar |  |  | SI | This is a screening tool for the initial assessmen... |
| Q26 | varchar |  |  | SI | Coronavirus Disease 2019 (COVID-19) Global Cases b... |
| Q26a | varchar |  |  | SI | For the most up to date list of countries and terr... |
| Q27 | varchar |  |  | SI | • Living in the same household as a COVID-19 patie... |
| Q28 | varchar |  |  | SI | Patient has fever or symptoms of lower respiratory... |
| Q29 | varchar |  |  | SI | Fever with no other symptoms |
| Q30 | varchar |  |  | SI | Acute respiratory infection of any degree of sever... |
| Q31 | varchar |  |  | SI | Severe acute respiratory infection requiring admis... |
| Q32 | varchar |  |  | SI | Reserved symptom 1 |
| Q33 | varchar |  |  | SI | Reserved symptom 2 |
| Q34 | varchar |  |  | SI | Other comments |
| Q35 | varchar |  |  | SI | A history of travel to or residence in a country, ... |
| Q35a | varchar |  |  | SI | OR |
| Q35b | varchar |  |  | SI | Had contact with a a confirmed or probable case of... |
| Q36 | varchar |  |  | SI | *OTHER countries to ask for - Hong Kong, Japan, Ma... |
| Q36a | varchar |  |  | SI | *OTHER countries to ask for - Category 1 countries... |
| Q36b | varchar |  |  | SI | *OTHER countries to ask for - Category 2 countries... |
| Q36c | varchar |  |  | SI | *Except areas of the country specifically referred... |
| Q37 | varchar |  |  | SI | History of travel to or residence in a country, ar... |
| Q38 | varchar |  |  | SI | Contact with a confirmed or probable case of COVID... |
| Q39 | varchar |  |  | SI | Worked in or attended a health care facility where... |
| Q40 | varchar |  |  | SI | Reserved travel 1 |
| Q41 | varchar |  |  | SI | Reserved travel 2 |
| Q42 | varchar |  |  | SI | Other comments |
| Q43 | varchar |  |  | SI | Definition of contact |
| Q43a | varchar |  |  | SI | A contact is a person who experienced any one of t... |
| Q43b | varchar |  |  | SI | 1. Face-to-face contact with a probable or confirm... |
| Q43c | varchar |  |  | SI | 2. Direct physical contact with a probable or conf... |
| Q43d | varchar |  |  | SI | 3. Direct care for a patient with probable or conf... |
| Q43e | varchar |  |  | SI | OR |
| Q43f | varchar |  |  | SI | 4. Other situations as indicated by local risk ass... |
| Q43g | varchar |  |  | SI | Note: for confirmed asymptomatic cases, the period... |
| Q44 | varchar |  |  | SI | A patient with severe acute respiratory illness (f... |
| Q44a | varchar |  |  | SI | AND the absence of an alternative diagnosis that f... |
| Q45 | varchar |  |  | SI | Has the patient travelled from another State in th... |
| Q46 | varchar |  |  | SI | Is the patient a healthcare worker? |
| Q47 | varchar |  |  | SI | Has the patient been advised to self-isolate by as... |
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