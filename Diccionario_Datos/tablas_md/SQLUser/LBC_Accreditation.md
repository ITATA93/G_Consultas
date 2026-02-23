# SQLUser.LBC_Accreditation

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCACC_RowID | bigint | PK |  | NO | - |
| ChildQ24DR | - |  |  | SI | Child Reference: Anomaly description |
| LBCACC_AccreditationSystem_DR | bigint |  | FK | SI | Accreditation System |
| LBCACC_Code | varchar |  |  | NO | Code |
| LBCACC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCACC_CreatedDate | date |  |  | SI | Created Date |
| LBCACC_CreatedTime | time |  |  | SI | Created Time |
| LBCACC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCACC_DateFrom | date |  |  | SI | From Date |
| LBCACC_DateTo | date |  |  | SI | To Date |
| LBCACC_Desc | varchar |  |  | NO | Description |
| LBCACC_Indicator | varchar |  |  | SI | Indicator |
| LBCACC_Owner | varchar |  |  | SI | Owner |
| LBCACC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCACC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCACC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Congenital anomaly |
| Q04 | - |  |  | SI | Diagnosed |
| Q05 | - |  |  | SI | Pregnancy gestation |
| Q06 | - |  |  | SI | weeks |
| Q07 | - |  |  | SI | days |
| Q08 | - |  |  | SI | Pregnancy gestation (weeks) |
| Q09 | - |  |  | SI | Pregnancy gestation (days) |
| Q10 | - |  |  | SI | Infant age |
| Q11 | - |  |  | SI | weeks |
| Q12 | - |  |  | SI | months |
| Q13 | - |  |  | SI | Infant age (weeks) |
| Q14 | - |  |  | SI | Infant age (months) |
| Q15 | - |  |  | SI | Fetal genetic testing |
| Q16 | - |  |  | SI | Other fetal genetic testing |
| Q17 | - |  |  | SI | Antenatal imaging |
| Q18 | - |  |  | SI | Other antenatal imaging |
| Q19 | - |  |  | SI | Fetal / Neonatal imaging |
| Q20 | - |  |  | SI | Other fetal / neonatal imaging |
| Q21 | - |  |  | SI | Fetal / Neonatal testing |
| Q22 | - |  |  | SI | Other fetal / neonatal testing |
| Q23 | - |  |  | SI | Notes |
| Q25 | - |  |  | SI | Notes |
| Q26 | - |  |  | SI | Relevant maternal / paternal history |
| Q27 | - |  |  | SI | Maternal environmental exposures (i.e. alcohol, dr... |
| Q28 | - |  |  | SI | Perinatal infection |
| Q29 | - |  |  | SI | Pregnancy outcome |
| Q30 | - |  |  | SI | Deceased date, if applicable |
| Q31 | - |  |  | SI | Transferred for care |
| Q32 | - |  |  | SI | Dummy1 |
| Q33 | - |  |  | SI | Notes |
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