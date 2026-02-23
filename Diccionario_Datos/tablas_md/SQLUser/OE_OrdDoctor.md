# SQLUser.OE_OrdDoctor

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ChildQ41DR | - |  |  | SI | Child Reference: Joint assessment |
| DOC_CTPCP_DR | varchar |  | FK | SI | Des Ref CTPCP |
| DOC_Childsub | double |  |  | NO | Childsub |
| DOC_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Occupation |
| Q02 | - |  |  | SI | Posture / Stresses |
| Q03 | - |  |  | SI | Off work because of current episode |
| Q04 | - |  |  | SI | If Yes, Off work from |
| Q05 | - |  |  | SI | Diagnosis |
| Q06 | - |  |  | SI | Location of pain |
| Q07 | - |  |  | SI | Visual analogue scale score |
| Q08 | - |  |  | SI | Pain started |
| Q09 | - |  |  | SI | Current pain |
| Q10 | - |  |  | SI | Cause(s) of pain |
| Q11 | - |  |  | SI | Pain occurs |
| Q12 | - |  |  | SI | Sleep disturbed by pain |
| Q13 | - |  |  | SI | Comments - pain |
| Q14 | - |  |  | SI | Recurrent problem |
| Q15 | - |  |  | SI | If Yes - Previous history and treatment |
| Q16 | - |  |  | SI | Current radiology images |
| Q17 | - |  |  | SI | Previous radiology images |
| Q18 | - |  |  | SI | Comments - history |
| Q19 | - |  |  | SI | Current health |
| Q20 | - |  |  | SI | Current conditions |
| Q21 | - |  |  | SI | Operations / Illnesses |
| Q22 | - |  |  | SI | Unexplained weight loss |
| Q23 | - |  |  | SI | Past steroid use |
| Q24 | - |  |  | SI | Dizziness |
| Q25 | - |  |  | SI | Bladder control |
| Q26 | - |  |  | SI | Gait |
| Q27 | - |  |  | SI | Pain with cough / sneeze |
| Q28 | - |  |  | SI | Cognition |
| Q29 | - |  |  | SI | Assistive devices |
| Q30 | - |  |  | SI | Pattern |
| Q31 | - |  |  | SI | Forward head posture |
| Q32 | - |  |  | SI | Thoracic kyphosis |
| Q33 | - |  |  | SI | Lumbar lordosis |
| Q34 | - |  |  | SI | Scoliosis |
| Q35 | - |  |  | SI | Lateral shifts |
| Q36 | - |  |  | SI | Hips / Knees |
| Q37 | - |  |  | SI | Feet |
| Q38 | - |  |  | SI | Palpation assessment |
| Q39 | - |  |  | SI | Comments - general orthopaedic objective |
| Q40 | - |  |  | SI | Flexion / Extention / Rotation right |
| Q42 | - |  |  | SI | Special test |
| Q43 | - |  |  | SI | Impression |
| Q44 | - |  |  | SI | Comments - joint assessment |
| Q45 | - |  |  | SI | Goal(s) |
| Q46 | - |  |  | SI | Comments - goal(s) |
| Q47 | - |  |  | SI | Plan |
| Q48 | - |  |  | SI | Comments - Plan |
| Q49 | - |  |  | SI | Home exercise program |
| Q50 | - |  |  | SI | Number of treatments per week |
| Q51 | - |  |  | SI | Number of weeks |
| Q52 | - |  |  | SI | History - Pain |
| Q53 | - |  |  | SI | History - Other |
| Q54 | - |  |  | SI | Gait |
| Q55 | - |  |  | SI | Posture |
| Q56 | - |  |  | SI | Palpation |
| Q57 | - |  |  | SI | Flexion / Extention / Rotation left |
| Q58 | - |  |  | SI | Date |
| Q59 | - |  |  | SI | Time |
| Q60 | - |  |  | SI | Patient Preference |
| Q61 | - |  |  | SI | Short Term Goal(s) |
| Q62 | - |  |  | SI | Long Term Goal(s) |
| Q63 | - |  |  | SI | Pain score |
| Q63ObsDR | - |  |  | SI | Pain score DR |
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