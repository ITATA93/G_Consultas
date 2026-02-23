# questionnaire.QTCFAIR

> Dementia - Find, Assess/Investigate, Refer (FAIR) Assessment

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dementia - Find, Assess/Investigate, Refer (FAIR) Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Find-Assessment and Investigation |
| Q02 | date |  |  | SI | Date |
| Q03 | varchar |  |  | SI | Step 1: Part 1 - Exclusions |
| Q04 | varchar |  |  | SI | Exclusions (select any that apply to the patient) |
| Q05 | varchar |  |  | SI | Is patient excluded from assessment |
| Q06 | varchar |  |  | SI | DO NOT PROCEED with assessment. Go to end of profo... |
| Q07 | varchar |  |  | SI | Step 1: Part 2- Diagnosis |
| Q08 | varchar |  |  | SI | Is there already a formal Diagnosis of Dementia re... |
| Q09 | varchar |  |  | SI | Continue usual care but consider referral to the M... |
| Q10 | varchar |  |  | SI | Does the patient have delirium |
| Q11 | varchar |  |  | SI | Continue to ''Step 2: Assess & Investigate'' |
| Q12 | varchar |  |  | SI | Has the patient been forgetful in the last 12 mont... |
| Q13 | varchar |  |  | SI | Who has been asked |
| Q14 | varchar |  |  | SI | Continue usual care. Go to end of questionnaire an... |
| Q15 | varchar |  |  | SI | Continue to ''Step 2: Assess & Investigate''  Plea... |
| Q16 | varchar |  |  | SI | Ensure the following orders have been recorded if ... |
| Q17 | varchar |  |  | SI | Please complete the Abbreviated Mental Test Score ... |
| Q18 | varchar |  |  | SI | Does the patient have a resolving delirium or inco... |
| Q19 | varchar |  |  | SI | Refer to GP for Review |
| Q20 | varchar |  |  | SI | Does the patient have delirium and need inpatient ... |
| Q21 | varchar |  |  | SI | Refer to DME or Mental Health Liaison Service via ... |
| Q22 | varchar |  |  | SI | Does the patient have dementia and need assistance... |
| Q23 | varchar |  |  | SI | Refer to Mental Health Liaison Service via referra... |
| Q24 | varchar |  |  | SI | Completed |
| Q25 | varchar |  |  | SI | For all emergency admissions, 75 years of age and ... |
| Q26 | varchar |  |  | SI | STEP 2 & 3: Can be completed later |
| Q27 | varchar |  |  | SI | If this patient HAS a known formal diagnosis of De... |
| Q28 | varchar |  |  | SI | If the patients Demential status is unknown, conti... |
| Q29 | varchar |  |  | SI | Continue to ''Step 1: Part 2- Diagnosis'' |
| Q30 | varchar |  |  | SI | Continue to ''Step 2: Assess & Investigate'' |
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