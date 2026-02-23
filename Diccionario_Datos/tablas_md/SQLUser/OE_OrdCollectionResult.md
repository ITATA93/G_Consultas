# SQLUser.OE_OrdCollectionResult

**Schema:** SQLUser
**Columnas:** 118
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEL_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| DEL_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DEL_Childsub | double |  |  | NO | Childsub |
| DEL_Comments | varchar |  |  | SI | Comments |
| DEL_Date | date |  |  | SI | Date |
| DEL_DeliveredTo | varchar |  |  | SI | Delivered To |
| DEL_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| DEL_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| DEL_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| DEL_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| DEL_Method_DR | bigint |  | FK | SI | Des Ref Method |
| DEL_RowId | varchar |  |  | NO | - |
| DEL_Time | time |  |  | SI | Time |
| DEL_User | varchar |  |  | SI | User |
| Q01 | - |  |  | SI | Physiotherapy - Casting Documentation |
| Q02 | - |  |  | SI | Cast Number |
| Q03 | - |  |  | SI | AIM/S OF CASTING |
| Q06 | - |  |  | SI | Staff / Family / Carer at appointment |
| Q09 | - |  |  | SI | PRECAUTIONS |
| Q10 | - |  |  | SI | Please circle |
| Q11 | - |  |  | SI | PLAN IF REQUIRED (e.g. Orthotics / wheelchair / ai... |
| Q12 | - |  |  | SI | STANDING, GAIT & FUNCTIONAL ASSESSMENT |
| Q13 | - |  |  | SI | RANGE OF MOVEMENT PRE CAST |
| Q14 | - |  |  | SI | Right |
| Q15 | - |  |  | SI | R1 |
| Q16 | - |  |  | SI | R2 |
| Q17 | - |  |  | SI | Left |
| Q18 | - |  |  | SI | R1 |
| Q19 | - |  |  | SI | R2 |
| Q20 | - |  |  | SI | Knee extension |
| Q21 | - |  |  | SI | Knee extension Right R1 |
| Q22 | - |  |  | SI | Knee extension Right R2 |
| Q23 | - |  |  | SI | Knee extension Left R1 |
| Q24 | - |  |  | SI | Knee extension Left R2 |
| Q25 | - |  |  | SI | Ankle DF (Knee 90°) |
| Q26 | - |  |  | SI | Ankle DF (Knee 90°) Right R1 |
| Q27 | - |  |  | SI | Ankle DF (Knee 90°) Right R2 |
| Q28 | - |  |  | SI | Ankle DF (Knee 90°) Left R1 |
| Q29 | - |  |  | SI | Ankle DF (Knee 90°) Left R2 |
| Q30 | - |  |  | SI | Ankle DF (Knee 0°) Right R1 |
| Q31 | - |  |  | SI | Ankle DF (Knee 0°) Right R2 |
| Q32 | - |  |  | SI | Ankle DF (Knee 0°) Left R1 |
| Q33 | - |  |  | SI | Ankle DF (Knee 0°) Left R2 |
| Q34 | - |  |  | SI | Other Measures |
| Q35 | - |  |  | SI | Strength Measuring Chair (SMC) |
| Q44 | - |  |  | SI | CAST APPLICATION |
| Q45 | - |  |  | SI | Under layer |
| Q46 | - |  |  | SI | Wrapping materials |
| Q47 | - |  |  | SI | Size |
| Q48 | - |  |  | SI | Backslab |
| Q49 | - |  |  | SI | Backslab Description |
| Q50 | - |  |  | SI | POST CASTING REVIEW |
| Q51 | - |  |  | SI | POP heel wedge |
| Q52 | - |  |  | SI | PLAN FOR CAST REMOVAL |
| Q53 | - |  |  | SI | Date |
| Q54 | - |  |  | SI | Plan Detail |
| Q55 | - |  |  | SI | Additional comments (e.g. AFOs/ Splints) |
| Q56 | - |  |  | SI | Review Plan |
| Q57 | - |  |  | SI | Ankle DF (Knee 0°) |
| Q58 | - |  |  | SI | Type of information provided to patient / parents |
| Q59 | - |  |  | SI | Comment |
| Q60 | - |  |  | SI | Date |
| Q61 | - |  |  | SI | Time |
| Q63 | - |  |  | SI | Knee extension |
| Q64 | - |  |  | SI | Ankle DF (Knee 90°) |
| Q65 | - |  |  | SI | Ankle DF (Knee 0°) |
| Q66 | - |  |  | SI | R1 |
| Q67 | - |  |  | SI | R1 |
| Q68 | - |  |  | SI | R1 |
| Q69 | - |  |  | SI | R1 |
| Q70 | - |  |  | SI | R1 |
| Q71 | - |  |  | SI | R1 |
| Q72 | - |  |  | SI | R2 |
| Q73 | - |  |  | SI | R2 |
| Q74 | - |  |  | SI | R2 |
| Q75 | - |  |  | SI | R2 |
| Q76 | - |  |  | SI | R2 |
| Q77 | - |  |  | SI | R2 |
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