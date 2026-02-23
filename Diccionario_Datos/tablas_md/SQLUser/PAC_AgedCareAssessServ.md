# SQLUser.PAC_AgedCareAssessServ

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACAS_RowId | bigint | PK |  | NO | - |
| ACAS_Code | varchar |  |  | SI | Code |
| ACAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACAS_CreatedDate | date |  |  | SI | Created Date |
| ACAS_CreatedTime | time |  |  | SI | Created Time |
| ACAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACAS_DateFrom | date |  |  | SI | Date From |
| ACAS_DateTo | date |  |  | SI | Date To |
| ACAS_Desc | varchar |  |  | SI | Description |
| ACAS_NationalCode | varchar |  |  | SI | National Code |
| ACAS_Owner | varchar |  |  | SI | Owner |
| ACAS_SepRef | varchar |  |  | SI | SepRef |
| ACAS_UpdatedDate | date |  |  | SI | Updated Date |
| ACAS_UpdatedTime | time |  |  | SI | Updated Time |
| ACAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Accommodation |
| Q04 | - |  |  | SI | Accommodation type |
| Q05 | - |  |  | SI | Other accommodation type |
| Q06 | - |  |  | SI | Number of bedrooms |
| Q07 | - |  |  | SI | Number of adults living in the house |
| Q08 | - |  |  | SI | Number of children in the house |
| Q09 | - |  |  | SI | Number of pets in the house |
| Q10 | - |  |  | SI | Accommodation suitable for haemodialysis notes |
| Q11 | - |  |  | SI | Haemodialysis Space Assessment |
| Q12 | - |  |  | SI | 3x3 meter space available |
| Q13 | - |  |  | SI | Space notes |
| Q14 | - |  |  | SI | Describe access to home |
| Q15 | - |  |  | SI | Consider narrow doorway / passage / stairs / entry... |
| Q16 | - |  |  | SI | Entry doorways width confirmed to allow dialysis c... |
| Q17 | - |  |  | SI | Potential dialysis space room flooring type |
| Q18 | - |  |  | SI | Access to water pipe/ tap and sewerage close to pr... |
| Q19 | - |  |  | SI | Electricity outlet available with minimum requirem... |
| Q20 | - |  |  | SI | Photos taken of |
| Q21 | - |  |  | SI | Any additional work required to utilise existing p... |
| Q22 | - |  |  | SI | Additional work required |
| Q23 | - |  |  | SI | Outcome / Plan |
| Q24 | - |  |  | SI | Outcome of home haemodialysis suitability assessme... |
| Q25 | - |  |  | SI | Space suitable for haemodialysis |
| Q26 | - |  |  | SI | Outcome |
| Q27 | - |  |  | SI | Plan |
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