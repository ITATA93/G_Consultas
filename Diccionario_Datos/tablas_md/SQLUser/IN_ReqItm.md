# SQLUser.IN_ReqItm

**Schema:** SQLUser
**Columnas:** 209
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INRQI_INRQ_ParRef | bigint | PK |  | NO | Des Ref To INRQ |
| INRQI_CTUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| INRQI_Childsub | numeric |  |  | NO | INRQI Childsub (New Key) |
| INRQI_Date | date |  |  | NO | Date Needed |
| INRQI_INCI_DR | bigint |  | FK | NO | Des Ref to INCI |
| INRQI_LockedRequest | varchar |  |  | SI | Locked Request |
| INRQI_OutstandQty | double |  |  | SI | Outstanding Quantity |
| INRQI_RecLoc_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| INRQI_ReqQty | double |  |  | NO | Request Quantity |
| INRQI_ReturnDate | date |  |  | SI | Date to be Returned (Loan Items) |
| INRQI_RowId | varchar |  |  | NO | - |
| INRQI_Type | varchar |  |  | SI | Request Type |
| Q01 | - |  |  | SI | Suicidal and self-injury behaviour (past week) |
| Q02 | - |  |  | SI | Suicidal ideation (most severe in past week) |
| Q03 | - |  |  | SI | Activating events (recent) |
| Q04 | - |  |  | SI | If recent loss, please describe |
| Q05 | - |  |  | SI | Treatment history |
| Q06 | - |  |  | SI | Other risk factors |
| Q07 | - |  |  | SI | Clinical status (recent) |
| Q08 | - |  |  | SI | Protective factors (recent) |
| Q09 | - |  |  | SI | Other protective factors |
| Q10 | - |  |  | SI | Describe any suicidal, self-injury or aggressive b... |
| Q100 | - |  |  | SI | When the person is interrupted (by an outside circ... |
| Q101 | - |  |  | SI | Overdose: person has pills in hand but is stopped ... |
| Q102 | - |  |  | SI | Shooting: person has gun pointed toward self, gun ... |
| Q103 | - |  |  | SI | Jumping: person is poised to jump, is grabbed and ... |
| Q104 | - |  |  | SI | Hanging: person has noose around neck but has not ... |
| Q105 | - |  |  | SI | Has there been a time when you started to do somet... |
| Q106 | - |  |  | SI | 2. Lifetime |
| Q107 | - |  |  | SI | 2. Past 3 months |
| Q108 | - |  |  | SI | Lifetime: total number of interrupted |
| Q109 | - |  |  | SI | Past 3 months: total number of interrupted |
| Q11 | - |  |  | SI | Ask questions 1 and 2. If both are negative, proce... |
| Q110 | - |  |  | SI | If yes, describe |
| Q111 | - |  |  | SI | Aborted or self-interrupted attempt |
| Q112 | - |  |  | SI | When person begins to take steps toward making a s... |
| Q113 | - |  |  | SI | Examples are similar to interrupted attempts, exce... |
| Q114 | - |  |  | SI | Has there been a time when you started to do somet... |
| Q115 | - |  |  | SI | Lifetime |
| Q116 | - |  |  | SI | Past 3 months |
| Q117 | - |  |  | SI | Lifetime: total number of aborted or self interrup... |
| Q118 | - |  |  | SI | Past 3 months: total number of aborted or self int... |
| Q119 | - |  |  | SI | If yes, describe |
| Q12 | - |  |  | SI | If the answer to question 1 and/or 2 is “yes”, com... |
| Q120 | - |  |  | SI | Preparatory acts or behavior |
| Q121 | - |  |  | SI | Acts or preparation towards imminently making a su... |
| Q122 | - |  |  | SI | (e.g., buying pills, purchasing a gun) or preparin... |
| Q123 | - |  |  | SI | Have you taken any steps towards making a suicide ... |
| Q124 | - |  |  | SI | Lifetime |
| Q125 | - |  |  | SI | Past 3 months |
| Q126 | - |  |  | SI | Lifetime: total # of preparatory acts |
| Q127 | - |  |  | SI | Past 3 months: total # of preparatory acts |
| Q128 | - |  |  | SI | If yes, describe |
| Q129 | - |  |  | SI | Actual lethality / medical damage |
| Q13 | - |  |  | SI | 1. Wish to be dead |
| Q130 | - |  |  | SI | 0. No physical damage or very minor physical damag... |
| Q131 | - |  |  | SI | 1. Minor physical damage (e.g., lethargic speech |
| Q132 | - |  |  | SI | 2. Moderate physical damage |
| Q133 | - |  |  | SI | 3. Moderately severe physical damage |
| Q134 | - |  |  | SI | intact |
| Q135 | - |  |  | SI | 4. Severe physical damage |
| Q136 | - |  |  | SI | burns over 20% of body |
| Q137 | - |  |  | SI | 5. Death |
| Q138 | - |  |  | SI | Most recent attempt date |
| Q139 | - |  |  | SI | Most recent attempt code |
| Q14 | - |  |  | SI | Subject endorses thoughts about a wish to be dead ... |
| Q140 | - |  |  | SI | Most lethal attempt date |
| Q141 | - |  |  | SI | Most lethal attempt code |
| Q142 | - |  |  | SI | Initial / First attempt date |
| Q143 | - |  |  | SI | Initial / First attempt code |
| Q144 | - |  |  | SI | Potential lethality: only answer if actual lethali... |
| Q145 | - |  |  | SI | Likely lethality of actual attempt if no medical d... |
| Q146 | - |  |  | SI | put gun in mouth and pulled the trigger but gun fa... |
| Q147 | - |  |  | SI | 0 = Behavior not likely to result in injury |
| Q148 | - |  |  | SI | 1 = Behavior likely to result in injury but not li... |
| Q149 | - |  |  | SI | 2 = Behavior likely to result in death despite ava... |
| Q15 | - |  |  | SI | Have you wished you were dead or wished you could ... |
| Q150 | - |  |  | SI | Most recent attempt date |
| Q151 | - |  |  | SI | Most recent attempt code |
| Q152 | - |  |  | SI | Most lethal attempt date |
| Q153 | - |  |  | SI | Most lethal attempt code |
| Q154 | - |  |  | SI | Initial / First attempt date |
| Q155 | - |  |  | SI | Initial / First attempt code |
| Q156 | - |  |  | SI | Instructions: Check all risk and protective factor... |
| Q157 | - |  |  | SI | review of medical record(s) and/or consultation wi... |
| Q16 | - |  |  | SI | Lifetime |
| Q17 | - |  |  | SI | Past 1 month |
| Q18 | - |  |  | SI | If yes, describe |
| Q19 | - |  |  | SI | 3. Active suicidal ideation with any methods (not ... |
| Q20 | - |  |  | SI | Subject endorses thoughts of suicide and has thoug... |
| Q21 | - |  |  | SI | place or method details worked out (e.g., thought ... |
| Q22 | - |  |  | SI | “I thought about taking an overdose but I never ma... |
| Q23 | - |  |  | SI | Have you been thinking about how you might do this... |
| Q24 | - |  |  | SI | Lifetime |
| Q25 | - |  |  | SI | Past 1 month |
| Q26 | - |  |  | SI | If yes, describe |
| Q27 | - |  |  | SI | 4. Active suicidal ideation with some intent to ac... |
| Q28 | - |  |  | SI | Active suicidal thoughts of killing oneself and su... |
| Q29 | - |  |  | SI | Have you had these thoughts and had some intention... |
| Q30 | - |  |  | SI | Lifetime |
| Q31 | - |  |  | SI | Past 1 month |
| Q32 | - |  |  | SI | If yes, describe |
| Q33 | - |  |  | SI | 5. Active suicidal ideation with specific plan and... |
| Q34 | - |  |  | SI | Thoughts of killing oneself with details of plan f... |
| Q35 | - |  |  | SI | Have you started to work out or worked out the det... |
| Q36 | - |  |  | SI | Lifetime |
| Q37 | - |  |  | SI | Past 1 month |
| Q38 | - |  |  | SI | If yes, describe |
| Q39 | - |  |  | SI | The following features should be rated with respec... |
| Q40 | - |  |  | SI | Ask about time he/she was feeling the most suicida... |
| Q41 | - |  |  | SI | Lifetime - most severe ideation: (Type # 1-5) |
| Q42 | - |  |  | SI | Recent - most severe ideation: (Type # 1-5) |
| Q43 | - |  |  | SI | Lifetime - description of ideation |
| Q44 | - |  |  | SI | Recent - description of ideation |
| Q45 | - |  |  | SI | Frequency |
| Q46 | - |  |  | SI | How many times have you had these thoughts? |
| Q47 | - |  |  | SI | Lifetime: most severe |
| Q48 | - |  |  | SI | Recent: most severe |
| Q49 | - |  |  | SI | Duration |
| Q50 | - |  |  | SI | When you have the thoughts how long do they last? |
| Q51 | - |  |  | SI | Lifetime: most severe |
| Q52 | - |  |  | SI | Recent: most severe |
| Q53 | - |  |  | SI | 2. Non-specific active suicidal thoughts |
| Q54 | - |  |  | SI | General non-specific thoughts of wanting to end on... |
| Q55 | - |  |  | SI | of ways to kill oneself / associated methods, inte... |
| Q56 | - |  |  | SI | Have you actually had any thoughts of killing your... |
| Q57 | - |  |  | SI | Lifetime |
| Q58 | - |  |  | SI | Past 1 month |
| Q59 | - |  |  | SI | If yes, describe |
| Q60 | - |  |  | SI | Controllability |
| Q61 | - |  |  | SI | Could/Can you stop thinking about killing yourself... |
| Q62 | - |  |  | SI | Lifetime: most severe |
| Q63 | - |  |  | SI | Recent: most severe |
| Q64 | - |  |  | SI | Deterrents |
| Q65 | - |  |  | SI | Are there things - anyone or anything (e.g., famil... |
| Q66 | - |  |  | SI | Lifetime: most severe |
| Q67 | - |  |  | SI | Recent: most severe |
| Q68 | - |  |  | SI | Reasons for ideation |
| Q69 | - |  |  | SI | What sort of reasons did you have for thinking abo... |
| Q70 | - |  |  | SI | (in other words you couldn’t go on living with thi... |
| Q71 | - |  |  | SI | Lifetime: most severe |
| Q72 | - |  |  | SI | Recent: most severe |
| Q73 | - |  |  | SI | (Check all that apply, so long as these are separa... |
| Q74 | - |  |  | SI | Actual Attempt |
| Q75 | - |  |  | SI | Lifetime |
| Q76 | - |  |  | SI | Past 3 months |
| Q77 | - |  |  | SI | A potentially self-injurious act committed with at... |
| Q78 | - |  |  | SI | Intent does not have to be 100%. If there is any i... |
| Q79 | - |  |  | SI | There does not have to be any injury or harm, just... |
| Q80 | - |  |  | SI | Inferring Intent: even if an individual denies int... |
| Q81 | - |  |  | SI | but suicide can be inferred (e.g., gunshot to head... |
| Q82 | - |  |  | SI | what they did could be lethal, intent may be infer... |
| Q83 | - |  |  | SI | Have you made a suicide attempt? |
| Q84 | - |  |  | SI | Have you done anything to harm yourself? |
| Q85 | - |  |  | SI | Have you done anything dangerous where you could h... |
| Q86 | - |  |  | SI | What did you do? |
| Q87 | - |  |  | SI | Did you______ as a way to end your life? |
| Q88 | - |  |  | SI | Did you want to die (even a little) when you_____? |
| Q89 | - |  |  | SI | Were you trying to end your life when you _____? |
| Q90 | - |  |  | SI | Or did you think it was possible you could have di... |
| Q91 | - |  |  | SI | Or did you do it purely for other reasons / withou... |
| Q92 | - |  |  | SI | yourself (like to relieve stress, feel better, get... |
| Q93 | - |  |  | SI | If yes, describe |
| Q94 | - |  |  | SI | Total number of attempts (lifetime) |
| Q95 | - |  |  | SI | Total number of attempts (past 3 months) |
| Q96 | - |  |  | SI | Has subject engaged in non-suicidal self-injurious... |
| Q97 | - |  |  | SI | 1. Lifetime |
| Q98 | - |  |  | SI | 1. Past 3 months |
| Q99 | - |  |  | SI | Interrupted attempt |
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