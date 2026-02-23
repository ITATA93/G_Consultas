# SQLUser.PAC_ResidualTumour

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESTUM_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bundle Compliance Percentage |
| Q04 | - |  |  | SI | % |
| Q05 | - |  |  | SI | Has the patient been identified? |
| Q06 | - |  |  | SI | Has the correct indication for system flushing bee... |
| Q07 | - |  |  | SI | Has it been verified that the patient is informed ... |
| Q08 | - |  |  | SI | Has all the necessary material for the procedure b... |
| Q09 | - |  |  | SI | Was hand hygiene performed according to protocol? |
| Q10 | - |  |  | SI | Has the infusion line been clamped and the needlef... |
| Q11 | - |  |  | SI | Has the connection cone been disinfected? |
| Q12 | - |  |  | SI | Has a new needlefree connector been applied and th... |
| Q13 | - |  |  | SI | Was the pulsatile flush performed with 10ml of phy... |
| Q14 | - |  |  | SI | Has the port protector been applied? |
| Q15 | - |  |  | SI | Notes |
| Q16 | - |  |  | SI | Score |
| Q17 | - |  |  | SI | Classification |
| Q18 | - |  |  | SI | 0 - 100 |
| Q19 | - |  |  | SI | Higher percentages represent higher compliance to ... |
| Q20 | - |  |  | SI | 0 - 100: Higher percentages represent higher compl... |
| Q21 | - |  |  | SI | CVCs are the leading cause of device-related bacte... |
| Q22 | - |  |  | SI | The aim of th Periodic flushing of the Central Ven... |
| Q23 | - |  |  | SI | Were clean non-sterile gloves used? |
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
| RESTUM_Code | varchar |  |  | NO | Code |
| RESTUM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESTUM_CreatedDate | date |  |  | SI | Created Date |
| RESTUM_CreatedTime | time |  |  | SI | Created Time |
| RESTUM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESTUM_Desc | varchar |  |  | NO | Description |
| RESTUM_Owner | varchar |  |  | SI | Owner |
| RESTUM_UpdatedDate | date |  |  | SI | Updated Date |
| RESTUM_UpdatedTime | time |  |  | SI | Updated Time |
| RESTUM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*