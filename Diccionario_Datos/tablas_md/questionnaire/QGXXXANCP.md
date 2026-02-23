# questionnaire.QGXXXANCP

> Angio Nursing Care Plan

**Schema:** questionnaire
**Columnas:** 139
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Angio Nursing Care Plan

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Clinical Observations |
| Q02 | bit |  |  | SI | Core Observaitons |
| Q03 | varchar |  |  | SI | Frequency |
| Q04 | varchar |  |  | SI | Core Obs Freq |
| Q05 | bit |  |  | SI | Neurovascular |
| Q06 | varchar |  |  | SI | Nuerov freq |
| Q07 | bit |  |  | SI | Neurological |
| Q08 | varchar |  |  | SI | neurological freq |
| Q09 | bit |  |  | SI | Cardiac Monitoring |
| Q10 | varchar |  |  | SI | Cardiac Monitoring Freq |
| Q100 | varchar |  |  | SI | Pain Management |
| Q11 | bit |  |  | SI | BSL  |
| Q12 | varchar |  |  | SI | BSL freq |
| Q13 | varchar |  |  | SI | ECG freq |
| Q14 | varchar |  |  | SI | Pre Op |
| Q15 | varchar |  |  | SI | Post Op |
| Q16 | varchar |  |  | SI | Nutrition / Hydration |
| Q17 | bit |  |  | SI | NBM |
| Q18 | varchar |  |  | SI | Falls Risk  |
| Q19 | bit |  |  | SI | Falls Risk Screening Attended |
| Q20 | bit |  |  | SI | All patients treated as high risk |
| Q21 | varchar |  |  | SI | Pressure Injury Risk Screening Attended  |
| Q22 | bit |  |  | SI | Pressure Injury Risk Screening Attended  |
| Q23 | bit |  |  | SI | Vital Signs |
| Q24 | varchar |  |  | SI | vs freq |
| Q25 | bit |  |  | SI | Core Observations |
| Q26po | varchar |  |  | SI | Core obs freq |
| Q27po | bit |  |  | SI | Neurovascular |
| Q28po | varchar |  |  | SI | Neurov freq |
| Q29po | bit |  |  | SI | Neurological |
| Q30po | varchar |  |  | SI | Neuro freq |
| Q31po | bit |  |  | SI | Cardiac Monitoring |
| Q32po | varchar |  |  | SI | cardiac freq |
| Q33po | bit |  |  | SI | BSL |
| Q34po | varchar |  |  | SI | BSL freq |
| Q35 | bit |  |  | SI | ECG |
| Q36po | varchar |  |  | SI | ECG freq |
| Q37 | bit |  |  | SI | Confirm diet / fluid  restrictions / sip test |
| Q38 | bit |  |  | SI | Food and Fluids Given |
| Q39 | varchar |  |  | SI | Adhere to falls strategies |
| Q40 | bit |  |  | SI | Bed low and bed rails up when unattended |
| Q41 | bit |  |  | SI | Assist / escort when ambulating & toileting |
| Q42 | bit |  |  | SI | Ensure appropriate footwwear |
| Q43 | bit |  |  | SI | Call bell within reach |
| Q44 | bit |  |  | SI | Pressure Injury Risk Screening Attended  |
| Q45 | bit |  |  | SI | ECG |
| Q46po | varchar |  |  | SI | Clinical Observations |
| Q47 | varchar |  |  | SI | Frequency  |
| Q48 | varchar |  |  | SI | Mobility  |
| Q49 | bit |  |  | SI | As Desired |
| Q50po | bit |  |  | SI | 30 Degrees |
| Q51 | varchar |  |  | SI | 30d Freq |
| Q52po | bit |  |  | SI | Upright in bed |
| Q53 | varchar |  |  | SI | uprigh in bed freq |
| Q54po | bit |  |  | SI | Sit in chair |
| Q55 | varchar |  |  | SI | sit in chairfreq |
| Q56po | bit |  |  | SI | Ambulate |
| Q57 | varchar |  |  | SI | ambulate pofreq |
| Q58 | varchar |  |  | SI | Pain Management Schedule |
| Q59 | bit |  |  | SI | Pain Score Attended on Admission |
| Q60po | bit |  |  | SI | Pain score on return to ward - review as necessary |
| Q61po | bit |  |  | SI | Analgesia as prescribed |
| Q62po | time |  |  | SI | an eat and drink at |
| Q63 | time |  |  | SI | Time food & fluids goven |
| Q64 | varchar |  |  | SI | VTE Assessment Completed  |
| Q65po | varchar |  |  | SI | VTE Assessment Completed Post OP |
| Q66 | bit |  |  | SI | Pressure injury risk screening attended |
| Q67 | numeric |  |  | SI | WaterlowScore |
| Q68po | numeric |  |  | SI | Waterlow Score Post Op |
| Q69po | bit |  |  | SI | Confirm pressure areas are intact |
| Q70po | bit |  |  | SI | Mobilise when able |
| Q71 | varchar |  |  | SI | Elimination |
| Q72 | bit |  |  | SI | Confirm patient has passed urine pre-op |
| Q73po | bit |  |  | SI | Confirm patinet has passed urine post-op |
| Q74 | varchar |  |  | SI | Elimination Notes Pre Op |
| Q75po | varchar |  |  | SI | Elimination Notes Post Op |
| Q76 | varchar |  |  | SI | Cannula |
| Q77 | bit |  |  | SI | Document cannula insertion |
| Q78po | bit |  |  | SI | Check cannula site hourly |
| Q79 | bit |  |  | SI | Check for signs of fluid infiltration |
| Q80po | bit |  |  | SI | No cannula inserted |
| Q81po | bit |  |  | SI | Removed cannula prior to discharge |
| Q82 | varchar |  |  | SI | Wound / Puncture site care |
| Q83 | bit |  |  | SI | Note anypre-existing wound / skin problems on admi... |
| Q84po | varchar |  |  | SI | Wound / Puncture site care |
| Q86 | varchar |  |  | SI | Discharge PLanning |
| Q87 | bit |  |  | SI | Planned transfer to ward post op |
| Q89 | varchar |  |  | SI | NOK / Escort Name |
| Q90 | varchar |  |  | SI | Contact No. |
| Q91 | varchar |  |  | SI | Contact at end of procedure |
| Q92 | varchar |  |  | SI | Transport Home |
| Q93 | time |  |  | SI | Planned Discharge Time |
| Q94 | bit |  |  | SI | NOK / Escort Aware |
| Q95 | bit |  |  | SI | Discharge documentation given to patient |
| Q96 | bit |  |  | SI | Belongings and X-rays given to patient |
| Q97 | varchar |  |  | SI | Confirm pressure areas are intact |
| Q98 | varchar |  |  | SI | Pressure Injury Risk Screening Attended  |
| Q99 | varchar |  |  | SI | Pressure Injury |
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