# SQLUser.ORC_Anaest_Complications

**Schema:** SQLUser
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANACOM_RowId | bigint | PK |  | NO | - |
| ANACOM_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| ANACOM_Cardiac | varchar |  |  | SI | Cardiac |
| ANACOM_Code | varchar |  |  | NO | Code |
| ANACOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANACOM_CreatedDate | date |  |  | SI | Created Date |
| ANACOM_CreatedTime | time |  |  | SI | Created Time |
| ANACOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANACOM_DateFrom | date |  |  | SI | Date From |
| ANACOM_DateTo | date |  |  | SI | Date To |
| ANACOM_Desc | varchar |  |  | NO | Description |
| ANACOM_Other | varchar |  |  | SI | Other |
| ANACOM_Owner | varchar |  |  | SI | Owner |
| ANACOM_Respiratory | varchar |  |  | SI | Respiratory |
| ANACOM_UpdatedDate | date |  |  | SI | Updated Date |
| ANACOM_UpdatedTime | time |  |  | SI | Updated Time |
| ANACOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Referral Reason |
| Q02 | - |  |  | SI | Patient Details |
| Q03 | - |  |  | SI | Living Condition |
| Q04 | - |  |  | SI | House |
| Q05 | - |  |  | SI | Utilities Availability |
| Q06 | - |  |  | SI | Education Level |
| Q07 | - |  |  | SI | Handicap (if yes record in comments) |
| Q08 | - |  |  | SI | Patient Detail Comments |
| Q09 | - |  |  | SI | Care Giving Details |
| Q10 | - |  |  | SI | Caregiver |
| Q11 | - |  |  | SI | If Other Caregiver |
| Q12 | - |  |  | SI | Caregiver Education |
| Q13 | - |  |  | SI | Caregiver Availability |
| Q14 | - |  |  | SI | Caregiver Comments |
| Q15 | - |  |  | SI | Family Information |
| Q16 | - |  |  | SI | Siblings (record number of brothers and sisters) |
| Q17 | - |  |  | SI | Mother Education |
| Q18 | - |  |  | SI | Mother Occupation |
| Q19 | - |  |  | SI | Father Education |
| Q20 | - |  |  | SI | Father Occupation |
| Q21 | - |  |  | SI | Income |
| Q22 | - |  |  | SI | Family Information Comments |
| Q23 | - |  |  | SI | Plan |
| Q24 | - |  |  | SI | Plan |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*