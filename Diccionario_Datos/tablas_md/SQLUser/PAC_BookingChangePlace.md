# SQLUser.PAC_BookingChangePlace

**Schema:** SQLUser
**Columnas:** 123
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BCP_RowId | bigint | PK |  | NO | - |
| BCP_Code | varchar |  |  | NO | Code |
| BCP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BCP_CreatedDate | date |  |  | SI | Created Date |
| BCP_CreatedTime | time |  |  | SI | Created Time |
| BCP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BCP_DateFrom | date |  |  | SI | Date From |
| BCP_DateTo | date |  |  | SI | Date To |
| BCP_Desc | varchar |  |  | NO | Description |
| BCP_NationalCode | varchar |  |  | SI | National code |
| BCP_Owner | varchar |  |  | SI | Owner |
| BCP_UpdatedDate | date |  |  | SI | Updated Date |
| BCP_UpdatedTime | time |  |  | SI | Updated Time |
| BCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Gravida |
| Q04 | - |  |  | SI | Para |
| Q05 | - |  |  | SI | Gestation at proposed date of induction |
| Q06 | - |  |  | SI | weeks |
| Q07 | - |  |  | SI | Gestation at proposed date of induction (days) |
| Q08 | - |  |  | SI | days |
| Q09 | - |  |  | SI | Primary indication |
| Q10 | - |  |  | SI | Gestation |
| Q11 | - |  |  | SI | Gestation at rupture |
| Q12 | - |  |  | SI | weeks |
| Q13 | - |  |  | SI | Gestation at rupture days |
| Q14 | - |  |  | SI | days |
| Q15 | - |  |  | SI | Diabetes mellitus type |
| Q16 | - |  |  | SI | Gestation |
| Q17 | - |  |  | SI | GDM control |
| Q18 | - |  |  | SI | Gestation |
| Q19 | - |  |  | SI | Gestation |
| Q20 | - |  |  | SI | Type of hypertension disorder |
| Q21 | - |  |  | SI | Gestation |
| Q22 | - |  |  | SI | Gestation |
| Q23 | - |  |  | SI | Gestation |
| Q24 | - |  |  | SI | Twin pregnancy type |
| Q25 | - |  |  | SI | Gestation |
| Q26 | - |  |  | SI | Gestation |
| Q27 | - |  |  | SI | Gestation |
| Q28 | - |  |  | SI | Maternal age |
| Q29 | - |  |  | SI | Gestation |
| Q30 | - |  |  | SI | Gestation |
| Q31 | - |  |  | SI | Fetal growth anomaly |
| Q32 | - |  |  | SI | Gestation |
| Q33 | - |  |  | SI | Gestation |
| Q34 | - |  |  | SI | Gestation |
| Q35 | - |  |  | SI | Gestation |
| Q36 | - |  |  | SI | Other indication |
| Q37 | - |  |  | SI | For further review and approval |
| Q38 | - |  |  | SI | Comments |
| Q39 | - |  |  | SI | Additional indicators |
| Q40 | - |  |  | SI | Other indicators |
| Q41 | - |  |  | SI | Comments |
| Q42 | - |  |  | SI | Booked by |
| Q43 | - |  |  | SI | Approved by |
| Q44 | - |  |  | SI | Induction process, including risks, discussed with... |
| Q45 | - |  |  | SI | Patient given induction of labour information broc... |
| Q46 | - |  |  | SI | Brochure name |
| Q48 | - |  |  | SI | For further review and approval |
| Q49 | - |  |  | SI | For further review and approval |
| Q50 | - |  |  | SI | For further review and approval |
| Q51 | - |  |  | SI | For further review and approval |
| Q52 | - |  |  | SI | For further review and approval |
| Q53 | - |  |  | SI | For further review and approval |
| Q54 | - |  |  | SI | For further review and approval |
| Q55 | - |  |  | SI | For further review and approval |
| Q56 | - |  |  | SI | For further review and approval |
| Q57 | - |  |  | SI | For further review and approval |
| Q58 | - |  |  | SI | For further review and approval |
| Q59 | - |  |  | SI | For further review and approval |
| Q60 | - |  |  | SI | For further review and approval |
| Q61 | - |  |  | SI | For further review and approval |
| Q62 | - |  |  | SI | For further review and approval |
| Q63 | - |  |  | SI | For further review and approval |
| Q64 | - |  |  | SI | For further review and approval |
| Q65 | - |  |  | SI | Induction Booking |
| Q66 | - |  |  | SI | Additional Indicators for Induction |
| Q67 | - |  |  | SI | Primary Indication for Induction |
| Q68 | - |  |  | SI | Comments |
| Q69 | - |  |  | SI | Gestation |
| Q70 | - |  |  | SI | Modified Bishop Score |
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