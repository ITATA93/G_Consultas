# SQLUser.LBC_BloodProductEntryMode

**Schema:** SQLUser
**Columnas:** 113
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPEM_RowID | bigint | PK |  | NO | - |
| LBCBPEM_Code | varchar |  |  | NO | Code |
| LBCBPEM_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCBPEM_CreatedDate | date |  |  | SI | Created Date |
| LBCBPEM_CreatedTime | time |  |  | SI | Created Time |
| LBCBPEM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBPEM_Desc | varchar |  |  | NO | Description |
| LBCBPEM_ExcludeFromElectronicIssue | varchar |  |  | SI | Exclude From Electronic Issue |
| LBCBPEM_Owner | varchar |  |  | SI | Owner |
| LBCBPEM_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBPEM_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBPEM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Does the patient have a fever of 38C or above? |
| Q04 | - |  |  | SI | Does the patient have any symptoms of lower respir... |
| Q05 | - |  |  | SI | Has the patient travelled to Wuhan, Hubei Province... |
| Q06 | - |  |  | SI | Has the patient had any close contact with a perso... |
| Q07 | - |  |  | SI | Contact is defined as: |
| Q08 | - |  |  | SI | • Providing direct care for COVID-19 patients, wor... |
| Q09 | - |  |  | SI | • Working together in proximity or sharing the sam... |
| Q10 | - |  |  | SI | • Traveling together with a COVID-19 patient in an... |
| Q11 | - |  |  | SI | Has the patient had any close contact with a perso... |
| Q12 | - |  |  | SI | WHO Infection Prevention and Control measures at t... |
| Q13 | - |  |  | SI | • Give suspect patient a medical mask and direct p... |
| Q14 | - |  |  | SI | • Keep at least 1 meter distance between suspected... |
| Q15 | - |  |  | SI | • Instruct all patients to cover nose and mouth du... |
| Q16 | - |  |  | SI | • Perform hand hygiene after contact with respirat... |
| Q17 | - |  |  | SI | Score |
| Q18 | - |  |  | SI | Classification |
| Q19 | - |  |  | SI | ≤ 20 |
| Q20 | - |  |  | SI | This patient does NOT meet the WHO clinical criter... |
| Q21 | - |  |  | SI | ≥ 21 |
| Q22 | - |  |  | SI | This patient meets the WHO clinical criteria for a... |
| Q23 | - |  |  | SI | <= 20: This patient does NOT meet the WHO clinical... |
| Q24 | - |  |  | SI | >= 21: This patient meets the WHO clinical criteri... |
| Q25 | - |  |  | SI | This is a screening tool for the initial assessmen... |
| Q26 | - |  |  | SI | Coronavirus Disease 2019 (COVID-19) Global Cases b... |
| Q26a | - |  |  | SI | For the most up to date list of countries and terr... |
| Q27 | - |  |  | SI | • Living in the same household as a COVID-19 patie... |
| Q28 | - |  |  | SI | Patient has fever or symptoms of lower respiratory... |
| Q29 | - |  |  | SI | Fever with no other symptoms |
| Q30 | - |  |  | SI | Acute respiratory infection of any degree of sever... |
| Q31 | - |  |  | SI | Severe acute respiratory infection requiring admis... |
| Q32 | - |  |  | SI | Reserved symptom 1 |
| Q33 | - |  |  | SI | Reserved symptom 2 |
| Q34 | - |  |  | SI | Other comments |
| Q35 | - |  |  | SI | A history of travel to or residence in a country, ... |
| Q35a | - |  |  | SI | OR |
| Q35b | - |  |  | SI | Had contact with a a confirmed or probable case of... |
| Q36 | - |  |  | SI | *OTHER countries to ask for - Hong Kong, Japan, Ma... |
| Q36a | - |  |  | SI | *OTHER countries to ask for - Category 1 countries... |
| Q36b | - |  |  | SI | *OTHER countries to ask for - Category 2 countries... |
| Q36c | - |  |  | SI | *Except areas of the country specifically referred... |
| Q37 | - |  |  | SI | History of travel to or residence in a country, ar... |
| Q38 | - |  |  | SI | Contact with a confirmed or probable case of COVID... |
| Q39 | - |  |  | SI | Worked in or attended a health care facility where... |
| Q40 | - |  |  | SI | Reserved travel 1 |
| Q41 | - |  |  | SI | Reserved travel 2 |
| Q42 | - |  |  | SI | Other comments |
| Q43 | - |  |  | SI | Definition of contact |
| Q43a | - |  |  | SI | A contact is a person who experienced any one of t... |
| Q43b | - |  |  | SI | 1. Face-to-face contact with a probable or confirm... |
| Q43c | - |  |  | SI | 2. Direct physical contact with a probable or conf... |
| Q43d | - |  |  | SI | 3. Direct care for a patient with probable or conf... |
| Q43e | - |  |  | SI | OR |
| Q43f | - |  |  | SI | 4. Other situations as indicated by local risk ass... |
| Q43g | - |  |  | SI | Note: for confirmed asymptomatic cases, the period... |
| Q44 | - |  |  | SI | A patient with severe acute respiratory illness (f... |
| Q44a | - |  |  | SI | AND the absence of an alternative diagnosis that f... |
| Q45 | - |  |  | SI | Has the patient travelled from another State in th... |
| Q46 | - |  |  | SI | Is the patient a healthcare worker? |
| Q47 | - |  |  | SI | Has the patient been advised to self-isolate by as... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*