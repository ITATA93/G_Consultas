# SQLUser.ORC_Parasthesia

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PARAS_RowId | bigint | PK |  | NO | - |
| PARAS_Code | varchar |  |  | NO | Code |
| PARAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PARAS_CreatedDate | date |  |  | SI | Created Date |
| PARAS_CreatedTime | time |  |  | SI | Created Time |
| PARAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PARAS_DateFrom | date |  |  | SI | Date From |
| PARAS_DateTo | date |  |  | SI | Date To |
| PARAS_Desc | varchar |  |  | NO | Description |
| PARAS_Owner | varchar |  |  | SI | Owner |
| PARAS_UpdatedDate | date |  |  | SI | Updated Date |
| PARAS_UpdatedTime | time |  |  | SI | Updated Time |
| PARAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date reviewed |
| Q04 | - |  |  | SI | Next review date |
| Q05 | - |  |  | SI | Authored / Reviewed by |
| Q06 | - |  |  | SI | Consultation by |
| Q07 | - |  |  | SI | General practitioner |
| Q08 | - |  |  | SI | Management plan approved by |
| Q09 | - |  |  | SI | Management plan should be approved in consultation... |
| Q10 | - |  |  | SI | Names / Additional detail |
| Q11 | - |  |  | SI | Key worker |
| Q12 | - |  |  | SI | Key worker / team |
| Q13 | - |  |  | SI | Contact number |
| Q14 | - |  |  | SI | Patient must always be triaged according to the or... |
| Q15 | - |  |  | SI | Case summary |
| Q16 | - |  |  | SI | Predetermined management strategy |
| Q17 | - |  |  | SI | Predicted presenting problems |
| Q18 | - |  |  | SI | Expected actions |
| Q19 | - |  |  | SI | Notify key worker of presentation to Emergency Dep... |
| Q20 | - |  |  | SI | This is a guideline only and should be discussed w... |
| Q21 | - |  |  | SI | Consulted with |
| Q22 | - |  |  | SI | Consultation comments |
| Q23 | - |  |  | SI | Please ensure the patient's alerts are updated to ... |
| Q24 | - |  |  | SI | Plan status |
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