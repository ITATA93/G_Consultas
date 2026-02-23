# SQLUser.PAC_ClinicalIndicator

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CI_RowId | bigint | PK |  | NO | - |
| CI_CTLocs | varchar |  |  | SI | Locations |
| CI_Code | varchar |  |  | NO | Code |
| CI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CI_CreatedDate | date |  |  | SI | Created Date |
| CI_CreatedTime | time |  |  | SI | Created Time |
| CI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CI_DateFrom | date |  |  | SI | Date From |
| CI_DateTo | date |  |  | SI | Date To |
| CI_Desc | varchar |  |  | NO | Description |
| CI_Owner | varchar |  |  | SI | Owner |
| CI_UpdatedDate | date |  |  | SI | Updated Date |
| CI_UpdatedTime | time |  |  | SI | Updated Time |
| CI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ19DR | - |  |  | SI | Child Reference: Other symptoms |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Recall timeframe |
| Q04 | - |  |  | SI | Recall timeframe |
| Q05 | - |  |  | SI | Please consider questions and answer them as they ... |
| Q06 | - |  |  | SI | Please consider questions and answer them as they ... |
| Q07 | - |  |  | SI | Q1. What have been the patient's main problems? |
| Q08 | - |  |  | SI | Q2. Please select one box that best describes how ... |
| Q09 | - |  |  | SI | They are validated instrument that can be used in ... |
| Q10 | - |  |  | SI | Individual item scores are useful when tracking pa... |
| Q21 | - |  |  | SI | Pain |
| Q22 | - |  |  | SI | Shortness of breath |
| Q23 | - |  |  | SI | Weakness or lack of energy |
| Q24 | - |  |  | SI | Nausea (Feeling like you are going to be sick) |
| Q25 | - |  |  | SI | Vomiting (Being sick) |
| Q26 | - |  |  | SI | Poor appetite |
| Q27 | - |  |  | SI | Guidelines |
| Q28 | - |  |  | SI | The Palliative Care Outcome Scale (POS) measures a... |
| Q29 | - |  |  | SI | The POS measures are specifically developed for us... |
| Q30 | - |  |  | SI | POS is designed to be responsive to change. It can... |
| Q31 | - |  |  | SI | Changes in scores over time are important to detec... |
| Q32 | - |  |  | SI | IPOS results can be used to calculate i) individua... |
| Q33 | - |  |  | SI | https://pos-pal.org/maix/how-to-administer.php |
| Q34 | - |  |  | SI | https://pos-pal.org/maix/how-to-score.php#:~:text=... |
| Q35 | - |  |  | SI | Score |
| Q36 | - |  |  | SI | Constipation |
| Q37 | - |  |  | SI | Sore or dry mouth |
| Q38 | - |  |  | SI | Drowsiness |
| Q39 | - |  |  | SI | Poor mobility |
| Q40 | - |  |  | SI | Q3. Has she/he been feeling anxious or worried abo... |
| Q41 | - |  |  | SI | Q4. Have any of his/her family or friends been anx... |
| Q42 | - |  |  | SI | Q5. Do you think she/he felt depressed? |
| Q43 | - |  |  | SI | Q6. Do you think she/he has felt at peace? |
| Q44 | - |  |  | SI | Q7. Has the patient been able to share how she/he ... |
| Q45 | - |  |  | SI | Q8. Has the patient had as much information as she... |
| Q46 | - |  |  | SI | Q9. Have any practical problems resulting from his... |
| Q47 | - |  |  | SI | Score |
| Q48 | - |  |  | SI | Classification |
| Q49 | - |  |  | SI | The POS measures are a family of tools to measure ... |
| Q50 | - |  |  | SI | They are validated instrument that can be used in ... |
| Q51 | - |  |  | SI | The POS measures are specifically developed for us... |
| Q52 | - |  |  | SI | 0 - 68: Higher scores are indicative a higher leve... |
| Q53 | - |  |  | SI | 0 |
| Q54 | - |  |  | SI | 68 |
| Q55 | - |  |  | SI | Higher level of impact |
| Q56 | - |  |  | SI | Lower level of impact |
| Q57 | - |  |  | SI | 0 - 68 |
| Q58 | - |  |  | SI | Higher scores are indicative a higher level of imp... |
| Q59 | - |  |  | SI | (* Score upper limit if no other symptoms are reco... |
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