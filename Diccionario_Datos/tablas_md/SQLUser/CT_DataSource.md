# SQLUser.CT_DataSource

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDS_RowID | bigint | PK |  | NO | - |
| CTDS_Code | varchar |  |  | NO | Code |
| CTDS_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CTDS_DateFrom | date |  |  | SI | Date From |
| CTDS_DateTo | date |  |  | SI | Date To |
| CTDS_Desc | varchar |  |  | NO | Description |
| CTDS_IconName | varchar |  |  | SI | Icon  |
| CTDS_Owner | varchar |  |  | SI | Code Table Owner |
| CTDS_Type | varchar |  |  | SI | Source Type - uses Standard Type "SourceType" |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date discharged from acute pain service |
| Q04 | - |  |  | SI | The following assessment is to be completed 24 hou... |
| Q05 | - |  |  | SI | Back pain / Site check |
| Q06 | - |  |  | SI | Back pain / Site comments |
| Q07 | - |  |  | SI | Motor |
| Q08 | - |  |  | SI | Motor comments |
| Q09 | - |  |  | SI | Sensory |
| Q10 | - |  |  | SI | Sensory comments |
| Q11 | - |  |  | SI | Bladder / Bowel control |
| Q12 | - |  |  | SI | Bladder / Bowel control comments |
| Q13 | - |  |  | SI | Discharge advice |
| Q14 | - |  |  | SI | Discharge advice comments |
| Q15 | - |  |  | SI | Discharge card |
| Q16 | - |  |  | SI | Discharge card comments |
| Q17 | - |  |  | SI | Special follow up instructions (If any) |
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