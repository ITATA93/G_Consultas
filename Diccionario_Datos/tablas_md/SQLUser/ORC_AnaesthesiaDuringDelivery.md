# SQLUser.ORC_AnaesthesiaDuringDelivery

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANDUDE_RowId | bigint | PK |  | NO | - |
| ANDUDE_AvailDuringDeliv | varchar |  |  | SI | Available during delivery  |
| ANDUDE_AvailDuringTOP | varchar |  |  | SI | Available during TOP  |
| ANDUDE_Code | varchar |  |  | NO | Code |
| ANDUDE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANDUDE_CreatedDate | date |  |  | SI | Created Date |
| ANDUDE_CreatedTime | time |  |  | SI | Created Time |
| ANDUDE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANDUDE_DateFrom | date |  |  | SI | Date From |
| ANDUDE_DateTo | date |  |  | SI | Date To |
| ANDUDE_Desc | varchar |  |  | NO | Description |
| ANDUDE_Owner | varchar |  |  | SI | Owner |
| ANDUDE_UpdatedDate | date |  |  | SI | Updated Date |
| ANDUDE_UpdatedTime | time |  |  | SI | Updated Time |
| ANDUDE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Worker name |
| Q02 | - |  |  | SI | Initial assessment date |
| Q03 | - |  |  | SI | Sources of information |
| Q04 | - |  |  | SI | Social / Family profile |
| Q06 | - |  |  | SI | Formal support / Services involved |
| Q07 | - |  |  | SI | Financial circumstances |
| Q08 | - |  |  | SI | Legal issues |
| Q09 | - |  |  | SI | Current living situation |
| Q10 | - |  |  | SI | Status: Housing stable* |
| Q11 | - |  |  | SI | Adjustment to current situation |
| Q12 | - |  |  | SI | Mental health state |
| Q13 | - |  |  | SI | Carer issues |
| Q14 | - |  |  | SI | Threat to Person (Self or Others) * |
| Q15 | - |  |  | SI | Other risk assessment * |
| Q16 | - |  |  | SI | Other |
| Q17 | - |  |  | SI | Indentified strengths / Resources of patient |
| Q18 | - |  |  | SI | Summary / Recommentations / Discharge plan |
| Q19 | - |  |  | SI | (*Coping Skills / Status |
| Q20 | - |  |  | SI | (Internal or External |
| Q21 | - |  |  | SI | (Goals / Plans |
| Q21A | - |  |  | SI | Resources |
| Q22 | - |  |  | SI | (Description of family system, marital status, |
| Q22A | - |  |  | SI | Friends, Social networks spiritualty, Informal sup... |
| Q23 | - |  |  | SI | Legal / Financial |
| Q25 | - |  |  | SI | Current living situation |
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