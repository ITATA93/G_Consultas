# SQLUser.PAC_Diabetes

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIAB_RowId | bigint | PK |  | NO | - |
| DIAB_Code | varchar |  |  | NO | Code |
| DIAB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DIAB_CreatedDate | date |  |  | SI | Created Date |
| DIAB_CreatedTime | time |  |  | SI | Created Time |
| DIAB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DIAB_Desc | varchar |  |  | NO | Description |
| DIAB_Owner | varchar |  |  | SI | Owner |
| DIAB_UpdatedDate | date |  |  | SI | Updated Date |
| DIAB_UpdatedTime | time |  |  | SI | Updated Time |
| DIAB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Reintubation |
| Q02 | - |  |  | SI | Non-invasive ventilation |
| Q03 | - |  |  | SI | Invasive ventiltion |
| Q04 | - |  |  | SI | Continuous positive airway pressure (CPAP) |
| Q05 | - |  |  | SI | Renal replacement therapy |
| Q06 | - |  |  | SI | Vassopressors / inatropes |
| Q07 | - |  |  | SI | Cardiopulmonary resuscitation (CPR) |
| Q08 | - |  |  | SI | Other care will be provided |
| Q09 | - |  |  | SI | Rationale |
| Q10 | - |  |  | SI | Review date |
| Q11 | - |  |  | SI | Discussed with patient |
| Q12 | - |  |  | SI | Discussed with relatives |
| Q13 | - |  |  | SI | Discussed with other team members |
| Q14 | - |  |  | SI | Discussed with referring team |
| Q15 | - |  |  | SI | Summary of discussions |
| Q16 | - |  |  | SI | Limitation decision changed / reversed- rationale |
| Q17 | - |  |  | SI | Reintubation |
| Q18 | - |  |  | SI | Non-invasive ventilation |
| Q19 | - |  |  | SI | Invasive ventiltion |
| Q20 | - |  |  | SI | Continuous positive airway pressure (CPAP) |
| Q21 | - |  |  | SI | Renal replacement therapy |
| Q22 | - |  |  | SI | Vassopressors / inatropes |
| Q23 | - |  |  | SI | Cardiopulmonary resuscitation (CPR) |
| Q24 | - |  |  | SI | Other care will Not be provided |
| Q25 | - |  |  | SI | Discussed with other team members |
| Q26 | - |  |  | SI | Name |
| Q27 | - |  |  | SI | Discussed with referring team |
| Q28 | - |  |  | SI | Name |
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