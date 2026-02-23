# SQLUser.PAC_SnomedCrossMapTargets

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOCMT_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Further node clearance |
| Q02 | - |  |  | SI | Cavity shave	 |
| Q03 | - |  |  | SI | Chemotherapy planned |
| Q04 | - |  |  | SI | Chemotherapy in progress	 |
| Q05 | - |  |  | SI | Radiotherapy planned	 |
| Q06 | - |  |  | SI | Radiotherapy in progress	 |
| Q07 | - |  |  | SI | Notes |
| Q08 | - |  |  | SI | Axilla |
| Q09 | - |  |  | SI | Upper arm |
| Q10 | - |  |  | SI | Cubital fossa |
| Q11 | - |  |  | SI | Forearm / wrist |
| Q12 | - |  |  | SI | Trunk |
| Q13 | - |  |  | SI | Compliant with exercise |
| Q14 | - |  |  | SI | Arm movement |
| Q15 | - |  |  | SI | Advice given |
| Q16 | - |  |  | SI | Notes |
| Q17 | - |  |  | SI | Appointment offered |
| Q18 | - |  |  | SI | Follow up call offered |
| Q19 | - |  |  | SI | Any other information |
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
| SNOCMT_CreatedDate | date |  |  | SI | Created Date |
| SNOCMT_CreatedTime | time |  |  | SI | Created Time |
| SNOCMT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOCMT_TargetAdvice | varchar |  |  | SI | TargetAdvice |
| SNOCMT_TargetCodes | varchar |  |  | SI | TargetCodes |
| SNOCMT_TargetID | varchar |  |  | SI | TargetID |
| SNOCMT_TargetRule | varchar |  |  | SI | TargetRule |
| SNOCMT_TargetSchemeID | varchar |  |  | SI | TargetSchemeID |
| SNOCMT_UpdatedDate | date |  |  | SI | Updated Date |
| SNOCMT_UpdatedTime | time |  |  | SI | Updated Time |
| SNOCMT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*