# questionnaire.QTCSPMSQ

> Short Portable Mental State Questionnaire (SPMSQ)

**Schema:** questionnaire
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Short Portable Mental State Questionnaire (SPMSQ)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | 4. What is your phone number? *Ask address if no p... |
| Q11 | varchar |  |  | SI | Patient response |
| Q12 | varchar |  |  | SI | 5. How old are you? |
| Q13 | varchar |  |  | SI | Patient response |
| Q14 | varchar |  |  | SI | 6. When were you born? |
| Q15 | varchar |  |  | SI | Patient response |
| Q16 | varchar |  |  | SI | 7. Who is the current leader of this country? |
| Q17 | varchar |  |  | SI | Patient response |
| Q18 | varchar |  |  | SI | 8. Who was the leader before them? |
| Q19 | varchar |  |  | SI | Patient response |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | 9. What is your mother's maiden name? |
| Q21 | varchar |  |  | SI | Patient response |
| Q22 | varchar |  |  | SI | 10. Can you count backward from 20 by 3's? |
| Q23 | varchar |  |  | SI | Patient response |
| Q24 | varchar |  |  | SI | Guidelines |
| Q25 | varchar |  |  | SI | This questionnaire is optional for both consumer a... |
| Q26 | varchar |  |  | SI | In administering the SPMSQ, the Interviewer should... |
| Q27 | varchar |  |  | SI | Sometimes people have trouble remembering things. ... |
| Q28 | varchar |  |  | SI | Each of the ten questions should be asked as print... |
| Q29 | varchar |  |  | SI | Interviewer should write the person's answers on t... |
| Q3 | varchar |  |  | SI | Highest level of education |
| Q30 | varchar |  |  | SI | If the person refuses to answer, check the column ... |
| Q31 | varchar |  |  | SI | Allow the person sufficient time to answer, but mo... |
| Q32 | varchar |  |  | SI | To be correct, answers must be given without refer... |
| Q33 | varchar |  |  | SI | Refusal to answer counts as incorrect. |
| Q34 | varchar |  |  | SI | If the person gives an incorrect answer or waits a... |
| Q35 | varchar |  |  | SI | One more error is allowed in the scoring if a pati... |
| Q36 | varchar |  |  | SI | This variance has been built into the tool based o... |
| Q37 | varchar |  |  | SI | Question Scoring Guidance |
| Q39 | varchar |  |  | SI | Q2. Day of the week: The correct day, Monday, Tues... |
| Q4 | varchar |  |  | SI | 1. What is the date, month and year? |
| Q43 | varchar |  |  | SI | Short Portable Mental Status Questionnaire (SPMSQ)... |
| Q44 | varchar |  |  | SI | Q1. Date: The answer is correct if the person prov... |
| Q45 | varchar |  |  | SI | Q3. Name of this place: Any accurate description o... |
| Q46 | varchar |  |  | SI | Q8. Leader before them:  Only the last name of the... |
| Q47 | varchar |  |  | SI | Q9. Mother's maiden name: Score the person correct... |
| Q48 | varchar |  |  | SI | The name of the town or city, or (if institutional... |
| Q49 | varchar |  |  | SI | Interviewers should note the score interpretation ... |
| Q5 | varchar |  |  | SI | Patient response |
| Q50 | varchar |  |  | SI | Q4. Telephone Number: The person's telephone numbe... |
| Q51 | varchar |  |  | SI | However, poor performance on the SPMSQ is highly c... |
| Q52 | varchar |  |  | SI | The interviewer can verify the number via the phon... |
| Q53 | varchar |  |  | SI | later during the interview. If the person repeats ... |
| Q54 | varchar |  |  | SI | phone question. This alternative should only be us... |
| Q55 | varchar |  |  | SI | Q5. How old are you: Score correct or incorrect ac... |
| Q56 | varchar |  |  | SI | Q6. When were you born: Score correctly if the per... |
| Q57 | varchar |  |  | SI | Q7. Leader of this country: The correct last name ... |
| Q58 | varchar |  |  | SI | Q10. Subtraction: Read this question exactly as pr... |
| Q6 | varchar |  |  | SI | 2. What is the day of the week? |
| Q7 | varchar |  |  | SI | Patient response |
| Q8 | varchar |  |  | SI | 3. What is the name of this place? |
| Q9 | varchar |  |  | SI | Patient response |
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