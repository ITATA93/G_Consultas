# SQLUser.CT_LOINC

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLOINC_RowID | bigint | PK |  | NO | - |
| CTLOINC_Code | varchar |  |  | SI | Code |
| CTLOINC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTLOINC_CreatedDate | date |  |  | SI | Created Date |
| CTLOINC_CreatedTime | time |  |  | SI | Created Time |
| CTLOINC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTLOINC_DateFrom | date |  |  | SI | Effective date for the record |
| CTLOINC_DateTo | date |  |  | SI | Last day the record is active  |
| CTLOINC_Desc | varchar |  |  | SI | Description |
| CTLOINC_LOINCCode | varchar |  |  | SI | LOINC Code |
| CTLOINC_Owner | varchar |  |  | SI | Owner |
| CTLOINC_UpdatedDate | date |  |  | SI | Updated Date |
| CTLOINC_UpdatedTime | time |  |  | SI | Updated Time |
| CTLOINC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Temperature |
| Q01ObsDR | - |  |  | SI | Temperature DR |
| Q02 | - |  |  | SI | Pulse |
| Q02ObsDR | - |  |  | SI | Pulse DR |
| Q03 | - |  |  | SI | Respiration |
| Q03ObsDR | - |  |  | SI | Respiration DR |
| Q04 | - |  |  | SI | Systolic BP |
| Q04ObsDR | - |  |  | SI | Systolic BP DR |
| Q05 | - |  |  | SI | Diastolic BP |
| Q05ObsDR | - |  |  | SI | Diastolic BP DR |
| Q06 | - |  |  | SI | AVPU - Conscious Level |
| Q06ObsDR | - |  |  | SI | AVPU - Conscious Level DR |
| Q07 | - |  |  | SI | Have you been craving amphetamines&nbsp |
| Q08 | - |  |  | SI | Have you lost interest in things or no longer take... |
| Q09 | - |  |  | SI | Have you felt your movements are slow? |
| Q10 | - |  |  | SI | Have you felt tired? |
| Q11 | - |  |  | SI | Have you had any vivid or unpleasant dreams? |
| Q12 | - |  |  | SI | Have you felt sad? |
| Q13 | - |  |  | SI | Have you felt anxious? |
| Q14 | - |  |  | SI | Have you felt agitated? |
| Q15 | - |  |  | SI | Has your appetite increased or are you eating too ... |
| Q16 | - |  |  | SI | Have you been craving for sleep or sleeping too mu... |
| Q17 | - |  |  | SI | Craving |
| Q18 | - |  |  | SI | Interest |
| Q19 | - |  |  | SI | Motor coordination |
| Q20 | - |  |  | SI | Tired |
| Q21 | - |  |  | SI | Dreams |
| Q22 | - |  |  | SI | Mood |
| Q23 | - |  |  | SI | Anxiety |
| Q24 | - |  |  | SI | Agitation |
| Q25 | - |  |  | SI | Appetite |
| Q26 | - |  |  | SI | Sleep |
| Q27 | - |  |  | SI | Score |
| Q28 | - |  |  | SI | Classification |
| Q29 | - |  |  | SI | 0 - 40 |
| Q30 | - |  |  | SI | Higher scores indicating greater severity |
| Q31 | - |  |  | SI | 0 - 40: Higher scores indicating greater severity |
| Q32 | - |  |  | SI | Total scores are indicative of increasing or decre... |
| Q33 | - |  |  | SI | Date |
| Q34 | - |  |  | SI | Time |
| Q35 | - |  |  | SI | This withdrawal questionnaire is used to monitor t... |
| Q36 | - |  |  | SI | Vital signs observation chart is required when com... |
| Q37 | - |  |  | SI | Srisurapanont M, Jarusuraisin N, Jittiwutikan J. A... |
| Q38 | - |  |  | SI | Fischer J, Roche A, Duraisingam V. AWQ – Amphetami... |
| Q39 | - |  |  | SI | https://aodscreening.flinders.edu.au/withdrawal |
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