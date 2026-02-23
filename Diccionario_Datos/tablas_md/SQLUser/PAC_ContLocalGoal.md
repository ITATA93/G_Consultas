# SQLUser.PAC_ContLocalGoal

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCGOAL_RowId | bigint | PK |  | NO | - |
| LOCGOAL_Code | varchar |  |  | NO | Code |
| LOCGOAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOCGOAL_CreatedDate | date |  |  | SI | Created Date |
| LOCGOAL_CreatedTime | time |  |  | SI | Created Time |
| LOCGOAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOCGOAL_DateFrom | date |  |  | SI | Date From |
| LOCGOAL_DateTo | date |  |  | SI | Date To |
| LOCGOAL_Desc | varchar |  |  | NO | Description |
| LOCGOAL_Owner | varchar |  |  | SI | Owner |
| LOCGOAL_UpdatedDate | date |  |  | SI | Updated Date |
| LOCGOAL_UpdatedTime | time |  |  | SI | Updated Time |
| LOCGOAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Consent provided by |
| Q04 | - |  |  | SI | Other consent provided by |
| Q05 | - |  |  | SI | Procedure |
| Q06 | - |  |  | SI | Removal details |
| Q07 | - |  |  | SI | Reason for removal |
| Q08 | - |  |  | SI | Other reason for removal details |
| Q09 | - |  |  | SI | Provided patient information |
| Q10 | - |  |  | SI | Type of information provided |
| Q11 | - |  |  | SI | Removal procedure details |
| Q12 | - |  |  | SI | Insertion details |
| Q13 | - |  |  | SI | Contraception provision action completed |
| Q14 | - |  |  | SI | Exclusion of pregnancy |
| Q15 | - |  |  | SI | Medical Eligibility Criteria (MEC) |
| Q16 | - |  |  | SI | MEC notes |
| Q17 | - |  |  | SI | Sexually transmitted infection (STI) screening und... |
| Q18 | - |  |  | SI | Date of most recent STI screen |
| Q19 | - |  |  | SI | Estimated date of STI screen |
| Q20 | - |  |  | SI | STI screen details |
| Q21 | - |  |  | SI | Type of intrauterine device (IUD) |
| Q22 | - |  |  | SI | Other type of IUD |
| Q23 | - |  |  | SI | Discussion undertaken in regard to benefits, risk ... |
| Q24 | - |  |  | SI | Uterine length (cm) |
| Q25 | - |  |  | SI | Uterine position |
| Q26 | - |  |  | SI | IUD serial number |
| Q27 | - |  |  | SI | IUD lot number |
| Q28 | - |  |  | SI | Expiry date |
| Q29 | - |  |  | SI | Provided patient information |
| Q30 | - |  |  | SI | Type of information provided |
| Q31 | - |  |  | SI | Card (with insertion details) provided to patient |
| Q32 | - |  |  | SI | Need for additional contraception / abstinence for... |
| Q33 | - |  |  | SI | Need for follow up urine Beta-hCG in 4 weeks discu... |
| Q34 | - |  |  | SI | Insertion procedure details |
| Q35 | - |  |  | SI | Removal details |
| Q36 | - |  |  | SI | Insertion details |
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