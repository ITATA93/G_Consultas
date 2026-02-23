# SQLUser.OEC_CancelReason

**Schema:** SQLUser
**Columnas:** 119
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANCREA_RowId | bigint | PK |  | NO | - |
| CANCREA_Code | varchar |  |  | NO | Code |
| CANCREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CANCREA_CreatedDate | date |  |  | SI | Created Date |
| CANCREA_CreatedTime | time |  |  | SI | Created Time |
| CANCREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANCREA_Desc | varchar |  |  | NO | Description |
| CANCREA_Owner | varchar |  |  | SI | Owner |
| CANCREA_UpdatedDate | date |  |  | SI | Updated Date |
| CANCREA_UpdatedTime | time |  |  | SI | Updated Time |
| CANCREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Perineum |
| Q02 | - |  |  | SI | None Identified |
| Q03 | - |  |  | SI | PR performed if perineum intact |
| Q04 | - |  |  | SI | If declined, reason |
| Q05 | - |  |  | SI | Trauma |
| Q06 | - |  |  | SI | Location |
| Q07 | - |  |  | SI | Indication for episiotomy |
| Q08 | - |  |  | SI | Repair required |
| Q09 | - |  |  | SI | Discussed with mother |
| Q10 | - |  |  | SI | Consent obtained |
| Q11 | - |  |  | SI | Catheterised |
| Q12 | - |  |  | SI | Indwelling |
| Q13 | - |  |  | SI | PR prior to repair |
| Q14 | - |  |  | SI | Tampon |
| Q15 | - |  |  | SI | Venue for repair |
| Q16 | - |  |  | SI | Repair by |
| Q17 | - |  |  | SI | Start time |
| Q18 | - |  |  | SI | Start date / time |
| Q19 | - |  |  | SI | Swab count |
| Q20 | - |  |  | SI | Needle count |
| Q21 | - |  |  | SI | Signature 1 |
| Q22 | - |  |  | SI | Signature 2 |
| Q23 | - |  |  | SI | Anaesthetic |
| Q24 | - |  |  | SI | Lignocaine (mls) |
| Q25 | - |  |  | SI | Suture material |
| Q26 | - |  |  | SI | Technique |
| Q33 | - |  |  | SI | Finish date / time |
| Q34 | - |  |  | SI | Finish time |
| Q35 | - |  |  | SI | Haemostasis |
| Q36 | - |  |  | SI | Sutures for removal |
| Q37 | - |  |  | SI | Vaginal pack in situ |
| Q38 | - |  |  | SI | Analgesia |
| Q39 | - |  |  | SI | PV examination |
| Q40 | - |  |  | SI | PR examination |
| Q41 | - |  |  | SI | If declined, reason |
| Q42 | - |  |  | SI | Tampon removed |
| Q43 | - |  |  | SI | Antibiotics |
| Q44 | - |  |  | SI | Laxatives |
| Q45 | - |  |  | SI | Swab count |
| Q46 | - |  |  | SI | Needle count |
| Q47 | - |  |  | SI | Count performed by |
| Q48 | - |  |  | SI | Signature 1 |
| Q49 | - |  |  | SI | Signature 2 |
| Q50 | - |  |  | SI | For postnatal consultant review |
| Q51 | - |  |  | SI | Comment |
| Q52 | - |  |  | SI | Pre-repair |
| Q53 | - |  |  | SI | Advice given |
| Q54 | - |  |  | SI | Post repair |
| Q55 | - |  |  | SI | Date |
| Q56 | - |  |  | SI | Time |
| Q57 | - |  |  | SI | None Identified |
| Q58 | - |  |  | SI | PR performed if perineum intact |
| Q59 | - |  |  | SI | Discussed with mother |
| Q60 | - |  |  | SI | Consent obtained |
| Q61 | - |  |  | SI | Catheterized |
| Q62 | - |  |  | SI | Indwelling |
| Q63 | - |  |  | SI | PR prior to repair |
| Q64 | - |  |  | SI | Tampon |
| Q65 | - |  |  | SI | Haemostasis |
| Q66 | - |  |  | SI | Sutures for removal |
| Q67 | - |  |  | SI | Vaginal pack in situ |
| Q68 | - |  |  | SI | Analgesia |
| Q69 | - |  |  | SI | PV examination |
| Q70 | - |  |  | SI | PR examination |
| Q71 | - |  |  | SI | Tampon removed |
| Q72 | - |  |  | SI | Antibiotics |
| Q73 | - |  |  | SI | Laxatives |
| Q74 | - |  |  | SI | For postnatal consultant review |
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