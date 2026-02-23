# SQLUser.ORC_OutcomeOfSurgery

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OUTS_RowId | bigint | PK |  | NO | - |
| OUTS_AnaestheticOutcome | varchar |  |  | SI | AnaestheticOutcome |
| OUTS_Code | varchar |  |  | NO | Code |
| OUTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OUTS_CreatedDate | date |  |  | SI | Created Date |
| OUTS_CreatedTime | time |  |  | SI | Created Time |
| OUTS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OUTS_DateFrom | date |  |  | SI | DateFrom |
| OUTS_DateTo | date |  |  | SI | DateTo |
| OUTS_Desc | varchar |  |  | NO | Description |
| OUTS_OperationOutcome | varchar |  |  | SI | OperationOutcome |
| OUTS_Owner | varchar |  |  | SI | Owner |
| OUTS_UpdatedDate | date |  |  | SI | Updated Date |
| OUTS_UpdatedTime | time |  |  | SI | Updated Time |
| OUTS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Postmenstrual age |
| Q04 | - |  |  | SI | Facial activity |
| Q05 | - |  |  | SI | Body movements |
| Q06 | - |  |  | SI | Quality of sleep |
| Q07 | - |  |  | SI | Quality of contact with  nurses	 |
| Q08 | - |  |  | SI | Consolability |
| Q09 | - |  |  | SI | Score |
| Q10 | - |  |  | SI | Classification |
| Q11 | - |  |  | SI | 0 - 6 |
| Q12 | - |  |  | SI | No pain |
| Q13 | - |  |  | SI | 6 - 8 |
| Q14 | - |  |  | SI | Presence of pain |
| Q15 | - |  |  | SI | 8 - 17 |
| Q16 | - |  |  | SI | Moderate to severe pain |
| Q17 | - |  |  | SI | EDIN (Échelle Douleur Inconfort Nouveau-Né, neonat... |
| Q18 | - |  |  | SI | This is a sightly modified version of the scale, i... |
| Q19 | - |  |  | SI | The modified EDIN scale has postmenstrual age (PMA... |
| Q20 | - |  |  | SI | 0 - 6: No pain |
| Q21 | - |  |  | SI | 6 - 8: Presence of pain |
| Q22 | - |  |  | SI | 8 - 17: Moderate to severe pain |
| Q23 | - |  |  | SI | The EDIN6 score is the sum total of each question ... |
| Q24 | - |  |  | SI | Score interpretation: score range is 0-17. Scores ... |
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