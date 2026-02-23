# SQLUser.PAC_ExtractType

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXTRTYPE_RowId | bigint | PK |  | NO | - |
| EXTRTYPE_Code | varchar |  |  | NO | Code |
| EXTRTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EXTRTYPE_CreatedDate | date |  |  | SI | Created Date |
| EXTRTYPE_CreatedTime | time |  |  | SI | Created Time |
| EXTRTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EXTRTYPE_DateFrom | date |  |  | SI | Date From |
| EXTRTYPE_DateTo | date |  |  | SI | Date To |
| EXTRTYPE_Desc | varchar |  |  | NO | Description |
| EXTRTYPE_Owner | varchar |  |  | SI | Owner |
| EXTRTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| EXTRTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| EXTRTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fetal monitoring equipment checks complete |
| Q02 | - |  |  | SI | Indication for fetal monitoring |
| Q03 | - |  |  | SI | Other |
| Q04 | - |  |  | SI | CTG commenced date and time |
| Q05 | - |  |  | SI | CTG commenced time |
| Q07 | - |  |  | SI | Consider: |
| Q08 | - |  |  | SI | Has the baby(ies) got good reserve? |
| Q09 | - |  |  | SI | Is the baby(ies) compensating due to intrauterine ... |
| Q10 | - |  |  | SI | Is there evidence of decompensating? |
| Q11 | - |  |  | SI | CTG discontinued date and time |
| Q12 | - |  |  | SI | CTG discontinued time |
| Q13 | - |  |  | SI | Clinical interventions required |
| Q14 | - |  |  | SI | Comments |
| Q15 | - |  |  | SI | DO NOT act on the basis of the CTG analysis alone,... |
| Q16 | - |  |  | SI | Care provider 1 |
| Q17 | - |  |  | SI | Signature |
| Q17UDt | - |  |  | SI | Signature Last Updated Date |
| Q17UTm | - |  |  | SI | Signature Last Updated Time |
| Q18 | - |  |  | SI | Care provider 2 |
| Q19 | - |  |  | SI | Signature |
| Q19UDt | - |  |  | SI | Signature Last Updated Date |
| Q19UTm | - |  |  | SI | Signature Last Updated Time |
| Q20 | - |  |  | SI | Date |
| Q21 | - |  |  | SI | Time |
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