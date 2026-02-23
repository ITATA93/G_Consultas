# SQLUser.CT_LocMRRequirements

**Schema:** SQLUser
**Columnas:** 154
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MR_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| ChildQ85DR | - |  |  | SI | Child Reference: TR Band time |
| MR_AllVolumes | varchar |  |  | SI | All Volumes |
| MR_Childsub | double |  |  | NO | Childsub |
| MR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MR_CreatedDate | date |  |  | SI | Created Date |
| MR_CreatedTime | time |  |  | SI | Created Time |
| MR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MR_LastTwoVolumes | varchar |  |  | SI | Last Two Volumes |
| MR_LatestVolumeOnly | varchar |  |  | SI | Latest Volume Only |
| MR_LeadTime | double |  |  | SI | Lead Time |
| MR_RecordType_DR | bigint |  | FK | SI | Des Ref RecordType |
| MR_RowId | varchar |  |  | NO | - |
| MR_UpdatedDate | date |  |  | SI | Updated Date |
| MR_UpdatedTime | time |  |  | SI | Updated Time |
| MR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
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
| Q100 | - |  |  | SI | Pain Management |
| Q11 | - |  |  | SI | BSL |
| Q12 | - |  |  | SI | BSL freq |
| Q13 | - |  |  | SI | ECG freq |
| Q14 | - |  |  | SI | Pre Op |
| Q15 | - |  |  | SI | Post Op |
| Q16 | - |  |  | SI | Nutrition / Hydration |
| Q17 | - |  |  | SI | NBM |
| Q18 | - |  |  | SI | Falls Risk |
| Q19 | - |  |  | SI | Falls Risk Screening Attended |
| Q20 | - |  |  | SI | All patients treated as high risk |
| Q21 | - |  |  | SI | Pressure Injury Risk Screening Attended |
| Q22 | - |  |  | SI | Pressure Injury Risk Screening Attended |
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
| Q37 | - |  |  | SI | Confirm diet / fluid  restrictions / sip test |
| Q38 | - |  |  | SI | Food and Fluids Given |
| Q39 | - |  |  | SI | Adhere to falls strategies |
| Q40 | - |  |  | SI | Bed low and bed rails up when unattended |
| Q41 | - |  |  | SI | Assist / escort when ambulating & toileting |
| Q42 | - |  |  | SI | Ensure appropriate footwwear |
| Q43 | - |  |  | SI | Call bell within reach |
| Q44 | - |  |  | SI | Pressure Injury Risk Screening Attended |
| Q45 | - |  |  | SI | ECG |
| Q46po | - |  |  | SI | Clinical Observations |
| Q47 | - |  |  | SI | Frequency |
| Q48 | - |  |  | SI | Mobility |
| Q49 | - |  |  | SI | As Desired |
| Q50po | - |  |  | SI | 30 Degrees |
| Q51 | - |  |  | SI | 30d Freq |
| Q52po | - |  |  | SI | Upright in bed |
| Q53 | - |  |  | SI | uprigh in bed freq |
| Q54po | - |  |  | SI | Sit in chair |
| Q55 | - |  |  | SI | sit in chairfreq |
| Q56po | - |  |  | SI | Ambulate |
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
| Q67 | - |  |  | SI | WaterlowScore |
| Q68po | - |  |  | SI | Waterlow Score Post Op |
| Q69po | - |  |  | SI | Confirm pressure areas are intact |
| Q70po | - |  |  | SI | Mobilise when able |
| Q71 | - |  |  | SI | Elimination |
| Q72 | - |  |  | SI | Confirm patient has passed urine pre-op |
| Q73po | - |  |  | SI | Confirm patinet has passed urine post-op |
| Q74 | - |  |  | SI | Elimination Notes Pre Op |
| Q75po | - |  |  | SI | Elimination Notes Post Op |
| Q76 | - |  |  | SI | Cannula |
| Q77 | - |  |  | SI | Document cannula insertion |
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
| Q94 | - |  |  | SI | NOK / Escort Aware |
| Q95 | - |  |  | SI | Discharge documentation given to patient |
| Q96 | - |  |  | SI | Belongings and X-rays given to patient |
| Q97 | - |  |  | SI | Confirm pressure areas are intact |
| Q98 | - |  |  | SI | Pressure Injury Risk Screening Attended |
| Q99 | - |  |  | SI | Pressure Injury |
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