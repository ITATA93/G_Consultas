# SQLUser.PAC_EpisiotomyCondition

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPIC_RowId | bigint | PK |  | NO | - |
| EPIC_Code | varchar |  |  | NO | Code |
| EPIC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EPIC_CreatedDate | date |  |  | SI | Created Date |
| EPIC_CreatedTime | time |  |  | SI | Created Time |
| EPIC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPIC_DateFrom | date |  |  | SI | Date From |
| EPIC_DateTo | date |  |  | SI | Date To |
| EPIC_Desc | varchar |  |  | NO | Description |
| EPIC_Owner | varchar |  |  | SI | Owner |
| EPIC_UpdatedDate | date |  |  | SI | Updated Date |
| EPIC_UpdatedTime | time |  |  | SI | Updated Time |
| EPIC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Facial expression |
| Q02 | - |  |  | SI | Body movements |
| Q03 | - |  |  | SI | Compliance with the ventilator (intubated patient) |
| Q04 | - |  |  | SI | Muscle tension |
| Q05 | - |  |  | SI | Physiological parameter |
| Q06 | - |  |  | SI | Directives of use of the MCPOT |
| Q07 | - |  |  | SI | 1. The patient must be observed at rest for one mi... |
| Q08 | - |  |  | SI | 2. The patient should be observed during nocicepti... |
| Q09 | - |  |  | SI | 3. The patient should be evaluated before and at t... |
| Q10 | - |  |  | SI | 4. For the rating of the MCPOT, the patient should... |
| Q11 | - |  |  | SI | 5. The patient should be attributed a score for ea... |
| Q12 | - |  |  | SI | (when performing passive flexion and extension of ... |
| Q13 | - |  |  | SI | Score |
| Q14 | - |  |  | SI | Classification |
| Q15 | - |  |  | SI | ≤ 2 |
| Q16 | - |  |  | SI | > 2 |
| Q17 | - |  |  | SI | <= 2: Minimal to no pain |
| Q18 | - |  |  | SI | >  2: Unacceptable level of pain |
| Q19 | - |  |  | SI | Minimal to no pain |
| Q20 | - |  |  | SI | Unacceptable level of pain |
| Q21 | - |  |  | SI | The Modified Critical Care Pain Observation Tool (... |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Time |
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