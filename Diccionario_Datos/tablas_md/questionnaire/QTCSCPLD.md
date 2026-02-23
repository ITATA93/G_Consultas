# questionnaire.QTCSCPLD

> Surgical Criteria Patient Led Discharge - Patient Criteria and Follow up

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Surgical Criteria Patient Led Discharge - Patient Criteria and Follow up

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Discharge Criteria |
| Q04 | varchar |  |  | SI | Heart rate - within +/- 20% pre-operative value |
| Q05 | varchar |  |  | SI | Respiratory rate - within +/- 20% pre-operative va... |
| Q06 | varchar |  |  | SI | Blood pressure - within +/- 20% pre-operative valu... |
| Q07 | varchar |  |  | SI | Post-op care instructions provided |
| Q08 | varchar |  |  | SI | Alert and oriented (At pre-anaesthetic level) |
| Q09 | varchar |  |  | SI | Minimal nausea and tolerating food / oral fluids |
| Q10 | varchar |  |  | SI | Pain controlled with oral analgesia |
| Q11 | varchar |  |  | SI | Voided |
| Q12 | varchar |  |  | SI | Intravenous access removed |
| Q13 | varchar |  |  | SI | Adult supervision at discharge |
| Q14 | varchar |  |  | SI | Discharge checklist completed |
| Q15 | varchar |  |  | SI | Safely mobilising |
| Q16 | varchar |  |  | SI | Wound - minimal discharge (post op) |
| Q17 | varchar |  |  | SI | Other (Specify) |
| Q18 | varchar |  |  | SI | Follow Up |
| Q19 | varchar |  |  | SI | Follow up method |
| Q20 | varchar |  |  | SI | Follow up method note |
| Q21 | varchar |  |  | SI | Patient informed how to re-engage with hospital sy... |
| Q22 | varchar |  |  | SI | Script sent to pharmacy |
| Q23 | varchar |  |  | SI | Medications supplied to patient |
| Q24 | varchar |  |  | SI | Script given to patient for outside pharmacy |
| Q25 | varchar |  |  | SI | Community health referral |
| Q26 | varchar |  |  | SI | Discharge summary given to patient |
| Q27 | varchar |  |  | SI | Medical certificate given to patient and/or carer |
| Q28 | varchar |  |  | SI | I confirm that all the discharge criteria have bee... |
| Q29 | varchar |  |  | SI | Reason patient not discharged using criteria led d... |
| Q30 | varchar |  |  | SI | Other (Specify) |
| Q31 | varchar |  |  | SI | Guidelines |
| Q32 | varchar |  |  | SI | How to initiate criteria led discharge (CLD) for a... |
| Q33 | varchar |  |  | SI | CLD aims to facilitate timely and clinical appropr... |
| Q34 | varchar |  |  | SI | All patients should be considered for criteria led... |
| Q35 | varchar |  |  | SI | • Surgical patient criteria led discharge form to ... |
| Q36 | varchar |  |  | SI | • The surgeon is to document the criteria led disc... |
| Q37 | varchar |  |  | SI | • If a post-operation review by the surgeon is req... |
| Q38 | varchar |  |  | SI | • Discharge scripts, discharge summaries, sick cer... |
| Q39 | varchar |  |  | SI | • Senior nurse to document assessment made for dis... |
| Q40 | varchar |  |  | SI | Note: If nursing staff are in any doubt they are t... |
| Q41 | varchar |  |  | SI | Discharge checklist - ensure all are complete prio... |
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