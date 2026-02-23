# questionnaire.QTCSOC

> Seizure Observations Chart

**Schema:** questionnaire
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Seizure Observations Chart

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | time |  |  | SI | Time |
| Q02 | date |  |  | SI | Date |
| Q03 | date |  |  | SI | Date of seizure |
| Q04 | time |  |  | SI | Time of seizure |
| Q05 | varchar |  |  | SI | What were the first things noticed when the seizur... |
| Q06 | varchar |  |  | SI | If not initially witnessed what alerted you to the... |
| Q07 | numeric |  |  | SI | Duration of seizure |
| Q08 | varchar |  |  | SI | UOM |
| Q09 | varchar |  |  | SI | One side of the body affected more than the other |
| Q10 | varchar |  |  | SI | Body stiff, jerk, twitch or convulse |
| Q11 | varchar |  |  | SI | Loss of consciousness |
| Q12 | numeric |  |  | SI | For how long was the patient unconscious, if appli... |
| Q13 | varchar |  |  | SI | UOM |
| Q14 | varchar |  |  | SI | Skin changes (i.e. flushed, cyanosed, clammy, pall... |
| Q15 | varchar |  |  | SI | Patient noted to be speaking/performing any action... |
| Q16 | varchar |  |  | SI | Description (if applicable) |
| Q17 | varchar |  |  | SI | Breathing changes |
| Q18 | varchar |  |  | SI | Description and interventions given for breathing ... |
| Q19 | varchar |  |  | SI | Did the patient experience any |
| Q20 | varchar |  |  | SI | Patient behaviour after the seizure (i.e. drowsy, ... |
| Q21 | numeric |  |  | SI | How long approximately post-seizure until the pati... |
| Q22 | varchar |  |  | SI | UOM |
| Q23 | varchar |  |  | SI | Does the patient have any memory of the event |
| Q24 | varchar |  |  | SI | If yes, provide a brief description |
| Q25 | varchar |  |  | SI | Medication administered during the seizure |
| Q26 | varchar |  |  | SI | Observations taken during seizure |
| Q27 | varchar |  |  | SI | Guidelines |
| Q28 | varchar |  |  | SI | Two basic categories of seizures |
| Q29 | varchar |  |  | SI | Partial or Focal seizures |
| Q30 | varchar |  |  | SI | Simple partial |
| Q31 | varchar |  |  | SI | • Localised seizures that occur in only one part o... |
| Q32 | varchar |  |  | SI | • There is no loss of consciousness and the event ... |
| Q33 | varchar |  |  | SI | Complex partial seizures |
| Q34 | varchar |  |  | SI | • Occur in only one part of the brain. |
| Q35 | varchar |  |  | SI | • Conscious state becomes altered, e.g. confusion,... |
| Q36 | varchar |  |  | SI | • Whilst this type of seizure generally only lasts... |
| Q37 | varchar |  |  | SI | Secondarily generalised seizures |
| Q38 | varchar |  |  | SI | • Commence in one part of the brain like simple pa... |
| Q39 | varchar |  |  | SI | • These seizures always commence as a partial seiz... |
| Q40 | varchar |  |  | SI | Generalised seizures - start in 1 part of the brai... |
| Q41 | varchar |  |  | SI | Absence seizures |
| Q42 | varchar |  |  | SI | • Previously known as petit mal, involve the whole... |
| Q43 | varchar |  |  | SI | • The individual (usually a child) loses awareness... |
| Q44 | varchar |  |  | SI | • Absence seizures appear similar to daydreaming a... |
| Q45 | varchar |  |  | SI | • These seizures generally start suddenly and last... |
| Q46 | varchar |  |  | SI | Myoclonic seizures |
| Q47 | varchar |  |  | SI | • Also involve the entire brain. |
| Q48 | varchar |  |  | SI | • Usually occur on waking or before bed when the p... |
| Q49 | varchar |  |  | SI | • These seizures are characterised by uncontrolled... |
| Q50 | varchar |  |  | SI | Tonic-clonic seizures |
| Q51 | varchar |  |  | SI | • Previously known as grand mal, involve the whole... |
| Q52 | varchar |  |  | SI | • This seizure is characterised by two main phases... |
| Q53 | varchar |  |  | SI | • This type of seizure usually lasts only a few mi... |
| Q54 | varchar |  |  | SI | • Afterwards the person is generally confused and ... |
| Q55 | varchar |  |  | SI | Atonic seizure |
| Q56 | varchar |  |  | SI | • Affect muscle tone causing the person to collaps... |
| Q57 | varchar |  |  | SI | • Recovery afterwards is fast. |
| Q58 | varchar |  |  | SI | • People who suffer from atonic seizures, are at s... |
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