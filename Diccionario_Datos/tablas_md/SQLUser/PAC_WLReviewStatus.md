# SQLUser.PAC_WLReviewStatus

**Schema:** SQLUser
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLRST_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Auto-Antibodies |
| Q04 | - |  |  | SI | IgG concentration |
| Q05 | - |  |  | SI | Liver histology |
| Q06 | - |  |  | SI | Viral hepatitis |
| Q07 | - |  |  | SI | Acronyms: |
| Q08 | - |  |  | SI | AIH: Auto-Immune Hepatitis |
| Q09 | - |  |  | SI | ANA: Anti-Nuclear Antibody |
| Q10 | - |  |  | SI | LKM: Liver Kidney Microsome type 1 |
| Q11 | - |  |  | SI | SLA: Soluble Liver Antigen |
| Q12 | - |  |  | SI | SMA: Smooth Muscle Antibody |
| Q13 | - |  |  | SI | IgG: Immunolobulin G |
| Q14 | - |  |  | SI | SAH score |
| Q15 | - |  |  | SI | Sensitivity |
| Q16 | - |  |  | SI | Specificity |
| Q17 | - |  |  | SI | Positive predictive value |
| Q18 | - |  |  | SI | Negative predictive value |
| Q19 | - |  |  | SI | ≥7 |
| Q20 | - |  |  | SI | 81% |
| Q21 | - |  |  | SI | (71% to 88%) |
| Q22 | - |  |  | SI | 99% |
| Q23 | - |  |  | SI | (97% to 100%) |
| Q24 | - |  |  | SI | 97% |
| Q25 | - |  |  | SI | (91% to 100%) |
| Q26 | - |  |  | SI | 93% |
| Q27 | - |  |  | SI | (89% to 96%) |
| Q28 | - |  |  | SI | ≥6 |
| Q29 | - |  |  | SI | 88% |
| Q30 | - |  |  | SI | (80% to 94%) |
| Q31 | - |  |  | SI | 97% |
| Q32 | - |  |  | SI | (94% to 99%) |
| Q33 | - |  |  | SI | 91% |
| Q34 | - |  |  | SI | (83% to 96%) |
| Q35 | - |  |  | SI | 95% |
| Q36 | - |  |  | SI | (92% to 98%) |
| Q37 | - |  |  | SI | ≥5 |
| Q38 | - |  |  | SI | 97% |
| Q39 | - |  |  | SI | (91% to 99%) |
| Q40 | - |  |  | SI | 93% |
| Q41 | - |  |  | SI | (89% to 96%) |
| Q42 | - |  |  | SI | 85% |
| Q43 | - |  |  | SI | (77% to 91%) |
| Q44 | - |  |  | SI | 99% |
| Q45 | - |  |  | SI | (96% to 100%) |
| Q46 | - |  |  | SI | Figures in parentheses are the 95% Clopper-Pearson... |
| Q47 | - |  |  | SI | Score |
| Q48 | - |  |  | SI | Classification |
| Q49 | - |  |  | SI | < 6 |
| Q50 | - |  |  | SI | Possible AIH (though further testing should be don... |
| Q51 | - |  |  | SI | 6 |
| Q52 | - |  |  | SI | Probable AIH |
| Q53 | - |  |  | SI | ≥7 |
| Q54 | - |  |  | SI | Likely AIH |
| Q55 | - |  |  | SI | Clinical score for estimating the probability that... |
| Q56 | - |  |  | SI | <6 : Possible AIH (though further testing should b... |
| Q57 | - |  |  | SI | 6: Probable AIH |
| Q58 | - |  |  | SI | >=7: Likely AIH |
| Q59 | - |  |  | SI | SAH score |
| Q60 | - |  |  | SI | SAH score |
| Q61 | - |  |  | SI | SAH score |
| Q62 | - |  |  | SI | Sensitivity |
| Q63 | - |  |  | SI | Sensitivity |
| Q64 | - |  |  | SI | Sensitivity |
| Q65 | - |  |  | SI | Specificity |
| Q66 | - |  |  | SI | Specificity |
| Q67 | - |  |  | SI | Specificity |
| Q68 | - |  |  | SI | Positive predictive value |
| Q69 | - |  |  | SI | Positive predictive value |
| Q70 | - |  |  | SI | Positive predictive value |
| Q71 | - |  |  | SI | Negative predictive value |
| Q72 | - |  |  | SI | Negative predictive value |
| Q73 | - |  |  | SI | Negative predictive value |
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
| WLRST_Code | varchar |  |  | NO | Code |
| WLRST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WLRST_CreatedDate | date |  |  | SI | Created Date |
| WLRST_CreatedTime | time |  |  | SI | Created Time |
| WLRST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WLRST_DateFrom | date |  |  | SI | Date From |
| WLRST_DateTo | date |  |  | SI | Date To |
| WLRST_Desc | varchar |  |  | NO | Description |
| WLRST_Owner | varchar |  |  | SI | Owner |
| WLRST_ResetReviewDate | varchar |  |  | SI | ResetReviewDate |
| WLRST_ResponseRequired | varchar |  |  | SI | Response Required |
| WLRST_UpdatedDate | date |  |  | SI | Updated Date |
| WLRST_UpdatedTime | time |  |  | SI | Updated Time |
| WLRST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*