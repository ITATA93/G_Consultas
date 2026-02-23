# SQLUser.MR_Encounter

**Schema:** SQLUser
**Columnas:** 164
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ENC_RowId | bigint | PK |  | NO | - |
| ChildQ85DR | - |  |  | SI | Child Reference: TR Band time |
| ENC_Appt_DR | varchar |  | FK | SI | only used for outpatient encounters -> a new encou... |
| ENC_CareProv_DR | varchar |  | FK | SI | saves the care Provider of the encounter
Note: en... |
| ENC_Contact_DR | bigint |  | FK | SI | only used for community contact encounters -> a ne... |
| ENC_EncounterType | varchar |  |  | SI | Encounter type standard type |
| ENC_EndDate | date |  |  | SI | end date of encounter |
| ENC_EndTime | time |  |  | SI | end time of encounter |
| ENC_Loc_DR | bigint |  | FK | SI | saves the location ID of the encounter
Note: enco... |
| ENC_MRAdm_DR | bigint |  | FK | SI | mradm the encounter belongs to
dependent on the e... |
| ENC_RBOperatingRoom_DR | bigint |  | FK | SI | Used for OT Type Encounters.
OT Encounters to rem... |
| ENC_StartDate | date |  |  | SI | start date of encounter |
| ENC_StartTime | time |  |  | SI | start time of encounter |
| ENC_Transaction_DR | varchar |  | FK | SI | only used for inpatient encounters -> a new encoun... |
| Q01 | - |  |  | SI | Clinical Observations |
| Q02 | - |  |  | SI | Core Observaitons |
| Q03 | - |  |  | SI | Frequency |
| Q04 | - |  |  | SI | Core Obs Freq |
| Q05 | - |  |  | SI | Neurovascular |
| Q06 | - |  |  | SI | Nuerov freq |
| Q07 | - |  |  | SI | Neurological |
| Q08 | - |  |  | SI | neurological freq |
| Q09 | - |  |  | SI | Cardiac Monitoring |
| Q10 | - |  |  | SI | Cardiac Monitoring Freq |
| Q100 | - |  |  | SI | Bowel Prep Taken |
| Q101 | - |  |  | SI | On Return To Ward |
| Q102 | - |  |  | SI | Prior to D/C |
| Q103 | - |  |  | SI | Catheter-Drain Insitu |
| Q104 | - |  |  | SI | Trial of Void Required |
| Q105 | - |  |  | SI | Pre Exisitng Wound or Skin Condition |
| Q106 | - |  |  | SI | Transfer to Ward Required |
| Q107 | - |  |  | SI | Post Op Ward |
| Q108 | - |  |  | SI | Tolerating Fluid |
| Q109 | - |  |  | SI | Bed low and bed rails up when unattended |
| Q11 | - |  |  | SI | BSL |
| Q110 | - |  |  | SI | Assist / escort when ambulating & toileting |
| Q111 | - |  |  | SI | Ensure appropriate footwwear |
| Q112 | - |  |  | SI | Call bell within reach |
| Q12 | - |  |  | SI | BSL freq |
| Q13 | - |  |  | SI | ECG freq |
| Q14 | - |  |  | SI | Pre Op |
| Q15 | - |  |  | SI | Post Op |
| Q16 | - |  |  | SI | Nutrition / Hydration |
| Q17 | - |  |  | SI | NBM |
| Q18 | - |  |  | SI | Falls Risk |
| Q19 | - |  |  | SI | Adhere to Falls Risk Strategy |
| Q20 | - |  |  | SI | All patients treated as high risk |
| Q21 | - |  |  | SI | Pressure Injury Risk |
| Q22 | - |  |  | SI | Bed Rest |
| Q23 | - |  |  | SI | Vital Signs |
| Q24 | - |  |  | SI | vs freq |
| Q25 | - |  |  | SI | Core Observations |
| Q26po | - |  |  | SI | Core obs freq |
| Q27po | - |  |  | SI | Neurovascular |
| Q28po | - |  |  | SI | Neurov freq |
| Q29po | - |  |  | SI | Neurological |
| Q30po | - |  |  | SI | Neuro freq |
| Q31po | - |  |  | SI | Cardiac Monitoring |
| Q32po | - |  |  | SI | cardiac freq |
| Q33po | - |  |  | SI | BSL |
| Q34po | - |  |  | SI | BSL freq |
| Q35 | - |  |  | SI | ECG |
| Q36po | - |  |  | SI | ECG freq |
| Q37 | - |  |  | SI | Tolerating Food |
| Q38 | - |  |  | SI | Food and Fluids Given |
| Q39 | - |  |  | SI | Adhere to falls strategies |
| Q40 | - |  |  | SI | Post Op Ward |
| Q41 | - |  |  | SI | Transfer to Ward Required |
| Q42 | - |  |  | SI | Ensure appropriate footwwear |
| Q43 | - |  |  | SI | Review Required |
| Q44 | - |  |  | SI | Pressure Area Intact |
| Q45 | - |  |  | SI | ECG |
| Q46po | - |  |  | SI | Clinical Observations |
| Q47 | - |  |  | SI | Frequency |
| Q48 | - |  |  | SI | Mobility |
| Q49 | - |  |  | SI | Patient Mobility and Transfer Risk Assessment Comp... |
| Q50po | - |  |  | SI | Mobility changed from Admission |
| Q51 | - |  |  | SI | 30d Freq |
| Q52po | - |  |  | SI | Physiotherapy Assessment |
| Q53 | - |  |  | SI | uprigh in bed freq |
| Q54po | - |  |  | SI | Pre-Op Checklist Completed |
| Q55 | - |  |  | SI | sit in chairfreq |
| Q56po | - |  |  | SI | Special Dietary Requirements |
| Q57 | - |  |  | SI | ambulate pofreq |
| Q58 | - |  |  | SI | Pain Management Schedule |
| Q59 | - |  |  | SI | Pain Score Attended on Admission |
| Q60po | - |  |  | SI | Pain score on return to ward - review as necessary |
| Q61po | - |  |  | SI | Analgesia as prescribed |
| Q62po | - |  |  | SI | an eat and drink at |
| Q63 | - |  |  | SI | Time food & fluids goven |
| Q64 | - |  |  | SI | VTE Assessment Completed |
| Q65po | - |  |  | SI | VTE Assessment Completed Post OP |
| Q66 | - |  |  | SI | Pressure injury risk screening attended |
| Q67 | - |  |  | SI | WaterlowScore Completed |
| Q68po | - |  |  | SI | Waterlow Score Post Op Completed |
| Q69po | - |  |  | SI | Confirm pressure areas are intact |
| Q70po | - |  |  | SI | Bed Rest |
| Q71 | - |  |  | SI | Elimination |
| Q72 | - |  |  | SI | Confirm patient has passed urine pre-op |
| Q73po | - |  |  | SI | Fluid Loss Documented |
| Q74 | - |  |  | SI | Nutrition & Hydration Notes |
| Q75po | - |  |  | SI | Nutrition Notes |
| Q76 | - |  |  | SI | Cannula |
| Q77 | - |  |  | SI | Cannula inserted in DSU |
| Q78po | - |  |  | SI | Check cannula site hourly |
| Q79 | - |  |  | SI | Check for signs of fluid infiltration |
| Q80po | - |  |  | SI | No cannula inserted |
| Q81po | - |  |  | SI | Removed cannula prior to discharge |
| Q82 | - |  |  | SI | Wound / Puncture site care |
| Q83 | - |  |  | SI | Note anypre-existing wound / skin problems on admi... |
| Q84po | - |  |  | SI | Wound / Puncture site care |
| Q86 | - |  |  | SI | Discharge PLanning |
| Q87 | - |  |  | SI | Planned transfer to ward post op |
| Q89 | - |  |  | SI | NOK / Escort Name |
| Q90 | - |  |  | SI | Contact No. |
| Q91 | - |  |  | SI | Contact at end of procedure |
| Q92 | - |  |  | SI | Transport Home |
| Q93 | - |  |  | SI | Planned Discharge Time |
| Q94 | - |  |  | SI | Patient's NOK Notified |
| Q95 | - |  |  | SI | Discharge Checklist and MPADDS Completed |
| Q96 | - |  |  | SI | Belongings and X-rays given to patient |
| Q97 | - |  |  | SI | Patient rights & patient journey discussed |
| Q98 | - |  |  | SI | Bowel Prep Notes |
| Q99 | - |  |  | SI | Dressing Dry & Intact |
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