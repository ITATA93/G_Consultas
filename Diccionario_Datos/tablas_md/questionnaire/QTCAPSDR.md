# questionnaire.QTCAPSDR

> Acute Pain Service Daily Review

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Acute Pain Service Daily Review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q04 | varchar |  |  | SI | Review pain at rest / movement scores in vital sig... |
| Q05 | varchar |  |  | SI | How has your pain been since last review |
| Q06 | varchar |  |  | SI | Location of pain |
| Q07 | varchar |  |  | SI | Pain categorisation |
| Q08 | varchar |  |  | SI | How did you sleep last night |
| Q09 | varchar |  |  | SI | Sleep details |
| Q10 | varchar |  |  | SI | Functional Activity |
| Q11 | varchar |  |  | SI | Activity (Coughing) |
| Q12 | varchar |  |  | SI | Activity (Deep breathing) |
| Q13 | varchar |  |  | SI | Triflow result |
| Q14 | varchar |  |  | SI | Activity (Sitting out of bed) |
| Q15 | varchar |  |  | SI | Activity (Mobilising) |
| Q16 | varchar |  |  | SI | Sedation State |
| Q17 | varchar |  |  | SI | Has the patient had a sedation score of ≥ 2 since ... |
| Q18 | varchar |  |  | SI | Sedation state since the last review, has the pati... |
| Q19 | varchar |  |  | SI | Reports of hallucinations |
| Q20 | varchar |  |  | SI | Vivid dreams |
| Q21 | varchar |  |  | SI | Other Neurological Symptoms |
| Q22 | varchar |  |  | SI | Do you have any itching |
| Q23 | varchar |  |  | SI | Itching (puritis) severity |
| Q24 | varchar |  |  | SI | Is the itching resolved with medications |
| Q25 | varchar |  |  | SI | Neurological notes |
| Q26 | varchar |  |  | SI | Since the last review, has the patient's respirato... |
| Q27 | varchar |  |  | SI | Since the last review, has the patient developed a... |
| Q28 | varchar |  |  | SI | Has the patient had opioid induced ventilatory imp... |
| Q29 | varchar |  |  | SI | Ventilatory impairment:&nbsp;Since the last review... |
| Q30 | varchar |  |  | SI | Respiratory notes |
| Q31 | varchar |  |  | SI | Since the last review, has the patient had a mean ... |
| Q32 | varchar |  |  | SI | Since the last review has the patient been given a... |
| Q33 | varchar |  |  | SI | Has analgesia significantly contributed to hypoten... |
| Q34 | varchar |  |  | SI | Cardiovascular notes |
| Q35 | varchar |  |  | SI | Oral intake status |
| Q36 | varchar |  |  | SI | Intake method |
| Q37 | varchar |  |  | SI | Do you have any nausea or vomiting |
| Q38 | varchar |  |  | SI | Has your nausea and/or vomiting prevented oral int... |
| Q39 | varchar |  |  | SI | Has your nausea and/or vomiting resolved with medi... |
| Q40 | varchar |  |  | SI | Is the patient taking aperients |
| Q41 | varchar |  |  | SI | Bowels (since last review) |
| Q42 | numeric |  |  | SI | Days since last bowel movement |
| Q43 | varchar |  |  | SI | Gastrointestinal notes |
| Q44 | varchar |  |  | SI | Type of analgesia |
| Q45 | varchar |  |  | SI | Site appears |
| Q46 | varchar |  |  | SI | Site check notes |
| Q47 | varchar |  |  | SI | Acute pain service plan |
| Q48 | varchar |  |  | SI | Dummy1 |
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