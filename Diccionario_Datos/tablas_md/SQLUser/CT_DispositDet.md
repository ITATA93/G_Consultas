# SQLUser.CT_DispositDet

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | CT_Disposit Parent Reference |
| DET_CareAvailability | varchar |  |  | SI | CareAvailability |
| DET_CareTyp | varchar |  |  | SI | CareTyp |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | Date From |
| DET_DateTo | date |  |  | SI | Date To |
| DET_IntentReAdmit | varchar |  |  | SI | IntentReAdmit |
| DET_ReasonForCritCareTransfe | varchar |  |  | SI | ReasonForCritCareTransfer |
| DET_RowId | varchar |  |  | NO | - |
| DET_SeparationReferral | varchar |  |  | SI | SeparationReferral |
| DET_TransferSource | varchar |  |  | SI | TransferSource |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | During the last 4 weeks, how much of the time has ... |
| Q04 | - |  |  | SI | During the last 4 weeks, how often have you had sh... |
| Q05 | - |  |  | SI | During the last 4 weeks, how often have your asthm... |
| Q06 | - |  |  | SI | During the last 4 weeks, how often have you used y... |
| Q07 | - |  |  | SI | How would you rate your asthma control during the ... |
| Q08 | - |  |  | SI | Score |
| Q09 | - |  |  | SI | Classification |
| Q10 | - |  |  | SI | 5 - 14 |
| Q11 | - |  |  | SI | Very poorly controlled asthma |
| Q12 | - |  |  | SI | 15 - 19 |
| Q13 | - |  |  | SI | Poorly controlled asthma |
| Q14 | - |  |  | SI | 20 - 25 |
| Q15 | - |  |  | SI | Well-controlled asthma |
| Q16 | - |  |  | SI | 5 - 14: Very poorly controlled asthma |
| Q17 | - |  |  | SI | 15 - 19:  Poorly controlled asthma |
| Q18 | - |  |  | SI | 20  - 25: Well-controlled asthma |
| Q19 | - |  |  | SI | The Adult Asthma Control Test (ACT) Score Question... |
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