# SQLUser.PAC_ServiceAgreementAdminCateg

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INS_ParRef | bigint | PK |  | NO | PAC_ServiceAgreement Parent Reference |
| INS_Childsub | double |  |  | NO | Childsub |
| INS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INS_CreatedDate | date |  |  | SI | Created Date |
| INS_CreatedTime | time |  |  | SI | Created Time |
| INS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INS_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INS_RowId | varchar |  |  | NO | - |
| INS_UpdatedDate | date |  |  | SI | Updated Date |
| INS_UpdatedTime | time |  |  | SI | Updated Time |
| INS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Consent provided by |
| Q04 | - |  |  | SI | Other consent provided by |
| Q05 | - |  |  | SI | Procedure |
| Q06 | - |  |  | SI | Removal details |
| Q07 | - |  |  | SI | Reason for removal |
| Q08 | - |  |  | SI | Other reason for removal details |
| Q09 | - |  |  | SI | Removal site |
| Q10 | - |  |  | SI | Other removal site |
| Q11 | - |  |  | SI | Follow up visit |
| Q12 | - |  |  | SI | weeks |
| Q13 | - |  |  | SI | Follow up visit in (weeks) |
| Q14 | - |  |  | SI | Removal procedure details |
| Q15 | - |  |  | SI | Insertion details |
| Q16 | - |  |  | SI | Contraception provision action already completed |
| Q17 | - |  |  | SI | Exclusion of pregnancy |
| Q18 | - |  |  | SI | Medical Eligibility Criteria (MEC) |
| Q19 | - |  |  | SI | MEC notes |
| Q20 | - |  |  | SI | Sexually transmitted infection (STI) screening und... |
| Q21 | - |  |  | SI | Date of most recent STI screen |
| Q22 | - |  |  | SI | Estimated date of STI screen |
| Q23 | - |  |  | SI | STI screen details |
| Q24 | - |  |  | SI | Discussion undertaken in regard to benefits, risk ... |
| Q25 | - |  |  | SI | Insertion site |
| Q26 | - |  |  | SI | Other insertion site details |
| Q27 | - |  |  | SI | Implant serial number |
| Q28 | - |  |  | SI | Implant lot number |
| Q29 | - |  |  | SI | Expiry date |
| Q30 | - |  |  | SI | Implant palpated by clinician post insertion |
| Q31 | - |  |  | SI | Implant palpated by patient post insertion |
| Q32 | - |  |  | SI | Provided patient information |
| Q33 | - |  |  | SI | Type of information provided |
| Q34 | - |  |  | SI | Card (with insertion details) provided to patient |
| Q35 | - |  |  | SI | Need for additional contraception / abstinence for... |
| Q36 | - |  |  | SI | Need for follow up urine Beta-hCG in 4 weeks discu... |
| Q37 | - |  |  | SI | Insertion procedure details |
| Q38 | - |  |  | SI | Discuss the following items with the patient and e... |
| Q39 | - |  |  | SI | BENEFITS, RISKS AND SIDE EFFECTS |
| Q40 | - |  |  | SI | The benefits, risks and side effects of using the ... |
| Q41 | - |  |  | SI | Effectiveness of implant. |
| Q42 | - |  |  | SI | Approximately 99% effective. |
| Q43 | - |  |  | SI | The implant does not offer STI protection. |
| Q44 | - |  |  | SI | ALLERGIC REACTIONS |
| Q45 | - |  |  | SI | The patient will advise of all known allergies inc... |
| Q46 | - |  |  | SI | INSERTION AND REMOVAL |
| Q47 | - |  |  | SI | The patient will advise all current and future hea... |
| Q48 | - |  |  | SI | SCARRING |
| Q49 | - |  |  | SI | Insertion and removal will leave a small scar in t... |
| Q50 | - |  |  | SI | REMOVAL AFTER THREE YEARS OR SOONER |
| Q51 | - |  |  | SI | The implant must be removed after three years, or ... |
| Q52 | - |  |  | SI | The patient is responsible to ensure that this hap... |
| Q53 | - |  |  | SI | Removal procedure details |
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