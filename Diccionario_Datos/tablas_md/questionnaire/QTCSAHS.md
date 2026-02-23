# questionnaire.QTCSAHS

> Simplified Autoimmune Hepatitis (SAH) Score

**Schema:** questionnaire
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Simplified Autoimmune Hepatitis (SAH) Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Auto-Antibodies |
| Q04 | varchar |  |  | SI | IgG concentration |
| Q05 | varchar |  |  | SI | Liver histology |
| Q06 | varchar |  |  | SI | Viral hepatitis |
| Q07 | varchar |  |  | SI | Acronyms: |
| Q08 | varchar |  |  | SI | AIH: Auto-Immune Hepatitis; |
| Q09 | varchar |  |  | SI | ANA: Anti-Nuclear Antibody; |
| Q10 | varchar |  |  | SI | LKM: Liver Kidney Microsome type 1; |
| Q11 | varchar |  |  | SI | SLA: Soluble Liver Antigen; |
| Q12 | varchar |  |  | SI | SMA: Smooth Muscle Antibody; |
| Q13 | varchar |  |  | SI | IgG: Immunolobulin G; |
| Q14 | varchar |  |  | SI | SAH score |
| Q15 | varchar |  |  | SI | Sensitivity |
| Q16 | varchar |  |  | SI | Specificity |
| Q17 | varchar |  |  | SI | Positive predictive value |
| Q18 | varchar |  |  | SI | Negative predictive value |
| Q19 | varchar |  |  | SI | ≥7 |
| Q20 | varchar |  |  | SI | 81% |
| Q21 | varchar |  |  | SI | (71% to 88%) |
| Q22 | varchar |  |  | SI | 99% |
| Q23 | varchar |  |  | SI | (97% to 100%) |
| Q24 | varchar |  |  | SI | 97% |
| Q25 | varchar |  |  | SI | (91% to 100%) |
| Q26 | varchar |  |  | SI | 93% |
| Q27 | varchar |  |  | SI | (89% to 96%) |
| Q28 | varchar |  |  | SI | ≥6 |
| Q29 | varchar |  |  | SI | 88% |
| Q30 | varchar |  |  | SI | (80% to 94%) |
| Q31 | varchar |  |  | SI | 97% |
| Q32 | varchar |  |  | SI | (94% to 99%) |
| Q33 | varchar |  |  | SI | 91% |
| Q34 | varchar |  |  | SI | (83% to 96%) |
| Q35 | varchar |  |  | SI | 95% |
| Q36 | varchar |  |  | SI | (92% to 98%) |
| Q37 | varchar |  |  | SI | ≥5 |
| Q38 | varchar |  |  | SI | 97% |
| Q39 | varchar |  |  | SI | (91% to 99%) |
| Q40 | varchar |  |  | SI | 93% |
| Q41 | varchar |  |  | SI | (89% to 96%) |
| Q42 | varchar |  |  | SI | 85% |
| Q43 | varchar |  |  | SI | (77% to 91%) |
| Q44 | varchar |  |  | SI | 99% |
| Q45 | varchar |  |  | SI | (96% to 100%) |
| Q46 | varchar |  |  | SI | Figures in parentheses are the 95% Clopper-Pearson... |
| Q47 | varchar |  |  | SI | Score |
| Q48 | varchar |  |  | SI | Classification |
| Q49 | varchar |  |  | SI | < 6  |
| Q50 | varchar |  |  | SI | Possible AIH (though further testing should be don... |
| Q51 | varchar |  |  | SI | 6 |
| Q52 | varchar |  |  | SI | Probable AIH |
| Q53 | varchar |  |  | SI | ≥7 |
| Q54 | varchar |  |  | SI | Likely AIH |
| Q55 | varchar |  |  | SI | Clinical score for estimating the probability that... |
| Q56 | varchar |  |  | SI | <6 : Possible AIH (though further testing should b... |
| Q57 | varchar |  |  | SI | 6: Probable AIH |
| Q58 | varchar |  |  | SI | >=7: Likely AIH |
| Q59 | varchar |  |  | SI | SAH score |
| Q60 | varchar |  |  | SI | SAH score |
| Q61 | varchar |  |  | SI | SAH score |
| Q62 | varchar |  |  | SI | Sensitivity |
| Q63 | varchar |  |  | SI | Sensitivity |
| Q64 | varchar |  |  | SI | Sensitivity |
| Q65 | varchar |  |  | SI | Specificity |
| Q66 | varchar |  |  | SI | Specificity |
| Q67 | varchar |  |  | SI | Specificity |
| Q68 | varchar |  |  | SI | Positive predictive value |
| Q69 | varchar |  |  | SI | Positive predictive value |
| Q70 | varchar |  |  | SI | Positive predictive value |
| Q71 | varchar |  |  | SI | Negative predictive value |
| Q72 | varchar |  |  | SI | Negative predictive value |
| Q73 | varchar |  |  | SI | Negative predictive value |
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