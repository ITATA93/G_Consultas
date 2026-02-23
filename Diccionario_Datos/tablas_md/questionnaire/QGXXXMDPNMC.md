# questionnaire.QGXXXMDPNMC

> Daily Postnatal Maternal Checks

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Daily Postnatal Maternal Checks

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Temperature |
| Q01ObsDR | varchar |  | FK | SI | Temperature DR |
| Q02 | varchar |  |  | SI | Respirations |
| Q02ObsDR | varchar |  | FK | SI | Respirations DR |
| Q03 | varchar |  |  | SI | Pulse |
| Q03ObsDR | varchar |  | FK | SI | Pulse DR |
| Q04 | varchar |  |  | SI | Systolic BP |
| Q04ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q05 | varchar |  |  | SI | Diastolic BP |
| Q05ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q06 | varchar |  |  | SI | Lochia |
| Q06ObsDR | varchar |  | FK | SI | Lochia DR |
| Q07 | varchar |  |  | SI | Fundus - involuting |
| Q07ObsDR | varchar |  | FK | SI | Fundus - involuting DR |
| Q08 | varchar |  |  | SI | Fundus |
| Q08ObsDR | varchar |  | FK | SI | Fundus DR |
| Q09 | varchar |  |  | SI | Fundus - other observations |
| Q09ObsDR | varchar |  | FK | SI | Fundus - other observations DR |
| Q10 | varchar |  |  | SI | Passed urine post delivery |
| Q10ObsDR | varchar |  | FK | SI | Passed urine post delivery DR |
| Q11 | varchar |  |  | SI | Problems passing urine |
| Q11ObsDR | varchar |  | FK | SI | Problems passing urine DR |
| Q12 | varchar |  |  | SI | Retaining urine |
| Q12ObsDR | varchar |  | FK | SI | Retaining urine DR |
| Q13 | varchar |  |  | SI | Catheter inserted |
| Q13ObsDR | varchar |  | FK | SI | Catheter inserted DR |
| Q14 | varchar |  |  | SI | Catheter in situ |
| Q14ObsDR | varchar |  | FK | SI | Catheter in situ DR |
| Q15 | varchar |  |  | SI | Catheter removed |
| Q15ObsDR | varchar |  | FK | SI | Catheter removed DR |
| Q16 | varchar |  |  | SI | Bowels moved |
| Q16ObsDR | varchar |  | FK | SI | Bowels moved DR |
| Q17 | varchar |  |  | SI | Haemorrhoids |
| Q17ObsDR | varchar |  | FK | SI | Haemorrhoids DR |
| Q18 | varchar |  |  | SI | Bowel control problems |
| Q18ObsDR | varchar |  | FK | SI | Bowel control problems DR |
| Q19 | varchar |  |  | SI | Pelvic floor exercises discussed |
| Q19ObsDR | varchar |  | FK | SI | Pelvic floor exercises discussed DR |
| Q20 | varchar |  |  | SI | Pelvic floor problems |
| Q20ObsDR | varchar |  | FK | SI | Pelvic floor problems DR |
| Q21 | varchar |  |  | SI | Type of feeding |
| Q21ObsDR | varchar |  | FK | SI | Type of feeding DR |
| Q22 | varchar |  |  | SI | Breasts |
| Q22ObsDR | varchar |  | FK | SI | Breasts DR |
| Q23 | varchar |  |  | SI | Management |
| Q24 | varchar |  |  | SI | Perineum |
| Q24ObsDR | varchar |  | FK | SI | Perineum DR |
| Q25 | varchar |  |  | SI | Wound |
| Q25ObsDR | varchar |  | FK | SI | Wound DR |
| Q26 | varchar |  |  | SI | General wellbeing and pain assessment |
| Q27 | varchar |  |  | SI | Adequate analgesia |
| Q27ObsDR | varchar |  | FK | SI | Adequate analgesia DR |
| Q28 | varchar |  |  | SI | Sutures to be removed |
| Q28ObsDR | varchar |  | FK | SI | Sutures to be removed DR |
| Q29 | varchar |  |  | SI | Have sutures been removed |
| Q29ObsDR | varchar |  | FK | SI | Have sutures been removed DR |
| Q30 | varchar |  |  | SI | Legs |
| Q30ObsDR | varchar |  | FK | SI | Legs DR |
| Q31 | varchar |  |  | SI | Mobility and clot prevention explained |
| Q31ObsDR | varchar |  | FK | SI | Mobility and clot prevention explained DR |
| Q32 | varchar |  |  | SI | Revised thrombosis risk |
| Q32ObsDR | varchar |  | FK | SI | Revised thrombosis risk DR |
| Q33 | varchar |  |  | SI | Summary of assessment and care |
| Q34 | varchar |  |  | SI | Midwife countersigning |
| Q35 | varchar |  |  | SI | TEDS in situ |
| Q36 | varchar |  |  | SI | Details |
| Q37 | date |  |  | SI | Date |
| Q38 | time |  |  | SI | Time |
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