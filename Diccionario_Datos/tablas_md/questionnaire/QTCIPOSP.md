# questionnaire.QTCIPOSP

> Integrated Palliative care Outcome Scale (IPOS Patient Version)

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Integrated Palliative care Outcome Scale (IPOS Patient Version)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Recall timeframe |
| Q04 | varchar |  |  | SI | Considering the last 3 days, please select appropr... |
| Q05 | varchar |  |  | SI | Considering the last week, please select appropria... |
| Q06 | varchar |  |  | SI | Q1. What have been your main problems or concerns? |
| Q07 | varchar |  |  | SI | Q2. Below is a list of symptoms, which you may or ... |
| Q08 | varchar |  |  | SI | Pain |
| Q09 | varchar |  |  | SI | Shortness of breath |
| Q10 | varchar |  |  | SI | Weakness or lack of energy |
| Q11 | varchar |  |  | SI | Nausea (feeling like you are going to be sick) |
| Q12 | varchar |  |  | SI | Vomiting (being sick) |
| Q13 | varchar |  |  | SI | Poor appetite |
| Q14 | varchar |  |  | SI | Constipation |
| Q15 | varchar |  |  | SI | Sore or dry mouth |
| Q16 | varchar |  |  | SI | Drowsiness |
| Q17 | varchar |  |  | SI | Poor mobility |
| Q18 | varchar |  |  | SI | Are there any other symptoms? |
| Q20 | varchar |  |  | SI | Q3. Have you been feeling anxious or worried about... |
| Q21 | varchar |  |  | SI | Q4. Have any of your family or friends been anxiou... |
| Q22 | varchar |  |  | SI | Q5. Have you been feeling depressed? |
| Q23 | varchar |  |  | SI | Q6. Have you felt at peace? |
| Q24 | varchar |  |  | SI | Q7. Have you been able to share how you are feelin... |
| Q25 | varchar |  |  | SI | Q8. Have you had as much information as you wanted... |
| Q26 | varchar |  |  | SI | Q10. How did you complete this questionnaire? |
| Q27 | varchar |  |  | SI | Q9. Have any practical problems resulting from you... |
| Q28 | varchar |  |  | SI | If you are worried about any of the issues raised ... |
| Q29 | varchar |  |  | SI | Guidelines |
| Q30 | varchar |  |  | SI | The POS measures are a family of tools to measure ... |
| Q31 | varchar |  |  | SI | The POS measures are specifically developed for us... |
| Q32 | varchar |  |  | SI | POS is designed to be responsive to change. It can... |
| Q34 | varchar |  |  | SI | https://pos-pal.org/maix/how-to-administer.php |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | Classification |
| Q37 | varchar |  |  | SI | • The Palliative Care Outcome Scale (POS) measures... |
| Q38 | varchar |  |  | SI | • The POS measures are specifically developed for ... |
| Q39 | varchar |  |  | SI | • POS is designed to be responsive to change. It c... |
| Q40 | varchar |  |  | SI | • Changes in scores over time are important to det... |
| Q41 | varchar |  |  | SI | • IPOS results can be used to calculate i) individ... |
| Q41a | varchar |  |  | SI | • Individual item scores are useful when tracking ... |
| Q42 | varchar |  |  | SI | • https://pos-pal.org/maix/how-to-score.php#:~:tex... |
| Q46 | varchar |  |  | SI | 0 - 68 |
| Q47 | varchar |  |  | SI | Higher scores are indicative of a higher level of ... |
| Q48 | varchar |  |  | SI | 0 - 68: Higher scores are indicative of a higher l... |
| Q50 | varchar |  |  | SI | • If additional symptoms are identified at the end... |
| Q51 | varchar |  |  | SI | • However, if an additional symptom score is used ... |
| Q52 | varchar |  |  | SI | • Note that Question 1, the additional symptoms fr... |
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