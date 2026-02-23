# questionnaire.QGXXXOPH16

> ER Finding

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuestionario/Formulario**. Plantilla de evaluación clínica estructurada. *(ER Finding)*

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Right Eye |
| Q02 | varchar |  |  | SI | Left Eye |
| Q03 | varchar |  |  | SI | Refractive error / Other |
| Q04 | varchar |  |  | SI | Refractive error / Other 2 |
| Q05 | varchar |  |  | SI | External / Lid / NLD |
| Q06 | varchar |  |  | SI | External  / Lid / NLD  |
| Q07 | varchar |  |  | SI | Conjuctiva  |
| Q08 | varchar |  |  | SI | Conjuctiva 2 |
| Q09 | varchar |  |  | SI | Cornea  |
| Q10 | varchar |  |  | SI | Cornea 2 |
| Q11 | varchar |  |  | SI | Pupil  |
| Q12 | varchar |  |  | SI | Pupil 2 |
| Q13 | varchar |  |  | SI | Pupil 2 |
| Q14 | varchar |  |  | SI | Glaucoma / AC |
| Q15 | varchar |  |  | SI | Glaucoma / AC 2 |
| Q16 | varchar |  |  | SI | Lens / Cataract |
| Q17 | varchar |  |  | SI | Lens / Cataract 2 |
| Q18 | varchar |  |  | SI | Vitreous / Retina / Optic nerve |
| Q19 | varchar |  |  | SI | Vitreous / Retina / Optic nerve 2 |
| Q20 | varchar |  |  | SI | Disposition |
| Q21 | varchar |  |  | SI | EOM / Strabinus / Ambyopia |
| Q22 | varchar |  |  | SI | EOM / Strabinus / Ambyopia 2 |
| Q23 | varchar |  |  | SI | Disposition |
| Q24 | date |  |  | SI | Date |
| Q25 | time |  |  | SI | Time |
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