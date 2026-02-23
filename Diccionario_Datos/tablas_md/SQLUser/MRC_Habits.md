# SQLUser.MRC_Habits

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HAB_RowId | bigint | PK |  | NO | - |
| HAB_Code | varchar |  |  | NO | Code |
| HAB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HAB_CreatedDate | date |  |  | SI | Created Date |
| HAB_CreatedTime | time |  |  | SI | Created Time |
| HAB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HAB_DateFrom | date |  |  | SI | Date From |
| HAB_DateTo | date |  |  | SI | Date To |
| HAB_Desc | varchar |  |  | NO | Description |
| HAB_Owner | varchar |  |  | SI | Owner |
| HAB_UpdatedDate | date |  |  | SI | Updated Date |
| HAB_UpdatedTime | time |  |  | SI | Updated Time |
| HAB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Establecimiento de Salud (código de descripción) |
| Q02 | - |  |  | SI | codigo establecimiento de salud |
| Q03 | - |  |  | SI | Fecha de Registro |
| Q04 | - |  |  | SI | Médico total menor 20 años |
| Q05 | - |  |  | SI | Médico total 20 años y más |
| Q06 | - |  |  | SI | Kinesiólogo total menor 20 años |
| Q07 | - |  |  | SI | Kinesiólogo total 20 años y más |
| Q08 | - |  |  | SI | Enfermera/ o total menor 20 años |
| Q09 | - |  |  | SI | Enfermera/ o total 20 años y más |
| Q10 | - |  |  | SI | Observaciones área admisiones |
| Q12 | - |  |  | SI | Mes |
| Q13 | - |  |  | SI | Año |
| QHR | - |  |  | SI | Establecimiento de Salud |
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