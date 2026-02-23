# questionnaire.QTCYBOCS

> Yale-Brown Obsessive Compulsive Scale (Y-BOCS)

**Schema:** questionnaire
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Yale-Brown Obsessive Compulsive Scale (Y-BOCS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Note: Scores should reflect the composite effect o... |
| Q02 | varchar |  |  | SI | Answer each question based on the average occurren... |
| Q03 | varchar |  |  | SI | How much of your time is occupied by obsessive tho... |
| Q04 | varchar |  |  | SI | How much do your obsessive thoughts interfere with... |
| Q05 | varchar |  |  | SI | How much distress do your obsessive thoughts cause... |
| Q06 | varchar |  |  | SI | How much of an effort do you make to resist the ob... |
| Q07 | varchar |  |  | SI | How much control do you have over your obsessive t... |
| Q08 | varchar |  |  | SI | How much time do you spend performing compulsive b... |
| Q09 | varchar |  |  | SI | How much do your compulsive behaviors interfere wi... |
| Q10 | varchar |  |  | SI | How anxious would you become if you were prevented... |
| Q11 | varchar |  |  | SI | How much of an effort do you make to resist the co... |
| Q12 | varchar |  |  | SI | How much control do you have over the compulsions? |
| Q13 | varchar |  |  | SI | Yale-Brown Obsessive Compulsive Scale (Y-BOCS) is ... |
| Q14 | varchar |  |  | SI | 0 - 7: Little or No OCD symptoms |
| Q15 | varchar |  |  | SI | 8 - 15: Mild OCD symptoms |
| Q16 | varchar |  |  | SI | 16 - 23: Moderate OCD symptoms |
| Q17 | varchar |  |  | SI | 24 - 31: Severe OCD symptoms |
| Q18 | varchar |  |  | SI | 32 - 40: Extreme OCD symptoms |
| Q19 | varchar |  |  | SI | Obsessive Thoughts Subtotal  |
| Q20 | varchar |  |  | SI | Compulsive Behaviors Subtotal |
| Q21 | varchar |  |  | SI | Definitions and examples of “Obessions” and “Compu... |
| Q22 | varchar |  |  | SI | Obsessions are unwelcome or distressing ideas, tho... |
| Q23 | varchar |  |  | SI | They may seem to occur against your will. |
| Q24 | varchar |  |  | SI | They may be repugnant to you, are often senseless,... |
| Q25 | varchar |  |  | SI | (for example, the recurrent thought or impulse to ... |
| Q26 | varchar |  |  | SI | Compulsions are behaviors or acts that you feel dr... |
| Q27 | varchar |  |  | SI | At times, you may try to resist doing them, but th... |
| Q28 | varchar |  |  | SI | You may experience anxiety that does not diminish ... |
| Q29 | varchar |  |  | SI | Score |
| Q30 | varchar |  |  | SI | Classification |
| Q31 | varchar |  |  | SI | 0 - 7 |
| Q32 | varchar |  |  | SI | Little or No OCD symptoms |
| Q33 | varchar |  |  | SI | 8 - 15 |
| Q34 | varchar |  |  | SI | Mild OCD symptoms |
| Q35 | varchar |  |  | SI | 16 - 23 |
| Q36 | varchar |  |  | SI | Moderate OCD symptoms |
| Q37 | varchar |  |  | SI | 24 - 31 |
| Q38 | varchar |  |  | SI | Severe OCD symptoms |
| Q39 | varchar |  |  | SI | 32 - 40 |
| Q40 | varchar |  |  | SI | Extreme OCD symptoms |
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