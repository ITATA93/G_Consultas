# SQLUser.MHC_TransferType

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHCTT_RowId | bigint | PK |  | NO | - |
| MHCTT_Code | varchar |  |  | NO | Code |
| MHCTT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHCTT_CreatedDate | date |  |  | SI | Created Date |
| MHCTT_CreatedTime | time |  |  | SI | Created Time |
| MHCTT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHCTT_DateFrom | date |  |  | SI | Date From |
| MHCTT_DateTo | date |  |  | SI | Date To |
| MHCTT_Desc | varchar |  |  | NO | Description |
| MHCTT_Owner | varchar |  |  | SI | Owner |
| MHCTT_UpdatedDate | date |  |  | SI | Updated Date |
| MHCTT_UpdatedTime | time |  |  | SI | Updated Time |
| MHCTT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Ev. puesto de trabajo |
| Q02 | - |  |  | SI | Barreras Arquitectonicas |
| Q03 | - |  |  | SI | AVD afectas |
| Q04 | - |  |  | SI | AIVD Afectadas |
| Q05 | - |  |  | SI | Orientación |
| Q06 | - |  |  | SI | Ev. Emocional |
| Q07 | - |  |  | SI | Participación Social / Act. Física |
| Q08 | - |  |  | SI | Intereses |
| Q09 | - |  |  | SI | Uso Férulas / Ortesis |
| Q10 | - |  |  | SI | Orientación |
| Q11 | - |  |  | SI | Memoria |
| Q12 | - |  |  | SI | Atención y cálculo |
| Q13 | - |  |  | SI | Memoria diferida |
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