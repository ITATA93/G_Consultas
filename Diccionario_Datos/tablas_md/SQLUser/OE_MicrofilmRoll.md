# SQLUser.OE_MicrofilmRoll

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OEMF_RowId | bigint | PK |  | NO | - |
| OEMF_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| OEMF_Roll | varchar |  |  | SI | Roll |
| OEMF_RollDesc | varchar |  |  | SI | Roll Description |
| OEMF_RollID | varchar |  |  | SI | Roll ID |
| Q01 | - |  |  | SI | Subluxation |
| Q02 | - |  |  | SI | Measurement |
| Q03 | - |  |  | SI | Oedema |
| Q04 | - |  |  | SI | (description, location, measurement) |
| Q05 | - |  |  | SI | VAS score |
| Q06 | - |  |  | SI | Pain |
| Q07 | - |  |  | SI | Location |
| Q08 | - |  |  | SI | Description |
| Q09 | - |  |  | SI | (sharp, dull, burning, stinging, aching, throbbing... |
| Q10 | - |  |  | SI | Indicate the location of your pain |
| Q11 | - |  |  | SI | Sensation |
| Q12 | - |  |  | SI | Left |
| Q13 | - |  |  | SI | Right |
| Q14 | - |  |  | SI | Light touch |
| Q15 | - |  |  | SI | Light touch (left) |
| Q15ObsDR | - |  |  | SI | Light touch (left) DR |
| Q16 | - |  |  | SI | Light touch (right) |
| Q16ObsDR | - |  |  | SI | Light touch (right) DR |
| Q17 | - |  |  | SI | Pain – Sharp / Dull |
| Q18 | - |  |  | SI | Pain – sharp / dull (left) |
| Q18ObsDR | - |  |  | SI | Pain – sharp / dull (left) DR |
| Q19 | - |  |  | SI | Pain – sharp / dull (right) |
| Q19ObsDR | - |  |  | SI | Pain – sharp / dull (right) DR |
| Q20 | - |  |  | SI | Temperature |
| Q21 | - |  |  | SI | Temperature (left) |
| Q21ObsDR | - |  |  | SI | Temperature (left) DR |
| Q22 | - |  |  | SI | Temperature (right) |
| Q22ObsDR | - |  |  | SI | Temperature (right) DR |
| Q23 | - |  |  | SI | Stereognosis |
| Q24 | - |  |  | SI | Stereognosis (left) |
| Q24ObsDR | - |  |  | SI | Stereognosis (left) DR |
| Q25 | - |  |  | SI | Stereognosis (right) |
| Q25ObsDR | - |  |  | SI | Stereognosis (right) DR |
| Q26 | - |  |  | SI | Kinaesthesia |
| Q27 | - |  |  | SI | Kinaesthesia (left) |
| Q27ObsDR | - |  |  | SI | Kinaesthesia (left) DR |
| Q28 | - |  |  | SI | Kinaesthesia (right) |
| Q28ObsDR | - |  |  | SI | Kinaesthesia (right) DR |
| Q29 | - |  |  | SI | Proprioception |
| Q30 | - |  |  | SI | Proprioception (left) |
| Q30ObsDR | - |  |  | SI | Proprioception (left) DR |
| Q31 | - |  |  | SI | Proprioception (right) |
| Q31ObsDR | - |  |  | SI | Proprioception (right) DR |
| Q32 | - |  |  | SI | 2 Point discrimination |
| Q33 | - |  |  | SI | 2 Point discrimination (left) |
| Q33ObsDR | - |  |  | SI | 2 Point discrimination (left) DR |
| Q34 | - |  |  | SI | 2 Point discrimination (right) |
| Q34ObsDR | - |  |  | SI | 2 Point discrimination (right) DR |
| Q35 | - |  |  | SI | Extinction |
| Q36 | - |  |  | SI | Extinction (left) |
| Q36ObsDR | - |  |  | SI | Extinction (left) DR |
| Q37 | - |  |  | SI | Extinction (right) |
| Q37ObsDR | - |  |  | SI | Extinction (right) DR |
| Q38 | - |  |  | SI | Inattention |
| Q39 | - |  |  | SI | Inattention (left) |
| Q39ObsDR | - |  |  | SI | Inattention (left) DR |
| Q40 | - |  |  | SI | Inattention (right) |
| Q40ObsDR | - |  |  | SI | Inattention (right) DR |
| Q41 | - |  |  | SI | Notes |
| Q42 | - |  |  | SI | Occupational therapist name |
| Q43 | - |  |  | SI | Signature |
| Q43UDt | - |  |  | SI | Signature Last Updated Date |
| Q43UTm | - |  |  | SI | Signature Last Updated Time |
| Q44 | - |  |  | SI | Date |
| Q45 | - |  |  | SI | Light touch comment |
| Q46 | - |  |  | SI | Pain comment |
| Q47 | - |  |  | SI | Temperature comment |
| Q48 | - |  |  | SI | Stereognosis comment |
| Q49 | - |  |  | SI | Kinaesthesia comment |
| Q50 | - |  |  | SI | Proprioception comment |
| Q51 | - |  |  | SI | 2 point discrimination comment |
| Q52 | - |  |  | SI | Extinction comment |
| Q53 | - |  |  | SI | Inattention comment |
| Q54 | - |  |  | SI | Comment |
| Q55 | - |  |  | SI | Date |
| Q56 | - |  |  | SI | Time |
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