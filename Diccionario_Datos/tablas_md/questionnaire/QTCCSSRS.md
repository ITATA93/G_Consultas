# questionnaire.QTCCSSRS

> Columbia-Suicide Severity Rating Scale (C-SSRS)

**Schema:** questionnaire
**Columnas:** 198
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Columbia-Suicide Severity Rating Scale (C-SSRS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Suicidal and self-injury behaviour (past week) |
| Q02 | varchar |  |  | SI | Suicidal ideation (most severe in past week) |
| Q03 | varchar |  |  | SI | Activating events (recent) |
| Q04 | varchar |  |  | SI | If recent loss, please describe |
| Q05 | varchar |  |  | SI | Treatment history |
| Q06 | varchar |  |  | SI | Other risk factors |
| Q07 | varchar |  |  | SI | Clinical status (recent) |
| Q08 | varchar |  |  | SI | Protective factors (recent) |
| Q09 | varchar |  |  | SI | Other protective factors |
| Q10 | varchar |  |  | SI | Describe any suicidal, self-injury or aggressive b... |
| Q100 | varchar |  |  | SI | When the person is interrupted (by an outside circ... |
| Q101 | varchar |  |  | SI | Overdose: person has pills in hand but is stopped ... |
| Q102 | varchar |  |  | SI | Shooting: person has gun pointed toward self, gun ... |
| Q103 | varchar |  |  | SI | Jumping: person is poised to jump, is grabbed and ... |
| Q104 | varchar |  |  | SI | Hanging: person has noose around neck but has not ... |
| Q105 | varchar |  |  | SI | Has there been a time when you started to do somet... |
| Q106 | varchar |  |  | SI | 2. Lifetime |
| Q107 | varchar |  |  | SI | 2. Past 3 months |
| Q108 | numeric |  |  | SI | Lifetime: total number of interrupted |
| Q109 | numeric |  |  | SI | Past 3 months: total number of interrupted |
| Q11 | varchar |  |  | SI | Ask questions 1 and 2. If both are negative, proce... |
| Q110 | varchar |  |  | SI | If yes, describe |
| Q111 | varchar |  |  | SI | Aborted or self-interrupted attempt |
| Q112 | varchar |  |  | SI | When person begins to take steps toward making a s... |
| Q113 | varchar |  |  | SI | Examples are similar to interrupted attempts, exce... |
| Q114 | varchar |  |  | SI | Has there been a time when you started to do somet... |
| Q115 | varchar |  |  | SI | Lifetime |
| Q116 | varchar |  |  | SI | Past 3 months |
| Q117 | numeric |  |  | SI | Lifetime: total number of aborted or self interrup... |
| Q118 | numeric |  |  | SI | Past 3 months: total number of aborted or self int... |
| Q119 | varchar |  |  | SI | If yes, describe |
| Q12 | varchar |  |  | SI | If the answer to question 1 and/or 2 is “yes”, com... |
| Q120 | varchar |  |  | SI | Preparatory acts or behavior |
| Q121 | varchar |  |  | SI | Acts or preparation towards imminently making a su... |
| Q122 | varchar |  |  | SI | (e.g., buying pills, purchasing a gun) or preparin... |
| Q123 | varchar |  |  | SI | Have you taken any steps towards making a suicide ... |
| Q124 | varchar |  |  | SI | Lifetime |
| Q125 | varchar |  |  | SI | Past 3 months |
| Q126 | numeric |  |  | SI | Lifetime: total # of preparatory acts |
| Q127 | numeric |  |  | SI | Past 3 months: total # of preparatory acts |
| Q128 | varchar |  |  | SI | If yes, describe |
| Q129 | varchar |  |  | SI | Actual lethality / medical damage |
| Q13 | varchar |  |  | SI | 1. Wish to be dead |
| Q130 | varchar |  |  | SI | 0. No physical damage or very minor physical damag... |
| Q131 | varchar |  |  | SI | 1. Minor physical damage (e.g., lethargic speech; ... |
| Q132 | varchar |  |  | SI | 2. Moderate physical damage; medical attention nee... |
| Q133 | varchar |  |  | SI | 3. Moderately severe physical damage; medical hosp... |
| Q134 | varchar |  |  | SI | intact; third-degree burns less than 20% of body; ... |
| Q135 | varchar |  |  | SI | 4. Severe physical damage; medical hospitalization... |
| Q136 | varchar |  |  | SI | burns over 20% of body; extensive blood loss with ... |
| Q137 | varchar |  |  | SI | 5. Death |
| Q138 | date |  |  | SI | Most recent attempt date |
| Q139 | varchar |  |  | SI | Most recent attempt code |
| Q14 | varchar |  |  | SI | Subject endorses thoughts about a wish to be dead ... |
| Q140 | date |  |  | SI | Most lethal attempt date |
| Q141 | varchar |  |  | SI | Most lethal attempt code |
| Q142 | date |  |  | SI | Initial / First attempt date |
| Q143 | varchar |  |  | SI | Initial / First attempt code |
| Q144 | varchar |  |  | SI | Potential lethality: only answer if actual lethali... |
| Q145 | varchar |  |  | SI | Likely lethality of actual attempt if no medical d... |
| Q146 | varchar |  |  | SI | put gun in mouth and pulled the trigger but gun fa... |
| Q147 | varchar |  |  | SI | 0 = Behavior not likely to result in injury |
| Q148 | varchar |  |  | SI | 1 = Behavior likely to result in injury but not li... |
| Q149 | varchar |  |  | SI | 2 = Behavior likely to result in death despite ava... |
| Q15 | varchar |  |  | SI | Have you wished you were dead or wished you could ... |
| Q150 | date |  |  | SI | Most recent attempt date |
| Q151 | varchar |  |  | SI | Most recent attempt code |
| Q152 | date |  |  | SI | Most lethal attempt date |
| Q153 | varchar |  |  | SI | Most lethal attempt code |
| Q154 | date |  |  | SI | Initial / First attempt date |
| Q155 | varchar |  |  | SI | Initial / First attempt code |
| Q156 | varchar |  |  | SI | Instructions: Check all risk and protective factor... |
| Q157 | varchar |  |  | SI | review of medical record(s) and/or consultation wi... |
| Q16 | varchar |  |  | SI | Lifetime |
| Q17 | varchar |  |  | SI | Past 1 month |
| Q18 | varchar |  |  | SI | If yes, describe |
| Q19 | varchar |  |  | SI | 3. Active suicidal ideation with any methods (not ... |
| Q20 | varchar |  |  | SI | Subject endorses thoughts of suicide and has thoug... |
| Q21 | varchar |  |  | SI | place or method details worked out (e.g., thought ... |
| Q22 | varchar |  |  | SI |  “I thought about taking an overdose but I never m... |
| Q23 | varchar |  |  | SI | Have you been thinking about how you might do this... |
| Q24 | varchar |  |  | SI | Lifetime |
| Q25 | varchar |  |  | SI | Past 1 month |
| Q26 | varchar |  |  | SI | If yes, describe |
| Q27 | varchar |  |  | SI | 4. Active suicidal ideation with some intent to ac... |
| Q28 | varchar |  |  | SI | Active suicidal thoughts of killing oneself and su... |
| Q29 | varchar |  |  | SI | Have you had these thoughts and had some intention... |
| Q30 | varchar |  |  | SI | Lifetime |
| Q31 | varchar |  |  | SI | Past 1 month |
| Q32 | varchar |  |  | SI | If yes, describe |
| Q33 | varchar |  |  | SI | 5. Active suicidal ideation with specific plan and... |
| Q34 | varchar |  |  | SI | Thoughts of killing oneself with details of plan f... |
| Q35 | varchar |  |  | SI | Have you started to work out or worked out the det... |
| Q36 | varchar |  |  | SI | Lifetime |
| Q37 | varchar |  |  | SI | Past 1 month |
| Q38 | varchar |  |  | SI | If yes, describe |
| Q39 | varchar |  |  | SI | The following features should be rated with respec... |
| Q40 | varchar |  |  | SI |  Ask about time he/she was feeling the most suicid... |
| Q41 | numeric |  |  | SI | Lifetime - most severe ideation: (Type # 1-5) |
| Q42 | numeric |  |  | SI | Recent - most severe ideation: (Type # 1-5) |
| Q43 | varchar |  |  | SI | Lifetime - description of ideation |
| Q44 | varchar |  |  | SI | Recent - description of ideation |
| Q45 | varchar |  |  | SI | Frequency |
| Q46 | varchar |  |  | SI | How many times have you had these thoughts? |
| Q47 | varchar |  |  | SI | Lifetime: most severe |
| Q48 | varchar |  |  | SI | Recent: most severe |
| Q49 | varchar |  |  | SI | Duration |
| Q50 | varchar |  |  | SI | When you have the thoughts how long do they last? |
| Q51 | varchar |  |  | SI | Lifetime: most severe |
| Q52 | varchar |  |  | SI | Recent: most severe |
| Q53 | varchar |  |  | SI | 2. Non-specific active suicidal thoughts |
| Q54 | varchar |  |  | SI | General non-specific thoughts of wanting to end on... |
| Q55 | varchar |  |  | SI | of ways to kill oneself / associated methods, inte... |
| Q56 | varchar |  |  | SI | Have you actually had any thoughts of killing your... |
| Q57 | varchar |  |  | SI | Lifetime |
| Q58 | varchar |  |  | SI | Past 1 month |
| Q59 | varchar |  |  | SI | If yes, describe |
| Q60 | varchar |  |  | SI | Controllability |
| Q61 | varchar |  |  | SI | Could/Can you stop thinking about killing yourself... |
| Q62 | varchar |  |  | SI | Lifetime: most severe |
| Q63 | varchar |  |  | SI | Recent: most severe |
| Q64 | varchar |  |  | SI | Deterrents |
| Q65 | varchar |  |  | SI | Are there things - anyone or anything (e.g., famil... |
| Q66 | varchar |  |  | SI | Lifetime: most severe |
| Q67 | varchar |  |  | SI | Recent: most severe |
| Q68 | varchar |  |  | SI | Reasons for ideation |
| Q69 | varchar |  |  | SI | What sort of reasons did you have for thinking abo... |
| Q70 | varchar |  |  | SI |  (in other words you couldn’t go on living with th... |
| Q71 | varchar |  |  | SI | Lifetime: most severe |
| Q72 | varchar |  |  | SI | Recent: most severe |
| Q73 | varchar |  |  | SI | (Check all that apply, so long as these are separa... |
| Q74 | varchar |  |  | SI | Actual Attempt |
| Q75 | varchar |  |  | SI | Lifetime |
| Q76 | varchar |  |  | SI | Past 3 months |
| Q77 | varchar |  |  | SI | A potentially self-injurious act committed with at... |
| Q78 | varchar |  |  | SI | Intent does not have to be 100%. If there is any i... |
| Q79 | varchar |  |  | SI | There does not have to be any injury or harm, just... |
| Q80 | varchar |  |  | SI | Inferring Intent: even if an individual denies int... |
| Q81 | varchar |  |  | SI | but suicide can be inferred (e.g., gunshot to head... |
| Q82 | varchar |  |  | SI | what they did could be lethal, intent may be infer... |
| Q83 | varchar |  |  | SI | Have you made a suicide attempt? |
| Q84 | varchar |  |  | SI | Have you done anything to harm yourself? |
| Q85 | varchar |  |  | SI | Have you done anything dangerous where you could h... |
| Q86 | varchar |  |  | SI | What did you do? |
| Q87 | varchar |  |  | SI | Did you______ as a way to end your life? |
| Q88 | varchar |  |  | SI | Did you want to die (even a little) when you_____? |
| Q89 | varchar |  |  | SI | Were you trying to end your life when you _____? |
| Q90 | varchar |  |  | SI | Or did you think it was possible you could have di... |
| Q91 | varchar |  |  | SI | Or did you do it purely for other reasons / withou... |
| Q92 | varchar |  |  | SI | yourself (like to relieve stress, feel better, get... |
| Q93 | varchar |  |  | SI | If yes, describe |
| Q94 | numeric |  |  | SI | Total number of attempts (lifetime) |
| Q95 | numeric |  |  | SI | Total number of attempts (past 3 months) |
| Q96 | varchar |  |  | SI | Has subject engaged in non-suicidal self-injurious... |
| Q97 | varchar |  |  | SI | 1. Lifetime |
| Q98 | varchar |  |  | SI | 1. Past 3 months |
| Q99 | varchar |  |  | SI | Interrupted attempt |
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