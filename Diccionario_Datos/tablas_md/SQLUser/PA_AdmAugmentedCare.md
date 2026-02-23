# SQLUser.PA_AdmAugmentedCare

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUG_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| AUG_ACPDisposal_DR | bigint |  | FK | SI | Des Ref ACPDisposal |
| AUG_ACPEndDate | date |  |  | SI | ACPEndDate |
| AUG_ACPSource_DR | bigint |  | FK | SI | Des Ref ACPSource |
| AUG_Childsub | double |  |  | NO | Childsub |
| AUG_Date | date |  |  | SI | Date |
| AUG_HDCDays | double |  |  | SI | HDCDays |
| AUG_ICLDays | double |  |  | SI | ICL Days |
| AUG_MaxNumberOfOrgans | varchar |  |  | SI | Max Number Of Organs |
| AUG_Planned_Unplanned | varchar |  |  | SI | Planned/Unplanned |
| AUG_RespiratoryIndicator | varchar |  |  | SI | Respiratory Indicator |
| AUG_RowId | varchar |  |  | NO | - |
| AUG_TimeFrom | time |  |  | SI | Time From |
| AUG_TimeTo | time |  |  | SI | Time To |
| AUG_UpdateDate | date |  |  | SI | UpdateDate |
| AUG_UpdateTime | time |  |  | SI | Update Time |
| AUG_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| AUG_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | 4. What is your phone number? *Ask address if no p... |
| Q11 | - |  |  | SI | Patient response |
| Q12 | - |  |  | SI | 5. How old are you? |
| Q13 | - |  |  | SI | Patient response |
| Q14 | - |  |  | SI | 6. When were you born? |
| Q15 | - |  |  | SI | Patient response |
| Q16 | - |  |  | SI | 7. Who is the current leader of this country? |
| Q17 | - |  |  | SI | Patient response |
| Q18 | - |  |  | SI | 8. Who was the leader before them? |
| Q19 | - |  |  | SI | Patient response |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | 9. What is your mother's maiden name? |
| Q21 | - |  |  | SI | Patient response |
| Q22 | - |  |  | SI | 10. Can you count backward from 20 by 3's? |
| Q23 | - |  |  | SI | Patient response |
| Q24 | - |  |  | SI | Guidelines |
| Q25 | - |  |  | SI | This questionnaire is optional for both consumer a... |
| Q26 | - |  |  | SI | In administering the SPMSQ, the Interviewer should... |
| Q27 | - |  |  | SI | Sometimes people have trouble remembering things. ... |
| Q28 | - |  |  | SI | Each of the ten questions should be asked as print... |
| Q29 | - |  |  | SI | Interviewer should write the person's answers on t... |
| Q3 | - |  |  | SI | Highest level of education |
| Q30 | - |  |  | SI | If the person refuses to answer, check the column ... |
| Q31 | - |  |  | SI | Allow the person sufficient time to answer, but mo... |
| Q32 | - |  |  | SI | To be correct, answers must be given without refer... |
| Q33 | - |  |  | SI | Refusal to answer counts as incorrect. |
| Q34 | - |  |  | SI | If the person gives an incorrect answer or waits a... |
| Q35 | - |  |  | SI | One more error is allowed in the scoring if a pati... |
| Q36 | - |  |  | SI | This variance has been built into the tool based o... |
| Q37 | - |  |  | SI | Question Scoring Guidance |
| Q39 | - |  |  | SI | Q2. Day of the week: The correct day, Monday, Tues... |
| Q4 | - |  |  | SI | 1. What is the date, month and year? |
| Q43 | - |  |  | SI | Short Portable Mental Status Questionnaire (SPMSQ)... |
| Q44 | - |  |  | SI | Q1. Date: The answer is correct if the person prov... |
| Q45 | - |  |  | SI | Q3. Name of this place: Any accurate description o... |
| Q46 | - |  |  | SI | Q8. Leader before them:  Only the last name of the... |
| Q47 | - |  |  | SI | Q9. Mother's maiden name: Score the person correct... |
| Q48 | - |  |  | SI | The name of the town or city, or (if institutional... |
| Q49 | - |  |  | SI | Interviewers should note the score interpretation ... |
| Q5 | - |  |  | SI | Patient response |
| Q50 | - |  |  | SI | Q4. Telephone Number: The person's telephone numbe... |
| Q51 | - |  |  | SI | However, poor performance on the SPMSQ is highly c... |
| Q52 | - |  |  | SI | The interviewer can verify the number via the phon... |
| Q53 | - |  |  | SI | later during the interview. If the person repeats ... |
| Q54 | - |  |  | SI | phone question. This alternative should only be us... |
| Q55 | - |  |  | SI | Q5. How old are you: Score correct or incorrect ac... |
| Q56 | - |  |  | SI | Q6. When were you born: Score correctly if the per... |
| Q57 | - |  |  | SI | Q7. Leader of this country: The correct last name ... |
| Q58 | - |  |  | SI | Q10. Subtraction: Read this question exactly as pr... |
| Q6 | - |  |  | SI | 2. What is the day of the week? |
| Q7 | - |  |  | SI | Patient response |
| Q8 | - |  |  | SI | 3. What is the name of this place? |
| Q9 | - |  |  | SI | Patient response |
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