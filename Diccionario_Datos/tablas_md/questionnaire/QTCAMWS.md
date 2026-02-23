# questionnaire.QTCAMWS

> Amphetamine Withdrawal Questionnaire (AWQ)

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Amphetamine Withdrawal Questionnaire (AWQ)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Temperature |
| Q01ObsDR | varchar |  | FK | SI | Temperature DR |
| Q02 | varchar |  |  | SI | Pulse |
| Q02ObsDR | varchar |  | FK | SI | Pulse DR |
| Q03 | varchar |  |  | SI | Respiration |
| Q03ObsDR | varchar |  | FK | SI | Respiration DR |
| Q04 | varchar |  |  | SI | Systolic BP |
| Q04ObsDR | varchar |  | FK | SI | Systolic BP DR |
| Q05 | varchar |  |  | SI | Diastolic BP |
| Q05ObsDR | varchar |  | FK | SI | Diastolic BP DR |
| Q06 | varchar |  |  | SI | AVPU - Conscious Level |
| Q06ObsDR | varchar |  | FK | SI | AVPU - Conscious Level DR |
| Q07 | varchar |  |  | SI | Have you been craving amphetamines&nbsp;or methamp... |
| Q08 | varchar |  |  | SI | Have you lost interest in things or no longer take... |
| Q09 | varchar |  |  | SI | Have you felt your movements are slow? |
| Q10 | varchar |  |  | SI | Have you felt tired? |
| Q11 | varchar |  |  | SI | Have you had any vivid or unpleasant dreams? |
| Q12 | varchar |  |  | SI | Have you felt sad? |
| Q13 | varchar |  |  | SI | Have you felt anxious? |
| Q14 | varchar |  |  | SI | Have you felt agitated? |
| Q15 | varchar |  |  | SI | Has your appetite increased or are you eating too ... |
| Q16 | varchar |  |  | SI | Have you been craving for sleep or sleeping too mu... |
| Q17 | varchar |  |  | SI | Craving |
| Q18 | varchar |  |  | SI | Interest |
| Q19 | varchar |  |  | SI | Motor coordination |
| Q20 | varchar |  |  | SI | Tired |
| Q21 | varchar |  |  | SI | Dreams |
| Q22 | varchar |  |  | SI | Mood |
| Q23 | varchar |  |  | SI | Anxiety |
| Q24 | varchar |  |  | SI | Agitation |
| Q25 | varchar |  |  | SI | Appetite |
| Q26 | varchar |  |  | SI | Sleep |
| Q27 | varchar |  |  | SI | Score |
| Q28 | varchar |  |  | SI | Classification |
| Q29 | varchar |  |  | SI | 0 - 40 |
| Q30 | varchar |  |  | SI | Higher scores indicating greater severity |
| Q31 | varchar |  |  | SI | 0 - 40: Higher scores indicating greater severity |
| Q32 | varchar |  |  | SI | Total scores are indicative of increasing or decre... |
| Q33 | date |  |  | SI | Date |
| Q34 | time |  |  | SI | Time |
| Q35 | varchar |  |  | SI | This withdrawal questionnaire is used to monitor t... |
| Q36 | varchar |  |  | SI | Vital signs observation chart is required when com... |
| Q37 | varchar |  |  | SI | Srisurapanont M, Jarusuraisin N, Jittiwutikan J. A... |
| Q38 | varchar |  |  | SI | Fischer J, Roche A, Duraisingam V. AWQ – Amphetami... |
| Q39 | varchar |  |  | SI | https://aodscreening.flinders.edu.au/withdrawal |
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