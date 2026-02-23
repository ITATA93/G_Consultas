# SQLUser.CT_State

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSTT_RowId | bigint | PK |  | NO | - |
| CTSTT_Code | varchar |  |  | NO | State Code |
| CTSTT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTSTT_CreatedDate | date |  |  | SI | Created Date |
| CTSTT_CreatedTime | time |  |  | SI | Created Time |
| CTSTT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTSTT_Desc | varchar |  |  | NO | State Description |
| CTSTT_Owner | varchar |  |  | SI | Owner |
| CTSTT_UpdatedDate | date |  |  | SI | Updated Date |
| CTSTT_UpdatedTime | time |  |  | SI | Updated Time |
| CTSTT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Admission risk marker |
| Q04 | - |  |  | SI | Blood urea (mmol/L) |
| Q05 | - |  |  | SI | Haemoglobin for men (g/L) |
| Q06 | - |  |  | SI | Haemoglobin for women (g/L) |
| Q07 | - |  |  | SI | Systolic blood pressure (mmHg) |
| Q08 | - |  |  | SI | Other markers |
| Q09 | - |  |  | SI | Sex |
| Q10 | - |  |  | SI | • Patients with a blatchford score of greater than... |
| Q11 | - |  |  | SI | The Blatchford score, which relies on only clinica... |
| Q12 | - |  |  | SI | Blatchford Score |
| Q13 | - |  |  | SI | Other markers |
| Q14 | - |  |  | SI | • Patients with a Blatchford score of zero are con... |
| Q15 | - |  |  | SI | Other markers |
| Q16 | - |  |  | SI | Pulse rate ≥ 100 (per min) |
| Q17 | - |  |  | SI | Presentation with melaena |
| Q18 | - |  |  | SI | Presentation with syncope |
| Q19 | - |  |  | SI | Hepatic disease |
| Q20 | - |  |  | SI | Cardiac failure |
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