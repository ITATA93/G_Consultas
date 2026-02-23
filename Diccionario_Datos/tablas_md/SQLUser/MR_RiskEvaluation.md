# SQLUser.MR_RiskEvaluation

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RISK_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| Q01 | - |  |  | SI | Comment |
| Q02 | - |  |  | SI | Pump Check |
| Q03 | - |  |  | SI | RN 1 (Pump Check) |
| Q04 | - |  |  | SI | RN 2 (Pump Check) |
| Q05 | - |  |  | SI | Rate of Infusion |
| Q06 | - |  |  | SI | Amount in Syringe |
| Q07 | - |  |  | SI | Syringe Change |
| Q08 | - |  |  | SI | Syringe Change |
| Q09 | - |  |  | SI | RN 1 (Syringe Change) |
| Q10 | - |  |  | SI | RN 2 (Syringe Change) |
| Q11 | - |  |  | SI | Programme Change |
| Q12 | - |  |  | SI | RN 1 (Programme Change) |
| Q13 | - |  |  | SI | RN 2 (Programme Change) |
| Q14 | - |  |  | SI | Rate Change |
| Q15 | - |  |  | SI | Rate Increase / Decrease |
| Q16 | - |  |  | SI | RN 1 (Rate Change) |
| Q17 | - |  |  | SI | RN 2 (Rate Change) |
| Q18 | - |  |  | SI | Entered Discarded Amount in S8 Book |
| Q19 | - |  |  | SI | KETAMINE DOSE INFORMATION |
| Q20 | - |  |  | SI | KETAMINE INFUSION CHECKS |
| Q21 | - |  |  | SI | Comment Display |
| Q22 | - |  |  | SI | mgs |
| Q23 | - |  |  | SI | mls |
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
| RISK_BodySysProbStat_DR | bigint |  | FK | SI | Des Ref BodySysProbStat |
| RISK_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| RISK_Childsub | double |  |  | NO | Childsub |
| RISK_Date | date |  |  | SI | Date |
| RISK_Desc | varchar |  |  | SI | Description |
| RISK_EndDate | date |  |  | SI | EndDate |
| RISK_RiskCriteria_DR | varchar |  | FK | SI | Des Ref Risk Criteria |
| RISK_RiskEval_DR | varchar |  | FK | SI | Des Ref RiskEval |
| RISK_RiskParam_DR | varchar |  | FK | SI | Des Ref Risk Param |
| RISK_RowId | varchar |  |  | NO | - |
| RISK_Time | time |  |  | SI | Time |
| RISK_UpdateDate | date |  |  | SI | Update Date |
| RISK_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| RISK_UpdateTime | time |  |  | SI | Update Time |
| RISK_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*