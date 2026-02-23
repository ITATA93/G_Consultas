# questionnaire.QTCAHOCCSOP

> Subluxation Oedema Pain Assessment

**Schema:** questionnaire
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Subluxation Oedema Pain Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Subluxation |
| Q02 | varchar |  |  | SI | Measurement |
| Q03 | varchar |  |  | SI | Oedema |
| Q04 | varchar |  |  | SI | (description, location, measurement) |
| Q05 | varchar |  |  | SI | VAS score |
| Q06 | varchar |  |  | SI | Pain |
| Q07 | varchar |  |  | SI | Location |
| Q08 | varchar |  |  | SI | Description |
| Q09 | varchar |  |  | SI | (sharp, dull, burning, stinging, aching, throbbing... |
| Q10 | varchar |  |  | SI | Indicate the location of your pain |
| Q11 | varchar |  |  | SI | Sensation |
| Q12 | varchar |  |  | SI | Left |
| Q13 | varchar |  |  | SI | Right |
| Q14 | varchar |  |  | SI | Light touch |
| Q15 | varchar |  |  | SI | Light touch (left) |
| Q15ObsDR | varchar |  | FK | SI | Light touch (left) DR |
| Q16 | varchar |  |  | SI | Light touch (right) |
| Q16ObsDR | varchar |  | FK | SI | Light touch (right) DR |
| Q17 | varchar |  |  | SI | Pain – Sharp / Dull |
| Q18 | varchar |  |  | SI | Pain – sharp / dull (left) |
| Q18ObsDR | varchar |  | FK | SI | Pain – sharp / dull (left) DR |
| Q19 | varchar |  |  | SI | Pain – sharp / dull (right) |
| Q19ObsDR | varchar |  | FK | SI | Pain – sharp / dull (right) DR |
| Q20 | varchar |  |  | SI | Temperature |
| Q21 | varchar |  |  | SI | Temperature (left) |
| Q21ObsDR | varchar |  | FK | SI | Temperature (left) DR |
| Q22 | varchar |  |  | SI | Temperature (right) |
| Q22ObsDR | varchar |  | FK | SI | Temperature (right) DR |
| Q23 | varchar |  |  | SI | Stereognosis |
| Q24 | varchar |  |  | SI | Stereognosis (left) |
| Q24ObsDR | varchar |  | FK | SI | Stereognosis (left) DR |
| Q25 | varchar |  |  | SI | Stereognosis (right) |
| Q25ObsDR | varchar |  | FK | SI | Stereognosis (right) DR |
| Q26 | varchar |  |  | SI | Kinaesthesia |
| Q27 | varchar |  |  | SI | Kinaesthesia (left) |
| Q27ObsDR | varchar |  | FK | SI | Kinaesthesia (left) DR |
| Q28 | varchar |  |  | SI | Kinaesthesia (right) |
| Q28ObsDR | varchar |  | FK | SI | Kinaesthesia (right) DR |
| Q29 | varchar |  |  | SI | Proprioception  |
| Q30 | varchar |  |  | SI | Proprioception (left) |
| Q30ObsDR | varchar |  | FK | SI | Proprioception (left) DR |
| Q31 | varchar |  |  | SI | Proprioception (right) |
| Q31ObsDR | varchar |  | FK | SI | Proprioception (right) DR |
| Q32 | varchar |  |  | SI | 2 Point discrimination |
| Q33 | varchar |  |  | SI | 2 Point discrimination (left) |
| Q33ObsDR | varchar |  | FK | SI | 2 Point discrimination (left) DR |
| Q34 | varchar |  |  | SI | 2 Point discrimination (right) |
| Q34ObsDR | varchar |  | FK | SI | 2 Point discrimination (right) DR |
| Q35 | varchar |  |  | SI | Extinction |
| Q36 | varchar |  |  | SI | Extinction (left) |
| Q36ObsDR | varchar |  | FK | SI | Extinction (left) DR |
| Q37 | varchar |  |  | SI | Extinction (right) |
| Q37ObsDR | varchar |  | FK | SI | Extinction (right) DR |
| Q38 | varchar |  |  | SI | Inattention |
| Q39 | varchar |  |  | SI | Inattention (left) |
| Q39ObsDR | varchar |  | FK | SI | Inattention (left) DR |
| Q40 | varchar |  |  | SI | Inattention (right) |
| Q40ObsDR | varchar |  | FK | SI | Inattention (right) DR |
| Q41 | varchar |  |  | SI | Notes |
| Q42 | varchar |  |  | SI | Occupational therapist name |
| Q43 | longvarbinary |  |  | SI | Signature |
| Q43UDt | date |  |  | SI | Signature Last Updated Date |
| Q43UTm | time |  |  | SI | Signature Last Updated Time |
| Q44 | date |  |  | SI | Date |
| Q45 | varchar |  |  | SI | Light touch comment |
| Q46 | varchar |  |  | SI | Pain comment |
| Q47 | varchar |  |  | SI | Temperature comment |
| Q48 | varchar |  |  | SI | Stereognosis comment |
| Q49 | varchar |  |  | SI | Kinaesthesia comment |
| Q50 | varchar |  |  | SI | Proprioception comment |
| Q51 | varchar |  |  | SI | 2 point discrimination comment |
| Q52 | varchar |  |  | SI | Extinction comment |
| Q53 | varchar |  |  | SI | Inattention comment |
| Q54 | varchar |  |  | SI | Comment |
| Q55 | date |  |  | SI | Date |
| Q56 | time |  |  | SI | Time |
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