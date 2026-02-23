# questionnaire.QTCPSQI

> The Pittsburgh Sleep Quality Index (PSQI)

**Schema:** questionnaire
**Columnas:** 181
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Pittsburgh Sleep Quality Index (PSQI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Instruction |
| Q04 | varchar |  |  | SI | The following questions relate to your usual sleep... |
| Q05 | varchar |  |  | SI | Your answers should indicate the most accurate rep... |
| Q06 | varchar |  |  | SI | Please answer all questions. |
| Q07 | varchar |  |  | SI | During the past months, what time have you usually... |
| Q08 | time |  |  | SI | Bed time |
| Q09 | varchar |  |  | SI | During the past month, how long (in minutes) has i... |
| Q10 | numeric |  |  | SI | Number of minutes |
| Q100 | varchar |  |  | SI | &lt;5 |
| Q101 | varchar |  |  | SI | Component Score |
| Q102 | varchar |  |  | SI | 0 |
| Q103 | varchar |  |  | SI | 1 |
| Q104 | varchar |  |  | SI | 2 |
| Q105 | varchar |  |  | SI | 3 |
| Q106 | varchar |  |  | SI | A score of '0' indicates no difficulty, while a sc... |
| Q107 | varchar |  |  | SI | Habitual sleep efficiency |
| Q108 | varchar |  |  | SI | &gt;85 |
| Q109 | varchar |  |  | SI | ≥75 and &lt;85 |
| Q11 | varchar |  |  | SI | During the past month, what time have you usually ... |
| Q110 | varchar |  |  | SI | ≥65 and &lt;75 |
| Q111 | varchar |  |  | SI | &lt;65 |
| Q112 | varchar |  |  | SI | Component Score |
| Q113 | varchar |  |  | SI | 0 |
| Q114 | varchar |  |  | SI | 1 |
| Q115 | varchar |  |  | SI | 2 |
| Q116 | varchar |  |  | SI | 3 |
| Q117 | varchar |  |  | SI | A score of '0' indicates no difficulty, while a sc... |
| Q118 | varchar |  |  | SI | Sleep disturbance |
| Q119 | varchar |  |  | SI | 0 |
| Q12 | time |  |  | SI | Getting up time |
| Q120 | varchar |  |  | SI | &gt;0 and ≤9 |
| Q121 | varchar |  |  | SI | &gt;9 and ≤18 |
| Q122 | varchar |  |  | SI | &gt;18 |
| Q123 | varchar |  |  | SI | Component Score |
| Q124 | varchar |  |  | SI | 0 |
| Q125 | varchar |  |  | SI | 1 |
| Q126 | varchar |  |  | SI | 2 |
| Q127 | varchar |  |  | SI | 3 |
| Q128 | varchar |  |  | SI | A score of '0' indicates no difficulty, while a sc... |
| Q129 | varchar |  |  | SI | A score of '0' indicates no difficulty, while a sc... |
| Q13 | varchar |  |  | SI | During the past month, how many hours of actual sl... |
| Q130 | varchar |  |  | SI | Daytime dysfunction |
| Q131 | varchar |  |  | SI | 0 |
| Q132 | varchar |  |  | SI | &gt;0 and ≤2 |
| Q133 | varchar |  |  | SI | &gt;2 and ≤4 |
| Q134 | varchar |  |  | SI | &gt;5 |
| Q135 | varchar |  |  | SI | Component Score |
| Q136 | varchar |  |  | SI | 0 |
| Q137 | varchar |  |  | SI | 1 |
| Q138 | varchar |  |  | SI | 2 |
| Q139 | varchar |  |  | SI | 3 |
| Q14 | varchar |  |  | SI | (this may be different than the numbers of hours y... |
| Q140 | varchar |  |  | SI | A score of '0' indicates no difficulty, while a sc... |
| Q15 | numeric |  |  | SI | Hours of sleep per night |
| Q16 | varchar |  |  | SI | For each of the remaining questions, check the one... |
| Q17 | varchar |  |  | SI | Please answer all questions. |
| Q18 | varchar |  |  | SI | During the past month, how often have you had trou... |
| Q19 | varchar |  |  | SI | A. Cannot get to sleep within 30 minutes |
| Q20 | varchar |  |  | SI | B. Wake up in the middle of the night or early mor... |
| Q21 | varchar |  |  | SI | C. Have to get up to use the bathroom |
| Q22 | varchar |  |  | SI | D. Cannot breathe comfortably |
| Q23 | varchar |  |  | SI | E. Cough or snore loudly |
| Q24 | varchar |  |  | SI | F. Feel too cold |
| Q25 | varchar |  |  | SI | G. Feel too hot |
| Q26 | varchar |  |  | SI | H. Had bad dreams |
| Q27 | varchar |  |  | SI | I. Have pain |
| Q28 | varchar |  |  | SI | J. Other reason(s), please describe |
| Q29 | varchar |  |  | SI | How often during the past month have you had troub... |
| Q30 | varchar |  |  | SI | During the past month, how would you rate your sle... |
| Q31 | varchar |  |  | SI | During the past month, how often have you taken me... |
| Q32 | varchar |  |  | SI | During the past month, how often have you had trou... |
| Q33 | varchar |  |  | SI | During the past month, how much of a problem has i... |
| Q34 | varchar |  |  | SI | Do you have a bed partner or room mate? |
| Q35 | varchar |  |  | SI | If you have a room mate or partner, ask him/her ho... |
| Q36 | varchar |  |  | SI | A. Loud snoring |
| Q37 | varchar |  |  | SI | B. Long pauses between breaths while asleep |
| Q38 | varchar |  |  | SI | C. Legs twitching or jerking while asleep |
| Q39 | varchar |  |  | SI | D. Episodes of disorientation or confusion during ... |
| Q40 | varchar |  |  | SI | E. Other restlessness while you sleep |
| Q41 | varchar |  |  | SI | Please describe |
| Q42 | varchar |  |  | SI | Component 1 - Subjective Sleep Quality |
| Q43 | numeric |  |  | SI | Subjective sleep quality |
| Q44 | varchar |  |  | SI | Component 2 - Sleep Latency |
| Q45 | numeric |  |  | SI | Sleep latency |
| Q46 | varchar |  |  | SI | Component 3 - Sleep Duration |
| Q47 | numeric |  |  | SI | Sleep duration |
| Q48 | varchar |  |  | SI | Component 4 - Habitual Sleep Efficiency |
| Q49 | numeric |  |  | SI | Habitual sleep efficiency |
| Q50 | varchar |  |  | SI | Component 5 - Sleep Disturbance |
| Q51 | numeric |  |  | SI | Sleep disturbaces |
| Q52 | varchar |  |  | SI | Component 6 - Use of Sleeping Medication |
| Q53 | numeric |  |  | SI | Use of sleeping medication |
| Q54 | varchar |  |  | SI | Component 7 - Daytime Dysfunction |
| Q55 | numeric |  |  | SI | Daytime dysfunction |
| Q56 | varchar |  |  | SI | Global PSQI&nbsp;score |
| Q57 | varchar |  |  | SI | The pittsburgh sleep quality index (psqi) is a sel... |
| Q58 | varchar |  |  | SI | Namely: quality, latency, duration, habitual sleep... |
| Q59 | varchar |  |  | SI | Buysse dj, reynolds cf, monk th, berman sr, kupfer... |
| Q60 | varchar |  |  | SI | The Pittsburgh Sleep Quality Index Score ranges be... |
| Q61 | varchar |  |  | SI | Subjective sleep quality |
| Q62 | varchar |  |  | SI | Sleep latency |
| Q63 | varchar |  |  | SI | Sleep duration |
| Q64 | varchar |  |  | SI | Habitual sleep efficiency |
| Q65 | varchar |  |  | SI | Sleep disturbaces |
| Q66 | varchar |  |  | SI | Use of sleeping medication |
| Q67 | varchar |  |  | SI | Daytime dysfunction |
| Q68 | varchar |  |  | SI | Global PSQI&nbsp;score |
| Q69 | varchar |  |  | SI | Subjective sleep quality |
| Q70 | varchar |  |  | SI | Sleep latency |
| Q71 | varchar |  |  | SI | Sleep duration |
| Q72 | varchar |  |  | SI | Habitual sleep efficiency |
| Q73 | varchar |  |  | SI | Sleep disturbaces |
| Q74 | varchar |  |  | SI | Use of sleeping medication |
| Q75 | varchar |  |  | SI | Daytime dysfunction |
| Q76 | varchar |  |  | SI | Global PSQI&nbsp;score |
| Q77 | varchar |  |  | SI | Component 2 - Sleep Latency |
| Q78 | varchar |  |  | SI | Component 3 - Sleep Duration |
| Q79 | varchar |  |  | SI | Component 4 - Habitual Sleep Efficiency |
| Q80 | varchar |  |  | SI | Component 5 - Sleep Disturbance |
| Q81 | varchar |  |  | SI | Component 6 - Use of Sleeping Medication |
| Q82 | varchar |  |  | SI | Component 7 - Daytime Dysfunction |
| Q83 | varchar |  |  | SI | Component 1 - Subjective Sleep Quality |
| Q84 | varchar |  |  | SI | A score of '0' indicates no difficulty, while a sc... |
| Q85 | varchar |  |  | SI | Sleep latency |
| Q86 | varchar |  |  | SI | 0 |
| Q87 | varchar |  |  | SI | &gt;0 and ≤2 |
| Q88 | varchar |  |  | SI | &gt;2 and ≤4 |
| Q89 | varchar |  |  | SI | &gt;5 |
| Q90 | varchar |  |  | SI | Component Score |
| Q91 | varchar |  |  | SI | 0 |
| Q92 | varchar |  |  | SI | 1 |
| Q93 | varchar |  |  | SI | 2 |
| Q94 | varchar |  |  | SI | 3 |
| Q95 | varchar |  |  | SI | A score of '0' indicates no difficulty, while a sc... |
| Q96 | varchar |  |  | SI | Sleep duration |
| Q97 | varchar |  |  | SI | &gt;7 |
| Q98 | varchar |  |  | SI | &gt;6 and ≤7 |
| Q99 | varchar |  |  | SI | ≥5 and ≤6 |
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