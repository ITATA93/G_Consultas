# SQLUser.DTC_DietCycle

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CYCLE_RowId | bigint | PK |  | NO | - |
| CYCLE_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| CYCLE_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| CYCLE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CYCLE_CreatedDate | date |  |  | SI | Created Date |
| CYCLE_CreatedTime | time |  |  | SI | Created Time |
| CYCLE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CYCLE_CycleNumber | varchar |  |  | SI | Cycle Number |
| CYCLE_DOW_DR | double |  | FK | SI | Des Ref DOW |
| CYCLE_DateFrom | date |  |  | SI | DateFrom |
| CYCLE_DateTo | date |  |  | SI | DateTo |
| CYCLE_MealType_DR | bigint |  | FK | SI | Des Ref MealType |
| CYCLE_Owner | varchar |  |  | SI | Owner |
| CYCLE_UpdatedDate | date |  |  | SI | Updated Date |
| CYCLE_UpdatedTime | time |  |  | SI | Updated Time |
| CYCLE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Describe status prior to event |
| Q02 | - |  |  | SI | Describe event |
| Q03 | - |  |  | SI | Onset |
| Q03N | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Cardiovascular history |
| Q05N | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Pulmonary history |
| Q07N | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Neurological history |
| Q09N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Other relevant history |
| Q12 | - |  |  | SI | Witnessed event |
| Q13 | - |  |  | SI | CPR initiated |
| Q14 | - |  |  | SI | Event duration prior to CPR |
| Q15 | - |  |  | SI | CPR time prior to ACLS |
| Q16 | - |  |  | SI | ACLS |
| Q17 | - |  |  | SI | Does patient have advance directives |
| Q18 | - |  |  | SI | Does patient have documented Do Not Resuscitate st... |
| Q19PCPR | - |  |  | SI | min |
| Q20PACLS | - |  |  | SI | min |
| Q21ACLS | - |  |  | SI | min |
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