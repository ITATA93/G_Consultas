# questionnaire.QTCPPA

> Perinatal Psychosocial Assessment

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perinatal Psychosocial Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Any previous depression, anxiety or other mental h... |
| Q04 | varchar |  |  | SI | Specify treatment for any depression, anxiety or o... |
| Q05 | varchar |  |  | SI | Mental health notes |
| Q06 | varchar |  |  | SI | Have any difficult events happened to you in the p... |
| Q07 | varchar |  |  | SI | Difficult events notes |
| Q08 | varchar |  |  | SI | Is there a problem with alcohol and/or drugs in yo... |
| Q09 | varchar |  |  | SI | Alcohol / Drugs notes |
| Q10 | varchar |  |  | SI | Is your partner or someone else in the household s... |
| Q11 | varchar |  |  | SI | Abusive behaviour notes |
| Q12 | varchar |  |  | SI | Have you experienced any kind of abuse in the past... |
| Q13 | varchar |  |  | SI | Abuse notes |
| Q14 | varchar |  |  | SI | Do all of your children still live with you |
| Q15 | varchar |  |  | SI | Children notes |
| Q16 | varchar |  |  | SI | Is your home environment stressful (e.g. too many ... |
| Q17 | varchar |  |  | SI | Home environment notes |
| Q18 | varchar |  |  | SI | Are your finances reasonable, can you live within ... |
| Q19 | varchar |  |  | SI | Financial notes |
| Q20 | varchar |  |  | SI | Have you experienced any trauma in the past - misc... |
| Q21 | varchar |  |  | SI | Trauma notes |
| Q22 | varchar |  |  | SI | Do you feel pleased about being pregnant |
| Q23 | varchar |  |  | SI | Pregnancy pleasure notes |
| Q24 | varchar |  |  | SI | Are you and your partner currently together |
| Q25 | varchar |  |  | SI | Partner notes |
| Q26 | varchar |  |  | SI | Is your partner supportive of you |
| Q27 | varchar |  |  | SI | Supportive partner notes |
| Q28 | varchar |  |  | SI | Does your family and friends care about how you fe... |
| Q29 | varchar |  |  | SI | Family / Friends notes |
| Q30 | varchar |  |  | SI | Do you know where to seek help if necessary regard... |
| Q31 | varchar |  |  | SI | Seek help notes |
| Q32 | varchar |  |  | SI | Miscellaneous notes |
| Q33 | varchar |  |  | SI | Actions (referrals to other services, review at ne... |
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