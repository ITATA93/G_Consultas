# SQLUser.PAC_ReferralStatus

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RST_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Please use this form to tell us about the symptoms... |
| Q04 | - |  |  | SI | Use the scale above to choose a number between 0 a... |
| Q05 | - |  |  | SI | Anxiety |
| Q06 | - |  |  | SI | Anxiety |
| Q07 | - |  |  | SI | Discouragement |
| Q08 | - |  |  | SI | Discouragement |
| Q09 | - |  |  | SI | Trapped by illness |
| Q10 | - |  |  | SI | Trapped by illness |
| Q11 | - |  |  | SI | Hopelessness |
| Q12 | - |  |  | SI | Hopelessness |
| Q13 | - |  |  | SI | Pointlessness |
| Q14 | - |  |  | SI | Pointlessness |
| Q15 | - |  |  | SI | Loss of control |
| Q16 | - |  |  | SI | Loss of control |
| Q17 | - |  |  | SI | Loss of roles |
| Q18 | - |  |  | SI | Loss of roles |
| Q19 | - |  |  | SI | Depression |
| Q20 | - |  |  | SI | Depression |
| Q21 | - |  |  | SI | Wish to die |
| Q22 | - |  |  | SI | Wish to die |
| Q23 | - |  |  | SI | Confusion |
| Q24 | - |  |  | SI | Confusion |
| Q25 | - |  |  | SI | Kissane DW, Appleton J, Lennon J,&nbsp |
| Q26 | - |  |  | SI | Simple synonyms are the use of 2-3 words you can r... |
| Q27 | - |  |  | SI | While there are lots of synonyms that could be use... |
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
| RST_Code | varchar |  |  | NO | Code |
| RST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RST_CreatedDate | date |  |  | SI | Created Date |
| RST_CreatedTime | time |  |  | SI | Created Time |
| RST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RST_DateFrom | date |  |  | SI | Date From |
| RST_DateTo | date |  |  | SI | Date To |
| RST_Desc | varchar |  |  | NO | Description |
| RST_IcanName | varchar |  |  | SI | Icon Name |
| RST_IconPriority | numeric |  |  | SI | Icon Priority |
| RST_NationalCode | varchar |  |  | SI | National Code |
| RST_Owner | varchar |  |  | SI | Owner |
| RST_UpdatedDate | date |  |  | SI | Updated Date |
| RST_UpdatedTime | time |  |  | SI | Updated Time |
| RST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| RST_VisitStatus | varchar |  |  | SI | VisitStatus |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*