# SQLUser.PA_DischargeSummaryRevStat

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REVSTAT_ParRef | bigint | PK |  | NO | PA_DischargeSummary Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Quality of cry |
| Q04 | - |  |  | SI | Reaction to parents |
| Q05 | - |  |  | SI | State variation |
| Q06 | - |  |  | SI | Colour |
| Q07 | - |  |  | SI | Hydration |
| Q08 | - |  |  | SI | Response (talk, smile) to social overtures |
| Q09 | - |  |  | SI | Normal (1 point) |
| Q10 | - |  |  | SI | Moderate impairment (3 points) |
| Q11 | - |  |  | SI | Severe impairment (5 points) |
| Q12 | - |  |  | SI | 1. McCarthy PL, Sharpe MR, Spiesel SZ, et al. Obse... |
| Q13 | - |  |  | SI | 2. Nigrovic LE, Mahajan PV, Blumberg SM, et al. Th... |
| Q14 | - |  |  | SI | The Yale Observation Scale (YOS) was described by ... |
| Q15 | - |  |  | SI | The Yale Observation Scale (YOS) score is a clinic... |
| Q16 | - |  |  | SI | Normal (1 point) |
| Q17 | - |  |  | SI | Normal (1 point) |
| Q18 | - |  |  | SI | Normal (1 point) |
| Q19 | - |  |  | SI | Normal (1 point) |
| Q20 | - |  |  | SI | Normal (1 point) |
| Q21 | - |  |  | SI | Normal (1 point) |
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
| REVSTAT_Childsub | double |  |  | NO | Childsub |
| REVSTAT_ReviewStatus_DR | bigint |  | FK | SI | Des Ref PACClinSumReviewStatus |
| REVSTAT_RowId | varchar |  |  | NO | - |
| REVSTAT_UpdateDate | date |  |  | SI | UpdateDate |
| REVSTAT_UpdateDoctor_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| REVSTAT_UpdateTime | time |  |  | SI | UpdateTime |
| REVSTAT_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*