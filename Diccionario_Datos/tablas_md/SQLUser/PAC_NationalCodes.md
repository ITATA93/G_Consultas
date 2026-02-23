# SQLUser.PAC_NationalCodes

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NATC_RowId | bigint | PK |  | NO | - |
| NATC_ActualValue | varchar |  |  | SI | ActualValue |
| NATC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NATC_CreatedDate | date |  |  | SI | Created Date |
| NATC_CreatedTime | time |  |  | SI | Created Time |
| NATC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NATC_DateFrom | date |  |  | SI | DateFrom |
| NATC_DateTo | date |  |  | SI | DateTo |
| NATC_FieldName | varchar |  |  | SI | FieldName |
| NATC_MappedValue | varchar |  |  | SI | MappedValue |
| NATC_NoDisplayOnWEB | varchar |  |  | SI | No Display On WEB |
| NATC_Owner | varchar |  |  | SI | Owner |
| NATC_ReportingType_DR | bigint |  | FK | SI | Des Ref ReportingType |
| NATC_TableField_DR | varchar |  | FK | SI | Des Ref TableField |
| NATC_TableName | varchar |  |  | SI | TableName |
| NATC_Table_DR | bigint |  | FK | SI | Des Ref Table |
| NATC_UpdatedDate | date |  |  | SI | Updated Date |
| NATC_UpdatedTime | time |  |  | SI | Updated Time |
| NATC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Age (years) |
| Q02 | - |  |  | SI | Intracerebral Hemorrhage (ICH) volume (cm³) |
| Q03 | - |  |  | SI | ICH location |
| Q04 | - |  |  | SI | Glasgow Coma Scale (GCS) Score |
| Q05 | - |  |  | SI | Pre-ICH cognitive impairment |
| Q06 | - |  |  | SI | The FUNC score is a clinical tool used at hospital... |
| Q08 | - |  |  | SI | FUNC Score categories and percent achieving functi... |
| Q09 | - |  |  | SI | Score 0-4: 0% |
| Q10 | - |  |  | SI | Score 5-7: 29% |
| Q11 | - |  |  | SI | Score 8: 48% |
| Q12 | - |  |  | SI | Score 9-10: 75% |
| Q13 | - |  |  | SI | Score 11: 95% |
| Q14 | - |  |  | SI | Functional Outcome in Patients with Primary Intrac... |
| Q15 | - |  |  | SI | Date |
| Q16 | - |  |  | SI | Time |
| Q17 | - |  |  | SI | Score |
| Q18 | - |  |  | SI | Classification |
| Q19 | - |  |  | SI | 0 - 4 |
| Q20 | - |  |  | SI | 0% achieving functional independence at 90 days |
| Q21 | - |  |  | SI | 5 - 7 |
| Q22 | - |  |  | SI | 29% achieving functional independence at 90 days |
| Q23 | - |  |  | SI | 8 |
| Q24 | - |  |  | SI | 48% achieving functional independence at 90 days |
| Q25 | - |  |  | SI | 9 - 10 |
| Q26 | - |  |  | SI | 75% achieving functional independence at 90 days |
| Q27 | - |  |  | SI | 11 |
| Q28 | - |  |  | SI | 95% achieving functional independence at 90 days |
| Q29 | - |  |  | SI | 0 - 4: 0% achieving functional independence at 90 ... |
| Q30 | - |  |  | SI | 5 - 7: 0% achieving functional independence at 90 ... |
| Q31 | - |  |  | SI | 8: 48% achieving functional independence at 90 day... |
| Q32 | - |  |  | SI | 9 - 10: 75% achieving functional independence at 9... |
| Q33 | - |  |  | SI | 11: 95% achieving functional independence at 90 da... |
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