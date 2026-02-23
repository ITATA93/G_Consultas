# SQLUser.LBC_FailureCode

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCFC_RowID | bigint | PK |  | NO | - |
| LBCFC_Code | varchar |  |  | SI | Code |
| LBCFC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCFC_CreatedDate | date |  |  | SI | Created Date |
| LBCFC_CreatedTime | time |  |  | SI | Created Time |
| LBCFC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCFC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCFC_DateTo | date |  |  | SI | Last day the record is active  |
| LBCFC_Desc | varchar |  |  | NO | Description |
| LBCFC_Owner | varchar |  |  | SI | Owner |
| LBCFC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCFC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCFC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Temperature |
| Q01ObsDR | - |  |  | SI | Temperature DR |
| Q02 | - |  |  | SI | Respirations |
| Q02ObsDR | - |  |  | SI | Respirations DR |
| Q03 | - |  |  | SI | Pulse |
| Q03ObsDR | - |  |  | SI | Pulse DR |
| Q04 | - |  |  | SI | Systolic BP |
| Q04ObsDR | - |  |  | SI | Systolic BP DR |
| Q05 | - |  |  | SI | Diastolic BP |
| Q05ObsDR | - |  |  | SI | Diastolic BP DR |
| Q06 | - |  |  | SI | Lochia |
| Q06ObsDR | - |  |  | SI | Lochia DR |
| Q07 | - |  |  | SI | Fundus - involuting |
| Q07ObsDR | - |  |  | SI | Fundus - involuting DR |
| Q08 | - |  |  | SI | Fundus |
| Q08ObsDR | - |  |  | SI | Fundus DR |
| Q09 | - |  |  | SI | Fundus - other observations |
| Q09ObsDR | - |  |  | SI | Fundus - other observations DR |
| Q10 | - |  |  | SI | Passed urine post delivery |
| Q10ObsDR | - |  |  | SI | Passed urine post delivery DR |
| Q11 | - |  |  | SI | Problems passing urine |
| Q11ObsDR | - |  |  | SI | Problems passing urine DR |
| Q12 | - |  |  | SI | Retaining urine |
| Q12ObsDR | - |  |  | SI | Retaining urine DR |
| Q13 | - |  |  | SI | Catheter inserted |
| Q13ObsDR | - |  |  | SI | Catheter inserted DR |
| Q14 | - |  |  | SI | Catheter in situ |
| Q14ObsDR | - |  |  | SI | Catheter in situ DR |
| Q15 | - |  |  | SI | Catheter removed |
| Q15ObsDR | - |  |  | SI | Catheter removed DR |
| Q16 | - |  |  | SI | Bowels moved |
| Q16ObsDR | - |  |  | SI | Bowels moved DR |
| Q17 | - |  |  | SI | Haemorrhoids |
| Q17ObsDR | - |  |  | SI | Haemorrhoids DR |
| Q18 | - |  |  | SI | Bowel control problems |
| Q18ObsDR | - |  |  | SI | Bowel control problems DR |
| Q19 | - |  |  | SI | Pelvic floor exercises discussed |
| Q19ObsDR | - |  |  | SI | Pelvic floor exercises discussed DR |
| Q20 | - |  |  | SI | Pelvic floor problems |
| Q20ObsDR | - |  |  | SI | Pelvic floor problems DR |
| Q21 | - |  |  | SI | Type of feeding |
| Q21ObsDR | - |  |  | SI | Type of feeding DR |
| Q22 | - |  |  | SI | Breasts |
| Q22ObsDR | - |  |  | SI | Breasts DR |
| Q23 | - |  |  | SI | Management |
| Q24 | - |  |  | SI | Perineum |
| Q24ObsDR | - |  |  | SI | Perineum DR |
| Q25 | - |  |  | SI | Wound |
| Q25ObsDR | - |  |  | SI | Wound DR |
| Q26 | - |  |  | SI | General wellbeing and pain assessment |
| Q27 | - |  |  | SI | Adequate analgesia |
| Q27ObsDR | - |  |  | SI | Adequate analgesia DR |
| Q28 | - |  |  | SI | Sutures to be removed |
| Q28ObsDR | - |  |  | SI | Sutures to be removed DR |
| Q29 | - |  |  | SI | Have sutures been removed |
| Q29ObsDR | - |  |  | SI | Have sutures been removed DR |
| Q30 | - |  |  | SI | Legs |
| Q30ObsDR | - |  |  | SI | Legs DR |
| Q31 | - |  |  | SI | Mobility and clot prevention explained |
| Q31ObsDR | - |  |  | SI | Mobility and clot prevention explained DR |
| Q32 | - |  |  | SI | Revised thrombosis risk |
| Q32ObsDR | - |  |  | SI | Revised thrombosis risk DR |
| Q33 | - |  |  | SI | Summary of assessment and care |
| Q34 | - |  |  | SI | Midwife countersigning |
| Q35 | - |  |  | SI | TEDS in situ |
| Q36 | - |  |  | SI | Details |
| Q37 | - |  |  | SI | Date |
| Q38 | - |  |  | SI | Time |
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