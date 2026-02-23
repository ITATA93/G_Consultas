# questionnaire.QTCSQ

> Sleep Questionnaire

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Sleep Questionnaire

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | The following questions relate to your usual sleep... |
| Q02 | time |  |  | SI | What time have You usually gone to bed at night? |
| Q03 | numeric |  |  | SI | How long (in minutes) has it usually taken you to ... |
| Q04 | time |  |  | SI | What time have you usually gotten up in the mornin... |
| Q05 | numeric |  |  | SI | How many hours of actual sleep did you get at nigh... |
| Q06 | numeric |  |  | SI | How many times do you wake up with palpitation? |
| Q07 | numeric |  |  | SI | How many times do you wake up with choking or acid... |
| Q08 | numeric |  |  | SI | How many times do you wake up with chest pain? |
| Q09 | numeric |  |  | SI | How many times do you wake up with difficulty brea... |
| Q10 | varchar |  |  | SI | Daytime behavior |
| Q11 | varchar |  |  | SI | How long have you had the sleepiness problem? |
| Q12 | varchar |  |  | SI | Does your sleepiness affect your work? |
| Q13 | varchar |  |  | SI | Do you have memory problem? |
| Q14 | varchar |  |  | SI | Do you have difficulty in concentration? |
| Q15 | varchar |  |  | SI | How many times have you had car accident during dr... |
| Q16 | varchar |  |  | SI | Do you take a nap ( how many times and for how lon... |
| Q17 | varchar |  |  | SI | Do you have difficulty breathing through the nose |
| Q18 | varchar |  |  | SI | How many cup of coffee, tea or soft drink do you h... |
| Q19 | varchar |  |  | SI | If you have a roommate or bed partner, ask him/ he... |
| Q20 | varchar |  |  | SI | Loud snoring |
| Q21 | varchar |  |  | SI | Long pauses between breaths while asleep |
| Q22 | varchar |  |  | SI | Legs twitching or jerking while asleep |
| Q23 | varchar |  |  | SI | Episodes of disorientation or confusion during sle... |
| Q24 | varchar |  |  | SI | Other restlessness while you sleep; please describ... |
| Q25 | varchar |  |  | SI | How many times did this happen during the past mon... |
| Q26 | varchar |  |  | SI | Restless Leg syndrome |
| Q27 | varchar |  |  | SI | During the past month, have you had the following ... |
| Q28 | varchar |  |  | SI | Had trouble sleeping because you felt an urge to m... |
| Q29 | varchar |  |  | SI | You felt the urge to move, or unpleasant sensation... |
| Q30 | varchar |  |  | SI | You felt the urge to move, or unpleasant sensation... |
| Q31 | varchar |  |  | SI | You felt the urge to move, or unpleasant sensation... |
| Q32 | varchar |  |  | SI | Any similar family history? |
| Q33 | varchar |  |  | SI | Interpretation	 |
| Q34 | varchar |  |  | SI | Restless Leg syndrome |
| Q35 | varchar |  |  | SI | Symptoms suggestive of narcolepsy |
| Q36 | varchar |  |  | SI | Do you ever wake up and feel paralyzed? |
| Q37 | varchar |  |  | SI | When you are angry, excited, or laughing, do you f... |
| Q38 | varchar |  |  | SI | During sleep do you experience dreams and dream en... |
| Q39 | varchar |  |  | SI | Do you have auditory or visual hallucination when ... |
| Q40 | varchar |  |  | SI | Please check whether a doctor has told you that yo... |
| Q41 | varchar |  |  | SI | Emphysema or COPD |
| Q42 | varchar |  |  | SI | Chronic bronchitis or asthma |
| Q43 | varchar |  |  | SI | Allergic rhinitis |
| Q44 | varchar |  |  | SI | Angina or coronary heart disease or arterioscleros... |
| Q45 | varchar |  |  | SI | Heart attack |
| Q46 | varchar |  |  | SI | Stroke |
| Q47 | varchar |  |  | SI | Hypertension or high blood pressure |
| Q48 | varchar |  |  | SI | Diabetes |
| Q49 | varchar |  |  | SI | Hypothyroidism |
| Q50 | varchar |  |  | SI | Mention if there is another diagnosis |
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