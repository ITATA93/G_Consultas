# SQLUser.PAC_ServiceAgreementGPPractices

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GPP_ParRef | bigint | PK |  | NO | PAC_ServiceAgreement Parent Reference |
| GPP_Childsub | double |  |  | NO | Childsub |
| GPP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GPP_CreatedDate | date |  |  | SI | Created Date |
| GPP_CreatedTime | time |  |  | SI | Created Time |
| GPP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GPP_Practice | varchar |  |  | SI | Practice |
| GPP_RowId | varchar |  |  | NO | - |
| GPP_UpdatedDate | date |  |  | SI | Updated Date |
| GPP_UpdatedTime | time |  |  | SI | Updated Time |
| GPP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Skin inspection must be performed on all preterm n... |
| Q02 | - |  |  | SI | on admission |
| Q03 | - |  |  | SI | and daily until risk is reduced. |
| Q04 | - |  |  | SI | Document all pressure injuries, wounds, redness, s... |
| Q05 | - |  |  | SI | Skin inspection including looking under anything t... |
| Q06 | - |  |  | SI | Pressure injury present? |
| Q07 | - |  |  | SI | Commence individual wound chart for each wound ide... |
| Q08 | - |  |  | SI | Body map (baby) |
| Q09 | - |  |  | SI | Notes on skin inspection |
| Q10 | - |  |  | SI | Moisture problems? |
| Q11 | - |  |  | SI | Moisture management |
| Q12 | - |  |  | SI | Moisture management comments |
| Q13 | - |  |  | SI | Bed surface |
| Q14 | - |  |  | SI | Bed surface comments |
| Q15 | - |  |  | SI | Heels |
| Q16 | - |  |  | SI | Re-positioning plan |
| Q17 | - |  |  | SI | Reposition time-frame |
| Q18 | - |  |  | SI | Alternate between |
| Q19 | - |  |  | SI | Referrals required |
| Q20 | - |  |  | SI | • Skin inspection must be performed on all preterm... |
| Q21 | - |  |  | SI | on admission |
| Q22 | - |  |  | SI | and daily until risk is reduced. |
| Q23 | - |  |  | SI | • Document all pressure injuries, wounds, redness,... |
| Q24 | - |  |  | SI | on discharge or transfer, complete: |
| Q25 | - |  |  | SI | Braden Q Score |
| Q26 | - |  |  | SI | Skin inspection (for high to very high risk patien... |
| Q27 | - |  |  | SI | Positioning comments |
| Q28 | - |  |  | SI | Positioning plan |
| Q29 | - |  |  | SI | Additional comments |
| Q30 | - |  |  | SI | Have patients, carers and families been provided w... |
| Q31 | - |  |  | SI | Was the pressure injury present on admission? |
| Q32 | - |  |  | SI | Pressure injury stage |
| Q33 | - |  |  | SI | Was the pressure injury present on admission? |
| Q34 | - |  |  | SI | Date |
| Q35 | - |  |  | SI | Time |
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