# SQLUser.OR_AnaestSurgPathwayContrastAgent

**Schema:** SQLUser
**Columnas:** 125
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONAG_ParRef | varchar | PK |  | NO | OR_AnaestSurgPathway Parent Reference |
| CONAG_Amount | varchar |  |  | SI | Amount |
| CONAG_Childsub | double |  |  | NO | Childsub |
| CONAG_ContrastAgent_DR | bigint |  | FK | SI |  Des Ref ORC_ContrastAgent |
| CONAG_RowId | varchar |  |  | NO | - |
| ChildQ80DR | - |  |  | SI | Child Reference: Management Plan |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Fall Record |
| Q04 | - |  |  | SI | Patient admitted to hospital because of a fall |
| Q05 | - |  |  | SI | Fall number&nbsp |
| Q06 | - |  |  | SI | Date of fall |
| Q07 | - |  |  | SI | Time of fall |
| Q08 | - |  |  | SI | Location of fall |
| Q09 | - |  |  | SI | Describe location |
| Q10 | - |  |  | SI | Brief description of patient’s activity at time of... |
| Q11 | - |  |  | SI | Was the patient at risk of falls |
| Q12 | - |  |  | SI | Was the fall witnessed (seen) |
| Q13 | - |  |  | SI | Was patient supervised or assisted at time of the ... |
| Q14 | - |  |  | SI | Who was supervising |
| Q15 | - |  |  | SI | Other person supervising / notes |
| Q16 | - |  |  | SI | Was patient supposed to be supervised |
| Q17 | - |  |  | SI | Was the patient injured by the fall (e.g. bruise, ... |
| Q18 | - |  |  | SI | Description of injury |
| Q19 | - |  |  | SI | Details of injury |
| Q20 | - |  |  | SI | Type of fracture |
| Q21 | - |  |  | SI | Details of fracture |
| Q22 | - |  |  | SI | Was there a change in cognition post fall |
| Q23 | - |  |  | SI | Did a physical hazard cause the fall |
| Q24 | - |  |  | SI | Type of hazard |
| Q25 | - |  |  | SI | Footwear patient was wearing at the time of the fa... |
| Q26 | - |  |  | SI | Other footwear |
| Q27 | - |  |  | SI | Does the patient use a mobility aid |
| Q28 | - |  |  | SI | Other patient aid |
| Q29 | - |  |  | SI | Was the patient using the aid at the time of the f... |
| Q30 | - |  |  | SI | If the patient fell from bed, were bed rails in us... |
| Q31 | - |  |  | SI | Were&nbsp |
| Q32 | - |  |  | SI | If any fall interventions were not in place please... |
| Q33 | - |  |  | SI | Post Fall Management |
| Q34 | - |  |  | SI | Next of kin notified |
| Q35 | - |  |  | SI | Medical review complete / required (e.g. Imaging, ... |
| Q36 | - |  |  | SI | Medical review details |
| Q37 | - |  |  | SI | Allied Health review required |
| Q38 | - |  |  | SI | Allied health review details |
| Q39 | - |  |  | SI | Incident report completed |
| Q40 | - |  |  | SI | Incident number |
| Q41 | - |  |  | SI | Post Fall Huddle Record |
| Q42 | - |  |  | SI | To be completed by huddle leader |
| Q43 | - |  |  | SI | Huddle group leader |
| Q44 | - |  |  | SI | Role |
| Q45 | - |  |  | SI | Notified |
| Q46 | - |  |  | SI | Attended |
| Q47 | - |  |  | SI | Medical officer |
| Q48 | - |  |  | SI | Team leader |
| Q49 | - |  |  | SI | Physiotherapist |
| Q50 | - |  |  | SI | Occupational therapist |
| Q51 | - |  |  | SI | Pharmacist |
| Q52 | - |  |  | SI | Patient Care assistant |
| Q53 | - |  |  | SI | Medical officer notified |
| Q54 | - |  |  | SI | Medical officer&nbsp |
| Q55 | - |  |  | SI | Team leader&nbsp |
| Q56 | - |  |  | SI | Team leader attended |
| Q57 | - |  |  | SI | Physiotherapist&nbsp |
| Q58 | - |  |  | SI | Physiotherapist&nbsp |
| Q59 | - |  |  | SI | OT Therapy&nbsp |
| Q60 | - |  |  | SI | Occ. Therapy&nbsp |
| Q61 | - |  |  | SI | Pharmacist&nbsp |
| Q62 | - |  |  | SI | Pharmacist&nbsp |
| Q63 | - |  |  | SI | Patient care assistant notified |
| Q64 | - |  |  | SI | Patient care assistant attended |
| Q65 | - |  |  | SI | Other group members (if required) |
| Q66 | - |  |  | SI | Patient Account / Education Provided |
| Q67 | - |  |  | SI | Patient's account of the fall (What happened? Why ... |
| Q68 | - |  |  | SI | Fall prevention education provided |
| Q69 | - |  |  | SI | Education provided from |
| Q70 | - |  |  | SI | Other education provided |
| Q71 | - |  |  | SI | Cause of Fall |
| Q72 | - |  |  | SI | e.g. slipped on wet floor, dizzy, tripped on footw... |
| Q73 | - |  |  | SI | Why did the patient fall (cause) |
| Q74 | - |  |  | SI | Reason 1 |
| Q75 | - |  |  | SI | Reason 2 |
| Q76 | - |  |  | SI | Why did that happen |
| Q77 | - |  |  | SI | Reason 1 |
| Q78 | - |  |  | SI | Reason 2 |
| Q79 | - |  |  | SI | Management Plan |
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