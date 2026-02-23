# SQLUser.ARC_LabTestSet

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCTS_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| ARCTS_BloodProductGroup_DR | bigint |  | FK | SI | Blood Product Group |
| ARCTS_BloodProduct_DR | bigint |  | FK | SI | Blood Product |
| ARCTS_Childsub | double |  |  | NO | Childsub |
| ARCTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCTS_Conflict_DR | varchar |  | FK | SI | Conflict object DR
To store the conflicted Order ... |
| ARCTS_CreatedDate | date |  |  | SI | Created Date |
| ARCTS_CreatedTime | time |  |  | SI | Created Time |
| ARCTS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCTS_DateFrom | date |  |  | SI | Date From |
| ARCTS_DateTo | date |  |  | SI | Date To |
| ARCTS_LabSite_DR | bigint |  | FK | SI | Des Ref CTLOC_DR (Lab Site only) |
| ARCTS_RowId | varchar |  |  | NO | - |
| ARCTS_SpecimenContainerCollection_DR | bigint |  | FK | SI | Specimen Container Collection
If the Collection b... |
| ARCTS_TestSet_DR | bigint |  | FK | NO | TestSet Code |
| ARCTS_UpdatedDate | date |  |  | SI | Updated Date |
| ARCTS_UpdatedTime | time |  |  | SI | Updated Time |
| ARCTS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ARCTS_UseTestSetCollectionsDefault | varchar |  |  | SI | Flag to UseTestSetItemCollectionsDefault |
| Q01 | - |  |  | SI | Grado de Movilidad |
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