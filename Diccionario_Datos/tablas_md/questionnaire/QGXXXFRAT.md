# questionnaire.QGXXXFRAT

> Falls Risk Assessment Tool (FRAT) big

**Schema:** questionnaire
**Columnas:** 92
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Falls Risk Assessment Tool (FRAT) big

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Has the patient’s environment been assessed as saf... |
| Q02 | varchar |  |  | SI | Risk Factor |
| Q03 | varchar |  |  | SI | Has the patient been oriented to the ward and rout... |
| Q04 | varchar |  |  | SI | Has the patient had a fall in the last 12 months? |
| Q05 | varchar |  |  | SI | Does the patient have an altered cognitive state? |
| Q06 | varchar |  |  | SI | Is it acute, fluctuating or chronic? |
| Q07 | varchar |  |  | SI | Is the patient affected by any of the following? |
| Q08 | varchar |  |  | SI | Score together |
| Q09 | varchar |  |  | SI | Is the patient aware of their own limitations when... |
| Q10 | varchar |  |  | SI | Does the patient, upon observation, appear unstead... |
| Q11 | bit |  |  | SI | Yes - severely unsteady (needs constant hands on a... |
| Q12 | varchar |  |  | SI | Is it when standing, transferring or walking? |
| Q13 | varchar |  |  | SI | Risk Factor |
| Q14 | varchar |  |  | SI | No Scoring required on this page |
| Q15 | varchar |  |  | SI | Is the patient affected acutely or chronically, by... |
| Q16 | varchar |  |  | SI | Does the patient have impaired vision, which limit... |
| Q17 | varchar |  |  | SI | Does the patient have impaired hearing, which limi... |
| Q18 | varchar |  |  | SI | Does the patient have problems with the sensation ... |
| Q19 | varchar |  |  | SI | Does the patient have foot problems? E.g. Corns, b... |
| Q20 | varchar |  |  | SI | Does the patient have communication difficulties? ... |
| Q21 | varchar |  |  | SI | Does the patient have intravenous therapy / idc / ... |
| Q22 | varchar |  |  | SI | Is the patient within 24 hours post surgery / anae... |
| Q23 | varchar |  |  | SI | How many medications does the patient have prescri... |
| Q24 | varchar |  |  | SI | Include all listed on drug chart, PRN Meds = 1 med... |
| Q25 | varchar |  |  | SI | Does the patient take any of the following type of... |
| Q26 | varchar |  |  | SI | Does the patient wear appropriate, accurate fittin... |
| Q26a | varchar |  |  | SI | Does the patient wear appropriate, accurate fittin... |
| Q27 | varchar |  |  | SI | Is the patient’s clothing too long or loose fittin... |
| Q28 | varchar |  |  | SI | Has the patient had a weight loss or decline in fo... |
| Q29 | varchar |  |  | SI | More than one response is possible, but max score ... |
| Q30 | varchar |  |  | SI | Does the patient, upon observation, appear unstead... |
| Q31 | date |  |  | SI | Date |
| Q32 | varchar |  |  | SI | 10 - 19:  Patient is at potential risk for falls |
| Q33 | varchar |  |  | SI | 0 - 9: Patient is NOT at potential risk for falls |
| Q34 | varchar |  |  | SI | The Falls Risk Assessment Tool (FRAT)  assesses th... |
| Q36 | varchar |  |  | SI | Score |
| Q37 | varchar |  |  | SI | Classification |
| Q38 | varchar |  |  | SI | 10 - 19 |
| Q39 | varchar |  |  | SI | Patient is at potential risk for falls |
| Q40 | varchar |  |  | SI | 0 - 9 |
| Q41 | varchar |  |  | SI | Patient is NOT at potential risk for falls |
| Q42 | varchar |  |  | SI | Is this a daycase patient? |
| Q43 | varchar |  |  | SI | Age 65 or over? |
| Q44 | varchar |  |  | SI | Age |
| Q45 | varchar |  |  | SI | Does the patient have a fear of falling? |
| Q46 | varchar |  |  | SI | Does the patient have problems with balance or fur... |
| Q47 | varchar |  |  | SI | Is the patient bed bound? |
| Q48 | varchar |  |  | SI | Does the patient have any cognitive Impairment e.g... |
| Q49 | varchar |  |  | SI | Has the patient tried to walk alone but unsteady /... |
| Q50 | varchar |  |  | SI | Are the patient or relative anxious about falls? |
| Q51 | varchar |  |  | SI | In your professional judgement, is the patient at ... |
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