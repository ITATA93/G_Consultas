# SQLUser.PAC_TrafAccidCode

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRF_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Physical therapy impression |
| Q04 | - |  |  | SI | Patient condition |
| Q05 | - |  |  | SI | Long term goal |
| Q06 | - |  |  | SI | Main goal (chest) |
| Q07 | - |  |  | SI | Main goal (neurology) |
| Q08 | - |  |  | SI | Main goal (orthopaedic) |
| Q09 | - |  |  | SI | Target |
| Q10 | - |  |  | SI | Reassessment target |
| Q11 | - |  |  | SI | Additional short term goal |
| Q12 | - |  |  | SI | Treatment |
| Q13 | - |  |  | SI | Post treatment details |
| Q14 | - |  |  | SI | Were there any concerns or harmful conditions foll... |
| Q15 | - |  |  | SI | Concerns or harmful condition |
| Q16 | - |  |  | SI | Education provided |
| Q17 | - |  |  | SI | Other instruction |
| Q18 | - |  |  | SI | I have discussed diagnosis and plan with patient /... |
| Q19 | - |  |  | SI | Plan of treatment and instruction need to be revie... |
| Q20 | - |  |  | SI | Session number |
| Q21 | - |  |  | SI | Total number of sessions |
| Q22 | - |  |  | SI | Session date |
| Q23 | - |  |  | SI | Session start time |
| Q24 | - |  |  | SI | Session end time |
| Q25 | - |  |  | SI | Performed by |
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
| TRF_Code | varchar |  |  | NO | Code |
| TRF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRF_CreatedDate | date |  |  | SI | Created Date |
| TRF_CreatedTime | time |  |  | SI | Created Time |
| TRF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRF_DateFrom | date |  |  | SI | Date From |
| TRF_DateTo | date |  |  | SI | Date To |
| TRF_Desc | varchar |  |  | NO | Description |
| TRF_Owner | varchar |  |  | SI | Owner |
| TRF_UpdatedDate | date |  |  | SI | Updated Date |
| TRF_UpdatedTime | time |  |  | SI | Updated Time |
| TRF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*