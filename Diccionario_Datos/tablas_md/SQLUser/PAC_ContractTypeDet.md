# SQLUser.PAC_ContractTypeDet

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | bigint | PK |  | NO | PAC_ContractType Parent Reference |
| ChildQ21ADR | - |  |  | SI | Child Reference: Ovulation induction table |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_ContractRole | varchar |  |  | SI | ContractRole |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | Date From |
| DET_DateTo | date |  |  | SI | Date To |
| DET_FundArangement | varchar |  |  | SI | FundArangement |
| DET_RowId | varchar |  |  | NO | - |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Duration of current relationship (years) |
| Q01A | - |  |  | SI | Screening History |
| Q03 | - |  |  | SI | Menstrual History |
| Q08 | - |  |  | SI | Hirsutism |
| Q09 | - |  |  | SI | Galactorrhea |
| Q10 | - |  |  | SI | Abnormal weight gain |
| Q11 | - |  |  | SI | Dysmenorrhea |
| Q12 | - |  |  | SI | Contraception |
| Q12A | - |  |  | SI | Contraception type |
| Q12B | - |  |  | SI | Other contraception |
| Q12ObsDR | - |  |  | SI | Contraception DR |
| Q13 | - |  |  | SI | Sexual History |
| Q14 | - |  |  | SI | Coital frequency |
| Q15 | - |  |  | SI | Coital difficulty |
| Q16 | - |  |  | SI | Dyspareunia |
| Q16ObsDR | - |  |  | SI | Dyspareunia DR |
| Q17 | - |  |  | SI | Obstetric History |
| Q20 | - |  |  | SI | History of Infertility |
| Q21 | - |  |  | SI | Ovulation induction |
| Q21M | - |  |  | SI | Ovulation induction |
| Q22 | - |  |  | SI | Previous ART |
| Q22A | - |  |  | SI | ART type |
| Q22B | - |  |  | SI | ART place |
| Q22C | - |  |  | SI | ART year |
| Q22D | - |  |  | SI | ART year |
| Q23 | - |  |  | SI | Partner's Medical History |
| Q24 | - |  |  | SI | Partner's name |
| Q25 | - |  |  | SI | Partner's age (Years) |
| Q26 | - |  |  | SI | Number of children from this wife |
| Q27 | - |  |  | SI | Other wife / wives |
| Q28 | - |  |  | SI | Number of children from other wife / wives |
| Q29 | - |  |  | SI | Youngest child age (years) |
| Q30 | - |  |  | SI | Partner's occupation |
| Q31 | - |  |  | SI | Does the partner smoke? |
| Q31ObsDR | - |  |  | SI | Does the partner smoke? DR |
| Q32 | - |  |  | SI | Alcohol units per week - currently |
| Q32ObsDR | - |  |  | SI | Alcohol units per week - currently DR |
| Q33 | - |  |  | SI | Relevant medical history |
| Q34 | - |  |  | SI | Relevant surgical history |
| Q35 | - |  |  | SI | Genital trauma |
| Q36 | - |  |  | SI | Testicular biopsy |
| Q36A | - |  |  | SI | Biopsy date |
| Q36B | - |  |  | SI | Biopsy result |
| Q37 | - |  |  | SI | Partner's Semen Analysis |
| Q38 | - |  |  | SI | Semen volume (ml) |
| Q39 | - |  |  | SI | Sperm count (million) |
| Q40 | - |  |  | SI | Motility (%) |
| Q43 | - |  |  | SI | Ovulation Induction |
| Q47 | - |  |  | SI | Date |
| Q48 | - |  |  | SI | Time |
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