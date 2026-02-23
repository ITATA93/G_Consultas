# SQLUser.LBC_TestSetRevisionItem

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRI_ParRef | bigint | PK |  | NO | Parent TestSet DR |
| LBCTSRI_Billable | varchar |  |  | SI | Billable |
| LBCTSRI_BloodGroupStatus | varchar |  |  | SI | Resulting blood group status
Only applicable for ... |
| LBCTSRI_Bold | varchar |  |  | SI | Bold on Doctor Report |
| LBCTSRI_CalcAllRefResultsRequired | varchar |  |  | SI | Flag to indicate if calculation is only executed i... |
| LBCTSRI_CalcAlways | varchar |  |  | SI | Flag to indicate if calculation is always executed... |
| LBCTSRI_CalcFormula | varchar |  |  | SI | Test Set Item is Reportable
Default 'Y'
Calculat... |
| LBCTSRI_CalcIncludeNumCodes | varchar |  |  | SI | Flag to indicate if numeric codes should be consid... |
| LBCTSRI_CalcTSItems | varchar |  |  | SI | List of TSItems which are referenced in the calcul... |
| LBCTSRI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRI_CodedResultSeparator | varchar |  |  | SI | Multi Coded Result Separator |
| LBCTSRI_Column | integer |  |  | SI | The number of the column the Test Item is displaye... |
| LBCTSRI_IgnoreSigIfDeltaCheckPass | varchar |  |  | SI | Ignore Significant Result if Delta Check Passes |
| LBCTSRI_Italic | varchar |  |  | SI | Italics on Doctor Report |
| LBCTSRI_ManualInstrumentSchedule | varchar |  |  | SI | Manual Instrument Schedule
Do not schedule this t... |
| LBCTSRI_Materials | varchar |  |  | SI | Perform on material
If set this test set item wil... |
| LBCTSRI_PlotByDefault | varchar |  |  | SI | Plot on graph by default
Flag to indicate if the ... |
| LBCTSRI_PlotByDefaultForDocRpt | varchar |  |  | SI | Plot on graph by default For Doctor Report
Flag t... |
| LBCTSRI_PrintSequence | double |  |  | SI | Report Sequence
Sequence of the TestItem within t... |
| LBCTSRI_ReportPosition | varchar |  |  | SI | Report Position |
| LBCTSRI_Reportable | varchar |  |  | SI | - |
| LBCTSRI_Required | varchar |  |  | SI | Required: 'Yes' if the TestItem must be present in... |
| LBCTSRI_RowID | varchar |  |  | NO | - |
| LBCTSRI_Sequence | double |  |  | SI | Sequence
Sequence of the TestItem within the Test... |
| LBCTSRI_ShareResult | varchar |  |  | SI | Share Result
Share Result with all test set items... |
| LBCTSRI_SignificantResultEval | varchar |  |  | SI | Significant Result Evaluation  |
| LBCTSRI_TestItem_DR | bigint |  | FK | NO | TestItem |
| LBCTSRI_TextResultTemplate_DR | bigint |  | FK | SI | The text result template used if the test item is ... |
| Q01 | - |  |  | SI | Mes |
| Q02 | - |  |  | SI | Año |
| Q03 | - |  |  | SI | Normal con rezago |
| Q04 | - |  |  | SI | Normal con rezago 1 |
| Q05 | - |  |  | SI | Normal con rezago 2 |
| Q06 | - |  |  | SI | Normal con rezago 3 |
| Q07 | - |  |  | SI | Normal con rezago 4 |
| Q08 | - |  |  | SI | Normal con rezago 5 |
| Q09 | - |  |  | SI | Normal con rezago 6 |
| Q10 | - |  |  | SI | Normal con rezago 7 |
| Q11 | - |  |  | SI | Normal con rezago 8 |
| Q12 | - |  |  | SI | Riesgo |
| Q13 | - |  |  | SI | Riesgo 1 |
| Q14 | - |  |  | SI | Riesgo 2 |
| Q15 | - |  |  | SI | Riesgo 3 |
| Q16 | - |  |  | SI | Riesgo 4 |
| Q17 | - |  |  | SI | Riesgo 5 |
| Q18 | - |  |  | SI | Riesgo 6 |
| Q19 | - |  |  | SI | Riesgo 7 |
| Q20 | - |  |  | SI | Riesgo 8 |
| Q21 | - |  |  | SI | Retraso |
| Q22 | - |  |  | SI | Retraso 1 |
| Q23 | - |  |  | SI | Retraso 2 |
| Q24 | - |  |  | SI | Retraso 3 |
| Q25 | - |  |  | SI | Retraso 4 |
| Q26 | - |  |  | SI | Retraso 5 |
| Q27 | - |  |  | SI | Retraso 6 |
| Q28 | - |  |  | SI | Retraso 7 |
| Q29 | - |  |  | SI | Retraso 8 |
| Q30 | - |  |  | SI | Otra vulnerabilidad |
| Q31 | - |  |  | SI | Otra vulnerabilidad 1 |
| Q32 | - |  |  | SI | Otra vulnerabilidad 2 |
| Q33 | - |  |  | SI | Otra vulnerabilidad 3 |
| Q34 | - |  |  | SI | Otra vulnerabilidad 4 |
| Q35 | - |  |  | SI | Otra vulnerabilidad 5 |
| Q36 | - |  |  | SI | Otra vulnerabilidad 6 |
| Q37 | - |  |  | SI | Otra vulnerabilidad 7 |
| Q38 | - |  |  | SI | Otra vulnerabilidad 8 |
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