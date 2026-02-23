# SQLUser.PAC_TumourSiteGroup

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TUMSG_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Language |
| Q04 | - |  |  | SI | Please specify language |
| Q05 | - |  |  | SI | Mobility status |
| Q06 | - |  |  | SI | Has the patient consented for radiotherapy treatme... |
| Q07 | - |  |  | SI | Has the patient had previous radiotherapy treatmen... |
| Q08 | - |  |  | SI | Give details |
| Q09 | - |  |  | SI | Is the patient having concurrent chemotherapy? |
| Q10 | - |  |  | SI | Comments |
| Q11 | - |  |  | SI | Does the patient have a pacemaker? |
| Q12 | - |  |  | SI | Pacemakers details |
| Q13 | - |  |  | SI | Is dental clearance needed? |
| Q14 | - |  |  | SI | Details of dental clearance |
| Q15 | - |  |  | SI | Site of treatment |
| Q16 | - |  |  | SI | Treatment intent |
| Q17 | - |  |  | SI | Is contrast required? |
| Q18 | - |  |  | SI | Comments |
| Q19 | - |  |  | SI | Four-dimensional computed tomography scan required... |
| Q20 | - |  |  | SI | Scanning levels |
| Q21 | - |  |  | SI | Other |
| Q22 | - |  |  | SI | Positioning |
| Q23 | - |  |  | SI | Phase1 |
| Q24 | - |  |  | SI | Gray (Gy) |
| Q25 | - |  |  | SI | Number |
| Q26 | - |  |  | SI | Bolus |
| Q27 | - |  |  | SI | Phase 2 |
| Q28 | - |  |  | SI | Phase 3 / Boost |
| Q29 | - |  |  | SI | Gray (Gy) |
| Q30 | - |  |  | SI | Number |
| Q31 | - |  |  | SI | Bolus |
| Q32 | - |  |  | SI | Gray (Gy) |
| Q33 | - |  |  | SI | Number |
| Q34 | - |  |  | SI | Bolus |
| Q35 | - |  |  | SI | Remarks / Comments |
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
| TUMSG_Code | varchar |  |  | NO | Code |
| TUMSG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TUMSG_CreatedDate | date |  |  | SI | Created Date |
| TUMSG_CreatedTime | time |  |  | SI | Created Time |
| TUMSG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TUMSG_Desc | varchar |  |  | NO | Description |
| TUMSG_Owner | varchar |  |  | SI | Owner |
| TUMSG_UpdatedDate | date |  |  | SI | Updated Date |
| TUMSG_UpdatedTime | time |  |  | SI | Updated Time |
| TUMSG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*