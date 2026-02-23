# questionnaire.QTCSNOT22

> Sino-nasal Outcome Test SNOT-22

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Sino-nasal Outcome Test SNOT-22

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Need to blow nose   |
| Q02 | varchar |  |  | SI | Nasal blockage  	 |
| Q03 | varchar |  |  | SI | Sneezing	 |
| Q04 | varchar |  |  | SI | Runny nose	 |
| Q05 | varchar |  |  | SI | Cough	 |
| Q06 | varchar |  |  | SI | Post-nasal discharge	 |
| Q07 | varchar |  |  | SI | Thick nasal discharge	 |
| Q08 | varchar |  |  | SI | Ear fullness	 |
| Q09 | varchar |  |  | SI | Dizziness	 |
| Q10 | varchar |  |  | SI | Ear pain	 |
| Q11 | varchar |  |  | SI | Facial pain / pressure	 |
| Q12 | varchar |  |  | SI | Decreased sense of smell / taste	 |
| Q13 | varchar |  |  | SI | Difficulty falling asleep	 |
| Q14 | varchar |  |  | SI | Wake up at night	 |
| Q15 | varchar |  |  | SI | Lack of a good night’s sleep	 |
| Q16 | varchar |  |  | SI | Wake up tired |
| Q17 | varchar |  |  | SI | Fatigue |
| Q18 | varchar |  |  | SI | Reduced productivity	 |
| Q19 | varchar |  |  | SI | Reduced concentration	 |
| Q20 | varchar |  |  | SI | Frustrated / restless / irritable	 |
| Q21 | varchar |  |  | SI | Sad |
| Q22 | varchar |  |  | SI | Embarrassed	 |
| Q23 | varchar |  |  | SI | Mark the most important items affecting your healt... |
| Q24 | varchar |  |  | SI | 1. Considering how severe the problem is when you ... |
| Q25 | varchar |  |  | SI | 2. Please mark the most important items affecting ... |
| Q26 | varchar |  |  | SI | Score	 |
| Q27 | varchar |  |  | SI | Classification	 |
| Q28 | varchar |  |  | SI | <8	 |
| Q29 | varchar |  |  | SI | 8 - 20 |
| Q30 | varchar |  |  | SI | 21 - 50	 |
| Q31 | varchar |  |  | SI | >50 |
| Q32 | varchar |  |  | SI | The Sino-nasal Outcome Test (Snot-22) is a tool to... |
| Q33 | varchar |  |  | SI | The stratification of the SNOT-22 scores into Mild... |
| Q34 | varchar |  |  | SI | Normal  |
| Q35 | varchar |  |  | SI | Mild |
| Q36 | varchar |  |  | SI | Moderate  |
| Q37 | varchar |  |  | SI | Severe  |
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