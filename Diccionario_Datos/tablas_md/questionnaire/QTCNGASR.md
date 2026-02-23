# questionnaire.QTCNGASR

> Nurses' Global Assessment of Suicide Risk (NGASR)

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nurses' Global Assessment of Suicide Risk (NGASR)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date and time of assessment |
| Q02 | varchar |  |  | SI | Predictor variable |
| Q03 | varchar |  |  | SI | Level of engagement 4 (score of 5 or less = low le... |
| Q04 | varchar |  |  | SI | Interventions involve engaging the person daily in... |
| Q05 | varchar |  |  | SI | A one-to-one session focused on addressing the spe... |
| Q06 | varchar |  |  | SI | crisis. |
| Q07 | varchar |  |  | SI | A family meeting involving appropriate family memb... |
| Q08 | varchar |  |  | SI | needs to be done (or to happen) to reduce or resol... |
| Q09 | varchar |  |  | SI | A group session, involving other people in care. T... |
| Q10 | varchar |  |  | SI | an information focus, providing details about medi... |
| Q11 | varchar |  |  | SI | Level of engagement 3 (score between 6 and 8 = int... |
| Q12 | varchar |  |  | SI | Interventions involve providing intermittent level... |
| Q13 | varchar |  |  | SI | The nurse will talk with the person and discuss wh... |
| Q14 | varchar |  |  | SI | The nurse should advise the person that someone wi... |
| Q15 | varchar |  |  | SI | The nurse personally should make direct contact wi... |
| Q16 | varchar |  |  | SI | The person should be asked if they have any commen... |
| Q17 | varchar |  |  | SI | Level of engagement 2 (score between 9 and 11 = hi... |
| Q18 | varchar |  |  | SI | Interventions involve providing regular level of s... |
| Q19 | varchar |  |  | SI | A healthcare team member will make contact with th... |
| Q20 | varchar |  |  | SI | assess their situation. |
| Q21 | varchar |  |  | SI | The nurse will assess for distress and will ask th... |
| Q22 | varchar |  |  | SI | The nurse should advise the person why the healthc... |
| Q23 | varchar |  |  | SI | Level of engagement 1 (score 12 or more = very hig... |
| Q24 | varchar |  |  | SI | Interventions involve providing fullest level of s... |
| Q25 | varchar |  |  | SI | The person will require continuous access to a nur... |
| Q26 | varchar |  |  | SI | The nurse should advise the person of the nursing ... |
| Q27 | varchar |  |  | SI | The nurse should discuss the plan of care for the ... |
| Q28 | varchar |  |  | SI | Attempts should be made to explain to the person w... |
| Q29 | varchar |  |  | SI | person's needs. |
| Q30 | varchar |  |  | SI | Score |
| Q31 | varchar |  |  | SI | Classification |
| Q32 | varchar |  |  | SI | <= 5 |
| Q33 | varchar |  |  | SI | Low level of risk estimated |
| Q34 | varchar |  |  | SI | 6 - 8 |
| Q35 | varchar |  |  | SI | Intermediate level of risk |
| Q36 | varchar |  |  | SI | 9 - 11 |
| Q37 | varchar |  |  | SI | High level of risk |
| Q38 | varchar |  |  | SI | >=12 |
| Q39 | varchar |  |  | SI | Very high level of risk |
| Q40 | varchar |  |  | SI | <= 5: Low level of risk estimated |
| Q41 | varchar |  |  | SI | 6 - 8: Intermediate level of risk |
| Q42 | varchar |  |  | SI | 9 - 11: High level of risk |
| Q43 | varchar |  |  | SI | >=12: Very high level of risk |
| Q44 | varchar |  |  | SI | Nurses' Global Assessment of Suicide Risk (NGASR) |
| Q45 | varchar |  |  | SI | The Nurses' Global Assessment of Suicide Risk (NGA... |
| Q46 | varchar |  |  | SI | more confident in accurately assessing a patient's... |
| Q47 | time |  |  | SI | Time |
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