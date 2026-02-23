# SQLUser.PA_Adm2MaternityComplic

**Schema:** SQLUser
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MATC_ParRef | bigint | PK |  | NO | PA_Adm2 Parent Reference |
| MATC_Childsub | double |  |  | NO | Childsub |
| MATC_MaternityReason_DR | bigint |  | FK | SI | Des Ref MaternityReason |
| MATC_RowId | varchar |  |  | NO | - |
| MATC_UpdateDate | date |  |  | SI | Update Date |
| MATC_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| MATC_UpdateTime | time |  |  | SI | Update Time |
| MATC_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q01 | - |  |  | SI | Time |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Date of seizure |
| Q04 | - |  |  | SI | Time of seizure |
| Q05 | - |  |  | SI | What were the first things noticed when the seizur... |
| Q06 | - |  |  | SI | If not initially witnessed what alerted you to the... |
| Q07 | - |  |  | SI | Duration of seizure |
| Q08 | - |  |  | SI | UOM |
| Q09 | - |  |  | SI | One side of the body affected more than the other |
| Q10 | - |  |  | SI | Body stiff, jerk, twitch or convulse |
| Q11 | - |  |  | SI | Loss of consciousness |
| Q12 | - |  |  | SI | For how long was the patient unconscious, if appli... |
| Q13 | - |  |  | SI | UOM |
| Q14 | - |  |  | SI | Skin changes (i.e. flushed, cyanosed, clammy, pall... |
| Q15 | - |  |  | SI | Patient noted to be speaking/performing any action... |
| Q16 | - |  |  | SI | Description (if applicable) |
| Q17 | - |  |  | SI | Breathing changes |
| Q18 | - |  |  | SI | Description and interventions given for breathing ... |
| Q19 | - |  |  | SI | Did the patient experience any |
| Q20 | - |  |  | SI | Patient behaviour after the seizure (i.e. drowsy, ... |
| Q21 | - |  |  | SI | How long approximately post-seizure until the pati... |
| Q22 | - |  |  | SI | UOM |
| Q23 | - |  |  | SI | Does the patient have any memory of the event |
| Q24 | - |  |  | SI | If yes, provide a brief description |
| Q25 | - |  |  | SI | Medication administered during the seizure |
| Q26 | - |  |  | SI | Observations taken during seizure |
| Q27 | - |  |  | SI | Guidelines |
| Q28 | - |  |  | SI | Two basic categories of seizures |
| Q29 | - |  |  | SI | Partial or Focal seizures |
| Q30 | - |  |  | SI | Simple partial |
| Q31 | - |  |  | SI | • Localised seizures that occur in only one part o... |
| Q32 | - |  |  | SI | • There is no loss of consciousness and the event ... |
| Q33 | - |  |  | SI | Complex partial seizures |
| Q34 | - |  |  | SI | • Occur in only one part of the brain. |
| Q35 | - |  |  | SI | • Conscious state becomes altered, e.g. confusion,... |
| Q36 | - |  |  | SI | • Whilst this type of seizure generally only lasts... |
| Q37 | - |  |  | SI | Secondarily generalised seizures |
| Q38 | - |  |  | SI | • Commence in one part of the brain like simple pa... |
| Q39 | - |  |  | SI | • These seizures always commence as a partial seiz... |
| Q40 | - |  |  | SI | Generalised seizures - start in 1 part of the brai... |
| Q41 | - |  |  | SI | Absence seizures |
| Q42 | - |  |  | SI | • Previously known as petit mal, involve the whole... |
| Q43 | - |  |  | SI | • The individual (usually a child) loses awareness... |
| Q44 | - |  |  | SI | • Absence seizures appear similar to daydreaming a... |
| Q45 | - |  |  | SI | • These seizures generally start suddenly and last... |
| Q46 | - |  |  | SI | Myoclonic seizures |
| Q47 | - |  |  | SI | • Also involve the entire brain. |
| Q48 | - |  |  | SI | • Usually occur on waking or before bed when the p... |
| Q49 | - |  |  | SI | • These seizures are characterised by uncontrolled... |
| Q50 | - |  |  | SI | Tonic-clonic seizures |
| Q51 | - |  |  | SI | • Previously known as grand mal, involve the whole... |
| Q52 | - |  |  | SI | • This seizure is characterised by two main phases... |
| Q53 | - |  |  | SI | • This type of seizure usually lasts only a few mi... |
| Q54 | - |  |  | SI | • Afterwards the person is generally confused and ... |
| Q55 | - |  |  | SI | Atonic seizure |
| Q56 | - |  |  | SI | • Affect muscle tone causing the person to collaps... |
| Q57 | - |  |  | SI | • Recovery afterwards is fast. |
| Q58 | - |  |  | SI | • People who suffer from atonic seizures, are at s... |
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