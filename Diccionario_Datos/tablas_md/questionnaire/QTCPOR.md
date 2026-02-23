# questionnaire.QTCPOR

> Phacoemulsification Operation Report

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Phacoemulsification Operation Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Eye |
| Q04 | varchar |  |  | SI | Anaesthetic |
| Q05 | varchar |  |  | SI | Preparation and drape |
| Q06 | varchar |  |  | SI | Main incision |
| Q07 | varchar |  |  | SI | Other incision notes |
| Q08 | varchar |  |  | SI | Paracentesis |
| Q09 | varchar |  |  | SI | Other paracentesis notes |
| Q10 | varchar |  |  | SI | Continuous curvilinear capsulo-rhexis (CCC) |
| Q10a | varchar |  |  | SI | Continuous curvilinear capsulorhexis (CCC) |
| Q11 | varchar |  |  | SI | Hydrodissection |
| Q12 | varchar |  |  | SI | Phacoemulsification |
| Q13 | varchar |  |  | SI | Irrigation / Aspiration |
| Q14 | varchar |  |  | SI | Vision blue  |
| Q15 | varchar |  |  | SI | Intraocular lens implant |
| Q16 | varchar |  |  | SI | Position |
| Q17 | varchar |  |  | SI | Toric lens |
| Q18 | numeric |  |  | SI | Axis of toric (degrees) |
| Q19 | varchar |  |  | SI | Aphakic |
| Q20 | varchar |  |  | SI | Viscoelastic out |
| Q21 | varchar |  |  | SI | Intracameral cephazolin |
| Q22 | varchar |  |  | SI | Wound hydration |
| Q23 | varchar |  |  | SI | Suture |
| Q24 | numeric |  |  | SI | Number of sutures |
| Q25 | varchar |  |  | SI | Type of sutures |
| Q26 | varchar |  |  | SI | Subconjunctival dexamethasone |
| Q27 | varchar |  |  | SI | Pad |
| Q28 | varchar |  |  | SI | Notes |
| Q29 | varchar |  |  | SI | IOL specification |
| Q30 | varchar |  |  | SI | IOL model |
| Q31 | varchar |  |  | SI | Power |
| Q32 | varchar |  |  | SI | Cylinder |
| Q33 | varchar |  |  | SI | IOL specification notes |
| Q34 | varchar |  |  | SI | Operation Complication(s) |
| Q35 | varchar |  |  | SI |  Operation complication(s) |
| Q36 | varchar |  |  | SI | Operation complication notes |
| Q37 | varchar |  |  | SI | new annotated image |
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