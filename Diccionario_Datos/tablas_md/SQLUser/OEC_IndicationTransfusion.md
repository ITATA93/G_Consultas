# SQLUser.OEC_IndicationTransfusion

**Schema:** SQLUser
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INDTRANSF_RowId | bigint | PK |  | NO | - |
| INDTRANSF_Code | varchar |  |  | NO | Code |
| INDTRANSF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INDTRANSF_CreatedDate | date |  |  | SI | Created Date |
| INDTRANSF_CreatedTime | time |  |  | SI | Created Time |
| INDTRANSF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INDTRANSF_Desc | varchar |  |  | NO | Description |
| INDTRANSF_Owner | varchar |  |  | SI | Owner |
| INDTRANSF_UpdatedDate | date |  |  | SI | Updated Date |
| INDTRANSF_UpdatedTime | time |  |  | SI | Updated Time |
| INDTRANSF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Findings |
| Q02 | - |  |  | SI | Right Eye |
| Q03 | - |  |  | SI | Left Eye |
| Q04 | - |  |  | SI | Refractive error / Other |
| Q05 | - |  |  | SI | Refractive error / Other  2 |
| Q06 | - |  |  | SI | External / Lid / NLD |
| Q07 | - |  |  | SI | External / Lid / NLD  2 |
| Q08 | - |  |  | SI | Conjunctiva |
| Q09 | - |  |  | SI | Conjunctiva 2 |
| Q10 | - |  |  | SI | Cornea |
| Q11 | - |  |  | SI | Cornea 2 |
| Q12 | - |  |  | SI | Pupil |
| Q13 | - |  |  | SI | Pupil 2 |
| Q14 | - |  |  | SI | Glaucoma / AC |
| Q15 | - |  |  | SI | Glaucoma / AC  2 |
| Q16 | - |  |  | SI | Lens / Cataract |
| Q17 | - |  |  | SI | Lens / Cataract  2 |
| Q18 | - |  |  | SI | Vitreous/ Retina / Optic nerve |
| Q19 | - |  |  | SI | Vitreous/ Retina / Optic nerve  2 |
| Q20 | - |  |  | SI | EOM / Strabinus / Ambyopia |
| Q21 | - |  |  | SI | EOM / Strabinus / Ambyopia 2 |
| Q22 | - |  |  | SI | Disposition |
| Q23 | - |  |  | SI | Referred as |
| Q24 | - |  |  | SI | Patient Instructed to discontinue contact lense us... |
| Q25 | - |  |  | SI | Learning Needs |
| Q26 | - |  |  | SI | Learning needs assesed |
| Q27 | - |  |  | SI | Further teaching required |
| Q28 | - |  |  | SI | Learning needs / Teaching referral to |
| Q29 | - |  |  | SI | Date |
| Q30 | - |  |  | SI | Time |
| Q31 | - |  |  | SI | Refractive error / Other |
| Q32 | - |  |  | SI | Refractive error / Other |
| Q33 | - |  |  | SI | External / Lid / NLD |
| Q34 | - |  |  | SI | External / Lid / NLD |
| Q35 | - |  |  | SI | Conjunctiva |
| Q36 | - |  |  | SI | Conjunctiva |
| Q37 | - |  |  | SI | Cornea |
| Q38 | - |  |  | SI | Cornea |
| Q39 | - |  |  | SI | Pupil |
| Q40 | - |  |  | SI | Pupil |
| Q41 | - |  |  | SI | Glaucoma / AC |
| Q42 | - |  |  | SI | Glaucoma / AC |
| Q43 | - |  |  | SI | Lens / Cataract |
| Q44 | - |  |  | SI | Lens / Cataract |
| Q45 | - |  |  | SI | Vitreous/ Retina / Optic nerve |
| Q46 | - |  |  | SI | Vitreous/ Retina / Optic nerve |
| Q47 | - |  |  | SI | EOM / Strabinus / Ambyopia |
| Q48 | - |  |  | SI | EOM / Strabinus / Ambyopia |
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