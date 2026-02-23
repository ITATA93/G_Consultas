# SQLUser.CT_Search

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SRCH_RowID | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Type of assessment |
| Q02 | - |  |  | SI | Facial expression |
| Q03 | - |  |  | SI | Upper limb movements |
| Q04 | - |  |  | SI | Compliance with mechanical ventilation |
| Q05 | - |  |  | SI | Classification |
| Q06 | - |  |  | SI | Score |
| Q07 | - |  |  | SI | 3 |
| Q08 | - |  |  | SI | 4-5 |
| Q09 | - |  |  | SI | 6-11 |
| Q10 | - |  |  | SI | 12 |
| Q11 | - |  |  | SI | Note: for scores ≥ 6 consider sedation and/or anal... |
| Q12 | - |  |  | SI | Reference: www.ncbi.nlm.nih.gov/pubmed/11801819 |
| Q13 | - |  |  | SI | The Behavioral Pain Scale (BPS) is a useful tool t... |
| Q14 | - |  |  | SI | No pain |
| Q15 | - |  |  | SI | Mild pain |
| Q16 | - |  |  | SI | Unacceptale amount of pain |
| Q17 | - |  |  | SI | Maximum pain |
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
| RestrictionGroupList | varchar |  |  | SI | - |
| RestrictionLocationList | varchar |  |  | SI | - |
| RestrictionUserList | varchar |  |  | SI | - |
| SRCH_AccessReference | varchar |  |  | SI | Access Reference
Default to current logged in Use... |
| SRCH_AccessType | varchar |  |  | SI | Access Type 
Default to User |
| SRCH_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| SRCH_Component | bigint |  |  | SI | Component |
| SRCH_Context | varchar |  |  | SI | Context |
| SRCH_CreatedDate | date |  |  | SI | Created Date |
| SRCH_CreatedTime | time |  |  | SI | Created Time |
| SRCH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SRCH_DPLAccessType | varchar |  |  | SI | Dynamic Patient List Access Type |
| SRCH_Default | varchar |  |  | SI | Default |
| SRCH_Desc | varchar |  |  | NO | Description |
| SRCH_ExtendedDesc | varchar |  |  | SI | Extended Description |
| SRCH_Favourite | varchar |  |  | SI | Favourite |
| SRCH_Function | varchar |  |  | SI | Function |
| SRCH_Owner | varchar |  |  | SI | Owner |
| SRCH_UpdatedDate | date |  |  | SI | Updated Date |
| SRCH_UpdatedTime | time |  |  | SI | Updated Time |
| SRCH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*