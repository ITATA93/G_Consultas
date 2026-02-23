# SQLUser.CT_PathwayTimeline

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAT_RowID | bigint | PK |  | NO | - |
| PAT_Code | varchar |  |  | SI | Code |
| PAT_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| PAT_CreatedDate | date |  |  | SI | Created Date |
| PAT_CreatedTime | time |  |  | SI | Created Time |
| PAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PAT_DateFrom | date |  |  | SI | Date From |
| PAT_DateTo | date |  |  | SI | Date To |
| PAT_Desc | varchar |  |  | SI | Description |
| PAT_Owner | varchar |  |  | SI | Owner |
| PAT_PathwayStatuses | varchar |  |  | SI | Pathway Statuses |
| PAT_ProtocolTypes | varchar |  |  | SI | Protocol Types |
| PAT_UpdatedDate | date |  |  | SI | Updated Date |
| PAT_UpdatedTime | time |  |  | SI | Updated Time |
| PAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Type of Session |
| Q02 | - |  |  | SI | Referral Source |
| Q03 | - |  |  | SI | Referral Source Comment |
| Q04 | - |  |  | SI | Remarkable |
| Q05 | - |  |  | SI | Family History of Hearing Loss |
| Q06 | - |  |  | SI | Recurrent Ear Infections |
| Q07 | - |  |  | SI | Parental Concerns |
| Q08 | - |  |  | SI | Comment |
| Q09 | - |  |  | SI | Presence of Hearing Loss |
| Q10 | - |  |  | SI | Onset of Hearing Loss |
| Q11 | - |  |  | SI | Hearing Aid Use |
| Q12 | - |  |  | SI | Previous Audiological Assessment |
| Q13 | - |  |  | SI | Results of Previous Assessment |
| Q14 | - |  |  | SI | Fever |
| Q15 | - |  |  | SI | Otoscopy Test Result |
| Q16 | - |  |  | SI | Otoscopy Comment |
| Q17 | - |  |  | SI | Tympanometry (Right) |
| Q18 | - |  |  | SI | Tympanometry (Left) |
| Q19 | - |  |  | SI | Distortion Product Otoacoustic Emission (DPOAE) |
| Q20 | - |  |  | SI | Right Ear |
| Q21 | - |  |  | SI | Left Ear |
| Q22 | - |  |  | SI | Transient Evoked Otoacoustic Emission (TEOAE) |
| Q23 | - |  |  | SI | Right Ear |
| Q24 | - |  |  | SI | Left Ear |
| Q25 | - |  |  | SI | Behavioral Hearing Test Performed |
| Q26 | - |  |  | SI | Reliability |
| Q27 | - |  |  | SI | Final Outcome |
| Q28 | - |  |  | SI | Final Outcome Comment |
| Q29 | - |  |  | SI | Recommendations |
| Q30 | - |  |  | SI | Recommendations Comment |
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