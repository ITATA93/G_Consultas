# SQLUser.PA_Adm2DischargeSummary

**Schema:** SQLUser
**Columnas:** 207
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIS_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| DIS_ActiveProblems | varchar |  |  | SI | ActiveProblems |
| DIS_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DIS_Childsub | double |  |  | NO | Childsub |
| DIS_Date | date |  |  | SI | Date |
| DIS_DischargeSummaryType_DR | bigint |  | FK | SI | Des Ref DischargeSummaryType |
| DIS_DocumType_DR | bigint |  | FK | SI | Des Ref DocumType |
| DIS_FileName | varchar |  |  | SI | File Name |
| DIS_PADischargeSummary_DR | bigint |  | FK | SI | Des Ref PADischargeSummary |
| DIS_PrincipalDiagnosis | varchar |  |  | SI | Principal Diagnosis |
| DIS_RowId | varchar |  |  | NO | - |
| DIS_Status | varchar |  |  | SI | Status |
| DIS_UpdateDate | date |  |  | SI | Update Date |
| DIS_UpdateTime | time |  |  | SI | Update Time |
| DIS_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Type of assessment |
| Q04 | - |  |  | SI | Care type |
| Q05 | - |  |  | SI | Say: I am going to ask you some questions and give... |
| Q06 | - |  |  | SI | 1. Allow ten seconds for each reply. Say: |
| Q07 | - |  |  | SI | a) What year is this? |
| Q08 | - |  |  | SI | a) What year is this? (accept exact answer only) |
| Q09 | - |  |  | SI | b) What season is this? |
| Q10 | - |  |  | SI | b) What season is this? (during the last week of t... |
| Q100 | - |  |  | SI | The serial sevens task is presented as an alternat... |
| Q101 | - |  |  | SI | The two tasks are not equivalent. |
| Q102 | - |  |  | SI | The serial sevens is an easier tasks, and the scor... |
| Q103 | - |  |  | SI | It can be used as an alternative to spelling world... |
| Q104 | - |  |  | SI | It is important to score the test as fairly as pos... |
| Q105 | - |  |  | SI | Scoring the overlapping pentagons (question 11) |
| Q106 | - |  |  | SI | Examples are provided to score this task. |
| Q107 | - |  |  | SI | Many older adults draw shaky, wiggly lines with un... |
| Q108 | - |  |  | SI | These are acceptable, as long as the person has tw... |
| Q109 | - |  |  | SI | Modify the test by asking the person to take the p... |
| Q11 | - |  |  | SI | c) What month is this? |
| Q110 | - |  |  | SI | If the test cannot be modified, then omit the task... |
| Q111 | - |  |  | SI | The score from this task is subtracted from the to... |
| Q112 | - |  |  | SI | The person’s score is then adjusted to this new to... |
| Q113 | - |  |  | SI | Here is the formula for calculating adjusted score... |
| Q114 | - |  |  | SI | Note: SMMSE scores are provided in whole numbers, ... |
| Q115 | - |  |  | SI | For 0.5 or greater, round up to the next higher wh... |
| Q116 | - |  |  | SI | For 0.49, or lower, round down to the next lower w... |
| Q117 | - |  |  | SI | The following are examples of disabilities that ma... |
| Q118 | - |  |  | SI | Physical disabilities: |
| Q119 | - |  |  | SI | The disability should be permanent. Sometimes peop... |
| Q12 | - |  |  | SI | c) What month is this? (on the first day of a new ... |
| Q120 | - |  |  | SI | In these cases, let the problem resolve before tes... |
| Q121 | - |  |  | SI | The Standardised Mini-Mental State Examination is ... |
| Q122 | - |  |  | SI | This tool is widely used by Clinicians from differ... |
| Q123 | - |  |  | SI | In these cases, let the problem resolve before tes... |
| Q124 | - |  |  | SI | Some physical problems may take months to resolve ... |
| Q125 | - |  |  | SI | Examples of physical disabilities include: amputat... |
| Q126 | - |  |  | SI | Language: |
| Q127 | - |  |  | SI | Sometimes language difficulties impair a person’s ... |
| Q128 | - |  |  | SI | If English is not the person’s first language, try... |
| Q129 | - |  |  | SI | It can be difficult to decide when to exempt a per... |
| Q13 | - |  |  | SI | d) What is today's date? |
| Q130 | - |  |  | SI | One approach is to try as many of the tasks as pos... |
| Q131 | - |  |  | SI | If the person seems to understand some questions e... |
| Q132 | - |  |  | SI | If the person has consistent problems understandin... |
| Q133 | - |  |  | SI | If in doubt, get a translator or give the test in ... |
| Q134 | - |  |  | SI | If in doubt, get a translator or give the test in ... |
| Q135 | - |  |  | SI | Speech: |
| Q136 | - |  |  | SI | Some people have severe speech problems, so their ... |
| Q137 | - |  |  | SI | They score lower because they cannot answer within... |
| Q138 | - |  |  | SI | Some may reverse words and may say ‘winter’ when t... |
| Q139 | - |  |  | SI | These deficits unfortunately bias the test against... |
| Q14 | - |  |  | SI | d) What is today's date? (accept previous or next ... |
| Q140 | - |  |  | SI | It is important to be consistent and adhere to the... |
| Q141 | - |  |  | SI | Note can be made of these factors and performance ... |
| Q142 | - |  |  | SI | Education: |
| Q143 | - |  |  | SI | Low education or education in a language other tha... |
| Q144 | - |  |  | SI | Generally, these limitations should not exempt a p... |
| Q145 | - |  |  | SI | Note should be made that these factors may cause l... |
| Q146 | - |  |  | SI | The person’s disability should be clearly noted on... |
| Q147 | - |  |  | SI | Items that are affected by this disability should ... |
| Q148 | - |  |  | SI | The calculation of the adjusted score is done at t... |
| Q149 | - |  |  | SI | Folstein MF, Folstein SE, McHugh PR. “Mini-mental ... |
| Q15 | - |  |  | SI | e) What day of the week is this? |
| Q150 | - |  |  | SI | Molloy DW, Alemayehu E, Roberts R. Reliability of ... |
| Q16 | - |  |  | SI | e) What day of the week is this? (accept exact ans... |
| Q17 | - |  |  | SI | 2. Allow 10 Seconds for each reply. Say: |
| Q18 | - |  |  | SI | a) What country are we in? |
| Q19 | - |  |  | SI | a) What country are we in? (accept exact answer on... |
| Q20 | - |  |  | SI | b)  What state are we in? |
| Q21 | - |  |  | SI | b)  What state are we in? (accept exact answer onl... |
| Q22 | - |  |  | SI | c) What city / town are we in? |
| Q23 | - |  |  | SI | c) What city/town are we in? (accept exact answer ... |
| Q24 | - |  |  | SI | d) <At home> What is the street address of this ho... |
| Q25 | - |  |  | SI | d) <At home> What is the street address of this ho... |
| Q26 | - |  |  | SI | e) <At home> What room are we in? |
| Q27 | - |  |  | SI | e) <At home> What room are we in? <In facility> Wh... |
| Q28 | - |  |  | SI | 3. Say: I am going to name three objects. When I a... |
| Q29 | - |  |  | SI | Remember what they are because I am going to ask y... |
| Q30 | - |  |  | SI | WORDS:  Ball   Car   Man |
| Q31 | - |  |  | SI | WORDS FOR REPEATED USE: Bell, jar, fan |
| Q32 | - |  |  | SI | Say: Please repeat the three items for me |
| Q33 | - |  |  | SI | Say: Please repeat the three items for me (score o... |
| Q34 | - |  |  | SI | Allow 20 seconds for reply |
| Q35 | - |  |  | SI | 4. Say: Spell the word WORLD (you may help the per... |
| Q36 | - |  |  | SI | Say: Now spell it backwards please |
| Q37 | - |  |  | SI | (allow 30 seconds |
| Q38 | - |  |  | SI | WORLD backwards score |
| Q39 | - |  |  | SI | WORLD - backwards attempt |
| Q39TxtOnly | - |  |  | SI | WORLD - backwards attempt Plain Text Only |
| Q40 | - |  |  | SI | 4. Say: Subtract seven from 100 and keep subtracti... |
| Q41 | - |  |  | SI | Write down person's reply |
| Q42 | - |  |  | SI | Once person starts - do not interrupt - allow him/... |
| Q43 | - |  |  | SI | If person stops before five subtractions have been... |
| Q44 | - |  |  | SI | 5. Say: Now what were the three objects I asked yo... |
| Q45 | - |  |  | SI | 5. Say: Now what were the three objects I asked yo... |
| Q46 | - |  |  | SI | 6. Show wristwatch. Ask: What is this called? |
| Q47 | - |  |  | SI | 6. Show wristwatch. Ask: What is this called? (sco... |
| Q48 | - |  |  | SI | 7. Show pencil. Ask: what is this called? |
| Q49 | - |  |  | SI | 7. Show pencil. Ask: what is this called? (score o... |
| Q50 | - |  |  | SI | 8. Say: I would like you to repeat a phrase after ... |
| Q51 | - |  |  | SI | 8. Say: I would like you to repeat a phrase after ... |
| Q52 | - |  |  | SI | 9. Say: Read the words on this page and then do wh... |
| Q53 | - |  |  | SI | Then, hand the person the sheet with CLOSE YOUR EY... |
| Q54 | - |  |  | SI | If the subject just reads and does not close eyes,... |
| Q55 | - |  |  | SI | Score one point only if the person closes their ey... |
| Q56 | - |  |  | SI | The person does not have to read aloud. |
| Q57 | - |  |  | SI | People who have physical, non-cognitive disabiliti... |
| Q58 | - |  |  | SI | 10. Hand the person a pencil and paper |
| Q59 | - |  |  | SI | Say: Write any complete sentence on that piece of ... |
| Q60 | - |  |  | SI | Say: Write any complete sentence on that piece of ... |
| Q61 | - |  |  | SI | 11. Place design, pencil, eraser and paper in fron... |
| Q62 | - |  |  | SI | Say: Copy this design please |
| Q63 | - |  |  | SI | Allow multiple tries. |
| Q64 | - |  |  | SI | Wait until the person is finished and hands it bac... |
| Q65 | - |  |  | SI | Score one point for a correctly copied diagram. |
| Q66 | - |  |  | SI | The person must have drawn a four-sided figure bet... |
| Q67 | - |  |  | SI | Maximum time: one minute. |
| Q68 | - |  |  | SI | For example, an arm amputee obviously cannot “fold... |
| Q69 | - |  |  | SI | Design attempt |
| Q69TxtOnly | - |  |  | SI | Design attempt Plain Text Only |
| Q70 | - |  |  | SI | Design time taken (min) |
| Q71 | - |  |  | SI | 12. Ask the person if he is right or left handed. |
| Q72 | - |  |  | SI | Take a piece of paper, hold it up in front of the ... |
| Q73 | - |  |  | SI | Take this paper in your right/left hand (whichever... |
| Q74 | - |  |  | SI | Folding paper exercise |
| Q75 | - |  |  | SI | Adjusted score |
| Q76 | - |  |  | SI | Directions for administration of SMMSE |
| Q77 | - |  |  | SI | Before the questionnaire is administered, try to g... |
| Q78 | - |  |  | SI | Assess the person’s ability to hear and understand... |
| Q79 | - |  |  | SI | Introduce yourself and try to get the person’s con... |
| Q80 | - |  |  | SI | This helps to avoid catastrophic reactions. |
| Q81 | - |  |  | SI | Ask each question a maximum of three times. If the... |
| Q82 | - |  |  | SI | If the person answers incorrectly, score zero. Acc... |
| Q83 | - |  |  | SI | The following equipment is required to administer ... |
| Q84 | - |  |  | SI | A watch, a pencil, reverse of the SMMSE score shee... |
| Q85 | - |  |  | SI | If the person answers what did you say?, do not ex... |
| Q86 | - |  |  | SI | If the person interrupts (e.g. queries what is thi... |
| Q87 | - |  |  | SI | Scoring WORLD backwards (question 4) |
| Q88 | - |  |  | SI | This task accounts for 17% of the total score. It ... |
| Q89 | - |  |  | SI | There are many different ways and systems for scor... |
| Q90 | - |  |  | SI | Originally, Dr. Folstein advised that the score is... |
| Q91 | - |  |  | SI | The authors suggest the following method. Score OR... |
| Q92 | - |  |  | SI | Simply write down the correct response: D L R O W. |
| Q93 | - |  |  | SI | Now place the last five letters the person said be... |
| Q94 | - |  |  | SI | Now draw lines between the same letters on the res... |
| Q95 | - |  |  | SI | These lines MAY NOT CROSS. |
| Q96 | - |  |  | SI | The person’s score is the maximum number of lines ... |
| Q97 | - |  |  | SI | In SMMSE there are many different ways to score th... |
| Q98 | - |  |  | SI | Adjusting score |
| Q99 | - |  |  | SI | Scoring of serial sevens (alternative to question ... |
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