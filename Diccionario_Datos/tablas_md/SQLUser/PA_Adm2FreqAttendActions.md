# SQLUser.PA_Adm2FreqAttendActions

**Schema:** SQLUser
**Columnas:** 197
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FRA_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| FRA_Childsub | double |  |  | NO | Childsub |
| FRA_FreqAttendAction_DR | bigint |  | FK | SI | Des Ref FreqAttendAction |
| FRA_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Electroconvulsive therapy session |
| Q04 | - |  |  | SI | Care type |
| Q05 | - |  |  | SI | Say: I am going to ask you some questions and give... |
| Q06 | - |  |  | SI | 1.&nbsp |
| Q07 | - |  |  | SI | a) What year is this? |
| Q08 | - |  |  | SI | a) What year is this?&nbsp |
| Q09 | - |  |  | SI | b) What season is this? |
| Q10 | - |  |  | SI | b) What season is this? (during the last week of t... |
| Q100 | - |  |  | SI | It can be used as an alternate to spelling world b... |
| Q101 | - |  |  | SI | Scoring the overlapping pentagons (question 11) |
| Q102 | - |  |  | SI | Examples are provided to score this task. |
| Q103 | - |  |  | SI | Many older adults draw shaky, wiggly lines with un... |
| Q104 | - |  |  | SI | These are acceptable, as long as the person has tw... |
| Q105 | - |  |  | SI | Adjusting score |
| Q106 | - |  |  | SI | It is important to score the test as fairly as pos... |
| Q107 | - |  |  | SI | People who have physical, non-cognitive disabiliti... |
| Q108 | - |  |  | SI | For example, an arm amputee obviously cannot “fold... |
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
| Q121 | - |  |  | SI | Some physical problems may take months to resolve ... |
| Q122 | - |  |  | SI | Examples of physical disabilities include: amputat... |
| Q123 | - |  |  | SI | Language: |
| Q124 | - |  |  | SI | Sometimes language difficulties impair a person’s ... |
| Q125 | - |  |  | SI | If English is not the person’s first language, try... |
| Q126 | - |  |  | SI | It can be difficult to decide when to exempt a per... |
| Q127 | - |  |  | SI | One approach is to try as many of the tasks as pos... |
| Q128 | - |  |  | SI | If the person seems to understand some questions e... |
| Q129 | - |  |  | SI | If the person has consistent problems&nbsp |
| Q13 | - |  |  | SI | d) What is today's date? |
| Q130 | - |  |  | SI | If in doubt, get a translator or give the test in ... |
| Q131 | - |  |  | SI | If in doubt, get a translator or give the test in ... |
| Q132 | - |  |  | SI | Speech: |
| Q133 | - |  |  | SI | Some people have severe speech problems, so their ... |
| Q134 | - |  |  | SI | They score lower because they cannot answer within... |
| Q135 | - |  |  | SI | Some may reverse words and may say ‘winter’ when t... |
| Q136 | - |  |  | SI | These deficits unfortunately bias the test against... |
| Q137 | - |  |  | SI | It is important to be consistent and adhere to the... |
| Q138 | - |  |  | SI | Note can be made of these factors and performance ... |
| Q139 | - |  |  | SI | Education: |
| Q14 | - |  |  | SI | d) What is today's date?&nbsp |
| Q140 | - |  |  | SI | Low education or education in a language other tha... |
| Q141 | - |  |  | SI | Generally, these limitations should not exempt a p... |
| Q142 | - |  |  | SI | Generally, these limitations should not exempt a p... |
| Q143 | - |  |  | SI | Note should be made that these factors may cause l... |
| Q144 | - |  |  | SI | The person’s disability should be clearly noted on... |
| Q145 | - |  |  | SI | Items that are affected by this disability should ... |
| Q146 | - |  |  | SI | The calculation of the adjusted score is done at t... |
| Q147 | - |  |  | SI | Folstein MF, Folstein SE, McHugh PR. “Mini-mental ... |
| Q148 | - |  |  | SI | Molloy DW, Alemayehu E, Roberts R. Reliability of ... |
| Q149 | - |  |  | SI | The Standardised Mini-Mental State Examination is ... |
| Q15 | - |  |  | SI | e) What day of the week is this? |
| Q150 | - |  |  | SI | 9. Say: Read the words on this page and then do wh... |
| Q151 | - |  |  | SI | Say: Copy this design please |
| Q152 | - |  |  | SI | 4. Say: Subtract seven from 100 and keep subtracti... |
| Q153 | - |  |  | SI | WORLD backwards score |
| Q16 | - |  |  | SI | e) What day of the week is this?&nbsp |
| Q17 | - |  |  | SI | 2. Allow 10 Seconds for each reply. Say: |
| Q18 | - |  |  | SI | a) What country are we in? |
| Q19 | - |  |  | SI | a) What country are we in?&nbsp |
| Q20 | - |  |  | SI | b) What state are we in? |
| Q21 | - |  |  | SI | b)&nbsp |
| Q22 | - |  |  | SI | c) What city/town are we in? |
| Q23 | - |  |  | SI | c) What city/town are we in? (accept exact answer ... |
| Q24 | - |  |  | SI | d) &lt |
| Q25 | - |  |  | SI | d) &lt |
| Q26 | - |  |  | SI | &lt |
| Q27 | - |  |  | SI | e) &lt |
| Q28 | - |  |  | SI | e) &lt |
| Q29 | - |  |  | SI | 3. Say:&nbsp |
| Q30 | - |  |  | SI | Remember what they are because I am going to ask y... |
| Q31 | - |  |  | SI | WORDS:&nbsp |
| Q32 | - |  |  | SI | WORDS FOR REPEATED USE: Bell, jar, fan |
| Q33 | - |  |  | SI | Say: Please repeat the three items for me |
| Q34 | - |  |  | SI | Say: Please repeat the three items for me&nbsp |
| Q35 | - |  |  | SI | Allow 20 seconds for reply |
| Q36 | - |  |  | SI | 4. Say: Spell the word WORLD (you may help the per... |
| Q37 | - |  |  | SI | Say: Now spell it backwards please |
| Q38 | - |  |  | SI | (allow 30 seconds |
| Q39 | - |  |  | SI | WORLD backwards score |
| Q40 | - |  |  | SI | 4. Say: Subtract seven from 100 and keep subtracti... |
| Q41 | - |  |  | SI | Write down person's reply |
| Q42 | - |  |  | SI | Once person starts - do not interrupt - allow him/... |
| Q43 | - |  |  | SI | If person stops before five subtractions have been... |
| Q44 | - |  |  | SI | 5. Say: Now what were the three objects I asked yo... |
| Q45 | - |  |  | SI | 5. Say: Now what were the three objects I asked yo... |
| Q46 | - |  |  | SI | 6. Show wristwatch. Ask: What is this called? |
| Q47 | - |  |  | SI | 6. Show wristwatch. Ask: What is this called? (sco... |
| Q48 | - |  |  | SI | 7. Show pencil. Ask: What is this called? |
| Q49 | - |  |  | SI | 7. Show pencil. Ask: What is this called? (score o... |
| Q50 | - |  |  | SI | 8. Say: I would like you to repeat a phrase after ... |
| Q51 | - |  |  | SI | 8. Say: I would like you to repeat a phrase after ... |
| Q52 | - |  |  | SI | 9. Say: Read the words on this page and then do wh... |
| Q53 | - |  |  | SI | Then, hand the person the sheet with CLOSE YOUR EY... |
| Q54 | - |  |  | SI | If the subject just reads and does not close eyes,... |
| Q55 | - |  |  | SI | Score one point only if the person closes their ey... |
| Q56 | - |  |  | SI | The person does not have to read aloud. |
| Q57 | - |  |  | SI | 10. Hand the person a pencil and paper |
| Q58 | - |  |  | SI | Say: Write any complete sentence on that piece of ... |
| Q59 | - |  |  | SI | Say: Write any complete sentence on that piece of ... |
| Q60 | - |  |  | SI | 11. Place design, pencil, eraser and paper in fron... |
| Q61 | - |  |  | SI | Say: Copy this design please |
| Q62 | - |  |  | SI | Allow multiple tries. |
| Q63 | - |  |  | SI | Wait until the person is finished and hands it bac... |
| Q64 | - |  |  | SI | Score one point for a correctly copied diagram. |
| Q65 | - |  |  | SI | The person must have drawn a four-sided figure bet... |
| Q66 | - |  |  | SI | Maximum time: one minute. |
| Q67 | - |  |  | SI | Design time taken (min) |
| Q68 | - |  |  | SI | 12. Ask the person if he is right or left handed. |
| Q69 | - |  |  | SI | Take a piece of paper, hold it up in front of the ... |
| Q70 | - |  |  | SI | Take this paper in your right/left hand (whichever... |
| Q71 | - |  |  | SI | Folding paper exercise |
| Q72 | - |  |  | SI | Total test score |
| Q73 | - |  |  | SI | Adjusted score |
| Q74 | - |  |  | SI | Directions for administration of SMMSE |
| Q75 | - |  |  | SI | Before the questionnaire is administered, try to g... |
| Q76 | - |  |  | SI | Assess the person’s&nbsp |
| Q77 | - |  |  | SI | Introduce yourself and try to get the person’s con... |
| Q78 | - |  |  | SI | Before you begin, get&nbsp |
| Q79 | - |  |  | SI | Ask each question a maximum of three times. If the... |
| Q80 | - |  |  | SI | If the person answers incorrectly, score zero. Acc... |
| Q81 | - |  |  | SI | The following equipment is required to administer ... |
| Q82 | - |  |  | SI | A watch, a pencil, reverse of the SMMSE score shee... |
| Q83 | - |  |  | SI | If the person answers what did you say?, do not ex... |
| Q84 | - |  |  | SI | If the person interrupts (e.g. queries what is thi... |
| Q85 | - |  |  | SI | Scoring WORLD backwards (question 4) |
| Q86 | - |  |  | SI | This task accounts for 17% of the total score. It ... |
| Q87 | - |  |  | SI | There are many different ways and systems for scor... |
| Q88 | - |  |  | SI | Originally, Dr. Folstein advised that the score is... |
| Q89 | - |  |  | SI | The authors suggest the following method. Score OR... |
| Q90 | - |  |  | SI | Simply write down the correct response: D L R O W. |
| Q91 | - |  |  | SI | Now place the last five letters the person said be... |
| Q92 | - |  |  | SI | Now draw lines between the same letters on the res... |
| Q93 | - |  |  | SI | These lines MAY NOT CROSS. |
| Q94 | - |  |  | SI | The person’s score is the maximum number of lines ... |
| Q95 | - |  |  | SI | In SMMSE there are many different ways to score th... |
| Q96 | - |  |  | SI | Scoring of serial sevens (alternative to question ... |
| Q97 | - |  |  | SI | The serial sevens task is presented as an alternat... |
| Q98 | - |  |  | SI | The two taks are not equivalent. |
| Q99 | - |  |  | SI | The serial sevens is an easier taks, and the scori... |
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