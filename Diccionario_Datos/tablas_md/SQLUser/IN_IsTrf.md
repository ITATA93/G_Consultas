# SQLUser.IN_IsTrf

**Schema:** SQLUser
**Columnas:** 152
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INIT_RowId | bigint | PK |  | NO | - |
| INIT_AckDate | date |  |  | NO | Acknowledge date |
| INIT_AckDateLastUpdated | date |  |  | SI | DateLastUpdated |
| INIT_AckTime | time |  |  | NO | Acknowledge Time |
| INIT_AckTimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| INIT_AckUserLastUpdated_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| INIT_AckUser_DR | bigint |  | FK | SI | Acknowledge by |
| INIT_AcknowCompleted | varchar |  |  | SI | Acknowledgement Completed |
| INIT_CDRequestNumber | varchar |  |  | SI | CD Request Number  |
| INIT_Date | date |  |  | NO | Issue/Transfer Date |
| INIT_DateLastUpdated | date |  |  | SI | DateLastUpdated |
| INIT_FrLoc_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| INIT_INRQ_DR | bigint |  | FK | SI | Des Ref to INRQ |
| INIT_No | varchar |  |  | NO | Issue/Transfer Reference No |
| INIT_Remarks | varchar |  |  | SI | Remarks |
| INIT_RequestedBy | varchar |  |  | SI | Requested By  |
| INIT_SSUSR_DR | bigint |  | FK | NO | Des Ref to SSUSR |
| INIT_Time | time |  |  | NO | Transfer Time |
| INIT_TimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| INIT_ToLoc_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| INIT_Type | varchar |  |  | NO | Transaction Type (T-Iss/trf, W- ward Stk) |
| INIT_UserCompleted | varchar |  |  | SI | UserCompleted |
| INIT_UserLastUpdated_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| Q01 | - |  |  | SI | Cognitive and perception |
| Q02 | - |  |  | SI | Orientation |
| Q03 | - |  |  | SI | Orientation for place |
| Q04 | - |  |  | SI | Orientation for time |
| Q05 | - |  |  | SI | Awareness |
| Q06 | - |  |  | SI | Reason for hospitalization |
| Q07 | - |  |  | SI | Awareness of cognitive disabilities |
| Q08 | - |  |  | SI | Visual Perception |
| Q09 | - |  |  | SI | Objects identification |
| Q10 | - |  |  | SI | Figure-ground |
| Q11 | - |  |  | SI | Object constancy |
| Q12 | - |  |  | SI | Spatial Perception |
| Q13 | - |  |  | SI | Directions on client's body |
| Q14 | - |  |  | SI | Spatial relations |
| Q15 | - |  |  | SI | Spatial relations on picture |
| Q16 | - |  |  | SI | Praxis |
| Q17 | - |  |  | SI | Motor imitation |
| Q18 | - |  |  | SI | Utilization of objects |
| Q19 | - |  |  | SI | Symbolic actions |
| Q20 | - |  |  | SI | Memory |
| Q21 | - |  |  | SI | Visuomotor Construction |
| Q22 | - |  |  | SI | Copying geometric forms |
| Q23 | - |  |  | SI | Two-dimensional model |
| Q24 | - |  |  | SI | Pegboard construction |
| Q25 | - |  |  | SI | Colored block-design |
| Q26 | - |  |  | SI | Plain block-design |
| Q27 | - |  |  | SI | Puzzle |
| Q28 | - |  |  | SI | Clock drawing |
| Q29 | - |  |  | SI | Thinking Operations |
| Q30 | - |  |  | SI | Categorization |
| Q31 | - |  |  | SI | Object classification unstructured |
| Q32 | - |  |  | SI | Pictorial sequence A |
| Q33 | - |  |  | SI | Pictorial sequence B |
| Q34 | - |  |  | SI | Geometric sequences A |
| Q35 | - |  |  | SI | Geometric sequences B |
| Q36 | - |  |  | SI | Object classification structured |
| Q37 | - |  |  | SI | Verbal mathematical questions |
| Q38 | - |  |  | SI | Activity Daily Living |
| Q39 | - |  |  | SI | Bed mobility |
| Q40 | - |  |  | SI | Transfer |
| Q41 | - |  |  | SI | Locomotion |
| Q42 | - |  |  | SI | Toileting |
| Q43 | - |  |  | SI | Eating |
| Q44 | - |  |  | SI | Hygiene / Grooming |
| Q45 | - |  |  | SI | Bathing |
| Q46 | - |  |  | SI | Dressing |
| Q47 | - |  |  | SI | Fall Risk Assessment |
| Q48 | - |  |  | SI | Fall risk |
| Q49 | - |  |  | SI | High risk by |
| Q50 | - |  |  | SI | Fracture risk |
| Q51 | - |  |  | SI | Pain Assessment |
| Q52 | - |  |  | SI | Does patient have pain? |
| Q53 | - |  |  | SI | Location |
| Q54 | - |  |  | SI | Assessment tool |
| Q55 | - |  |  | SI | Pain assessment score |
| Q56 | - |  |  | SI | Characteristic of pain |
| Q57 | - |  |  | SI | Other characteristic |
| Q58 | - |  |  | SI | Frequency |
| Q59 | - |  |  | SI | Duration |
| Q60 | - |  |  | SI | Pain re-assessment score |
| Q61 | - |  |  | SI | Goals and Planning |
| Q62 | - |  |  | SI | Goal no 1 |
| Q63 | - |  |  | SI | Type |
| Q64 | - |  |  | SI | Performance |
| Q65 | - |  |  | SI | Satisfaction |
| Q66 | - |  |  | SI | Goal no 2 |
| Q67 | - |  |  | SI | Type |
| Q68 | - |  |  | SI | Performance |
| Q69 | - |  |  | SI | Satisfaction |
| Q70 | - |  |  | SI | Goal no 3 |
| Q71 | - |  |  | SI | Type |
| Q72 | - |  |  | SI | Performance |
| Q73 | - |  |  | SI | Satisfaction |
| Q74 | - |  |  | SI | Goal no 4 |
| Q75 | - |  |  | SI | Type |
| Q76 | - |  |  | SI | Performance |
| Q77 | - |  |  | SI | Satisfaction |
| Q78 | - |  |  | SI | Intervention plan |
| Q79 | - |  |  | SI | Re-assessment date |
| Q80 | - |  |  | SI | Instruction |
| Q81 | - |  |  | SI | Patient and/or family was given and understood abo... |
| Q82 | - |  |  | SI | Need reviewed |
| Q83 | - |  |  | SI | Goal |
| Q84 | - |  |  | SI | Type |
| Q85 | - |  |  | SI | Type |
| Q86 | - |  |  | SI | Type |
| Q87 | - |  |  | SI | Type |
| Q88 | - |  |  | SI | Date |
| Q89 | - |  |  | SI | Time |
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