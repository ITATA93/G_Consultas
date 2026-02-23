# SQLUser.PAC_Appeal

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPEAL_RowId | bigint | PK |  | NO | - |
| APPEAL_Code | varchar |  |  | NO | Code |
| APPEAL_CreatedDate | date |  |  | SI | Created Date |
| APPEAL_CreatedTime | time |  |  | SI | Created Time |
| APPEAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPEAL_DateFrom | date |  |  | SI | DateFrom |
| APPEAL_DateTo | date |  |  | SI | DateTo |
| APPEAL_Desc | varchar |  |  | NO | Description |
| APPEAL_UpdatedDate | date |  |  | SI | Updated Date |
| APPEAL_UpdatedTime | time |  |  | SI | Updated Time |
| APPEAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Disease |
| Q04 | - |  |  | SI | Surgical interventions |
| Q05 | - |  |  | SI | Ostomy |
| Q06 | - |  |  | SI | Surgical interventions |
| Q07 | - |  |  | SI | Ostomy |
| Q08 | - |  |  | SI | Extra intestinal manifestations |
| Q09 | - |  |  | SI | Extra intestinal manifestations, notes |
| Q10 | - |  |  | SI | Fragility |
| Q11 | - |  |  | SI | Fragility, notes |
| Q12 | - |  |  | SI | Significant comorbidity |
| Q13 | - |  |  | SI | Significant comorbidity, notes |
| Q14 | - |  |  | SI | Mesalazine therapy |
| Q15 | - |  |  | SI | Mesalazine, notes |
| Q16 | - |  |  | SI | Immunosuppressants therapy |
| Q17 | - |  |  | SI | Immunosuppressants therapy, notes |
| Q18 | - |  |  | SI | Steroids therapy |
| Q19 | - |  |  | SI | Steroids therapy, notes |
| Q20 | - |  |  | SI | Experimental drug therapy |
| Q21 | - |  |  | SI | Experimental drug therapy, notes |
| Q22 | - |  |  | SI | Biological drug therapy |
| Q23 | - |  |  | SI | Single biological drug ongoing therapy, notes |
| Q24 | - |  |  | SI | Single biological drug previous therapy, notes |
| Q25 | - |  |  | SI | Double biological drug ongoing therapy, notes |
| Q26 | - |  |  | SI | Double biological drug previous therapy, notes |
| Q27 | - |  |  | SI | Remember to use the register therapy before access... |
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