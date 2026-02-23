# SQLUser.OEC_RadiologyDoseUnits

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RDU_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Bed to Chair - Assessment |
| Q02 | - |  |  | SI | Bed to Chair - Patient Ability |
| Q03 | - |  |  | SI | Bed to Chair - Equipment Required |
| Q04 | - |  |  | SI | Bed to Chair - Prior Assessment |
| Q05 | - |  |  | SI | Bed to Chair - Staff Required |
| Q06 | - |  |  | SI | Chair to bed - Assessment |
| Q07 | - |  |  | SI | Chair to bed - Patient Ability |
| Q08 | - |  |  | SI | Chair to bed - Equipment Required |
| Q09 | - |  |  | SI | Chair to bed - Prior Assessment |
| Q10 | - |  |  | SI | Chair to bed - Staff Required |
| Q11 | - |  |  | SI | Chair to Chair - Assessment |
| Q12 | - |  |  | SI | Chair to Chair - Patient Ability |
| Q13 | - |  |  | SI | Chair to Chair - Equipment Required |
| Q14 | - |  |  | SI | Chair to Chair - Prior Assessment |
| Q15 | - |  |  | SI | Chair to Chair - Staff Required |
| Q16 | - |  |  | SI | Bed to Trolley to Bed - Assessment |
| Q17 | - |  |  | SI | Bed to Trolley to Bed - Patient Ability |
| Q18 | - |  |  | SI | Bed to Trolley to Bed - Equipment Required |
| Q19 | - |  |  | SI | Bed to Trolley to Bed - Prior Assessment |
| Q20 | - |  |  | SI | Bed to Trolley to Bed - Staff Required |
| Q21 | - |  |  | SI | Task |
| Q22 | - |  |  | SI | Assessment |
| Q23 | - |  |  | SI | Patient Ability |
| Q24 | - |  |  | SI | Equipment Required |
| Q25 | - |  |  | SI | Prior Assessment |
| Q26 | - |  |  | SI | Staff Required |
| Q27 | - |  |  | SI | Bed to Chair |
| Q28 | - |  |  | SI | Chair to bed |
| Q29 | - |  |  | SI | Chair to Chair |
| Q30 | - |  |  | SI | Bed to Trolley to Bed |
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
| RDU_Code | varchar |  |  | NO | Code |
| RDU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RDU_CreatedDate | date |  |  | SI | Created Date |
| RDU_CreatedTime | time |  |  | SI | Created Time |
| RDU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RDU_Desc | varchar |  |  | NO | Description |
| RDU_Owner | varchar |  |  | SI | Owner |
| RDU_UpdatedDate | date |  |  | SI | Updated Date |
| RDU_UpdatedTime | time |  |  | SI | Updated Time |
| RDU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*