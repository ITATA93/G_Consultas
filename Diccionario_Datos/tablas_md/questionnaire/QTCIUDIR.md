# questionnaire.QTCIUDIR

> Intrauterine Device (IUD) Insertion / Removal

**Schema:** questionnaire
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intrauterine Device (IUD) Insertion / Removal

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Consent provided by |
| Q04 | varchar |  |  | SI | Other consent provided by |
| Q05 | varchar |  |  | SI | Procedure |
| Q06 | varchar |  |  | SI | Removal details |
| Q07 | varchar |  |  | SI | Reason for removal |
| Q08 | varchar |  |  | SI | Other reason for removal details |
| Q09 | varchar |  |  | SI | Provided patient information |
| Q10 | varchar |  |  | SI | Type of information provided |
| Q11 | varchar |  |  | SI | Removal procedure details |
| Q12 | varchar |  |  | SI | Insertion details |
| Q13 | varchar |  |  | SI | Contraception provision action completed |
| Q14 | varchar |  |  | SI | Exclusion of pregnancy |
| Q15 | varchar |  |  | SI | Medical Eligibility Criteria (MEC) |
| Q16 | varchar |  |  | SI | MEC notes |
| Q17 | varchar |  |  | SI | Sexually transmitted infection (STI) screening und... |
| Q18 | date |  |  | SI | Date of most recent STI screen |
| Q19 | date |  |  | SI | Estimated date of STI screen |
| Q20 | varchar |  |  | SI | STI screen details |
| Q21 | varchar |  |  | SI | Type of intrauterine device (IUD) |
| Q22 | varchar |  |  | SI | Other type of IUD |
| Q23 | varchar |  |  | SI | Discussion undertaken in regard to benefits, risk ... |
| Q24 | numeric |  |  | SI | Uterine length (cm) |
| Q25 | varchar |  |  | SI | Uterine position |
| Q26 | varchar |  |  | SI | IUD serial number |
| Q27 | varchar |  |  | SI | IUD lot number |
| Q28 | date |  |  | SI | Expiry date |
| Q29 | varchar |  |  | SI | Provided patient information |
| Q30 | varchar |  |  | SI | Type of information provided |
| Q31 | varchar |  |  | SI | Card (with insertion details) provided to patient |
| Q32 | varchar |  |  | SI | Need for additional contraception / abstinence for... |
| Q33 | varchar |  |  | SI | Need for follow up urine Beta-hCG in 4 weeks discu... |
| Q34 | varchar |  |  | SI | Insertion procedure details |
| Q35 | varchar |  |  | SI | Removal details |
| Q36 | varchar |  |  | SI | Insertion details |
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