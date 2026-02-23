# SQLUser.OEC_AlertReason

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALR_RowId | bigint | PK |  | NO | - |
| ALR_Code | varchar |  |  | NO | Code |
| ALR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALR_CreatedDate | date |  |  | SI | Created Date |
| ALR_CreatedTime | time |  |  | SI | Created Time |
| ALR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALR_DateFrom | date |  |  | SI | DateFrom |
| ALR_DateTo | date |  |  | SI | DateTo |
| ALR_Desc | varchar |  |  | NO | Description |
| ALR_Owner | varchar |  |  | SI | Owner |
| ALR_UpdatedDate | date |  |  | SI | Updated Date |
| ALR_UpdatedTime | time |  |  | SI | Updated Time |
| ALR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Type of repair |
| Q02 | - |  |  | SI | Skin closure |
| Q02ObsDR | - |  |  | SI | Skin closure DR |
| Q03 | - |  |  | SI | Anaesthesia |
| Q04 | - |  |  | SI | Technique |
| Q05 | - |  |  | SI | Rectal exam before suturing |
| Q05ObsDR | - |  |  | SI | Rectal exam before suturing DR |
| Q06 | - |  |  | SI | Rectal exam after suturing |
| Q06ObsDR | - |  |  | SI | Rectal exam after suturing DR |
| Q07 | - |  |  | SI | Haemostasis achieved |
| Q07ObsDR | - |  |  | SI | Haemostasis achieved DR |
| Q08 | - |  |  | SI | Swabs and needles correct |
| Q08ObsDR | - |  |  | SI | Swabs and needles correct DR |
| Q09 | - |  |  | SI | Advised on perineal care |
| Q09ObsDR | - |  |  | SI | Advised on perineal care DR |
| Q10 | - |  |  | SI | Supervised by |
| Q11 | - |  |  | SI | Analgesia |
| Q11ObsDR | - |  |  | SI | Analgesia DR |
| Q12 | - |  |  | SI | Disruption of external anal sphincter |
| Q12ObsDR | - |  |  | SI | Disruption of external anal sphincter DR |
| Q13 | - |  |  | SI | Disruption of internal anal sphincter |
| Q13ObsDR | - |  |  | SI | Disruption of internal anal sphincter DR |
| Q14 | - |  |  | SI | Method of repair of external anal sphincter |
| Q14ObsDR | - |  |  | SI | Method of repair of external anal sphincter DR |
| Q15 | - |  |  | SI | Technique |
| Q16 | - |  |  | SI | PV exam after repair |
| Q16ObsDR | - |  |  | SI | PV exam after repair DR |
| Q17 | - |  |  | SI | PR exam after repair |
| Q17ObsDR | - |  |  | SI | PR exam after repair DR |
| Q18 | - |  |  | SI | Checked by |
| Q19 | - |  |  | SI | Advised on perineal care |
| Q19ObsDR | - |  |  | SI | Advised on perineal care DR |
| Q20 | - |  |  | SI | Follow-up appointment made |
| Q20ObsDR | - |  |  | SI | Follow-up appointment made DR |
| Q21 | - |  |  | SI | Management plan |
| Q22 | - |  |  | SI | Midwife countersigning |
| Q23 | - |  |  | SI | Start time |
| Q24 | - |  |  | SI | Finish time |
| Q25 | - |  |  | SI | Additional repairs required |
| Q26 | - |  |  | SI | Repaired by |
| Q27 | - |  |  | SI | Suture material |
| Q27ObsDR | - |  |  | SI | Suture material DR |
| Q28 | - |  |  | SI | Estimated blood loss (ml) |
| Q28ObsDR | - |  |  | SI | Estimated blood loss (ml) DR |
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