# questionnaire.QGXXXIOIC

> Intra-Operative Items Count

**Schema:** questionnaire
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intra-Operative Items Count

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01Q1 | varchar |  |  | SI | Item |
| Q01Q3 | numeric |  |  | SI | 1st Count |
| Q01Q4 | numeric |  |  | SI | 2nd Count |
| Q01Q5 | numeric |  |  | SI | 3rd Count |
| Q01Q6 | bit |  |  | SI | Complete |
| Q01Q7 | bit |  |  | SI | Incomplete |
| Q02 | varchar |  |  | SI | Resolution of Incomplete Count |
| Q03 | varchar |  |  | SI | Surgeon Informed |
| Q03Q2 | numeric |  |  | SI | Start |
| Q04 | varchar |  |  | SI | X-ray Performed |
| Q05 | varchar |  |  | SI | Incident Report Filed |
| Q06 | bit |  |  | SI | Sponge And Instruments Resolved  |
| Q07 | varchar |  |  | SI | Scrub Nurse: |
| Q08 | varchar |  |  | SI | Circulating Nurse: |
| Q09 | varchar |  |  | SI | Notes |
| Q10 | varchar |  |  | SI | Notes |
| Q11 | varchar |  |  | SI | Notes |
| Q12 | varchar |  |  | SI | Specify other: |
| Q20 | varchar |  |  | SI | Equipments |
| Q21 | varchar |  |  | SI | Scrub Nurse: |
| Q22 | varchar |  |  | SI | Circulating Nurse:  |
| Q23 | varchar |  |  | SI | Type |
| Q24 | varchar |  |  | SI | Initial Count (Start) |
| Q25 | varchar |  |  | SI | Add |
| Q26 | varchar |  |  | SI | Final Count (Total) |
| Q27 | varchar |  |  | SI | Final Count (Expected) |
| Q28 | varchar |  |  | SI | Used |
| Q29 | varchar |  |  | SI | Raytec (2x2) |
| Q30 | numeric |  |  | SI | Raytec (2x2) Initial  |
| Q31 | numeric |  |  | SI | Raytec (2x2) Add |
| Q32 | varchar |  |  | SI | Raytec (2x2) Expected |
| Q33 | numeric |  |  | SI | Raytec 2x2 Final Count |
| Q34 | varchar |  |  | SI | Raytec (4x4) |
| Q35 | numeric |  |  | SI | Raytec (4x4) I |
| Q36 | numeric |  |  | SI | Raytec (4x4) A |
| Q37 | varchar |  |  | SI | Raytec (4x4) F.E. |
| Q38 | numeric |  |  | SI | Raytec (4x4) F C |
| Q39 | varchar |  |  | SI | Gauze pad long  |
| Q40 | numeric |  |  | SI | Gauze pad long I |
| Q41 | numeric |  |  | SI | Gauze pad long A |
| Q42 | varchar |  |  | SI | Gauze pad long F E |
| Q43 | numeric |  |  | SI | Gauze pad long F C |
| Q44 | varchar |  |  | SI | Roll swab |
| Q45 | numeric |  |  | SI | Roll swab I |
| Q46 | numeric |  |  | SI | Roll swab A |
| Q47 | varchar |  |  | SI | Roll swab F E |
| Q48 | numeric |  |  | SI | Roll F C |
| Q49 | varchar |  |  | SI | ABD swab |
| Q50 | numeric |  |  | SI | ABD swab I |
| Q51 | numeric |  |  | SI | ABD swab A |
| Q52 | varchar |  |  | SI | ABD swab F E |
| Q53 | numeric |  |  | SI | ABD Swab F C |
| Q54 | varchar |  |  | SI | Peanut  |
| Q55 | numeric |  |  | SI | Peanut I |
| Q56 | numeric |  |  | SI | Peanut A |
| Q57 | varchar |  |  | SI | Peanut F E |
| Q58 | numeric |  |  | SI | Peanut F C  |
| Q59 | varchar |  |  | SI | Cottonoid |
| Q60 | numeric |  |  | SI | Cottonoid I |
| Q61 | numeric |  |  | SI | Cottonoid A |
| Q62 | varchar |  |  | SI | Cottonoid F E |
| Q63 | numeric |  |  | SI | Cottonoid F C |
| Q64 | varchar |  |  | SI | Blades  |
| Q65 | numeric |  |  | SI | Blades F C |
| Q66 | numeric |  |  | SI | Blades I |
| Q67 | numeric |  |  | SI | Blades A |
| Q68 | varchar |  |  | SI | Blades F E |
| Q69 | varchar |  |  | SI | Needle |
| Q70 | numeric |  |  | SI | Needle I |
| Q71 | numeric |  |  | SI | Needle A |
| Q72 | varchar |  |  | SI | Needle F E |
| Q73 | numeric |  |  | SI | Needle F C |
| Q74 | varchar |  |  | SI | Guide wire / Misc. Items |
| Q75 | numeric |  |  | SI | Guide wire / Misc. Items I |
| Q76 | numeric |  |  | SI | Guide wire / Misc. Items A |
| Q77 | varchar |  |  | SI | Guide wire / Misc. Items F E  |
| Q78 | numeric |  |  | SI | Guide wire / Misc. Items F C |
| Q79 | date |  |  | SI | Date |
| Q80 | time |  |  | SI | Time |
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