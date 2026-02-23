# SQLUser.PA_DischargeSummaryNonGov

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NG_ParRef | bigint | PK |  | NO | PA_DischargeSummary Parent Reference |
| NG_Childsub | double |  |  | NO | Childsub |
| NG_NonGovOrg_DR | bigint |  | FK | SI | Des Ref NonGovOrg |
| NG_PrimaryRecipient | varchar |  |  | SI | Primary Recipient |
| NG_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | International Normalised Ratio (INR) Guidelines fo... |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Indication and recommended INR range |
| Q05 | - |  |  | SI | Other indication, including INR range |
| Q06 | - |  |  | SI | INR range (If different to recommendation) |
| Q07 | - |  |  | SI | Rationale for different INR range |
| Q08 | - |  |  | SI | For All Patients Initiated on Warfarin |
| Q09 | - |  |  | SI | Warfarin education provided |
| Q10 | - |  |  | SI | Anticoagulation education record completed |
| Q11 | - |  |  | SI | Reason for no education |
| Q12 | - |  |  | SI | Usual dose, if taken previously (mg) |
| Q13 | - |  |  | SI | General practitioner details confirmed and updated |
| Q14 | - |  |  | SI | Requires bridging anticoagulation e.g. enoxaparin ... |
| Q15 | - |  |  | SI | Ensure patient has an inpatient order for bridging... |
| Q16 | - |  |  | SI | Ensure patient has: |
| Q17 | - |  |  | SI | 1. A discharge or outpatient prescription for brid... |
| Q18 | - |  |  | SI | 2. Equipment (e.g. sharps kit) required for self-a... |
| Q19 | - |  |  | SI | For Outpatients |
| Q20 | - |  |  | SI | Patient location |
| Q21 | - |  |  | SI | Other patient location |
| Q22 | - |  |  | SI | Warfarin administration |
| Q23 | - |  |  | SI | Ensure patient has an inpatient order for warfarin... |
| Q24 | - |  |  | SI | Ensure patient has a discharge or outpatient presc... |
| Q25 | - |  |  | SI | Guidelines |
| Q26 | - |  |  | SI | Use in conjunction with local warfarin management ... |
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