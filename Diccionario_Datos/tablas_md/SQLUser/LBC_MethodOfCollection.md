# SQLUser.LBC_MethodOfCollection

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCMC_RowID | bigint | PK |  | NO | - |
| LBCMC_Code | varchar |  |  | NO | Code |
| LBCMC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCMC_Comments | varchar |  |  | SI | Comments |
| LBCMC_CreatedDate | date |  |  | SI | Created Date |
| LBCMC_CreatedTime | time |  |  | SI | Created Time |
| LBCMC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCMC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCMC_DateTo | date |  |  | SI | Last day the record is active  |
| LBCMC_Desc | varchar |  |  | NO | Description |
| LBCMC_Owner | varchar |  |  | SI | Owner |
| LBCMC_PCode_DR | bigint |  | FK | SI | P-Code DR |
| LBCMC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCMC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCMC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date and time cardiorespiratory support was withdr... |
| Q04 | - |  |  | SI | Time cardiorespiratory support was withdrawn |
| Q05 | - |  |  | SI | Spontaneous movement |
| Q06 | - |  |  | SI | Breathing |
| Q07 | - |  |  | SI | Circulation |
| Q08 | - |  |  | SI | Date / Time of death |
| Q09 | - |  |  | SI | Time of death |
| Q10 | - |  |  | SI | Clinician |
| Q11 | - |  |  | SI | Signature |
| Q11UDt | - |  |  | SI | Signature Last Updated Date |
| Q11UTm | - |  |  | SI | Signature Last Updated Time |
| Q12 | - |  |  | SI | Absent arterial pulsatility for a minimum of 3 min... |
| Q13 | - |  |  | SI | OR in cases without an arterial line, by electrica... |
| Q14 | - |  |  | SI | Definition of Absence of Circulation |
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