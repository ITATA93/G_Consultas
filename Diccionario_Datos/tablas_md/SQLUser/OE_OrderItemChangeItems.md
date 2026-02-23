# SQLUser.OE_OrderItemChangeItems

**Schema:** SQLUser
**Columnas:** 145
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | OE_OrderItemChange Parent Reference |
| ChildQ31DR | - |  |  | SI | Child Reference: Hip Outcome Score (HOS) Activity ... |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_FieldName | varchar |  |  | SI | FieldName   |
| ITM_NewValue | varchar |  |  | SI | NewValue    |
| ITM_OldValue | varchar |  |  | SI | OldValue    |
| ITM_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Occupation |
| Q02 | - |  |  | SI | Affected Limb |
| Q03 | - |  |  | SI | VAS Score |
| Q04 | - |  |  | SI | Pain Location |
| Q05 | - |  |  | SI | Pain Description |
| Q06 | - |  |  | SI | Pain Pattern worse with the following |
| Q07 | - |  |  | SI | Other |
| Q08 | - |  |  | SI | Pain Pattern better with the following |
| Q09 | - |  |  | SI | Other |
| Q10 | - |  |  | SI | Does the pain radiate to other places? |
| Q100 | - |  |  | SI | Pelvic Landmarks |
| Q101 | - |  |  | SI | Palpation |
| Q102 | - |  |  | SI | Examination |
| Q103 | - |  |  | SI | Extra Label |
| Q104 | - |  |  | SI | Balance (Proprioception Control) |
| Q11 | - |  |  | SI | Pain Radiate Location |
| Q12 | - |  |  | SI | Other |
| Q13 | - |  |  | SI | Pain Present Since |
| Q14 | - |  |  | SI | Pain Progress |
| Q15 | - |  |  | SI | Current Pain History |
| Q16 | - |  |  | SI | Mechanism of Injury |
| Q17 | - |  |  | SI | Other |
| Q18 | - |  |  | SI | Swelling |
| Q19 | - |  |  | SI | When the swelling happend |
| Q20 | - |  |  | SI | Is there snapping or clicking with movement? |
| Q21 | - |  |  | SI | Medical History |
| Q22 | - |  |  | SI | Other |
| Q23 | - |  |  | SI | Any difficulties with bowels or bladder? |
| Q24 | - |  |  | SI | Comment |
| Q25 | - |  |  | SI | Previous Surgery |
| Q26 | - |  |  | SI | Comment |
| Q27 | - |  |  | SI | Previous Physical Therapy Treatment |
| Q28 | - |  |  | SI | X-ray |
| Q29 | - |  |  | SI | Report |
| Q30 | - |  |  | SI | Patient Goals |
| Q33 | - |  |  | SI | Current Level of function during your usual activi... |
| Q34 | - |  |  | SI | Current Level of function during your sports relat... |
| Q35 | - |  |  | SI | % |
| Q36 | - |  |  | SI | % |
| Q37 | - |  |  | SI | Overall, how would you rate your current level of ... |
| Q38 | - |  |  | SI | Gait |
| Q39 | - |  |  | SI | Comment |
| Q40 | - |  |  | SI | Lordosis |
| Q41A | - |  |  | SI | Pelvic Tilt |
| Q42 | - |  |  | SI | Lateral Shift |
| Q43 | - |  |  | SI | Front |
| Q44 | - |  |  | SI | Back |
| Q45 | - |  |  | SI | PSIS |
| Q46 | - |  |  | SI | ASIS |
| Q47 | - |  |  | SI | Effusion Right |
| Q48 | - |  |  | SI | Effusion Left |
| Q49 | - |  |  | SI | Atrophy |
| Q50 | - |  |  | SI | Comment |
| Q51 | - |  |  | SI | Contusions |
| Q52 | - |  |  | SI | Comment |
| Q53 | - |  |  | SI | Scars |
| Q54 | - |  |  | SI | Other |
| Q55 | - |  |  | SI | Temperature |
| Q56 | - |  |  | SI | Anterior Superior / Inferior Iliac Spine |
| Q57 | - |  |  | SI | Greater trochanter |
| Q58 | - |  |  | SI | Iliotibial Band |
| Q59 | - |  |  | SI | Gluteus Muscle |
| Q60 | - |  |  | SI | SI join |
| Q61 | - |  |  | SI | Posterior Superior Iliac Spine |
| Q62 | - |  |  | SI | Hamstring muscles |
| Q63 | - |  |  | SI | Other |
| Q64 | - |  |  | SI | Leg Length |
| Q65 | - |  |  | SI | Leg Length (cm) |
| Q66 | - |  |  | SI | Standing on one leg with eye open |
| Q67 | - |  |  | SI | Standing on one leg with eye closed |
| Q68 | - |  |  | SI | Stork standing test |
| Q72 | - |  |  | SI | Other Special Test |
| Q73 | - |  |  | SI | Diagnosis |
| Q74 | - |  |  | SI | Problems List |
| Q75 | - |  |  | SI | Rehabilitation Potential |
| Q76 | - |  |  | SI | Patient /Family Participation |
| Q77 | - |  |  | SI | Education |
| Q78 | - |  |  | SI | Short Term Goals |
| Q79 | - |  |  | SI | Long Term Goals |
| Q80 | - |  |  | SI | Treatment |
| Q81 | - |  |  | SI | Other |
| Q82 | - |  |  | SI | Number of Treatments per week |
| Q83 | - |  |  | SI | Number of weeks |
| Q84 | - |  |  | SI | Re Evaluation |
| Q85 | - |  |  | SI | Please answer every question with one response tha... |
| Q86 | - |  |  | SI | Because of your hip,  How much difficulty do you h... |
| Q87 | - |  |  | SI | How would you rate your current level of function ... |
| Q88 | - |  |  | SI | your usual daily activities? |
| Q90 | - |  |  | SI | How would you rate your current level of function ... |
| Q91 | - |  |  | SI | daily activities? |
| Q92 | - |  |  | SI | Because of your hip, How much difficulty do you ha... |
| Q93 | - |  |  | SI | Observation |
| Q94 | - |  |  | SI | Pelvic Landmarks |
| Q95 | - |  |  | SI | Palpation |
| Q96 | - |  |  | SI | Examination |
| Q97 | - |  |  | SI | Chief Complaint |
| Q98 | - |  |  | SI | Balance (Proprioception Control) |
| Q99 | - |  |  | SI | Chief Complaint |
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