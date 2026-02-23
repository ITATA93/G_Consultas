# questionnaire.QTCPIPMPNI

> Pressure Injury Prevention and Management Plan - Neonate/Infant

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pressure Injury Prevention and Management Plan - Neonate/Infant

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Skin inspection must be performed on all preterm n... |
| Q02 | varchar |  |  | SI | on admission |
| Q03 | varchar |  |  | SI | and daily until risk is reduced. |
| Q04 | varchar |  |  | SI | Document all pressure injuries, wounds, redness, s... |
| Q05 | varchar |  |  | SI | Skin inspection including looking under anything t... |
| Q06 | varchar |  |  | SI | Pressure injury present? |
| Q07 | varchar |  |  | SI | Commence individual wound chart for each wound ide... |
| Q08 | varchar |  |  | SI | Body map (baby) |
| Q09 | varchar |  |  | SI | Notes on skin inspection |
| Q10 | varchar |  |  | SI | Moisture problems? |
| Q11 | varchar |  |  | SI | Moisture management |
| Q12 | varchar |  |  | SI | Moisture management comments |
| Q13 | varchar |  |  | SI | Bed surface |
| Q14 | varchar |  |  | SI | Bed surface comments |
| Q15 | varchar |  |  | SI | Heels |
| Q16 | varchar |  |  | SI | Re-positioning plan |
| Q17 | varchar |  |  | SI | Reposition time-frame |
| Q18 | varchar |  |  | SI | Alternate between |
| Q19 | varchar |  |  | SI | Referrals required |
| Q20 | varchar |  |  | SI | • Skin inspection must be performed on all preterm... |
| Q21 | varchar |  |  | SI | on admission |
| Q22 | varchar |  |  | SI | and daily until risk is reduced. |
| Q23 | varchar |  |  | SI | • Document all pressure injuries, wounds, redness,... |
| Q24 | varchar |  |  | SI | on discharge or transfer, complete: |
| Q25 | varchar |  |  | SI | Braden Q Score |
| Q26 | varchar |  |  | SI | Skin inspection (for high to very high risk patien... |
| Q27 | varchar |  |  | SI | Positioning comments |
| Q28 | varchar |  |  | SI | Positioning plan |
| Q29 | varchar |  |  | SI | Additional comments |
| Q30 | varchar |  |  | SI | Have patients, carers and families been provided w... |
| Q31 | varchar |  |  | SI | Was the pressure injury present on admission? |
| Q32 | varchar |  |  | SI | Pressure injury stage |
| Q33 | varchar |  |  | SI | Was the pressure injury present on admission? |
| Q34 | date |  |  | SI | Date |
| Q35 | time |  |  | SI | Time |
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