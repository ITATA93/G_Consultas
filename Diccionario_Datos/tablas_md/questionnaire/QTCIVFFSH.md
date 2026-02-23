# questionnaire.QTCIVFFSH

> Fertility Screening History

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fertility Screening History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | numeric |  |  | SI | Duration of current relationship (years) |
| Q01A | varchar |  |  | SI | Screening History |
| Q03 | varchar |  |  | SI | Menstrual History |
| Q08 | varchar |  |  | SI | Hirsutism |
| Q09 | varchar |  |  | SI | Galactorrhea |
| Q10 | varchar |  |  | SI | Abnormal weight gain |
| Q11 | varchar |  |  | SI | Dysmenorrhea |
| Q12 | varchar |  |  | SI | Contraception |
| Q12A | varchar |  |  | SI | Contraception type |
| Q12B | varchar |  |  | SI | Other contraception |
| Q12ObsDR | varchar |  | FK | SI | Contraception DR |
| Q13 | varchar |  |  | SI | Sexual History |
| Q14 | varchar |  |  | SI | Coital frequency |
| Q15 | varchar |  |  | SI | Coital difficulty |
| Q16 | varchar |  |  | SI | Dyspareunia |
| Q16ObsDR | varchar |  | FK | SI | Dyspareunia DR |
| Q17 | varchar |  |  | SI | Obstetric History |
| Q20 | varchar |  |  | SI | History of Infertility |
| Q21 | varchar |  |  | SI | Ovulation induction |
| Q21M | varchar |  |  | SI | Ovulation induction |
| Q22 | varchar |  |  | SI | Previous ART |
| Q22A | varchar |  |  | SI | ART type |
| Q22B | varchar |  |  | SI | ART place |
| Q22C | date |  |  | SI | ART year |
| Q22D | varchar |  |  | SI | ART year |
| Q23 | varchar |  |  | SI | Partner's Medical History |
| Q24 | varchar |  |  | SI | Partner's name |
| Q25 | numeric |  |  | SI | Partner's age (Years) |
| Q26 | numeric |  |  | SI | Number of children from this wife |
| Q27 | varchar |  |  | SI | Other wife / wives |
| Q28 | numeric |  |  | SI | Number of children from other wife / wives |
| Q29 | numeric |  |  | SI | Youngest child age (years) |
| Q30 | varchar |  |  | SI | Partner's occupation |
| Q31 | varchar |  |  | SI | Does the partner smoke? |
| Q31ObsDR | varchar |  | FK | SI | Does the partner smoke? DR |
| Q32 | varchar |  |  | SI | Alcohol units per week - currently |
| Q32ObsDR | varchar |  | FK | SI | Alcohol units per week - currently DR |
| Q33 | varchar |  |  | SI | Relevant medical history |
| Q34 | varchar |  |  | SI | Relevant surgical history |
| Q35 | varchar |  |  | SI | Genital trauma |
| Q36 | varchar |  |  | SI | Testicular biopsy |
| Q36A | date |  |  | SI | Biopsy date |
| Q36B | varchar |  |  | SI | Biopsy result |
| Q37 | varchar |  |  | SI | Partner's Semen Analysis |
| Q38 | numeric |  |  | SI | Semen volume (ml) |
| Q39 | numeric |  |  | SI | Sperm count (million) |
| Q40 | numeric |  |  | SI | Motility (%) |
| Q43 | varchar |  |  | SI | Ovulation Induction |
| Q47 | date |  |  | SI | Date |
| Q48 | time |  |  | SI | Time |
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