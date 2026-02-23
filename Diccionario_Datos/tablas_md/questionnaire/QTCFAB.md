# questionnaire.QTCFAB

> Frontal Assessment Battery (FAB)

**Schema:** questionnaire
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Frontal Assessment Battery (FAB)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time  |
| Q03 | varchar |  |  | SI | In what way are they alike |
| Q04 | varchar |  |  | SI | Patient's response |
| Q05 | varchar |  |  | SI | A banana and an orange |
| Q06 | varchar |  |  | SI | Banana / Orange - patient's response |
| Q07 | varchar |  |  | SI | A table and a chair |
| Q08 | varchar |  |  | SI | Table / Chair - patient's response |
| Q09 | varchar |  |  | SI | A tulip, a rose and a daisy |
| Q10 | varchar |  |  | SI | Tulip / Rose / Daisy - patient's response |
| Q11 | varchar |  |  | SI | If the patient says, “they are not alike” (total f... |
| Q12 | varchar |  |  | SI | However, credit 0 points for the first item. Do no... |
| Q13 | varchar |  |  | SI | Only category responses [fruits, furniture, flower... |
| Q14 | varchar |  |  | SI | Similarities |
| Q15 | varchar |  |  | SI | “Say as many words as you can beginning with the l... |
| Q16 | varchar |  |  | SI | The time allowed is 60 seconds. |
| Q17 | varchar |  |  | SI | If the patient gives no response during the first ... |
| Q18 | varchar |  |  | SI | If the patient pauses 10 seconds, prompt them by s... |
| Q19 | varchar |  |  | SI | Word repetitions or variations [shoe, shoemaker], ... |
| Q20 | varchar |  |  | SI | Lexical fluency |
| Q21 | varchar |  |  | SI | Look carefully at what I'm doing. |
| Q22 | varchar |  |  | SI | The examiner, seated in front of the patient, perf... |
| Q23 | varchar |  |  | SI | Now, with your right hand do the same series, firs... |
| Q24 | varchar |  |  | SI | The examiner performs the series 3 times in total ... |
| Q25 | varchar |  |  | SI | Now, do it on your own. |
| Q26 | varchar |  |  | SI | Observe the patient's actions. |
| Q27 | varchar |  |  | SI | Motor series |
| Q28 | varchar |  |  | SI | “Tap twice when I tap once. |
| Q29 | varchar |  |  | SI | To ensure that the patient has understood the inst... |
| Q30 | varchar |  |  | SI | “Tap once when I tap twice.” |
| Q31 | varchar |  |  | SI | To ensure that the patient has understood the inst... |
| Q32 | varchar |  |  | SI | The examiner then performs the following series:  ... |
| Q33 | varchar |  |  | SI | Conflicting instructions |
| Q34 | varchar |  |  | SI | “Tap once when I tap once.” |
| Q35 | varchar |  |  | SI | To ensure that the patient has understood the inst... |
| Q36 | varchar |  |  | SI | “Do not tap when I tap twice.”	 |
| Q37 | varchar |  |  | SI | To ensure that the patient has understood the inst... |
| Q38 | varchar |  |  | SI | The examiner then performs the following series:  ... |
| Q39 | varchar |  |  | SI | Go-No Go |
| Q40 | varchar |  |  | SI | 1. The examiner is seated in front of the patient |
| Q41 | varchar |  |  | SI | 2. Place the patient's hands palm up on his/her kn... |
| Q42 | varchar |  |  | SI | 3. Without saying anything or looking at the patie... |
| Q43 | varchar |  |  | SI | 4. If the patient takes the hands, the examiner wi... |
| Q44 | varchar |  |  | SI | Prehension behaviour |
| Q45 | varchar |  |  | SI | Similarities sub-score |
| Q46 | varchar |  |  | SI | Lexical fluency sub-score |
| Q47 | varchar |  |  | SI | Motor series sub-score |
| Q48 | varchar |  |  | SI | Conflicting instructions sub-score |
| Q49 | varchar |  |  | SI | Go-No-Go sub-score |
| Q50 | varchar |  |  | SI | Prehension behaviour sub-score |
| Q51 | varchar |  |  | SI | Dubois B, Slachevsky A, Litvan I, Pillon B. The FA... |
| Q52 | varchar |  |  | SI | Slachevsky A, Villalpando JM, Sarazin M, et al. Fr... |
| Q53 | varchar |  |  | SI | A banana and an orange |
| Q54 | varchar |  |  | SI | A table and a chair |
| Q55 | varchar |  |  | SI | A tulip, a rose and a daisy |
| Q56 | varchar |  |  | SI | The Frontal Assessment Battery (FAB) generates sco... |
| Q57 | varchar |  |  | SI | The interpretation of the total FAB score is too d... |
| Q58 | varchar |  |  | SI | Patient's response |
| Q59 | varchar |  |  | SI | Patient's response |
| Q60 | varchar |  |  | SI | Patient's response |
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