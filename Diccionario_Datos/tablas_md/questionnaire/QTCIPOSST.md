# questionnaire.QTCIPOSST

> Integrated Palliative care Outcome Scale (IPOS Staff Version)

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Integrated Palliative care Outcome Scale (IPOS Staff Version)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Recall timeframe |
| Q04 | varchar |  |  | SI | Recall timeframe |
| Q05 | varchar |  |  | SI | Please consider questions and answer them as they ... |
| Q06 | varchar |  |  | SI | Please consider questions and answer them as they ... |
| Q07 | varchar |  |  | SI | Q1. What have been the patient's main problems? |
| Q08 | varchar |  |  | SI | Q2. Please select one box that best describes how ... |
| Q09 | varchar |  |  | SI | They are validated instrument that can be used in ... |
| Q10 | varchar |  |  | SI | Individual item scores are useful when tracking pa... |
| Q21 | varchar |  |  | SI | Pain |
| Q22 | varchar |  |  | SI | Shortness of breath |
| Q23 | varchar |  |  | SI | Weakness or lack of energy |
| Q24 | varchar |  |  | SI | Nausea (Feeling like you are going to be sick) |
| Q25 | varchar |  |  | SI | Vomiting (Being sick) |
| Q26 | varchar |  |  | SI | Poor appetite |
| Q27 | varchar |  |  | SI | Guidelines |
| Q28 | varchar |  |  | SI | The Palliative Care Outcome Scale (POS) measures a... |
| Q29 | varchar |  |  | SI | The POS measures are specifically developed for us... |
| Q30 | varchar |  |  | SI | POS is designed to be responsive to change. It can... |
| Q31 | varchar |  |  | SI | Changes in scores over time are important to detec... |
| Q32 | varchar |  |  | SI | IPOS results can be used to calculate i) individua... |
| Q33 | varchar |  |  | SI | https://pos-pal.org/maix/how-to-administer.php |
| Q34 | varchar |  |  | SI | https://pos-pal.org/maix/how-to-score.php#:~:text=... |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | Constipation |
| Q37 | varchar |  |  | SI | Sore or dry mouth |
| Q38 | varchar |  |  | SI | Drowsiness |
| Q39 | varchar |  |  | SI | Poor mobility |
| Q40 | varchar |  |  | SI | Q3. Has she/he been feeling anxious or worried abo... |
| Q41 | varchar |  |  | SI | Q4. Have any of his/her family or friends been anx... |
| Q42 | varchar |  |  | SI | Q5. Do you think she/he felt depressed? |
| Q43 | varchar |  |  | SI | Q6. Do you think she/he has felt at peace? |
| Q44 | varchar |  |  | SI | Q7. Has the patient been able to share how she/he ... |
| Q45 | varchar |  |  | SI | Q8. Has the patient had as much information as she... |
| Q46 | varchar |  |  | SI | Q9. Have any practical problems resulting from his... |
| Q47 | varchar |  |  | SI | Score |
| Q48 | varchar |  |  | SI | Classification |
| Q49 | varchar |  |  | SI | The POS measures are a family of tools to measure ... |
| Q50 | varchar |  |  | SI | They are validated instrument that can be used in ... |
| Q51 | varchar |  |  | SI | The POS measures are specifically developed for us... |
| Q52 | varchar |  |  | SI | 0 - 68: Higher scores are indicative a higher leve... |
| Q53 | varchar |  |  | SI | 0 |
| Q54 | varchar |  |  | SI | 68 |
| Q55 | varchar |  |  | SI | Higher level of impact |
| Q56 | varchar |  |  | SI | Lower level of impact |
| Q57 | varchar |  |  | SI | 0 - 68 |
| Q58 | varchar |  |  | SI | Higher scores are indicative a higher level of imp... |
| Q59 | varchar |  |  | SI | (* Score upper limit if no other symptoms are reco... |
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