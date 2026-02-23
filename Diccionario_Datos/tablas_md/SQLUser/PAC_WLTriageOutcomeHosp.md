# SQLUser.PAC_WLTriageOutcomeHosp

**Schema:** SQLUser
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSP_ParRef | bigint | PK |  | NO | PAC_WLTriageOutcome Parent Reference |
| HOSP_Childsub | double |  |  | NO | Childsub |
| HOSP_CreatedDate | date |  |  | SI | Created Date |
| HOSP_CreatedTime | time |  |  | SI | Created Time |
| HOSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOSP_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| HOSP_RowId | varchar |  |  | NO | - |
| HOSP_UpdatedDate | date |  |  | SI | Updated Date |
| HOSP_UpdatedTime | time |  |  | SI | Updated Time |
| HOSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Surgeon |
| Q04 | - |  |  | SI | Surgeon (public) |
| Q05 | - |  |  | SI | Surgeon (private) |
| Q06 | - |  |  | SI | Medical oncologist&nbsp |
| Q07 | - |  |  | SI | Medical oncologist (public) |
| Q08 | - |  |  | SI | Medical oncologist (private) |
| Q09 | - |  |  | SI | Medical officer |
| Q10 | - |  |  | SI | Medical officer (public) |
| Q11 | - |  |  | SI | Medical officer (private) |
| Q12 | - |  |  | SI | Referral from&nbsp |
| Q13 | - |  |  | SI | Other referral details |
| Q14 | - |  |  | SI | Notes |
| Q15 | - |  |  | SI | Core biopsy |
| Q16 | - |  |  | SI | Estrogen receptor (ER) |
| Q17 | - |  |  | SI | Progesterone receptor (PR) |
| Q18 | - |  |  | SI | Human epidermal growth factor receptor 2 (HER2) |
| Q19 | - |  |  | SI | Ki-67 nuclear antigen |
| Q20 | - |  |  | SI | Notes |
| Q21 | - |  |  | SI | ER |
| Q22 | - |  |  | SI | PR |
| Q23 | - |  |  | SI | HER2 |
| Q24 | - |  |  | SI | Ki67 |
| Q25 | - |  |  | SI | Family history of breast cancer |
| Q26 | - |  |  | SI | BReast CAncer gene (BRCA) mutation |
| Q27 | - |  |  | SI | Referral to |
| Q28 | - |  |  | SI | Other referral to |
| Q29 | - |  |  | SI | Notes |
| Q30 | - |  |  | SI | Operation |
| Q31 | - |  |  | SI | Chemotherapy (Adjuvant / Neo-adjuvant) |
| Q32 | - |  |  | SI | Herceptin |
| Q33 | - |  |  | SI | Radiotherapy&nbsp |
| Q34 | - |  |  | SI | Hormone |
| Q35 | - |  |  | SI | Supportive medicine |
| Q36 | - |  |  | SI | Metastatic work up |
| Q37 | - |  |  | SI | Metastatic disease |
| Q38 | - |  |  | SI | Other site details |
| Q39 | - |  |  | SI | Notes |
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