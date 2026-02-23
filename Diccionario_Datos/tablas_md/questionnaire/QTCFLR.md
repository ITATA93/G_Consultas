# questionnaire.QTCFLR

> Fall Record

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fall Record

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Fall Record |
| Q04 | varchar |  |  | SI | Patient admitted to hospital because of a fall |
| Q05 | numeric |  |  | SI | Fall number&nbsp;this admission |
| Q06 | date |  |  | SI | Date of fall |
| Q07 | time |  |  | SI | Time of fall |
| Q08 | varchar |  |  | SI | Location of fall |
| Q09 | varchar |  |  | SI | Describe location |
| Q10 | varchar |  |  | SI | Brief description of patient’s activity at time of... |
| Q11 | varchar |  |  | SI | Was the patient at risk of falls |
| Q12 | varchar |  |  | SI | Was the fall witnessed (seen) |
| Q13 | varchar |  |  | SI | Was patient supervised or assisted at time of the ... |
| Q14 | varchar |  |  | SI | Who was supervising |
| Q15 | varchar |  |  | SI | Other person supervising / notes |
| Q16 | varchar |  |  | SI | Was patient supposed to be supervised |
| Q17 | varchar |  |  | SI | Was the patient injured by the fall (e.g. bruise, ... |
| Q18 | varchar |  |  | SI | Description of injury |
| Q19 | varchar |  |  | SI | Details of injury |
| Q20 | varchar |  |  | SI | Type of fracture |
| Q21 | varchar |  |  | SI | Details of fracture |
| Q22 | varchar |  |  | SI | Was there a change in cognition post fall |
| Q23 | varchar |  |  | SI | Did a physical hazard cause the fall |
| Q24 | varchar |  |  | SI | Type of hazard |
| Q25 | varchar |  |  | SI | Footwear patient was wearing at the time of the fa... |
| Q26 | varchar |  |  | SI | Other footwear |
| Q27 | varchar |  |  | SI | Does the patient use a mobility aid |
| Q28 | varchar |  |  | SI | Other patient aid |
| Q29 | varchar |  |  | SI | Was the patient using the aid at the time of the f... |
| Q30 | varchar |  |  | SI | If the patient fell from bed, were bed rails in us... |
| Q31 | varchar |  |  | SI | Were&nbsp;ALL&nbsp;fall prevention strategies in p... |
| Q32 | varchar |  |  | SI | If any fall interventions were not in place please... |
| Q33 | varchar |  |  | SI | Post Fall Management |
| Q34 | varchar |  |  | SI | Next of kin notified |
| Q35 | varchar |  |  | SI | Medical review complete / required (e.g. Imaging, ... |
| Q36 | varchar |  |  | SI | Medical review details |
| Q37 | varchar |  |  | SI | Allied Health review required |
| Q38 | varchar |  |  | SI | Allied health review details |
| Q39 | varchar |  |  | SI | Incident report completed |
| Q40 | varchar |  |  | SI | Incident number |
| Q41 | varchar |  |  | SI | Post Fall Huddle Record |
| Q42 | varchar |  |  | SI | To be completed by huddle leader |
| Q43 | varchar |  |  | SI | Huddle group leader |
| Q44 | varchar |  |  | SI | Role |
| Q45 | varchar |  |  | SI | Notified |
| Q46 | varchar |  |  | SI | Attended |
| Q47 | varchar |  |  | SI | Medical officer |
| Q48 | varchar |  |  | SI | Team leader |
| Q49 | varchar |  |  | SI | Physiotherapist |
| Q50 | varchar |  |  | SI | Occupational therapist |
| Q51 | varchar |  |  | SI | Pharmacist |
| Q52 | varchar |  |  | SI | Patient Care assistant |
| Q53 | varchar |  |  | SI | Medical officer notified |
| Q54 | varchar |  |  | SI | Medical officer&nbsp;attended |
| Q55 | varchar |  |  | SI | Team leader&nbsp;notified |
| Q56 | varchar |  |  | SI | Team leader attended |
| Q57 | varchar |  |  | SI | Physiotherapist&nbsp;notified |
| Q58 | varchar |  |  | SI | Physiotherapist&nbsp;attended |
| Q59 | varchar |  |  | SI | OT Therapy&nbsp;notified |
| Q60 | varchar |  |  | SI | Occ. Therapy&nbsp;attended |
| Q61 | varchar |  |  | SI | Pharmacist&nbsp;notified |
| Q62 | varchar |  |  | SI | Pharmacist&nbsp;attended |
| Q63 | varchar |  |  | SI | Patient care assistant notified |
| Q64 | varchar |  |  | SI | Patient care assistant attended |
| Q65 | varchar |  |  | SI | Other group members (if required) |
| Q66 | varchar |  |  | SI | Patient Account / Education Provided |
| Q67 | varchar |  |  | SI | Patient's account of the fall (What happened? Why ... |
| Q68 | varchar |  |  | SI | Fall prevention education provided |
| Q69 | varchar |  |  | SI | Education provided from |
| Q70 | varchar |  |  | SI | Other education provided |
| Q71 | varchar |  |  | SI | Cause of Fall |
| Q72 | varchar |  |  | SI | e.g. slipped on wet floor, dizzy, tripped on footw... |
| Q73 | varchar |  |  | SI | Why did the patient fall (cause) |
| Q74 | varchar |  |  | SI | Reason 1 |
| Q75 | varchar |  |  | SI | Reason 2 |
| Q76 | varchar |  |  | SI | Why did that happen |
| Q77 | varchar |  |  | SI | Reason 1 |
| Q78 | varchar |  |  | SI | Reason 2 |
| Q79 | varchar |  |  | SI | Management Plan |
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