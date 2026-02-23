# SQLUser.ORC_ContrastAgent

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORCCA_RowId | bigint | PK |  | NO | - |
| ORCCA_Code | varchar |  |  | NO | Code |
| ORCCA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORCCA_CreatedDate | date |  |  | SI | Created Date |
| ORCCA_CreatedTime | time |  |  | SI | Created Time |
| ORCCA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORCCA_DateFrom | date |  |  | SI | Date From |
| ORCCA_DateTo | date |  |  | SI | Date To |
| ORCCA_Desc | varchar |  |  | NO | Description |
| ORCCA_Owner | varchar |  |  | SI | Owner |
| ORCCA_UpdatedDate | date |  |  | SI | Updated Date |
| ORCCA_UpdatedTime | time |  |  | SI | Updated Time |
| ORCCA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | If zero is no distress and 10 is extreme distress,... |
| Q02 | - |  |  | SI | 	Please indicate below, if any of the following ha... |
| Q03 | - |  |  | SI | Practical problems |
| Q04 | - |  |  | SI | Family problems |
| Q05 | - |  |  | SI | Emotional problems |
| Q06 | - |  |  | SI | Spiritual or religious concerns |
| Q07 | - |  |  | SI | Physical problems |
| Q08 | - |  |  | SI | Comments |
| Q09 | - |  |  | SI | Patient / family member signature |
| Q09UDt | - |  |  | SI | Patient / family member signature Last Updated Dat... |
| Q09UTm | - |  |  | SI | Patient / family member signature Last Updated Tim... |
| Q10 | - |  |  | SI | Screening point |
| Q11 | - |  |  | SI | Are referrals recommended? |
| Q12 | - |  |  | SI | Dietetics |
| Q13 | - |  |  | SI | Occupational therapy |
| Q14 | - |  |  | SI | Palliative care |
| Q15 | - |  |  | SI | Pastoral care |
| Q16 | - |  |  | SI | Physiotherapy |
| Q17 | - |  |  | SI | Psychology / psychiatry |
| Q18 | - |  |  | SI | Social work |
| Q19 | - |  |  | SI | Specialist work |
| Q20 | - |  |  | SI | Speech therapy |
| Q21 | - |  |  | SI | Reason |
| Q22 | - |  |  | SI | Reason |
| Q23 | - |  |  | SI | Reason |
| Q24 | - |  |  | SI | Reason |
| Q25 | - |  |  | SI | Reason |
| Q26 | - |  |  | SI | Reason |
| Q27 | - |  |  | SI | Reason |
| Q28 | - |  |  | SI | Reason |
| Q29 | - |  |  | SI | Reason |
| Q30 | - |  |  | SI | Other services |
| Q31 | - |  |  | SI | Patient agreed to above referral(s) being made? |
| Q32 | - |  |  | SI | Treating doctor aware of referral(s) being made? |
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