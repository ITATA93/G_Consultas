# questionnaire.QGXXXOPH27

> OPH Screening Finding

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* OPH Screening Finding

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Findings |
| Q02 | varchar |  |  | SI | Right Eye |
| Q03 | varchar |  |  | SI | Left Eye |
| Q04 | varchar |  |  | SI | Refractive error / Other  |
| Q05 | varchar |  |  | SI | Refractive error / Other  2 |
| Q06 | varchar |  |  | SI | External / Lid / NLD  |
| Q07 | varchar |  |  | SI | External / Lid / NLD  2 |
| Q08 | varchar |  |  | SI | Conjunctiva |
| Q09 | varchar |  |  | SI | Conjunctiva 2 |
| Q10 | varchar |  |  | SI | Cornea |
| Q11 | varchar |  |  | SI | Cornea 2 |
| Q12 | varchar |  |  | SI | Pupil |
| Q13 | varchar |  |  | SI | Pupil 2 |
| Q14 | varchar |  |  | SI | Glaucoma / AC  |
| Q15 | varchar |  |  | SI | Glaucoma / AC  2 |
| Q16 | varchar |  |  | SI | Lens / Cataract  |
| Q17 | varchar |  |  | SI | Lens / Cataract  2 |
| Q18 | varchar |  |  | SI | Vitreous/ Retina / Optic nerve  |
| Q19 | varchar |  |  | SI | Vitreous/ Retina / Optic nerve  2 |
| Q20 | varchar |  |  | SI | EOM / Strabinus / Ambyopia |
| Q21 | varchar |  |  | SI | EOM / Strabinus / Ambyopia 2 |
| Q22 | varchar |  |  | SI | Disposition |
| Q23 | varchar |  |  | SI | Referred as |
| Q24 | varchar |  |  | SI | Patient Instructed to discontinue contact lense us... |
| Q25 | varchar |  |  | SI | Learning Needs |
| Q26 | varchar |  |  | SI | Learning needs assesed |
| Q27 | varchar |  |  | SI | Further teaching required |
| Q28 | varchar |  |  | SI | Learning needs / Teaching referral to |
| Q29 | date |  |  | SI | Date |
| Q30 | time |  |  | SI | Time |
| Q31 | varchar |  |  | SI | Refractive error / Other |
| Q32 | varchar |  |  | SI | Refractive error / Other |
| Q33 | varchar |  |  | SI | External / Lid / NLD |
| Q34 | varchar |  |  | SI | External / Lid / NLD |
| Q35 | varchar |  |  | SI | Conjunctiva |
| Q36 | varchar |  |  | SI | Conjunctiva |
| Q37 | varchar |  |  | SI | Cornea |
| Q38 | varchar |  |  | SI | Cornea |
| Q39 | varchar |  |  | SI | Pupil |
| Q40 | varchar |  |  | SI | Pupil |
| Q41 | varchar |  |  | SI | Glaucoma / AC |
| Q42 | varchar |  |  | SI | Glaucoma / AC |
| Q43 | varchar |  |  | SI | Lens / Cataract |
| Q44 | varchar |  |  | SI | Lens / Cataract |
| Q45 | varchar |  |  | SI | Vitreous/ Retina / Optic nerve |
| Q46 | varchar |  |  | SI | Vitreous/ Retina / Optic nerve |
| Q47 | varchar |  |  | SI | EOM / Strabinus / Ambyopia |
| Q48 | varchar |  |  | SI | EOM / Strabinus / Ambyopia |
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