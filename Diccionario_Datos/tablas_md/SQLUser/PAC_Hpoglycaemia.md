# SQLUser.PAC_Hpoglycaemia

**Schema:** SQLUser
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HPOG_RowId | bigint | PK |  | NO | - |
| HPOG_Code | varchar |  |  | NO | Code |
| HPOG_CreatedDate | date |  |  | SI | Created Date |
| HPOG_CreatedTime | time |  |  | SI | Created Time |
| HPOG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HPOG_Desc | varchar |  |  | NO | Description |
| HPOG_UpdatedDate | date |  |  | SI | Updated Date |
| HPOG_UpdatedTime | time |  |  | SI | Updated Time |
| HPOG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of current intensive care unit (ICU) admissio... |
| Q04 | - |  |  | SI | Days in ICU |
| Q05 | - |  |  | SI | Research trial information |
| Q06 | - |  |  | SI | Suitability to leave ICU |
| Q07 | - |  |  | SI | Decision date / time |
| Q08 | - |  |  | SI | Decision time |
| Q09 | - |  |  | SI | Discharge planning notes |
| Q10 | - |  |  | SI | Sedation |
| Q11 | - |  |  | SI | Sleep / Sleep pattern |
| Q12 | - |  |  | SI | Delirium |
| Q13 | - |  |  | SI | Adequate analgesia |
| Q14 | - |  |  | SI | Adequate glucose control |
| Q15 | - |  |  | SI | Feeing regimen |
| Q16 | - |  |  | SI | Lines - Dated / Removed / Changed |
| Q17 | - |  |  | SI | Antibiotics review |
| Q18 | - |  |  | SI | Venous Thromboembolism (VTE) prophylaxis |
| Q19 | - |  |  | SI | Stress ulcer prophylaxis |
| Q20 | - |  |  | SI | Resuscitation review / order |
| Q21 | - |  |  | SI | Need for family / relative discussion |
| Q22 | - |  |  | SI | Allied health referrals |
| Q23 | - |  |  | SI | Research |
| Q24 | - |  |  | SI | Patient diary |
| Q25 | - |  |  | SI | Bowels |
| Q26 | - |  |  | SI | Date bowels last opened |
| Q27 | - |  |  | SI | Notes |
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