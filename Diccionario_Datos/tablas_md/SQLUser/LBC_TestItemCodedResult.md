# SQLUser.LBC_TestItemCodedResult

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTICR_ParRef | bigint | PK |  | NO | The Test Item the Standard Code can be selected fo... |
| LBCTICR_ClinicalReviewFlag | varchar |  |  | SI | Flag to indicate clinical review |
| LBCTICR_Code | varchar |  |  | NO | Code 
Exception for collation to allow + and - si... |
| LBCTICR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTICR_CodeTranslated | varchar |  |  | SI | - |
| LBCTICR_DateFrom | date |  |  | NO | Effective date for the record |
| LBCTICR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTICR_DefaultSnomedTerms | varchar |  |  | SI | List of default snomed codes (will be copied to th... |
| LBCTICR_Desc | varchar |  |  | NO | Description
Exception for collation to allow + an... |
| LBCTICR_DescTranslated | varchar |  |  | SI | - |
| LBCTICR_ExcludeFromElectronicIssue | varchar |  |  | SI |  Exclude From Electronic Issue |
| LBCTICR_ImplicitValue | varchar |  |  | SI | Implicit value
Only available for antibody screen |
| LBCTICR_InfectionReport | varchar |  |  | SI | Infection Report |
| LBCTICR_InfectionReportTime | time |  |  | SI | Infection Report Time |
| LBCTICR_NotPerformed | varchar |  |  | SI | Not Performed Flag |
| LBCTICR_RangeFlag | varchar |  |  | SI | Flag to indicate if range is normal, abnormal or b... |
| LBCTICR_RowID | varchar |  |  | NO | - |
| LBCTICR_SuppressBilling | varchar |  |  | SI | Suppress Billing |
| Q01 | - |  |  | SI | Mes |
| Q02 | - |  |  | SI | Año |
| Q03 | - |  |  | SI | Total Ambulancia |
| Q04 | - |  |  | SI | Ambulancia por compra de servicio |
| Q05 | - |  |  | SI | Total Marítimo |
| Q06 | - |  |  | SI | Marítimo por compra de servicio |
| Q07 | - |  |  | SI | Total Aéreo |
| Q08 | - |  |  | SI | Aéreo por compra de servicio |
| QHR | - |  |  | SI | Establecimiento |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*