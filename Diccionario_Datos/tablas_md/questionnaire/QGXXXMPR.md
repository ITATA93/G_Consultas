# questionnaire.QGXXXMPR

> Perineal repair

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Perineal repair

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Type of repair |
| Q02 | varchar |  |  | SI | Skin closure |
| Q02ObsDR | varchar |  | FK | SI | Skin closure DR |
| Q03 | varchar |  |  | SI | Anaesthesia |
| Q04 | varchar |  |  | SI | Technique |
| Q05 | varchar |  |  | SI | Rectal exam before suturing |
| Q05ObsDR | varchar |  | FK | SI | Rectal exam before suturing DR |
| Q06 | varchar |  |  | SI | Rectal exam after suturing |
| Q06ObsDR | varchar |  | FK | SI | Rectal exam after suturing DR |
| Q07 | varchar |  |  | SI | Haemostasis achieved |
| Q07ObsDR | varchar |  | FK | SI | Haemostasis achieved DR |
| Q08 | varchar |  |  | SI | Swabs and needles correct |
| Q08ObsDR | varchar |  | FK | SI | Swabs and needles correct DR |
| Q09 | varchar |  |  | SI | Advised on perineal care |
| Q09ObsDR | varchar |  | FK | SI | Advised on perineal care DR |
| Q10 | varchar |  |  | SI | Supervised by |
| Q11 | varchar |  |  | SI | Analgesia |
| Q11ObsDR | varchar |  | FK | SI | Analgesia DR |
| Q12 | varchar |  |  | SI | Disruption of external anal sphincter |
| Q12ObsDR | varchar |  | FK | SI | Disruption of external anal sphincter DR |
| Q13 | varchar |  |  | SI | Disruption of internal anal sphincter |
| Q13ObsDR | varchar |  | FK | SI | Disruption of internal anal sphincter DR |
| Q14 | varchar |  |  | SI | Method of repair of external anal sphincter |
| Q14ObsDR | varchar |  | FK | SI | Method of repair of external anal sphincter DR |
| Q15 | varchar |  |  | SI | Technique |
| Q16 | varchar |  |  | SI | PV exam after repair |
| Q16ObsDR | varchar |  | FK | SI | PV exam after repair DR |
| Q17 | varchar |  |  | SI | PR exam after repair |
| Q17ObsDR | varchar |  | FK | SI | PR exam after repair DR |
| Q18 | varchar |  |  | SI | Checked by |
| Q19 | varchar |  |  | SI | Advised on perineal care |
| Q19ObsDR | varchar |  | FK | SI | Advised on perineal care DR |
| Q20 | varchar |  |  | SI | Follow-up appointment made |
| Q20ObsDR | varchar |  | FK | SI | Follow-up appointment made DR |
| Q21 | varchar |  |  | SI | Management plan |
| Q22 | varchar |  |  | SI | Midwife countersigning |
| Q23 | time |  |  | SI | Start time |
| Q24 | time |  |  | SI | Finish time |
| Q25 | varchar |  |  | SI | Additional repairs required |
| Q26 | varchar |  |  | SI | Repaired by |
| Q27 | varchar |  |  | SI | Suture material |
| Q27ObsDR | varchar |  | FK | SI | Suture material DR |
| Q28 | varchar |  |  | SI | Estimated blood loss (ml) |
| Q28ObsDR | varchar |  | FK | SI | Estimated blood loss (ml) DR |
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