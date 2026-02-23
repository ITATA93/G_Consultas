# SQLUser.PAC_TreatmentStream

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRSTR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Have you had any corticosteroid injection within t... |
| Q02 | - |  |  | SI | Do you have any coagulation disorder or take any a... |
| Q03 | - |  |  | SI | Do you have thrombosis? |
| Q04 | - |  |  | SI | Do you suffer from epilepsy? |
| Q05 | - |  |  | SI | Do you have any acute inflammation? |
| Q06 | - |  |  | SI | Do you have any polyneuropathy? |
| Q07 | - |  |  | SI | Have you had any tumor or recent radiotherapy/chem... |
| Q08 | - |  |  | SI | Have you had ESWT treatment in the past 2 months? |
| Q09 | - |  |  | SI | Risks and Side Effects include: |
| Q10 | - |  |  | SI | Swelling, redness, haematoma and pain. |
| Q11 | - |  |  | SI | Symptoms should reduce within 2 to 5 days and prio... |
| Q12 | - |  |  | SI | I understand the treatment and have had the risks ... |
| Q13 | - |  |  | SI | Patient signature |
| Q13UDt | - |  |  | SI | Patient signature Last Updated Date |
| Q13UTm | - |  |  | SI | Patient signature Last Updated Time |
| Q14 | - |  |  | SI | Date |
| Q15 | - |  |  | SI | I have asked these questions and explained the tre... |
| Q16 | - |  |  | SI | Care giver signature |
| Q16UDt | - |  |  | SI | Care giver signature Last Updated Date |
| Q16UTm | - |  |  | SI | Care giver signature Last Updated Time |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Additional information |
| Q19 | - |  |  | SI | Additional information |
| Q20 | - |  |  | SI | Additional information |
| Q21 | - |  |  | SI | Additional information |
| Q22 | - |  |  | SI | Additional information |
| Q23 | - |  |  | SI | Additional information |
| Q24 | - |  |  | SI | Additional information |
| Q25 | - |  |  | SI | Additional information |
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
| TRSTR_AdmType_List | varchar |  |  | SI | comma delimited string of Episode Type Restriction... |
| TRSTR_Code | varchar |  |  | NO | Code |
| TRSTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRSTR_CreatedDate | date |  |  | SI | Created Date |
| TRSTR_CreatedTime | time |  |  | SI | Created Time |
| TRSTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRSTR_DateFrom | date |  |  | SI | Date From |
| TRSTR_DateTo | date |  |  | SI | Date To |
| TRSTR_Desc | varchar |  |  | NO | Description |
| TRSTR_Owner | varchar |  |  | SI | Owner |
| TRSTR_Priority | integer |  |  | SI | Priority |
| TRSTR_Subregion_DR | bigint |  | FK | SI | Subregion  |
| TRSTR_UpdatedDate | date |  |  | SI | Updated Date |
| TRSTR_UpdatedTime | time |  |  | SI | Updated Time |
| TRSTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*