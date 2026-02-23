# SQLUser.OR_An_Oper_Scrub_Nurse

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPSCN_ParRef | varchar | PK |  | NO | OR_Anaest_Operation Parent Reference |
| OPSCN_Childsub | numeric |  |  | NO | Childsub |
| OPSCN_RowId | varchar |  |  | NO | - |
| OPSCN_Scrub_Nurse_DR | varchar |  | FK | NO | Scrub Nurse Des Ref to CTCP |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | In what way are they alike |
| Q04 | - |  |  | SI | Patient's response |
| Q05 | - |  |  | SI | A banana and an orange |
| Q06 | - |  |  | SI | Banana / Orange - patient's response |
| Q07 | - |  |  | SI | A table and a chair |
| Q08 | - |  |  | SI | Table / Chair - patient's response |
| Q09 | - |  |  | SI | A tulip, a rose and a daisy |
| Q10 | - |  |  | SI | Tulip / Rose / Daisy - patient's response |
| Q11 | - |  |  | SI | If the patient says, “they are not alike” (total f... |
| Q12 | - |  |  | SI | However, credit 0 points for the first item. Do no... |
| Q13 | - |  |  | SI | Only category responses [fruits, furniture, flower... |
| Q14 | - |  |  | SI | Similarities |
| Q15 | - |  |  | SI | “Say as many words as you can beginning with the l... |
| Q16 | - |  |  | SI | The time allowed is 60 seconds. |
| Q17 | - |  |  | SI | If the patient gives no response during the first ... |
| Q18 | - |  |  | SI | If the patient pauses 10 seconds, prompt them by s... |
| Q19 | - |  |  | SI | Word repetitions or variations [shoe, shoemaker], ... |
| Q20 | - |  |  | SI | Lexical fluency |
| Q21 | - |  |  | SI | Look carefully at what I'm doing. |
| Q22 | - |  |  | SI | The examiner, seated in front of the patient, perf... |
| Q23 | - |  |  | SI | Now, with your right hand do the same series, firs... |
| Q24 | - |  |  | SI | The examiner performs the series 3 times in total ... |
| Q25 | - |  |  | SI | Now, do it on your own. |
| Q26 | - |  |  | SI | Observe the patient's actions. |
| Q27 | - |  |  | SI | Motor series |
| Q28 | - |  |  | SI | “Tap twice when I tap once. |
| Q29 | - |  |  | SI | To ensure that the patient has understood the inst... |
| Q30 | - |  |  | SI | “Tap once when I tap twice.” |
| Q31 | - |  |  | SI | To ensure that the patient has understood the inst... |
| Q32 | - |  |  | SI | The examiner then performs the following series:  ... |
| Q33 | - |  |  | SI | Conflicting instructions |
| Q34 | - |  |  | SI | “Tap once when I tap once.” |
| Q35 | - |  |  | SI | To ensure that the patient has understood the inst... |
| Q36 | - |  |  | SI | “Do not tap when I tap twice.”	 |
| Q37 | - |  |  | SI | To ensure that the patient has understood the inst... |
| Q38 | - |  |  | SI | The examiner then performs the following series:  ... |
| Q39 | - |  |  | SI | Go-No Go |
| Q40 | - |  |  | SI | 1. The examiner is seated in front of the patient |
| Q41 | - |  |  | SI | 2. Place the patient's hands palm up on his/her kn... |
| Q42 | - |  |  | SI | 3. Without saying anything or looking at the patie... |
| Q43 | - |  |  | SI | 4. If the patient takes the hands, the examiner wi... |
| Q44 | - |  |  | SI | Prehension behaviour |
| Q45 | - |  |  | SI | Similarities sub-score |
| Q46 | - |  |  | SI | Lexical fluency sub-score |
| Q47 | - |  |  | SI | Motor series sub-score |
| Q48 | - |  |  | SI | Conflicting instructions sub-score |
| Q49 | - |  |  | SI | Go-No-Go sub-score |
| Q50 | - |  |  | SI | Prehension behaviour sub-score |
| Q51 | - |  |  | SI | Dubois B, Slachevsky A, Litvan I, Pillon B. The FA... |
| Q52 | - |  |  | SI | Slachevsky A, Villalpando JM, Sarazin M, et al. Fr... |
| Q53 | - |  |  | SI | A banana and an orange |
| Q54 | - |  |  | SI | A table and a chair |
| Q55 | - |  |  | SI | A tulip, a rose and a daisy |
| Q56 | - |  |  | SI | The Frontal Assessment Battery (FAB) generates sco... |
| Q57 | - |  |  | SI | The interpretation of the total FAB score is too d... |
| Q58 | - |  |  | SI | Patient's response |
| Q59 | - |  |  | SI | Patient's response |
| Q60 | - |  |  | SI | Patient's response |
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