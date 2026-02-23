# SQLUser.ORC_TherapyforComplications

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| THFOCO_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Referral source |
| Q02 | - |  |  | SI | Date of referral |
| Q03 | - |  |  | SI | Referrer |
| Q04 | - |  |  | SI | Date of initial assessment |
| Q05 | - |  |  | SI | Does the patient have a care plan? |
| Q06 | - |  |  | SI | Has the patient had a falls screen test? |
| Q07 | - |  |  | SI | Compensible |
| Q08 | - |  |  | SI | Exercise physiologist |
| Q09 | - |  |  | SI | Other team involvement |
| Q10 | - |  |  | SI | Activities of daily living (personal / community /... |
| Q11 | - |  |  | SI | Home access |
| Q12 | - |  |  | SI | Client's perception of condition and outcome |
| Q13 | - |  |  | SI | Pre-morbid function / activities |
| Q14 | - |  |  | SI | Current activity |
| Q15 | - |  |  | SI | Communication |
| Q16 | - |  |  | SI | Falls history |
| Q17 | - |  |  | SI | Psychosocial health / stress / sleep |
| Q18 | - |  |  | SI | SMART goals |
| Q18TxtOnly | - |  |  | SI | SMART goals Plain Text Only |
| Q19 | - |  |  | SI | Mobility |
| Q20 | - |  |  | SI | Bed mobility |
| Q21 | - |  |  | SI | Transfers |
| Q22 | - |  |  | SI | Gait |
| Q23 | - |  |  | SI | Gait |
| Q24 | - |  |  | SI | Gait aid |
| Q25 | - |  |  | SI | Comments |
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
| THFOCO_Code | varchar |  |  | NO | Code |
| THFOCO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| THFOCO_CreatedDate | date |  |  | SI | Created Date |
| THFOCO_CreatedTime | time |  |  | SI | Created Time |
| THFOCO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| THFOCO_DateFrom | date |  |  | SI | Date From |
| THFOCO_DateTo | date |  |  | SI | Date To |
| THFOCO_Desc | varchar |  |  | NO | Description |
| THFOCO_Owner | varchar |  |  | SI | Owner |
| THFOCO_UpdatedDate | date |  |  | SI | Updated Date |
| THFOCO_UpdatedTime | time |  |  | SI | Updated Time |
| THFOCO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*