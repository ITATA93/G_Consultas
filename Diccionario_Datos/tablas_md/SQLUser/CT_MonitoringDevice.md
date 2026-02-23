# SQLUser.CT_MonitoringDevice

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MONDEV_RowId | bigint | PK |  | NO | - |
| MONDEV_Bed_DR | varchar |  | FK | SI | Des Ref PACBed |
| MONDEV_Code | varchar |  |  | NO | Code |
| MONDEV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MONDEV_CreatedDate | date |  |  | SI | Created Date |
| MONDEV_CreatedTime | time |  |  | SI | Created Time |
| MONDEV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MONDEV_DateFrom | date |  |  | SI | Date From |
| MONDEV_DateTo | date |  |  | SI | Date To |
| MONDEV_Desc | varchar |  |  | NO | Description |
| MONDEV_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| MONDEV_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| MONDEV_Owner | varchar |  |  | SI | Owner |
| MONDEV_Resource_DR | bigint |  | FK | SI | Des Ref RBResource |
| MONDEV_Room_DR | bigint |  | FK | SI | Des Ref PACRoom |
| MONDEV_UpdatedDate | date |  |  | SI | Updated Date |
| MONDEV_UpdatedTime | time |  |  | SI | Updated Time |
| MONDEV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Gender |
| Q02 | - |  |  | SI | Smoking status |
| Q03 | - |  |  | SI | History of motion sickness or PONV |
| Q04 | - |  |  | SI | Use of postoperative opioids |
| Q05 | - |  |  | SI | Apfel score identifies surgical patients who may b... |
| Q06 | - |  |  | SI | Score : Classification |
| Q07 | - |  |  | SI | 0: 10% Risk of PONV in 24 hours |
| Q08 | - |  |  | SI | 1: 21% Risk of PONV in 24 hours |
| Q09 | - |  |  | SI | 2 : 39% Risk of PONV in 24 hours |
| Q10 | - |  |  | SI | 3 : 61% Risk of PONV in 24 hours |
| Q11 | - |  |  | SI | 4 : 79% Risk of PONV in 24 hours |
| Q12 | - |  |  | SI | Date of assessment |
| Q13 | - |  |  | SI | Time of assessment |
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