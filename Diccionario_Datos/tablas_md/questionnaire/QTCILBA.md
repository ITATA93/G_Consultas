# questionnaire.QTCILBA

> Induction of Labour Booking Assessment

**Schema:** questionnaire
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Induction of Labour Booking Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Gravida |
| Q04 | varchar |  |  | SI | Para |
| Q05 | numeric |  |  | SI | Gestation at proposed date of induction |
| Q06 | varchar |  |  | SI | weeks |
| Q07 | numeric |  |  | SI | Gestation at proposed date of induction (days) |
| Q08 | varchar |  |  | SI | days |
| Q09 | varchar |  |  | SI | Primary indication |
| Q10 | varchar |  |  | SI | Gestation |
| Q11 | numeric |  |  | SI | Gestation at rupture |
| Q12 | varchar |  |  | SI | weeks |
| Q13 | numeric |  |  | SI | Gestation at rupture days |
| Q14 | varchar |  |  | SI | days |
| Q15 | varchar |  |  | SI | Diabetes mellitus type |
| Q16 | varchar |  |  | SI | Gestation |
| Q17 | varchar |  |  | SI | GDM control |
| Q18 | varchar |  |  | SI | Gestation |
| Q19 | varchar |  |  | SI | Gestation |
| Q20 | varchar |  |  | SI | Type of hypertension disorder |
| Q21 | varchar |  |  | SI | Gestation |
| Q22 | varchar |  |  | SI | Gestation |
| Q23 | varchar |  |  | SI | Gestation |
| Q24 | varchar |  |  | SI | Twin pregnancy type |
| Q25 | varchar |  |  | SI | Gestation |
| Q26 | varchar |  |  | SI | Gestation |
| Q27 | varchar |  |  | SI | Gestation |
| Q28 | varchar |  |  | SI | Maternal age |
| Q29 | varchar |  |  | SI | Gestation |
| Q30 | varchar |  |  | SI | Gestation |
| Q31 | varchar |  |  | SI | Fetal growth anomaly |
| Q32 | varchar |  |  | SI | Gestation |
| Q33 | varchar |  |  | SI | Gestation |
| Q34 | varchar |  |  | SI | Gestation |
| Q35 | varchar |  |  | SI | Gestation |
| Q36 | varchar |  |  | SI | Other indication |
| Q37 | varchar |  |  | SI | For further review and approval |
| Q38 | varchar |  |  | SI | Comments |
| Q39 | varchar |  |  | SI | Additional indicators |
| Q40 | varchar |  |  | SI | Other indicators |
| Q41 | varchar |  |  | SI | Comments |
| Q42 | varchar |  |  | SI | Booked by |
| Q43 | varchar |  |  | SI | Approved by |
| Q44 | varchar |  |  | SI | Induction process, including risks, discussed with... |
| Q45 | varchar |  |  | SI | Patient given induction of labour information broc... |
| Q46 | varchar |  |  | SI | Brochure name |
| Q48 | varchar |  |  | SI | For further review and approval |
| Q49 | varchar |  |  | SI | For further review and approval |
| Q50 | varchar |  |  | SI | For further review and approval |
| Q51 | varchar |  |  | SI | For further review and approval |
| Q52 | varchar |  |  | SI | For further review and approval |
| Q53 | varchar |  |  | SI | For further review and approval |
| Q54 | varchar |  |  | SI | For further review and approval |
| Q55 | varchar |  |  | SI | For further review and approval |
| Q56 | varchar |  |  | SI | For further review and approval |
| Q57 | varchar |  |  | SI | For further review and approval |
| Q58 | varchar |  |  | SI | For further review and approval |
| Q59 | varchar |  |  | SI | For further review and approval |
| Q60 | varchar |  |  | SI | For further review and approval |
| Q61 | varchar |  |  | SI | For further review and approval |
| Q62 | varchar |  |  | SI | For further review and approval |
| Q63 | varchar |  |  | SI | For further review and approval |
| Q64 | varchar |  |  | SI | For further review and approval |
| Q65 | varchar |  |  | SI | Induction Booking |
| Q66 | varchar |  |  | SI | Additional Indicators for Induction |
| Q67 | varchar |  |  | SI | Primary Indication for Induction |
| Q68 | varchar |  |  | SI | Comments |
| Q69 | varchar |  |  | SI | Gestation |
| Q70 | varchar |  |  | SI | Modified Bishop Score |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*