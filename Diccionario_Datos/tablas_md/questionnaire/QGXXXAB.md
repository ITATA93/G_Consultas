# questionnaire.QGXXXAB

> Abdomen Examination

**Schema:** questionnaire
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Abdomen Examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Surgical scars |
| Q01N | varchar |  |  | SI | Note |
| Q01ObsDR | varchar |  | FK | SI | Surgical scars DR |
| Q03 | varchar |  |  | SI | Ostomy |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Ostomy DR |
| Q05 | varchar |  |  | SI | Globular |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Globular DR |
| Q07 | varchar |  |  | SI | Ascites |
| Q07N | varchar |  |  | SI | Note |
| Q07ObsDR | varchar |  | FK | SI | Ascites DR |
| Q09 | varchar |  |  | SI | Lattices venous |
| Q09N | varchar |  |  | SI | Note |
| Q09ObsDR | varchar |  | FK | SI | Lattices venous DR |
| Q11 | varchar |  |  | SI | Abdominal tenderness |
| Q11L | varchar |  |  | SI | Location |
| Q11N | varchar |  |  | SI | Note |
| Q11ObsDR | varchar |  | FK | SI | Abdominal tenderness DR |
| Q11R | varchar |  |  | SI | Radiation |
| Q15 | varchar |  |  | SI | Blumberg sign |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Blumberg sign DR |
| Q17 | varchar |  |  | SI | Murphys sign |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Murphys sign DR |
| Q19 | varchar |  |  | SI | Sign of jordan |
| Q19N | varchar |  |  | SI | Note |
| Q19ObsDR | varchar |  | FK | SI | Sign of jordan DR |
| Q21 | varchar |  |  | SI | Peritonism |
| Q21N | varchar |  |  | SI | Note |
| Q21ObsDR | varchar |  | FK | SI | Peritonism DR |
| Q23 | varchar |  |  | SI | Peristalsis |
| Q23N | varchar |  |  | SI | Note |
| Q23ObsDR | varchar |  | FK | SI | Peristalsis DR |
| Q25 | varchar |  |  | SI | Palpable liver |
| Q25N | varchar |  |  | SI | Note |
| Q25ObsDR | varchar |  | FK | SI | Palpable liver DR |
| Q27 | varchar |  |  | SI | Palpable spleen |
| Q27N | varchar |  |  | SI | Note |
| Q27ObsDR | varchar |  | FK | SI | Palpable spleen DR |
| Q29 | varchar |  |  | SI | Palpable abdominal masses |
| Q29N | varchar |  |  | SI | Note |
| Q29ObsDR | varchar |  | FK | SI | Palpable abdominal masses DR |
| Q31 | varchar |  |  | SI | Bladder distention |
| Q31N | varchar |  |  | SI | Note |
| Q31ObsDR | varchar |  | FK | SI | Bladder distention DR |
| Q33 | varchar |  |  | SI | Hernia |
| Q33N | varchar |  |  | SI | Note |
| Q33ObsDR | varchar |  | FK | SI | Hernia DR |
| Q35 | varchar |  |  | SI | Inguinal lymphadenopathy |
| Q35N | varchar |  |  | SI | Note |
| Q35ObsDR | varchar |  | FK | SI | Inguinal lymphadenopathy DR |
| Q37 | varchar |  |  | SI | Other |
| Q39 | varchar |  |  | SI | Caput medusae |
| Q39ObsDR | varchar |  | FK | SI | Caput medusae DR |
| Q50 | varchar |  |  | SI | Rebound tenderness |
| Q50L | varchar |  |  | SI | Location |
| Q50N | varchar |  |  | SI | Note |
| Q50ObsDR | varchar |  | FK | SI | Rebound tenderness DR |
| Q50R | varchar |  |  | SI | Radiation |
| Q51 | varchar |  |  | SI | Guarding |
| Q51N | varchar |  |  | SI | Note |
| Q51ObsDR | varchar |  | FK | SI | Guarding DR |
| Q52 | varchar |  |  | SI | Flank tenderness |
| Q52N | varchar |  |  | SI | Note |
| Q52ObsDR | varchar |  | FK | SI | Flank tenderness DR |
| Q52a | varchar |  |  | SI | Flank tenderness |
| Q52aObsDR | varchar |  | FK | SI | Flank tenderness DR |
| Q53 | varchar |  |  | SI | Rectal examination done |
| Q53N | varchar |  |  | SI | Note |
| Q54N | varchar |  |  | SI | Note |
| Q55 | varchar |  |  | SI | Bowel sounds |
| Q55N | varchar |  |  | SI | Note |
| Q55ObsDR | varchar |  | FK | SI | Bowel sounds DR |
| Q56 | varchar |  |  | SI | Caput medusae |
| Q56N | varchar |  |  | SI | Note |
| Q56ObsDR | varchar |  | FK | SI | Caput medusae DR |
| Q57 | varchar |  |  | SI | Rectal examination |
| Q60 | varchar |  |  | SI | Appearance of abdomen |
| Q60N | varchar |  |  | SI | Note |
| Q60ObsDR | varchar |  | FK | SI | Appearance of abdomen DR |
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