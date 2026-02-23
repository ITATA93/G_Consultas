# SQLUser.PAC_FetalHeartLocation

**Schema:** SQLUser
**Columnas:** 138
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FEHEL_Rowid | bigint | PK |  | NO | - |
| FEHEL_Code | varchar |  |  | NO | Code |
| FEHEL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FEHEL_CreatedDate | date |  |  | SI | Created Date |
| FEHEL_CreatedTime | time |  |  | SI | Created Time |
| FEHEL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FEHEL_DateFrom | date |  |  | SI | Date From |
| FEHEL_DateTo | date |  |  | SI | Date To |
| FEHEL_Desc | varchar |  |  | NO | Description |
| FEHEL_Owner | varchar |  |  | SI | Owner |
| FEHEL_UpdatedDate | date |  |  | SI | Updated Date |
| FEHEL_UpdatedTime | time |  |  | SI | Updated Time |
| FEHEL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | HoNOS rating guidelines |
| Q02 | - |  |  | SI | • Rate items in the order presented below |
| Q03 | - |  |  | SI | • Use all available information in making your rat... |
| Q04 | - |  |  | SI | • Do not include information already rated in an e... |
| Q05 | - |  |  | SI | • Consider both the degree of distress the problem... |
| Q06 | - |  |  | SI | • Rate the most severe problem that occurred in th... |
| Q07 | - |  |  | SI | • The rating period is generally the preceding two... |
| Q08 | - |  |  | SI | • Each item is rated on a five-point item of sever... |
| Q09 | - |  |  | SI | 0 No problem. |
| Q10 | - |  |  | SI | 1 Minor problem requiring no formal action. |
| Q11 | - |  |  | SI | 2 Mild problem. |
| Q12 | - |  |  | SI | 3 Problem of moderate severity. |
| Q13 | - |  |  | SI | 4 Severe to very severe problem. |
| Q14 | - |  |  | SI | 9 Not known or not applicable. |
| Q15 | - |  |  | SI | • As far as possible, the use of rating point 9 sh... |
| Q16 | - |  |  | SI | HoNOS rating guidelines |
| Q17 | - |  |  | SI | • Rate items in order presented below |
| Q18 | - |  |  | SI | • Use all available information in making your rat... |
| Q19 | - |  |  | SI | • Do not include information already rated in an e... |
| Q20 | - |  |  | SI | • Consider both the degree of distress the problem... |
| Q21 | - |  |  | SI | • Rate the most severe problem that occurred in th... |
| Q22 | - |  |  | SI | • The rating period is generally the preceding two... |
| Q23 | - |  |  | SI | • Each item is rated on a five-point item of sever... |
| Q24 | - |  |  | SI | 0 No problem. |
| Q25 | - |  |  | SI | 1 Minor problem requiring no formal action. |
| Q26 | - |  |  | SI | 2 Mild problem. |
| Q27 | - |  |  | SI | 3 Problem of moderate severity. |
| Q28 | - |  |  | SI | 4 Severe to very severe problem. |
| Q29 | - |  |  | SI | 9 Not known or not applicable. |
| Q30 | - |  |  | SI | • As far as possible, the use of rating point 9 sh... |
| Q31 | - |  |  | SI | Overactive, aggressive, disruptive or agitated beh... |
| Q32 | - |  |  | SI | Include such behaviour due to any cause, eg, drugs... |
| Q33 | - |  |  | SI | Do not include bizarre behaviour, rated at scale 6... |
| Q34 | - |  |  | SI | Non-accidental self-injury |
| Q35 | - |  |  | SI | Do not include accidental self-injury (due eg, to ... |
| Q36 | - |  |  | SI | Do not include illness or injury as a direct conse... |
| Q37 | - |  |  | SI | Problem drinking or drug-taking |
| Q38 | - |  |  | SI | Do not include aggressive or destructive behaviour... |
| Q39 | - |  |  | SI | Do not include physical illness or disability due ... |
| Q40 | - |  |  | SI | Cognitive problems |
| Q41 | - |  |  | SI | Include problems of memory, orientation and unders... |
| Q42 | - |  |  | SI | Do not include temporary problems (eg, hangovers) ... |
| Q43 | - |  |  | SI | Physical illness or disability problems |
| Q44 | - |  |  | SI | Include illness or disability from any cause that ... |
| Q45 | - |  |  | SI | Include side-effects from medication |
| Q46 | - |  |  | SI | Do not include mental or behavioural problems rate... |
| Q47 | - |  |  | SI | Problems associated with hallucinations and delusi... |
| Q48 | - |  |  | SI | Include hallucinations and delusions irrespective ... |
| Q49 | - |  |  | SI | Include odd and bizarre behaviour associated with ... |
| Q50 | - |  |  | SI | Do not include aggressive, destructive or overacti... |
| Q51 | - |  |  | SI | Problems with depressed mood |
| Q52 | - |  |  | SI | Do not include over-activity or agitation, rated a... |
| Q53 | - |  |  | SI | Do not include suicidal ideation or attempts, rate... |
| Q54 | - |  |  | SI | Other mental and behavioural problems |
| Q55 | - |  |  | SI | Specify the type of problem: |
| Q56 | - |  |  | SI | Specify the type of problem: |
| Q57 | - |  |  | SI | Specify the type of problem: |
| Q58 | - |  |  | SI | Specify the type of problem: |
| Q59 | - |  |  | SI | Rate only the most severe clinical problem not con... |
| Q60 | - |  |  | SI | A phobic: B anxiety |
| Q61 | - |  |  | SI | Problems with relationships |
| Q62 | - |  |  | SI | Rate the patient’s most severe problem associated ... |
| Q63 | - |  |  | SI | Problems with activities of daily living |
| Q64 | - |  |  | SI | Rate the overall level of functioning in activitie... |
| Q65 | - |  |  | SI | where to live, occupation and recreation, mobility... |
| Q66 | - |  |  | SI | Include any lack of motivation for using self-help... |
| Q67 | - |  |  | SI | Do not include lack of opportunities for exercisin... |
| Q68 | - |  |  | SI | Problems with living conditions |
| Q69 | - |  |  | SI | Rate the overall severity of problems with the qua... |
| Q70 | - |  |  | SI | Are the basic necessities met (heat, light, hygien... |
| Q71 | - |  |  | SI | Do not rate the level of functional disability its... |
| Q72 | - |  |  | SI | NB: Rate patient’s usual accommodation. If in acut... |
| Q73 | - |  |  | SI | Problems with occupation and activities |
| Q74 | - |  |  | SI | Rate the overall level of problems with quality of... |
| Q75 | - |  |  | SI | Consider factors such as stigma, lack of qualified... |
| Q76 | - |  |  | SI | Do not rate the level of functional disability its... |
| Q77 | - |  |  | SI | NB: Rate the patient’s usual situation. If in acut... |
| Q78 | - |  |  | SI | The Health of the Nation Outcome Scales (HoNOS) is... |
| Q79 | - |  |  | SI | HONOS Age Range Is 18 to 64 years |
| Q80 | - |  |  | SI | HONOS is not a diagnostic tool, scores are to comp... |
| Q81 | - |  |  | SI | HONOS is not a diagnostic tool, scores are to comp... |
| Q82 | - |  |  | SI | Score |
| Q83 | - |  |  | SI | Classification |
| Q84 | - |  |  | SI | Do not include delusions or hallucinations, rated ... |
| Q85 | - |  |  | SI | HONOS is not a diagnostic tool, scores are compare... |
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