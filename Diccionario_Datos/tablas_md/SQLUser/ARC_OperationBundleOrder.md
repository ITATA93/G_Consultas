# SQLUser.ARC_OperationBundleOrder

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORD_ParRef | bigint | PK |  | NO | ARC_Operation Parent Reference |
| ORD_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| ORD_Anaesthetists | varchar |  |  | SI | Anaesthetists |
| ORD_Childsub | double |  |  | NO | Childsub |
| ORD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORD_CreatedDate | date |  |  | SI | Created Date |
| ORD_CreatedTime | time |  |  | SI | Created Time |
| ORD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORD_DateFrom | date |  |  | SI | Date From |
| ORD_DateTo | date |  |  | SI | Date To |
| ORD_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| ORD_OperStaffRole_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffRole |
| ORD_PercExternalCP | double |  |  | SI | Percentage for External Care Provider |
| ORD_PercInternalCP | double |  |  | SI | Percentage for Internal Care Provider |
| ORD_PercOther | double |  |  | SI | Percentage Other |
| ORD_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| ORD_RowId | varchar |  |  | NO | - |
| ORD_Surgeon | varchar |  |  | SI | Surgeon |
| ORD_UpdatedDate | date |  |  | SI | Updated Date |
| ORD_UpdatedTime | time |  |  | SI | Updated Time |
| ORD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Tipo de técnica |
| Q02 | - |  |  | SI | Lugar del cuerpo |
| Q03 | - |  |  | SI | Procedimiento específico |
| Q04 | - |  |  | SI | Preparación |
| Q05 | - |  |  | SI | Tolerancia |
| Q06 | - |  |  | SI | Incidentes |
| Q07 | - |  |  | SI | Detalle Otro |
| Q08 | - |  |  | SI | Detalle Incidentes |
| Q09 | - |  |  | SI | EVA previo |
| Q10 | - |  |  | SI | EVA posterior |
| Q11 | - |  |  | SI | ROM previo |
| Q12 | - |  |  | SI | ROM posterior |
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