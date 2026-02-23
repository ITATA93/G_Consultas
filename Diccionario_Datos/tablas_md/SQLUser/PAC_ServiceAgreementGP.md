# SQLUser.PAC_ServiceAgreementGP

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GP_ParRef | bigint | PK |  | NO | PAC_ServiceAgreement Parent Reference |
| GP_Childsub | double |  |  | NO | Childsub |
| GP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GP_CreatedDate | date |  |  | SI | Created Date |
| GP_CreatedTime | time |  |  | SI | Created Time |
| GP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GP_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| GP_RowId | varchar |  |  | NO | - |
| GP_UpdatedDate | date |  |  | SI | Updated Date |
| GP_UpdatedTime | time |  |  | SI | Updated Time |
| GP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Skin inspection including looking under tubes, pro... |
| Q02 | - |  |  | SI | Pressure injury present?	 |
| Q03 | - |  |  | SI | Ensure a separate Wound Management form is complet... |
| Q04 | - |  |  | SI | Moisture management	 |
| Q05 | - |  |  | SI | Moisture management comments	 |
| Q06 | - |  |  | SI | Bed surface	 |
| Q07 | - |  |  | SI | Bed surface comments	 |
| Q08 | - |  |  | SI | Chair |
| Q09 | - |  |  | SI | Chair comments	 |
| Q10 | - |  |  | SI | Heels |
| Q11 | - |  |  | SI | Re-positioning plan	 |
| Q12 | - |  |  | SI | High density foam mattress	 |
| Q13 | - |  |  | SI | Static air filled mattress overlay	 |
| Q14 | - |  |  | SI | Alternating pressure overlay (2 cycle)	 |
| Q15 | - |  |  | SI | Alternating pressure mattress (2 cell cycle)	 |
| Q16 | - |  |  | SI | Alternatine pressure mattress(3 cell cycle)	 |
| Q17 | - |  |  | SI | Heels comments |
| Q18 | - |  |  | SI | Body Map |
| Q19 | - |  |  | SI | Pressure Injury Present |
| Q20 | - |  |  | SI | Have patients, carers and families been provided w... |
| Q21 | - |  |  | SI | Was pressure injury present on admission? |
| Q22 | - |  |  | SI | Moisture management problems |
| Q23 | - |  |  | SI | Referral considerations |
| Q24 | - |  |  | SI | Consider referral to: |
| Q25 | - |  |  | SI | • Continence advisor if moisture management proble... |
| Q26 | - |  |  | SI | • Dietician if nutrition concerns |
| Q27 | - |  |  | SI | • Physiotherapist if mobility concerns |
| Q28 | - |  |  | SI | • Occupational therapy for assessment of need or t... |
| Q29 | - |  |  | SI | • Wound consultant if patient has a pressure injur... |
| Q30 | - |  |  | SI | • Podiatry if patient has a lower limb pressure in... |
| Q31 | - |  |  | SI | Communicate pressure injury risk level, presence o... |
| Q32 | - |  |  | SI | Skin Inspection must be performed on all patients ... |
| Q33 | - |  |  | SI | Bed surface |
| Q34 | - |  |  | SI | Skin inspection comments |
| Q35 | - |  |  | SI | Date |
| Q36 | - |  |  | SI | Time |
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