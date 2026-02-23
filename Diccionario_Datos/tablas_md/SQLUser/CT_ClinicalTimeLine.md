# SQLUser.CT_ClinicalTimeLine

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCTL_RowID | bigint | PK |  | NO | - |
| AddTaskItem | varchar |  |  | SI | - |
| CTCTL_AutoRefreshEnabled | varchar |  |  | SI | Enable Auto-Refresh |
| CTCTL_AutoRefreshInterval | varchar |  |  | SI | Auto-Refresh Interval |
| CTCTL_Code | varchar |  |  | NO | Code |
| CTCTL_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CTCTL_CollapseLegends | bit |  |  | SI | Collapse Legends |
| CTCTL_CollapseNoDataColumns | bit |  |  | SI | Collapse No Data Columns |
| CTCTL_CreatedDate | date |  |  | SI | Created Date |
| CTCTL_CreatedTime | time |  |  | SI | Created Time |
| CTCTL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTCTL_DateFrom | date |  |  | SI | Effective date for the record |
| CTCTL_DateTo | date |  |  | SI | Last day the record is active |
| CTCTL_Desc | varchar |  |  | NO | Description |
| CTCTL_EpisodeFilter | varchar |  |  | SI | Across Episode or filter by Current Episode |
| CTCTL_EpisodeFilterPrefDisabled | varchar |  |  | SI | Enable Episode Filter checkbox for user preference... |
| CTCTL_HideControls | bit |  |  | SI | Hide Controls |
| CTCTL_Owner | varchar |  |  | SI | Owner |
| CTCTL_ReadOnly | varchar |  |  | SI | CTL Read-Only checkbox |
| CTCTL_TimePreference_DR | bigint |  | FK | SI | Reference to Time Preference Code Table |
| CTCTL_UpdatedDate | date |  |  | SI | Updated Date |
| CTCTL_UpdatedTime | time |  |  | SI | Updated Time |
| CTCTL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| EventTimeline | varchar |  |  | SI | - |
| GraphReference | varchar |  |  | SI | - |
| ItemOwner | varchar |  |  | SI | - |
| ObsProfile | varchar |  |  | SI | - |
| OrderTimeline | varchar |  |  | SI | - |
| PathwayTimeline | varchar |  |  | SI | - |
| Q01 | - |  |  | SI | Pulgar Derecho |
| Q01ObsDR | - |  |  | SI | Pulgar Derecho DR |
| Q02 | - |  |  | SI | Pulgar Izquierdo |
| Q02ObsDR | - |  |  | SI | Pulgar Izquierdo DR |
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