# SQLUser.ARC_BillBodyParts

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBP_RowId | bigint | PK |  | NO | - |
| BBP_Code | varchar |  |  | NO | Code |
| BBP_CreatedDate | date |  |  | SI | Created Date |
| BBP_CreatedTime | time |  |  | SI | Created Time |
| BBP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BBP_Desc | varchar |  |  | NO | Description |
| BBP_UpdatedDate | date |  |  | SI | Updated Date |
| BBP_UpdatedTime | time |  |  | SI | Updated Time |
| BBP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02 | - |  |  | SI | MES |
| Q03 | - |  |  | SI | AÑO |
| Q04 | - |  |  | SI | Total Número de Cupos Programados |
| Q05 | - |  |  | SI | Total Número de Cupos Utilizados |
| Q06 | - |  |  | SI | Total Número de Cupos Disponibles |
| Q07 | - |  |  | SI | Número de Cupos Programados |
| Q08 | - |  |  | SI | Número de Cupos Utilizados |
| Q09 | - |  |  | SI | Número de Cupos Disponibles |
| Q10 | - |  |  | SI | N° de Cupos CAM INV Adicionales Programados |
| Q11 | - |  |  | SI | N° de Cupos CAM INV Adicionales&nbsp |
| Q12 | - |  |  | SI | N° de Cupos CAM INV Adicionales Disponibles |
| Q13 | - |  |  | SI | N° de Cupos CAM. INV.&nbsp |
| Q14 | - |  |  | SI | N° de Cupos CAM. INV. Utilizados |
| Q15 | - |  |  | SI | N° de Cupos CAM. INV.&nbsp |
| QHR | - |  |  | SI | ESTABLECIMIENTO |
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