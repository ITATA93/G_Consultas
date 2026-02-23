# SQLUser.ORC_AnaestBlockSide

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORCABS_RowId | bigint | PK |  | NO | - |
| ORCABS_Code | varchar |  |  | NO | Code |
| ORCABS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORCABS_CreatedDate | date |  |  | SI | Created Date |
| ORCABS_CreatedTime | time |  |  | SI | Created Time |
| ORCABS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORCABS_DateFrom | date |  |  | SI | Date From |
| ORCABS_DateTo | date |  |  | SI | Date To |
| ORCABS_Desc | varchar |  |  | NO | Description |
| ORCABS_Owner | varchar |  |  | SI | Owner |
| ORCABS_UpdatedDate | date |  |  | SI | Updated Date |
| ORCABS_UpdatedTime | time |  |  | SI | Updated Time |
| ORCABS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Occulomotor |
| Q02 | - |  |  | SI | Nystagmus |
| Q03 | - |  |  | SI | Smooth pursuit |
| Q04 | - |  |  | SI | Saccades |
| Q05 | - |  |  | SI | VOR suppression |
| Q06 | - |  |  | SI | Comments |
| Q07 | - |  |  | SI | Head Thrust |
| Q08 | - |  |  | SI | Head thrust left |
| Q09 | - |  |  | SI | Head thrust right |
| Q10 | - |  |  | SI | Comments |
| Q11 | - |  |  | SI | Vestibular Occular Reflex (VOR) |
| Q12 | - |  |  | SI | VOR horizontal symptoms |
| Q13 | - |  |  | SI | Duration |
| Q14 | - |  |  | SI | VOR vertical symptoms |
| Q15 | - |  |  | SI | Duration |
| Q16 | - |  |  | SI | Dix-Hallpike |
| Q17 | - |  |  | SI | Dix-Hallpike left |
| Q18 | - |  |  | SI | Dix-Hallpike right |
| Q19 | - |  |  | SI | Symptoms |
| Q20 | - |  |  | SI | Symptoms |
| Q21 | - |  |  | SI | Horizontal canal |
| Q22 | - |  |  | SI | Symptoms |
| Q23 | - |  |  | SI | Hearing |
| Q24 | - |  |  | SI | Hearing |
| Q25 | - |  |  | SI | Comment |
| Q26 | - |  |  | SI | Test of skew |
| Q27 | - |  |  | SI | Test of skew left |
| Q28 | - |  |  | SI | Test of skew right |
| Q29 | - |  |  | SI | Comments |
| Q30 | - |  |  | SI | Date |
| Q31 | - |  |  | SI | Time |
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