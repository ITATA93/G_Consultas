# SQLUser.CT_TimePreference

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTP_RowId | bigint | PK |  | NO | - |
| CTTP_Code | varchar |  |  | NO | Time Preference Code |
| CTTP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTTP_DateFrom | date |  |  | NO | Date From |
| CTTP_DateTo | date |  |  | SI | Date To |
| CTTP_Desc | varchar |  |  | NO | Room Description |
| CTTP_Interval | varchar |  |  | SI | Interval |
| CTTP_MinusTime | double |  |  | SI | Minus Time |
| CTTP_OffsetDOB | double |  |  | SI | DOB Start Offset |
| CTTP_Owner | varchar |  |  | SI | Owner |
| CTTP_PlusTime | double |  |  | SI | Plus Time |
| CTTP_TimeDirection | varchar |  |  | SI | Time Direction |
| CTTP_TimeUnit | varchar |  |  | SI | Time Unit |
| CTTP_TimeWindow | varchar |  |  | SI | Time Window |
| CTTP_UseGestation | varchar |  |  | SI | Use Gestation Age |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Height (Ht) |
| Q03ObsDR | - |  |  | SI | Height (Ht) DR |
| Q04 | - |  |  | SI | Weight |
| Q04ObsDR | - |  |  | SI | Weight DR |
| Q06 | - |  |  | SI | Total BODE Index score |
| Q07 | - |  |  | SI | Notes |
| Q08 | - |  |  | SI | Celli BR, Cote CG, Marin JM,&nbsp |
| Q09 | - |  |  | SI | The BODE index is a tool that is used by healthcar... |
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