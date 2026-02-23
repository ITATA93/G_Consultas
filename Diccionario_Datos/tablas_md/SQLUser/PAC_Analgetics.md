# SQLUser.PAC_Analgetics

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANLG_RowId | bigint | PK |  | NO | - |
| ANLG_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ANLG_Code | varchar |  |  | NO | Code |
| ANLG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANLG_CreatedDate | date |  |  | SI | Created Date |
| ANLG_CreatedTime | time |  |  | SI | Created Time |
| ANLG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANLG_DateFrom | date |  |  | SI | DateFrom |
| ANLG_DateTo | date |  |  | SI | DateTo |
| ANLG_Desc | varchar |  |  | NO | Description |
| ANLG_Owner | varchar |  |  | SI | Owner |
| ANLG_PainMgmt | varchar |  |  | SI | Checkbox for Angiography Pain Management Restricti... |
| ANLG_UpdatedDate | date |  |  | SI | Updated Date |
| ANLG_UpdatedTime | time |  |  | SI | Updated Time |
| ANLG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of treatment |
| Q04 | - |  |  | SI | Arrive time |
| Q05 | - |  |  | SI | Treatment number |
| Q06 | - |  |  | SI | Reason for referral |
| Q07 | - |  |  | SI | Other referral reason |
| Q08 | - |  |  | SI | Planned treatment depth |
| Q09 | - |  |  | SI | Other treatment depth |
| Q10 | - |  |  | SI | Treatment outcomes |
| Q11 | - |  |  | SI | Reason for missed treatment |
| Q12 | - |  |  | SI | Patient departure time |
| Q13 | - |  |  | SI | Total treatment time (minutes) |
| Q14 | - |  |  | SI | Primary attendant inside chamber |
| Q15 | - |  |  | SI | Second attendant inside chamber |
| Q16 | - |  |  | SI | Primary attendant outside chamber |
| Q17 | - |  |  | SI | Technician |
| Q18 | - |  |  | SI | Chamber compression number |
| Q19 | - |  |  | SI | Treatment complications |
| Q20 | - |  |  | SI | Barotrauma affected site |
| Q21 | - |  |  | SI | CNS oxygen toxicity duration |
| Q22 | - |  |  | SI | Other complications |
| Q23 | - |  |  | SI | Hyperbaric treatment notes |
| Q24 | - |  |  | SI | CNS oxygen toxicity seizure duration |
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