# questionnaire.QGXXXOPH24

> Uveitis Assessment Form

**Schema:** questionnaire
**Columnas:** 107
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Uveitis Assessment Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Normal in Right Eye |
| Q02 | varchar |  |  | SI | Normal in Left Eye |
| Q03 | varchar |  |  | SI | Notes |
| Q04 | varchar |  |  | SI | Normal in Right Eye |
| Q05 | varchar |  |  | SI | Normal in Left Eye |
| Q06 | varchar |  |  | SI | Notes |
| Q07 | varchar |  |  | SI | Clarity |
| Q08 | varchar |  |  | SI | Clarity 2 |
| Q09 | varchar |  |  | SI | Right Eye |
| Q10 | varchar |  |  | SI | Left Eye |
| Q11 | varchar |  |  | SI | KPS |
| Q12 | varchar |  |  | SI | KPS 2 |
| Q13 | varchar |  |  | SI | Notes |
| Q14 | varchar |  |  | SI | Anterior Chamber |
| Q15 | varchar |  |  | SI | Right Eye |
| Q16 | varchar |  |  | SI | Left Eye |
| Q17 | varchar |  |  | SI | Depth |
| Q18 | varchar |  |  | SI | Depth |
| Q19 | varchar |  |  | SI | Notes |
| Q20 | varchar |  |  | SI | Cells |
| Q21 | varchar |  |  | SI | Cells 2 |
| Q22 | varchar |  |  | SI | Flare |
| Q23 | varchar |  |  | SI | Flare 2 |
| Q24 | varchar |  |  | SI | Pupils / Iris |
| Q25 | varchar |  |  | SI | Normal condition |
| Q26 | varchar |  |  | SI | Normal conditin 2 |
| Q27 | varchar |  |  | SI | Right Eye |
| Q28 | varchar |  |  | SI | Left Eye |
| Q29 | varchar |  |  | SI | desc |
| Q30 | varchar |  |  | SI | desc 2 |
| Q31 | varchar |  |  | SI | Notes |
| Q32 | varchar |  |  | SI | Lens |
| Q33 | varchar |  |  | SI | Right Eye |
| Q34 | varchar |  |  | SI | Left Eye |
| Q35 | varchar |  |  | SI | Lens conditions |
| Q36 | varchar |  |  | SI | Lens conditions 2 |
| Q37 | varchar |  |  | SI | Vitreous |
| Q38 | varchar |  |  | SI | Right Eye |
| Q39 | varchar |  |  | SI | Left Eye |
| Q40 | varchar |  |  | SI | Conditions |
| Q41 | varchar |  |  | SI | conditions 2 |
| Q42 | varchar |  |  | SI | Notes |
| Q43 | varchar |  |  | SI | Retina |
| Q44 | varchar |  |  | SI | Right Eye |
| Q45 | varchar |  |  | SI | Left Eye |
| Q46 | varchar |  |  | SI | Condition |
| Q47 | varchar |  |  | SI | conditions 2 |
| Q48 | varchar |  |  | SI | Notes  |
| Q49 | varchar |  |  | SI | Optic Nerve |
| Q50 | varchar |  |  | SI | Right Eye |
| Q51 | varchar |  |  | SI | Left Eye |
| Q52 | varchar |  |  | SI | Conditions |
| Q53 | varchar |  |  | SI | condition 2 |
| Q54 | varchar |  |  | SI | Notes |
| Q55 | varchar |  |  | SI | Uveitis Assessment |
| Q56 | varchar |  |  | SI | Onset |
| Q57 | varchar |  |  | SI | Course |
| Q58 | varchar |  |  | SI | Duration  |
| Q59 | varchar |  |  | SI | Pathology |
| Q60 | varchar |  |  | SI | Laterality |
| Q61 | varchar |  |  | SI | Diagnosis |
| Q62 | varchar |  |  | SI | Anatomical |
| Q63 | varchar |  |  | SI | Etiological |
| Q64 | varchar |  |  | SI | Image |
| Q65 | varchar |  |  | SI | Conditions |
| Q66 | varchar |  |  | SI | Conditions |
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