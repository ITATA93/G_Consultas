# SQLUser.ARC_ItemConflict

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONFL_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| CONFL_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| CONFL_AgePeriodInclusive | varchar |  |  | SI | AgePeriodInclusive |
| CONFL_AlertMsg | varchar |  |  | SI | Alert Message hs for 83716 PC |
| CONFL_Childsub | double |  |  | NO | Childsub |
| CONFL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONFL_CreatedDate | date |  |  | SI | Created Date |
| CONFL_CreatedTime | time |  |  | SI | Created Time |
| CONFL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONFL_DateFrom | date |  |  | SI | Date From |
| CONFL_DateTo | date |  |  | SI | Date To |
| CONFL_Diagnosis_DR | bigint |  | FK | SI | Diagnosis Des Ref MRCICDDx hs for 83716 PC |
| CONFL_DrugInteractSeverity_DR | bigint |  | FK | SI | Des Ref PHCDrugInteractSeverity |
| CONFL_Gender_DR | bigint |  | FK | SI | Des Ref CTSex |
| CONFL_ItmHighRange | varchar |  |  | SI | Test Item High range hs for 83716 PC |
| CONFL_ItmLowRange | varchar |  |  | SI | Test Item Lower range hs for 83716 PC  |
| CONFL_LowerAge | double |  |  | SI | LowerAge |
| CONFL_LowerAgePeriod | varchar |  |  | SI | LowerAgePeriod |
| CONFL_ObsItmHighRange | varchar |  |  | SI | Observation Test Item High Range hs for 83716 PC |
| CONFL_ObsItmLowRange | varchar |  |  | SI | Observation Item Lower Range hs for 83716 PC |
| CONFL_ObservtnItem_DR | bigint |  | FK | SI | Observation Item Des Ref to MRCObservationItem hs ... |
| CONFL_Operation_DR | bigint |  | FK | SI | Des Ref ORCOperation |
| CONFL_Period | varchar |  |  | SI | Period |
| CONFL_ReasonRequired | varchar |  |  | SI | ReasonRequired |
| CONFL_RowId | varchar |  |  | NO | - |
| CONFL_TestItemCode | varchar |  |  | SI | Test Item Code hs for 83716 PC |
| CONFL_TimeFrame | double |  |  | SI | TimeFrame |
| CONFL_UpdatedDate | date |  |  | SI | Updated Date |
| CONFL_UpdatedTime | time |  |  | SI | Updated Time |
| CONFL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CONFL_UpperAge | double |  |  | SI | UpperAge |
| CONFL_UpperAgePeriod | varchar |  |  | SI | UpperAgePeriod |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Thrombocytopaenia |
| Q04 | - |  |  | SI | Timing of platelet count fall |
| Q05 | - |  |  | SI | Thrombosis or other sequelae |
| Q06 | - |  |  | SI | Other causes for Thrombocytopaenia |
| Q07 | - |  |  | SI | Lo gk, juhl d, warkentin te, sigouin cs, eichler p... |
| Q08 | - |  |  | SI | The 4Ts Score for Heparin-Induced Thrombocytopenia... |
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