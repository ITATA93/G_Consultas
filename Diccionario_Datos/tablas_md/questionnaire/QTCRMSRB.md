# questionnaire.QTCRMSRB

> Review of Motor / Sensory Regional Blocks

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Review of Motor / Sensory Regional Blocks

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Block region under review |
| Q04 | varchar |  |  | SI | Eye block |
| Q05 | varchar |  |  | SI | Other eye block details |
| Q06 | varchar |  |  | SI | Brachial plexus block |
| Q07 | varchar |  |  | SI | Other brachial plexus block details |
| Q08 | varchar |  |  | SI | Forearm block |
| Q09 | varchar |  |  | SI | Other forearm block details |
| Q10 | varchar |  |  | SI | Back block |
| Q11 | varchar |  |  | SI | Other back block details |
| Q12 | varchar |  |  | SI | Chest block |
| Q13 | varchar |  |  | SI | Other chest block details |
| Q14 | varchar |  |  | SI | Abdominal block |
| Q15 | varchar |  |  | SI | Other abdominal block details |
| Q16 | varchar |  |  | SI | Lower limb block |
| Q17 | varchar |  |  | SI | Other lower limb block details |
| Q18 | varchar |  |  | SI | Other block region under review details |
| Q19 | varchar |  |  | SI | Laterality |
| Q21 | varchar |  |  | SI | Secondary block performed |
| Q22 | varchar |  |  | SI | Secondary block region under review |
| Q23 | varchar |  |  | SI | Secondary eye block |
| Q24 | varchar |  |  | SI | Other secondary eye block details |
| Q25 | varchar |  |  | SI | Secondary brachial plexus block |
| Q26 | varchar |  |  | SI | Other secondary brachial plexus block details |
| Q27 | varchar |  |  | SI | Secondary forearm block |
| Q28 | varchar |  |  | SI | Other secondary forearm block details |
| Q29 | varchar |  |  | SI | Secondary back block |
| Q30 | varchar |  |  | SI | Other secondary back block details |
| Q31 | varchar |  |  | SI | Secondary chest block |
| Q32 | varchar |  |  | SI | Other secondary chest block details |
| Q33 | varchar |  |  | SI | Secondary abdominal block |
| Q34 | varchar |  |  | SI | Other secondary abdominal block details |
| Q35 | varchar |  |  | SI | Secondary lower limb block |
| Q36 | varchar |  |  | SI | Other secondary lower limb block details |
| Q37 | varchar |  |  | SI | Specify other secondary details |
| Q38 | varchar |  |  | SI | Laterality (secondary block) |
| Q39 | varchar |  |  | SI | Secondary Site Check |
| Q41 | varchar |  |  | SI | Pain score at rest |
| Q41ObsDR | varchar |  | FK | SI | Pain score at rest DR |
| Q42 | varchar |  |  | SI | Current pain |
| Q43 | varchar |  |  | SI | Patient's pain description |
| Q44 | varchar |  |  | SI | Numbness, reduced feeling or reduced sensation |
| Q45 | varchar |  |  | SI | Patient's sensation description |
| Q46 | varchar |  |  | SI | Weakness |
| Q47 | varchar |  |  | SI | Patient's weakness description |
| Q48 | varchar |  |  | SI | Review notes |
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