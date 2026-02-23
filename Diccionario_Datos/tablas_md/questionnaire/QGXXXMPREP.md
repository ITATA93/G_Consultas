# questionnaire.QGXXXMPREP

> Perineal repair details

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perineal repair details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Perineum |
| Q02 | bit |  |  | SI | None Identified |
| Q03 | bit |  |  | SI | PR performed if perineum intact |
| Q04 | varchar |  |  | SI | If declined, reason |
| Q05 | varchar |  |  | SI | Trauma |
| Q06 | varchar |  |  | SI | Location |
| Q07 | varchar |  |  | SI | Indication for episiotomy |
| Q08 | varchar |  |  | SI | Repair required |
| Q09 | bit |  |  | SI | Discussed with mother |
| Q10 | bit |  |  | SI | Consent obtained |
| Q11 | bit |  |  | SI | Catheterised |
| Q12 | bit |  |  | SI | Indwelling |
| Q13 | bit |  |  | SI | PR prior to repair |
| Q14 | bit |  |  | SI | Tampon |
| Q15 | varchar |  |  | SI | Venue for repair |
| Q16 | varchar |  |  | SI | Repair by |
| Q17 | time |  |  | SI | Start time |
| Q18 | date |  |  | SI | Start date / time |
| Q19 | numeric |  |  | SI | Swab count |
| Q20 | numeric |  |  | SI | Needle count |
| Q21 | varchar |  |  | SI | Signature 1 |
| Q22 | varchar |  |  | SI | Signature 2 |
| Q23 | varchar |  |  | SI | Anaesthetic |
| Q24 | numeric |  |  | SI | Lignocaine (mls) |
| Q25 | varchar |  |  | SI | Suture material |
| Q26 | varchar |  |  | SI | Technique |
| Q33 | date |  |  | SI | Finish date / time |
| Q34 | time |  |  | SI | Finish time |
| Q35 | bit |  |  | SI | Haemostasis |
| Q36 | bit |  |  | SI | Sutures for removal |
| Q37 | bit |  |  | SI | Vaginal pack in situ |
| Q38 | bit |  |  | SI | Analgesia |
| Q39 | bit |  |  | SI | PV examination |
| Q40 | bit |  |  | SI | PR examination |
| Q41 | varchar |  |  | SI | If declined, reason |
| Q42 | bit |  |  | SI | Tampon removed |
| Q43 | bit |  |  | SI | Antibiotics |
| Q44 | bit |  |  | SI | Laxatives |
| Q45 | numeric |  |  | SI | Swab count |
| Q46 | numeric |  |  | SI | Needle count |
| Q47 | varchar |  |  | SI | Count performed by |
| Q48 | varchar |  |  | SI | Signature 1 |
| Q49 | varchar |  |  | SI | Signature 2 |
| Q50 | bit |  |  | SI | For postnatal consultant review |
| Q51 | varchar |  |  | SI | Comment |
| Q52 | varchar |  |  | SI | Pre-repair |
| Q53 | varchar |  |  | SI | Advice given |
| Q54 | varchar |  |  | SI | Post repair |
| Q55 | date |  |  | SI | Date |
| Q56 | time |  |  | SI | Time |
| Q57 | varchar |  |  | SI | None Identified |
| Q58 | varchar |  |  | SI | PR performed if perineum intact |
| Q59 | varchar |  |  | SI | Discussed with mother |
| Q60 | varchar |  |  | SI | Consent obtained |
| Q61 | varchar |  |  | SI | Catheterized  |
| Q62 | varchar |  |  | SI | Indwelling |
| Q63 | varchar |  |  | SI | PR prior to repair |
| Q64 | varchar |  |  | SI | Tampon |
| Q65 | varchar |  |  | SI | Haemostasis |
| Q66 | varchar |  |  | SI | Sutures for removal |
| Q67 | varchar |  |  | SI | Vaginal pack in situ |
| Q68 | varchar |  |  | SI | Analgesia |
| Q69 | varchar |  |  | SI | PV examination |
| Q70 | varchar |  |  | SI | PR examination |
| Q71 | varchar |  |  | SI | Tampon removed |
| Q72 | varchar |  |  | SI | Antibiotics |
| Q73 | varchar |  |  | SI | Laxatives |
| Q74 | varchar |  |  | SI | For postnatal consultant review |
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