# SQLUser.OE_OrdEnt

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEORN_OEORD_ParRef | numeric | PK |  | NO | Des Ref to OEORD |
| OEORN_BookingViolatesOffsets | bit |  |  | SI | Has Nodes Booked Outside of Offsets |
| OEORN_Childsub | numeric |  |  | NO | OEORN Child Sub (New key) |
| OEORN_GroupName | varchar |  |  | SI | Group Name |
| OEORN_OrdSetDate_DR | varchar |  | FK | SI | Des Ref Order Set Date |
| OEORN_OrdSets_DR | varchar |  | FK | SI | Des Ref to ARCOS |
| OEORN_RowId | varchar |  |  | NO | - |
| OEORN_SequenceDuration | varchar |  |  | SI | Sequence Plan Duration |
| OEORN_SequenceStartDate | date |  |  | SI | Sequence Start Date |
| OEORN_SequenceStartTime | time |  |  | SI | Sequence Start Time |
| OEORN_Type | varchar |  |  | SI | Type |
| Q01 | - |  |  | SI | Reason for referral |
| Q02 | - |  |  | SI | Risk Management: |
| Q03 | - |  |  | SI | Transfers |
| Q04 | - |  |  | SI | Gait |
| Q05 | - |  |  | SI | Gait Aid |
| Q06 | - |  |  | SI | Footwear |
| Q07 | - |  |  | SI | Weight bearing status |
| Q08 | - |  |  | SI | Steps |
| Q09 | - |  |  | SI | Hoist |
| Q10 | - |  |  | SI | Rails |
| Q11 | - |  |  | SI | Mobility in Pool |
| Q12 | - |  |  | SI | Assessment Notes |
| Q13 | - |  |  | SI | Orientation of Pool area |
| Q14 | - |  |  | SI | Hydrotherapy booklet provided |
| Q15 | - |  |  | SI | Patient Signature |
| Q15UDt | - |  |  | SI | Patient Signature Last Updated Date |
| Q15UTm | - |  |  | SI | Patient Signature Last Updated Time |
| Q16 | - |  |  | SI | Patient Signature Date |
| Q17 | - |  |  | SI | Therapist Signature |
| Q17UDt | - |  |  | SI | Therapist Signature Last Updated Date |
| Q17UTm | - |  |  | SI | Therapist Signature Last Updated Time |
| Q18 | - |  |  | SI | Therapist Signature Date |
| Q19 | - |  |  | SI | Care Provider |
| Q20 | - |  |  | SI | Communication / Cognitive / Psychosocial |
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