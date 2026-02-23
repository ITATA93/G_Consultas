# SQLUser.PA_AdmCnt

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACNT_RowID1 | double | PK |  | NO | - |
| ACNT_EMCnt | double |  |  | SI | Emergency Counter |
| ACNT_IPCnt | double |  |  | SI | In Patient Counter |
| ACNT_OPCnt | double |  |  | SI | Out Patient Counter |
| ACNT_PACnt | double |  |  | SI | Pre Admission Counter |
| ACNT_RowID | double |  |  | NO | PA_AdmCnt Row ID |
| Q01 | - |  |  | SI | The following questions relate to your usual sleep... |
| Q02 | - |  |  | SI | What time have You usually gone to bed at night? |
| Q03 | - |  |  | SI | How long (in minutes) has it usually taken you to ... |
| Q04 | - |  |  | SI | What time have you usually gotten up in the mornin... |
| Q05 | - |  |  | SI | How many hours of actual sleep did you get at nigh... |
| Q06 | - |  |  | SI | How many times do you wake up with palpitation? |
| Q07 | - |  |  | SI | How many times do you wake up with choking or acid... |
| Q08 | - |  |  | SI | How many times do you wake up with chest pain? |
| Q09 | - |  |  | SI | How many times do you wake up with difficulty brea... |
| Q10 | - |  |  | SI | Daytime behavior |
| Q11 | - |  |  | SI | How long have you had the sleepiness problem? |
| Q12 | - |  |  | SI | Does your sleepiness affect your work? |
| Q13 | - |  |  | SI | Do you have memory problem? |
| Q14 | - |  |  | SI | Do you have difficulty in concentration? |
| Q15 | - |  |  | SI | How many times have you had car accident during dr... |
| Q16 | - |  |  | SI | Do you take a nap ( how many times and for how lon... |
| Q17 | - |  |  | SI | Do you have difficulty breathing through the nose |
| Q18 | - |  |  | SI | How many cup of coffee, tea or soft drink do you h... |
| Q19 | - |  |  | SI | If you have a roommate or bed partner, ask him/ he... |
| Q20 | - |  |  | SI | Loud snoring |
| Q21 | - |  |  | SI | Long pauses between breaths while asleep |
| Q22 | - |  |  | SI | Legs twitching or jerking while asleep |
| Q23 | - |  |  | SI | Episodes of disorientation or confusion during sle... |
| Q24 | - |  |  | SI | Other restlessness while you sleep |
| Q25 | - |  |  | SI | How many times did this happen during the past mon... |
| Q26 | - |  |  | SI | Restless Leg syndrome |
| Q27 | - |  |  | SI | During the past month, have you had the following ... |
| Q28 | - |  |  | SI | Had trouble sleeping because you felt an urge to m... |
| Q29 | - |  |  | SI | You felt the urge to move, or unpleasant sensation... |
| Q30 | - |  |  | SI | You felt the urge to move, or unpleasant sensation... |
| Q31 | - |  |  | SI | You felt the urge to move, or unpleasant sensation... |
| Q32 | - |  |  | SI | Any similar family history? |
| Q33 | - |  |  | SI | Interpretation	 |
| Q34 | - |  |  | SI | Restless Leg syndrome |
| Q35 | - |  |  | SI | Symptoms suggestive of narcolepsy |
| Q36 | - |  |  | SI | Do you ever wake up and feel paralyzed? |
| Q37 | - |  |  | SI | When you are angry, excited, or laughing, do you f... |
| Q38 | - |  |  | SI | During sleep do you experience dreams and dream en... |
| Q39 | - |  |  | SI | Do you have auditory or visual hallucination when ... |
| Q40 | - |  |  | SI | Please check whether a doctor has told you that yo... |
| Q41 | - |  |  | SI | Emphysema or COPD |
| Q42 | - |  |  | SI | Chronic bronchitis or asthma |
| Q43 | - |  |  | SI | Allergic rhinitis |
| Q44 | - |  |  | SI | Angina or coronary heart disease or arterioscleros... |
| Q45 | - |  |  | SI | Heart attack |
| Q46 | - |  |  | SI | Stroke |
| Q47 | - |  |  | SI | Hypertension or high blood pressure |
| Q48 | - |  |  | SI | Diabetes |
| Q49 | - |  |  | SI | Hypothyroidism |
| Q50 | - |  |  | SI | Mention if there is another diagnosis |
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