# SQLUser.OEC_FormAlternativeReason

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FAR_RowId | bigint | PK |  | NO | - |
| FAR_Code | varchar |  |  | NO | Code |
| FAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FAR_CreatedDate | date |  |  | SI | Created Date |
| FAR_CreatedTime | time |  |  | SI | Created Time |
| FAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FAR_DateFrom | date |  |  | SI | Date From |
| FAR_DateTo | date |  |  | SI | Date To |
| FAR_Desc | varchar |  |  | NO | Description |
| FAR_Owner | varchar |  |  | SI | Owner |
| FAR_UpdatedDate | date |  |  | SI | Updated Date |
| FAR_UpdatedTime | time |  |  | SI | Updated Time |
| FAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Informed consent? |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Red Reflex abnormal |
| Q04 | - |  |  | SI | Right Eye |
| Q05 | - |  |  | SI | Left Eye |
| Q06 | - |  |  | SI | red |
| Q07 | - |  |  | SI | red2 |
| Q08 | - |  |  | SI | Notes |
| Q09 | - |  |  | SI | Notes |
| Q10 | - |  |  | SI | Vitrous abnormal |
| Q11 | - |  |  | SI | Right Eye |
| Q12 | - |  |  | SI | Left Eye |
| Q13 | - |  |  | SI | Vit |
| Q14 | - |  |  | SI | Vit2 |
| Q15 | - |  |  | SI | Notes |
| Q16 | - |  |  | SI | Notes |
| Q17 | - |  |  | SI | Optic Nerve abnormal |
| Q18 | - |  |  | SI | Manula abnormal |
| Q19 | - |  |  | SI | Right eye |
| Q20 | - |  |  | SI | Left Eye |
| Q21 | - |  |  | SI | Macula |
| Q22 | - |  |  | SI | macula 2 |
| Q23 | - |  |  | SI | notes |
| Q24 | - |  |  | SI | notes 2 |
| Q25 | - |  |  | SI | Vessles abnormal |
| Q26 | - |  |  | SI | Vessles |
| Q27 | - |  |  | SI | Vessles 2 |
| Q28 | - |  |  | SI | notes |
| Q29 | - |  |  | SI | notes 2 |
| Q30 | - |  |  | SI | Periphery anormal |
| Q31 | - |  |  | SI | peri |
| Q32 | - |  |  | SI | Peri 2 |
| Q33 | - |  |  | SI | Notes |
| Q34 | - |  |  | SI | Notes 2 |
| Q35 | - |  |  | SI | Time |
| Q36 | - |  |  | SI | Retina |
| Q37 | - |  |  | SI | Retina 2 |
| Q40 | - |  |  | SI | Detachment Type |
| Q41 | - |  |  | SI | Detachment type 2 |
| Q42 | - |  |  | SI | PVR grading |
| Q43 | - |  |  | SI | PVR grading |
| Q44 | - |  |  | SI | Notes |
| Q441 | - |  |  | SI | Right Eye |
| Q45 | - |  |  | SI | Notes 2 |
| Q451 | - |  |  | SI | Left Eye |
| Q46 | - |  |  | SI | Optic Nerve |
| Q47 | - |  |  | SI | Optic Nerve 2 |
| Q48 | - |  |  | SI | Macula Abnormal |
| Q49 | - |  |  | SI | Vitreous Abnormal |
| Q50 | - |  |  | SI | Vitreous normal left |
| Q51 | - |  |  | SI | Optic nerve abnormal left |
| Q52 | - |  |  | SI | Retina abnormal 2 |
| Q53 | - |  |  | SI | Manula abnormal 2 |
| Q54 | - |  |  | SI | Vessles abnomal |
| Q55 | - |  |  | SI | Periphery abnormal |
| Q56 | - |  |  | SI | Periphery abnormal 2 |
| Q57 | - |  |  | SI | Red reflex abnorml 2 |
| Q58 | - |  |  | SI | Image Annotation |
| Q59 | - |  |  | SI | Image Link |
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