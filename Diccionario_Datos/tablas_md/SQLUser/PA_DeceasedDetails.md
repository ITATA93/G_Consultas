# SQLUser.PA_DeceasedDetails

**Schema:** SQLUser
**Columnas:** 166
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PA_DeceasedPatient Parent Reference |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_RowId | varchar |  |  | NO | - |
| DET_Status | varchar |  |  | SI | Status |
| DET_Table | varchar |  |  | SI | Table |
| DET_TableRowId | varchar |  |  | SI | Table RowId |
| Q01 | - |  |  | SI | Date of injury |
| Q02 | - |  |  | SI | Date of administration |
| Q03 | - |  |  | SI | Time of administration |
| Q04 | - |  |  | SI | Answer |
| Q05 | - |  |  | SI | Score |
| Q06 | - |  |  | SI | 1. How old are you? |
| Q07 | - |  |  | SI | Q1 Answer |
| Q08 | - |  |  | SI | 2. What is your date of birth? |
| Q09 | - |  |  | SI | Q2 Answer |
| Q10 | - |  |  | SI | 3. What month are we in? |
| Q100 | - |  |  | SI | Duration of PTA |
| Q101 | - |  |  | SI | Severity of Injury |
| Q102 | - |  |  | SI | Less than 5 minutes	 |
| Q103 | - |  |  | SI | Very Mild |
| Q104 | - |  |  | SI | 5 - 60 minutes |
| Q105 | - |  |  | SI | Mild |
| Q106 | - |  |  | SI | 1 - 24 hours |
| Q107 | - |  |  | SI | Moderate |
| Q108 | - |  |  | SI | 1 - 7 days |
| Q109 | - |  |  | SI | Severe |
| Q11 | - |  |  | SI | Q3 Answer |
| Q110 | - |  |  | SI | 1 - 4 weeks |
| Q111 | - |  |  | SI | Very Severe |
| Q112 | - |  |  | SI | Greater than 4 weeks |
| Q113 | - |  |  | SI | Extremely Severe |
| Q114 | - |  |  | SI | The Abbreviated Westmead PTA Scale is a standardis... |
| Q115 | - |  |  | SI | P.T.A. may be deemed to be over on the first of 3 ... |
| Q116 | - |  |  | SI | P.T.A. may be deemed to be over on first day of a ... |
| Q117 | - |  |  | SI | Score details in the legend and guidelines |
| Q118 | - |  |  | SI | Please note, on the first administration, the pati... |
| Q119 | - |  |  | SI | The patient is then given the opportunity to learn... |
| Q12 | - |  |  | SI | 4. What time of day is it? (morning, afternoon or ... |
| Q120 | - |  |  | SI | For each subsequent day, the patient is asked the ... |
| Q13 | - |  |  | SI | Q4 Answer |
| Q14 | - |  |  | SI | 5. What day of the week is it? |
| Q15 | - |  |  | SI | Q5 Answer |
| Q16 | - |  |  | SI | 6. What year are we in? |
| Q17 | - |  |  | SI | Q6 Answer |
| Q18 | - |  |  | SI | 7. What is the name of this place?	 |
| Q19 | - |  |  | SI | Q7 Answer |
| Q20 | - |  |  | SI | 8. Have you seen my face before? |
| Q21 | - |  |  | SI | If examiner is likely to change frequently, instea... |
| Q22 | - |  |  | SI | Q8 Answer |
| Q23 | - |  |  | SI | 9. What is my name?  On first admin, identify pers... |
| Q24 | - |  |  | SI | If examiner is likely to change frequently, instea... |
| Q25 | - |  |  | SI | Q9 Answer |
| Q26 | - |  |  | SI | For questions 10 - 12, on first admin show 3 pictu... |
| Q27 | - |  |  | SI | 10. What are the three pictures you were shown yes... |
| Q28 | - |  |  | SI | Picture 1 |
| Q29 | - |  |  | SI | Picture 1 Answer |
| Q30 | - |  |  | SI | Picture 2 |
| Q31 | - |  |  | SI | Picture 2 Answer |
| Q32 | - |  |  | SI | Picture 3 |
| Q33 | - |  |  | SI | Picture 3 Answer |
| Q34 | - |  |  | SI | Picture 1 for next test |
| Q35 | - |  |  | SI | Picture 2 for next test |
| Q36 | - |  |  | SI | Picture 3 for next test |
| Q37 | - |  |  | SI | TESTING CONDITIONS |
| Q38 | - |  |  | SI | Testing should ideally take place at the bedside i... |
| Q39 | - |  |  | SI | There should also be no obvious cues or aids like ... |
| Q40 | - |  |  | SI | TESTING START / STOP |
| Q41 | - |  |  | SI | PTA testing begins when the patient has regained c... |
| Q42 | - |  |  | SI | The ideal time to test a patient is when they are ... |
| Q43 | - |  |  | SI | extremely severe patients this may not be the case... |
| Q44 | - |  |  | SI | PTA testing stops when the patient has reached the... |
| Q45 | - |  |  | SI | (i.e. achieving a perfect score of 12 on the Westm... |
| Q46 | - |  |  | SI | TESTING EXECUTION GUIDELINES |
| Q47 | - |  |  | SI | To carry out the test, ask the questions in the or... |
| Q48 | - |  |  | SI | When the patient does not spontaneously answer a q... |
| Q49 | - |  |  | SI | These options must be in sequential order and the ... |
| Q50 | - |  |  | SI | NB: Do not give the choice of 3 options if the pat... |
| Q51 | - |  |  | SI | Question 1: HOW OLD ARE YOU ? |
| Q52 | - |  |  | SI | The examiner must ask for clarification if the pat... |
| Q53 | - |  |  | SI | Question 2: WHAT IS YOUR DATE OF BIRTH ? |
| Q54 | - |  |  | SI | If the patient has difficulty with the concept of ... |
| Q55 | - |  |  | SI | Question 3: WHAT MONTH ARE WE IN ? |
| Q56 | - |  |  | SI | For emphasis the examiner can ask what month are w... |
| Q57 | - |  |  | SI | What is the 6th month called ?'. |
| Q58 | - |  |  | SI | Question 4: WHAT TIME OF DAY IS IT ? (MORNING, AFT... |
| Q59 | - |  |  | SI | The patient should answer with one of the 3 choice... |
| Q60 | - |  |  | SI | Question 5: WHAT DAY OF THE WEEK IS IT ? |
| Q61 | - |  |  | SI | The examiner may add for the sake of emphasis 'Wha... |
| Q62 | - |  |  | SI | Question 6: WHAT YEAR ARE WE IN ? |
| Q63 | - |  |  | SI | It is considered correct for patients to answer in... |
| Q64 | - |  |  | SI | Question 7: WHAT IS THE NAME OF THIS PLACE ? |
| Q65 | - |  |  | SI | The patient has to be able to give the name of the... |
| Q66 | - |  |  | SI | give them a choice of 3 options. To do this pick 2... |
| Q67 | - |  |  | SI | If the patient does not spontaneously answer the q... |
| Q68 | - |  |  | SI | If the patient correctly answers this first part, ... |
| Q69 | - |  |  | SI | If the patient can not spontaneously answer give t... |
| Q70 | - |  |  | SI | (NB: The patient must answer both parts of this qu... |
| Q71 | - |  |  | SI | The remaining questions are asked on the second da... |
| Q72 | - |  |  | SI | Question 8: HAVE YOU SEEN MY FACE BEFORE ? |
| Q73 | - |  |  | SI | All this question requires is a simple yes / no an... |
| Q74 | - |  |  | SI | Question 9: WHAT IS MY NAME ? |
| Q75 | - |  |  | SI | If the patient fails to respond spontaneously a ch... |
| Q76 | - |  |  | SI | Question 10: WHAT WERE THE 3 PICTURES THAT I SHOWE... |
| Q77 | - |  |  | SI | If the patient can not spontaneously recall the pi... |
| Q78 | - |  |  | SI | In both cases the patient must pick the 3 target c... |
| Q79 | - |  |  | SI | the remaining target cards. Score 1 point for each... |
| Q80 | - |  |  | SI | (NB: The position in which the cards are placed or... |
| Q81 | - |  |  | SI | SCORING & PICTURE CARDS |
| Q82 | - |  |  | SI | Write down the patient's answer along with indicat... |
| Q83 | - |  |  | SI | (Perhaps a pattern may emerge if a patient continu... |
| Q84 | - |  |  | SI | (NB: It has no bearing on how you score the questi... |
| Q85 | - |  |  | SI | PICTURE CARDS |
| Q86 | - |  |  | SI | The other important rule you have to know is that ... |
| Q87 | - |  |  | SI | (blank side up) and let the patient pick the 3 car... |
| Q88 | - |  |  | SI | (A set of cards is regarded as different from the ... |
| Q89 | - |  |  | SI | REHEARSING WITH THE PATIENT |
| Q90 | - |  |  | SI | At the end of testing you need to rehearse with th... |
| Q91 | - |  |  | SI |  it properly. Step 1 is to go through the incorrec... |
| Q92 | - |  |  | SI | tomorrow. (This is also the time to introduce the ... |
| Q93 | - |  |  | SI | Then say, 'John I will be coming to see you tomorr... |
| Q94 | - |  |  | SI | the memory items properly. To do this you need to ... |
| Q95 | - |  |  | SI | or 'What did you have for breakfast, lunch or dinn... |
| Q96 | - |  |  | SI | Then prior to leaving, show the patient the 3 pict... |
| Q97 | - |  |  | SI | Score and Classification |
| Q98 | - |  |  | SI | First administration (Within 24 hours of admission... |
| Q99 | - |  |  | SI | Subsequent series of administration (Within 24 hou... |
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