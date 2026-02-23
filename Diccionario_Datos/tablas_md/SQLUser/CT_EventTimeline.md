# SQLUser.CT_EventTimeline

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EVT_RowID | bigint | PK |  | NO | - |
| EVT_Code | varchar |  |  | NO | Code |
| EVT_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| EVT_CreatedDate | date |  |  | SI | Created Date |
| EVT_CreatedTime | time |  |  | SI | Created Time |
| EVT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EVT_DateFrom | date |  |  | NO | Date From |
| EVT_DateTo | date |  |  | SI | Date To |
| EVT_Desc | varchar |  |  | NO | Description |
| EVT_Owner | varchar |  |  | SI | Owner |
| EVT_ShowLabelsByDefault | varchar |  |  | SI | Show labels by default |
| EVT_UpdatedDate | date |  |  | SI | Updated Date |
| EVT_UpdatedTime | time |  |  | SI | Updated Time |
| EVT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Perspiration |
| Q02 | - |  |  | SI | Tremor |
| Q03 | - |  |  | SI | Agitation |
| Q04 | - |  |  | SI | Anxiety |
| Q05 | - |  |  | SI | Axilla temperature |
| Q06 | - |  |  | SI | Hallucinations |
| Q07 | - |  |  | SI | Orientation |
| Q08 | - |  |  | SI | 1 - 5: Mild withdrawal |
| Q09 | - |  |  | SI | 6 - 10: Moderate withdrawal |
| Q10 | - |  |  | SI | 11 - 14: Major withdrawal |
| Q11 | - |  |  | SI | ≥15: Major withdrawal, impending delirium tremors |
| Q12a | - |  |  | SI | The Alcohol Withdrawal Score is a scale that aims ... |
| Q12b | - |  |  | SI | of recording the Alcohol Withdrawal Syndrome of a ... |
| Q14 | - |  |  | SI | Date |
| Q15 | - |  |  | SI | Time |
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