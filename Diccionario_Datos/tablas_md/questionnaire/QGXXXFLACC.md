# questionnaire.QGXXXFLACC

> FLACC Behavioral Pain Assessment Scale

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* FLACC Behavioral Pain Assessment Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Face |
| Q02 | varchar |  |  | SI | Legs |
| Q03 | varchar |  |  | SI | Activity |
| Q04 | varchar |  |  | SI | Cry |
| Q05 | varchar |  |  | SI | Consolability |
| Q06 | varchar |  |  | SI | How to use the FLACC |
| Q07 | varchar |  |  | SI | Inpatient who are awake: |
| Q08 | varchar |  |  | SI | observe for 1 to 5 minutes or longer. Observe legs... |
| Q09 | varchar |  |  | SI | Inpatients wo are asleep: |
| Q10 | varchar |  |  | SI | observe for 5 minutes or longer. Observe body and ... |
| Q11 | varchar |  |  | SI | Face |
| Q12 | varchar |  |  | SI | Score 0 if the patient has a relaxed face, makes e... |
| Q13 | varchar |  |  | SI | Score 1 if the patient has a worried facial expres... |
| Q14 | varchar |  |  | SI | Score 2 if the patient has deep furrows in the for... |
| Q15 | varchar |  |  | SI | Legs |
| Q16 | varchar |  |  | SI | Score 0 if the muscle tone and motion in the limbs... |
| Q17 | varchar |  |  | SI | Score 1 if patient has increased tone, rigidity, o... |
| Q18 | varchar |  |  | SI | Score 2 if patient has hypertonicity, the legs are... |
| Q19 | varchar |  |  | SI | Activity |
| Q20 | varchar |  |  | SI | Score 0 if the patient moves easily and freely, no... |
| Q21 | varchar |  |  | SI | Score 1 if the patient shifts positions, appears h... |
| Q22 | varchar |  |  | SI | Score 2 if the patient is in a fixed position, roc... |
| Q23 | varchar |  |  | SI | Cry |
| Q24 | varchar |  |  | SI | Score 0 if the patient has no cry or moan, awake o... |
| Q25 | varchar |  |  | SI | Score 1 if the patient has occasional moans, cries... |
| Q26 | varchar |  |  | SI | Score 2 if the patient has frequent or continuous ... |
| Q27 | varchar |  |  | SI | Consolability |
| Q28 | varchar |  |  | SI | Score 0 if the patient is calm and does not requir... |
| Q29 | varchar |  |  | SI | Score 1 if the patient responds to comfort by touc... |
| Q30 | varchar |  |  | SI | Score 2 if the patient requires constant comfortin... |
| Q31 | varchar |  |  | SI | Whenever feasible, behavioral measurement of pain ... |
| Q32 | varchar |  |  | SI | 0: Relaxed and comfortable |
| Q33 | varchar |  |  | SI | 1–3: Mild discomfort |
| Q34 | varchar |  |  | SI | 4–6: Moderate pain |
| Q35 | varchar |  |  | SI | 7–10: Severe discomfort or pain or both |
| Q36 | varchar |  |  | SI | From Merkel, S. I., Voepel-Lewis, T., Shayevitz, J... |
| Q37 | varchar |  |  | SI |  require careful consideration of the context in w... |
| Q38 | varchar |  |  | SI | Instructions |
| Q39 | date |  |  | SI | Date |
| Q40 | time |  |  | SI | Time |
| Q41 | varchar |  |  | SI | Score |
| Q42 | varchar |  |  | SI | Classification |
| Q43 | varchar |  |  | SI | 0 |
| Q44 | varchar |  |  | SI | Relaxed and comfortable |
| Q45 | varchar |  |  | SI | 1 – 3 |
| Q46 | varchar |  |  | SI | Mild discomfort |
| Q47 | varchar |  |  | SI | 4 - 6 |
| Q48 | varchar |  |  | SI | Moderate pain |
| Q49 | varchar |  |  | SI | 7 - 10 |
| Q50 | varchar |  |  | SI | Severe discomfort or pain or both |
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