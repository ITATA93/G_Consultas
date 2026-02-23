# questionnaire.QTCPIIR

> Progestin Implant Insertion / Removal

**Schema:** questionnaire
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Progestin Implant Insertion / Removal

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
| Q09 | varchar |  |  | SI | Removal site |
| Q10 | varchar |  |  | SI | Other removal site |
| Q11 | varchar |  |  | SI | Follow up visit |
| Q12 | varchar |  |  | SI | weeks |
| Q13 | numeric |  |  | SI | Follow up visit in (weeks) |
| Q14 | varchar |  |  | SI | Removal procedure details |
| Q15 | varchar |  |  | SI | Insertion details |
| Q16 | varchar |  |  | SI | Contraception provision action already completed |
| Q17 | varchar |  |  | SI | Exclusion of pregnancy |
| Q18 | varchar |  |  | SI | Medical Eligibility Criteria (MEC) |
| Q19 | varchar |  |  | SI | MEC notes |
| Q20 | varchar |  |  | SI | Sexually transmitted infection (STI) screening und... |
| Q21 | date |  |  | SI | Date of most recent STI screen |
| Q22 | date |  |  | SI | Estimated date of STI screen |
| Q23 | varchar |  |  | SI | STI screen details |
| Q24 | varchar |  |  | SI | Discussion undertaken in regard to benefits, risk ... |
| Q25 | varchar |  |  | SI | Insertion site |
| Q26 | varchar |  |  | SI | Other insertion site details |
| Q27 | varchar |  |  | SI | Implant serial number |
| Q28 | varchar |  |  | SI | Implant lot number |
| Q29 | date |  |  | SI | Expiry date |
| Q30 | varchar |  |  | SI | Implant palpated by clinician post insertion |
| Q31 | varchar |  |  | SI | Implant palpated by patient post insertion |
| Q32 | varchar |  |  | SI | Provided patient information |
| Q33 | varchar |  |  | SI | Type of information provided |
| Q34 | varchar |  |  | SI | Card (with insertion details) provided to patient |
| Q35 | varchar |  |  | SI | Need for additional contraception / abstinence for... |
| Q36 | varchar |  |  | SI | Need for follow up urine Beta-hCG in 4 weeks discu... |
| Q37 | varchar |  |  | SI | Insertion procedure details |
| Q38 | varchar |  |  | SI | Discuss the following items with the patient and e... |
| Q39 | varchar |  |  | SI | BENEFITS, RISKS AND SIDE EFFECTS |
| Q40 | varchar |  |  | SI | The benefits, risks and side effects of using the ... |
| Q41 | varchar |  |  | SI | Effectiveness of implant. |
| Q42 | varchar |  |  | SI | Approximately 99% effective. |
| Q43 | varchar |  |  | SI | The implant does not offer STI protection. |
| Q44 | varchar |  |  | SI | ALLERGIC REACTIONS |
| Q45 | varchar |  |  | SI | The patient will advise of all known allergies inc... |
| Q46 | varchar |  |  | SI | INSERTION AND REMOVAL |
| Q47 | varchar |  |  | SI | The patient will advise all current and future hea... |
| Q48 | varchar |  |  | SI | SCARRING |
| Q49 | varchar |  |  | SI | Insertion and removal will leave a small scar in t... |
| Q50 | varchar |  |  | SI | REMOVAL AFTER THREE YEARS OR SOONER |
| Q51 | varchar |  |  | SI | The implant must be removed after three years, or ... |
| Q52 | varchar |  |  | SI | The patient is responsible to ensure that this hap... |
| Q53 | varchar |  |  | SI | Removal procedure details |
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