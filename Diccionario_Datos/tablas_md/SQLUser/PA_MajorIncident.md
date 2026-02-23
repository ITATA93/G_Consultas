# SQLUser.PA_MajorIncident

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MI_RowId | bigint | PK |  | NO | - |
| MI_CloseDate | date |  |  | SI | CloseDate |
| MI_CloseTime | time |  |  | SI | Close Time |
| MI_Date | date |  |  | SI | Date |
| MI_DateCloseReg | date |  |  | SI | Date Close Registration |
| MI_Description | varchar |  |  | SI | Description |
| MI_EstNumBeforeClose | double |  |  | SI | Esitmate Number Before Close |
| MI_IncidentReason | varchar |  |  | SI | Incident Reason |
| MI_IncidentReasonDet | varchar |  |  | SI | Incident Reason Details |
| MI_IncidentStat | varchar |  |  | SI | IncidentStat |
| MI_Location | varchar |  |  | SI | Location |
| MI_PriorityCode_DR | bigint |  | FK | SI | Call Priority Code |
| MI_Time | time |  |  | SI | Time |
| MI_TimeCloseReg | time |  |  | SI | Time Close Registration |
| MI_TransPriorityCode_DR | bigint |  | FK | SI | Transportation Priority Code |
| MI_UpdateDate | date |  |  | SI | Update Date |
| MI_UpdateTime | time |  |  | SI | Update Time |
| MI_User_DR | bigint |  | FK | SI | Des Ref User |
| NI_EstimateNumber | double |  |  | SI | Estimate Number |
| Q01 | - |  |  | SI | Grupo de pesquisa |
| Q02 | - |  |  | SI | Fecha toma de muestras |
| Q03 | - |  |  | SI | Hora de obtención |
| Q04 | - |  |  | SI | Responsable |
| Q05 | - |  |  | SI | Observaciones |
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