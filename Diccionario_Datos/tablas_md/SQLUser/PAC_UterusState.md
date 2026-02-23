# SQLUser.PAC_UterusState

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| UTER_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q10 | - |  |  | SI | Cry - individual behaviours |
| Q11 | - |  |  | SI | Consolability |
| Q12 | - |  |  | SI | Consolability - individual behaviours |
| Q13 | - |  |  | SI | Guidelines |
| Q14 | - |  |  | SI | Each of the five categories (F) Face |
| Q15 | - |  |  | SI | Individualise the tool: |
| Q16 | - |  |  | SI | The nurse should review the descriptors within eac... |
| Q17 | - |  |  | SI | Each of the five categories (F) Face |
| Q18 | - |  |  | SI | Patients who are awake: |
| Q19 | - |  |  | SI | Observe for at least 1-3 minutes. Observe legs and... |
| Q20 | - |  |  | SI | Patients who are asleep: |
| Q21 | - |  |  | SI | Observe for at least 5 minutes. Observe body and l... |
| Q22 | - |  |  | SI | Revised FLACC (r-FLACC) scale is an observational ... |
| Q3 | - |  |  | SI | Face |
| Q4 | - |  |  | SI | Face - individual behaviours |
| Q5 | - |  |  | SI | Legs |
| Q6 | - |  |  | SI | Legs - individual behaviours |
| Q7 | - |  |  | SI | Activity |
| Q8 | - |  |  | SI | Activity - individual behaviours |
| Q9 | - |  |  | SI | Cry |
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
| UTER_Code | varchar |  |  | NO | Code |
| UTER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| UTER_CreatedDate | date |  |  | SI | Created Date |
| UTER_CreatedTime | time |  |  | SI | Created Time |
| UTER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| UTER_DateFrom | date |  |  | SI | Date From |
| UTER_DateTo | date |  |  | SI | Date To |
| UTER_Desc | varchar |  |  | NO | Description |
| UTER_Owner | varchar |  |  | SI | Owner |
| UTER_UpdatedDate | date |  |  | SI | Updated Date |
| UTER_UpdatedTime | time |  |  | SI | Updated Time |
| UTER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*