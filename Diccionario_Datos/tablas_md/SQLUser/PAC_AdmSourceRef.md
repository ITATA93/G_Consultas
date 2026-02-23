# SQLUser.PAC_AdmSourceRef

**Schema:** SQLUser
**Columnas:** 180
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADSRF_RowId | bigint | PK |  | NO | - |
| ADSRF_Code | varchar |  |  | NO | Admission Source of Referral Code |
| ADSRF_CreatedDate | date |  |  | SI | Created Date |
| ADSRF_CreatedTime | time |  |  | SI | Created Time |
| ADSRF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADSRF_Desc | varchar |  |  | NO | Admission Source of Referral Description |
| ADSRF_RcFlag | varchar |  |  | SI | Archived Flag |
| ADSRF_UpdatedDate | date |  |  | SI | Updated Date |
| ADSRF_UpdatedTime | time |  |  | SI | Updated Time |
| ADSRF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Time |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | HEEADSSSS (Home Education Eating Activities Drugs ... |
| Q04 | - |  |  | SI | To be completed with 24 hours of admission. |
| Q05 | - |  |  | SI | HEEADSSS adolescent psychological assessment shoul... |
| Q06 | - |  |  | SI | If any concerns or 'Red Flags' with this assessmen... |
| Q07 | - |  |  | SI | Confidentiality explained |
| Q08 | - |  |  | SI | Mandatory reporting explained before commencing as... |
| Q09 | - |  |  | SI | Consent obtained |
| Q10 | - |  |  | SI | Home |
| Q11 | - |  |  | SI | Comments |
| Q11a | - |  |  | SI | Home Comments |
| Q12 | - |  |  | SI | Clinician concerns |
| Q123 | - |  |  | SI | Item |
| Q124 | - |  |  | SI | Comments |
| Q125 | - |  |  | SI | Clinician concerns |
| Q126 | - |  |  | SI | Actions |
| Q127 | - |  |  | SI | HEEADSSS - A Psychosocial Interview Format for Ado... |
| Q128 | - |  |  | SI | 1. Klein, Goldenring JM, Adelman. HEEADSSS 3.0: Th... |
| Q129 | - |  |  | SI | <https://www.contemporarypediatrics.com/view/heead... |
| Q12a | - |  |  | SI | Home clinician concerns |
| Q13 | - |  |  | SI | Actions |
| Q130 | - |  |  | SI | 2. Goldenring JM, Cohen E. Getting into adolescent... |
| Q13a | - |  |  | SI | Home actions |
| Q14 | - |  |  | SI | Education / Employment |
| Q15 | - |  |  | SI | Comments |
| Q15a | - |  |  | SI | Education / Employment comments |
| Q16 | - |  |  | SI | Clinician concerns |
| Q16a | - |  |  | SI | Education / Employment clinician concerns |
| Q17 | - |  |  | SI | Actions |
| Q17a | - |  |  | SI | Education / Employment actions |
| Q18 | - |  |  | SI | Eating / Exercise |
| Q19 | - |  |  | SI | Comments |
| Q19a | - |  |  | SI | Eating / Exercise comments |
| Q20 | - |  |  | SI | Clinician concerns |
| Q20a | - |  |  | SI | Eating / Exercise clinician concerns |
| Q21 | - |  |  | SI | Actions |
| Q21a | - |  |  | SI | Eating / Exercise actions |
| Q22 | - |  |  | SI | Activities and Peer Relationships |
| Q23 | - |  |  | SI | Comments |
| Q23a | - |  |  | SI | Activities and Peer Relationships comments |
| Q24 | - |  |  | SI | Clinician concerns |
| Q24a | - |  |  | SI | Activities and Peer Relationships clinician concer... |
| Q25 | - |  |  | SI | Actions |
| Q25a | - |  |  | SI | Activities and Peer Relationships actions |
| Q26 | - |  |  | SI | Drugs / Cigarettes / Alcohol |
| Q27 | - |  |  | SI | Comments |
| Q27a | - |  |  | SI | Drugs / Cigarettes / Alcohol comments |
| Q28 | - |  |  | SI | Clinician concerns |
| Q28a | - |  |  | SI | Drugs / Cigarettes / Alcohol clinician concerns |
| Q29 | - |  |  | SI | Actions |
| Q29a | - |  |  | SI | Drugs / Cigarettes / Alcohol actions |
| Q30 | - |  |  | SI | Sexuality |
| Q31 | - |  |  | SI | Comments |
| Q31a | - |  |  | SI | Sexuality  comments |
| Q32 | - |  |  | SI | Clinician concerns |
| Q32a | - |  |  | SI | Sexuality  clinician concerns |
| Q33 | - |  |  | SI | Actions |
| Q33a | - |  |  | SI | Sexuality  actions |
| Q34 | - |  |  | SI | Suicide / Depression / Mood Screen |
| Q35 | - |  |  | SI | Comments |
| Q35a | - |  |  | SI | Suicide / Depression / Mood Screen comments |
| Q36 | - |  |  | SI | Clinician concerns |
| Q36a | - |  |  | SI | Suicide / Depression / Mood Screen clinician conce... |
| Q37 | - |  |  | SI | Actions |
| Q37a | - |  |  | SI | Suicide / Depression / Mood Screen actions |
| Q38 | - |  |  | SI | Safety |
| Q39 | - |  |  | SI | Comments |
| Q39a | - |  |  | SI | Safety  comments |
| Q40 | - |  |  | SI | Clinician concerns |
| Q40a | - |  |  | SI | Safety  clinician concerns |
| Q41 | - |  |  | SI | Actions |
| Q41a | - |  |  | SI | Safety  actions |
| Q42 | - |  |  | SI | Spirituality |
| Q43 | - |  |  | SI | Comments |
| Q43a | - |  |  | SI | Spirituality  comments |
| Q44 | - |  |  | SI | Clinician concerns |
| Q44a | - |  |  | SI | Spirituality  clinician concerns |
| Q45 | - |  |  | SI | Actions |
| Q45a | - |  |  | SI | Spirituality  actions |
| Q46 | - |  |  | SI | Guidelines |
| Q47 | - |  |  | SI | The HEADSS mnemonic forms the basis for an assessm... |
| Q48 | - |  |  | SI | H – Home Environment |
| Q49 | - |  |  | SI | Where do you live? |
| Q50 | - |  |  | SI | Who lives with you? |
| Q51 | - |  |  | SI | How does each member get along? |
| Q52 | - |  |  | SI | Who could you go to if you needed help with a prob... |
| Q53 | - |  |  | SI | Parent(s) jobs? Recent moves? Run away? New people... |
| Q54 | - |  |  | SI | E - Education / Employment |
| Q55 | - |  |  | SI | What do you like / not like about school/work? |
| Q56 | - |  |  | SI | What can you do well / what areas would you like t... |
| Q57 | - |  |  | SI | How do you get along with teachers / other student... |
| Q58 | - |  |  | SI | Grades, suspensions? Changes? |
| Q59 | - |  |  | SI | Many young people experience bullying at school – ... |
| Q60 | - |  |  | SI | Sometimes when people are stressed they can over e... |
| Q61 | - |  |  | SI | In general, what is your diet like? |
| Q62 | - |  |  | SI | In screening more specifically for eating disorder... |
| Q63 | - |  |  | SI | A - Activities and Peer Relationships |
| Q64 | - |  |  | SI | With peers? (What do you do for fun? Where? When?) |
| Q65 | - |  |  | SI | With family? |
| Q66 | - |  |  | SI | Sports – regular exercise? |
| Q67 | - |  |  | SI | Hobbies? Tell me about the parties you go to. |
| Q68 | - |  |  | SI | How much TV would you watch a night? Favourite mus... |
| Q69 | - |  |  | SI | Crimes? Arrests? |
| Q70 | - |  |  | SI | D - Drugs / Cigarettes / Alcohol |
| Q71 | - |  |  | SI | Many people at your age are starting to experiment... |
| Q72 | - |  |  | SI | Have any of your friends tried these or maybe othe... |
| Q73 | - |  |  | SI | How about you, have you tried any? Then ask about ... |
| Q74 | - |  |  | SI | How much are they taking, how often and has freque... |
| Q75 | - |  |  | SI | S - Sexuality |
| Q76 | - |  |  | SI | Some people are getting involved in sexual relatio... |
| Q77 | - |  |  | SI | Degree and types of sexual experience |
| Q78 | - |  |  | SI | Number of partners |
| Q79 | - |  |  | SI | Masturbation |
| Q80 | - |  |  | SI | Contraception? |
| Q81 | - |  |  | SI | Knowledge about STDs |
| Q82 | - |  |  | SI | Has anyone ever touched you in a way that’s made y... |
| Q83 | - |  |  | SI | How do you feel about relationships in general / a... |
| Q84 | - |  |  | SI | S - Suicide / Depression / Mood Screen |
| Q85 | - |  |  | SI | How do you feel in yourself at the moment on a sca... |
| Q86 | - |  |  | SI | What sort of things do you do if you are feeling s... |
| Q87 | - |  |  | SI | Is there anyone you can talk to? |
| Q88 | - |  |  | SI | Do you feel this way often? |
| Q89 | - |  |  | SI | Some people who feel really down often feel like h... |
| Q90 | - |  |  | SI | Have you ever tried to hurt yourself or take your ... |
| Q91 | - |  |  | SI | Have you a plan… etc. |
| Q92 | - |  |  | SI | S - Safety |
| Q93 | - |  |  | SI | Sun protection, immunisation, bullying, carrying w... |
| Q94 | - |  |  | SI | S - Spirituality |
| Q95 | - |  |  | SI | Beliefs, religion, music, what helps them relax, e... |
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