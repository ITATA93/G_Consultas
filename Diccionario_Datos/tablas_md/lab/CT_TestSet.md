# lab.CT_TestSet

**Schema:** lab
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTS_RowId | varchar | PK |  | NO | - |
| CTTS_24hrUrine | varchar |  |  | SI | 24 hr Urine |
| CTTS_ALPHAUPSynonym | varchar |  |  | SI | ALPHAUP Synonym |
| CTTS_ALPHAUPSynonym2 | varchar |  |  | SI | ALPHAUP Synonym2 |
| CTTS_APActivity | varchar |  |  | SI | AP Activity |
| CTTS_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTTS_Activity_DR | varchar |  | FK | SI | Activity DR |
| CTTS_AutoAuth | varchar |  |  | SI | Auto Authorise |
| CTTS_BarcodeDefault | varchar |  |  | SI | Barcode Default |
| CTTS_BillType | varchar |  |  | SI | Bill Type |
| CTTS_BillingType | varchar |  |  | SI | Billing Type |
| CTTS_BloodTransfusionActivity | varchar |  |  | SI | Blood Transfusion Activity |
| CTTS_CancerCouncil | varchar |  |  | SI | Cancer Council |
| CTTS_CancerCouncilType | varchar |  |  | SI | Cancer Council Type |
| CTTS_CapUnit | double |  |  | SI | Cap Unit |
| CTTS_Code | varchar |  |  | NO | Code |
| CTTS_CompletionDate | varchar |  |  | SI | Completion Date |
| CTTS_CompletionTime | varchar |  |  | SI | Completion Time |
| CTTS_ConfidentialDisplay | varchar |  |  | SI | Confidential Display |
| CTTS_ConfidentialPrinting | varchar |  |  | SI | Confidential Printing |
| CTTS_CumReportRRHeading | varchar |  |  | SI | Cumulative Report RR Heading |
| CTTS_CumulativeGroup_DR | varchar |  | FK | SI | Cumulative Group |
| CTTS_CumulativeTestSet | varchar |  |  | SI | Cumulative Test Set |
| CTTS_CycleDays | numeric |  |  | SI | Cycle Days |
| CTTS_DayBook_Laboratory_DR | varchar |  | FK | SI | Day Book Laboratory DR |
| CTTS_DayBook_TS | varchar |  |  | SI | Day Book TS |
| CTTS_DepartmentSequence | numeric |  |  | NO | Department Sequence |
| CTTS_Department_DR | varchar |  | FK | SI | Department |
| CTTS_DisplaySequence | numeric |  |  | NO | Display Sequence |
| CTTS_DocCourierRun_DR | varchar |  | FK | SI | Courier Run for Doctors |
| CTTS_ExcludeFromEDI | varchar |  |  | SI | Exclude From EDI Transmission |
| CTTS_ExcludeFromFullFinal | varchar |  |  | SI | Exclude From Full Final |
| CTTS_ExcludesSex | varchar |  |  | SI | Excludes Sex |
| CTTS_ForcePathologReview | varchar |  |  | SI | Force Pathologist Review |
| CTTS_FrozenBT | varchar |  |  | SI | Frozen BT |
| CTTS_ICD10Rules_DR | varchar |  | FK | SI | ICD10 Rules DR |
| CTTS_LabelAliquot_DR | varchar |  | FK | SI | Label Aliquot DR |
| CTTS_LabelMain_DR | varchar |  | FK | SI | Label Main DR |
| CTTS_LocCourierRun_DR | varchar |  | FK | SI | Courier Run for Locations |
| CTTS_LongTerm | varchar |  |  | SI | Long Term |
| CTTS_ManualFile | varchar |  |  | SI | Manual File |
| CTTS_ManualShort | varchar |  |  | SI | Manual |
| CTTS_MinimumDiffCounter | numeric |  |  | SI | Minimum Diff Counter |
| CTTS_MultipleAllowed | varchar |  |  | SI | Multiple Allowed |
| CTTS_Name | varchar |  |  | SI | Name |
| CTTS_NationalNameLong | varchar |  |  | SI | National Name Long |
| CTTS_NationalNameShort | varchar |  |  | SI | National Name Short |
| CTTS_NationalNumber | varchar |  |  | SI | National Number |
| CTTS_NotifyCCR | varchar |  |  | SI | Notify CCR |
| CTTS_PairedSera | varchar |  |  | SI | Paired Sera Test (Y/N) |
| CTTS_PairedSeraTS_DR | varchar |  | FK | SI | Paired Sera Test Set |
| CTTS_PairedSeraTimePeriod | numeric |  |  | SI | Paired Sera Time Perios (Days) |
| CTTS_PathologistOption | varchar |  |  | SI | Pathologist Option |
| CTTS_PathologistType | varchar |  |  | SI | Pathologist Type |
| CTTS_PrintSeq | double |  |  | SI | Print Sequence |
| CTTS_Priority_DR | varchar |  | FK | SI | Des Ref Priority |
| CTTS_QuotationFee | double |  |  | SI | Quotation Fee |
| CTTS_Referred | varchar |  |  | SI | Referred Test Set |
| CTTS_ReportGroup | varchar |  |  | SI | Report Group |
| CTTS_ReportGroupTime | double |  |  | SI | Report Group Time limit |
| CTTS_ReportName | varchar |  |  | SI | Report Name |
| CTTS_ReportPage_Doctor_DR | varchar |  | FK | SI | Doctor's Report Page |
| CTTS_ReportPage_Hospital_DR | varchar |  | FK | SI | Report Page Hospital |
| CTTS_ReportableComments | varchar |  |  | SI | Reportable Comments in Cummulative |
| CTTS_ReportableResults | varchar |  |  | SI | Reportable Results |
| CTTS_ResultTestItem_DR | varchar |  | FK | SI | Result Test Item DR |
| CTTS_Reviewed | varchar |  |  | SI | Reviewed |
| CTTS_SOPFile | varchar |  |  | SI | SOP File |
| CTTS_SOPShort | varchar |  |  | SI | SOP Short |
| CTTS_Section_DR | varchar |  | FK | SI | Section DR |
| CTTS_SnomedCodes | varchar |  |  | SI | Snomed Codes |
| CTTS_SpecimenContainer | varchar |  |  | SI | Specimen Container scenario |
| CTTS_StopTestSplitting | varchar |  |  | SI | Stop Test Splitting |
| CTTS_StrictDiffCounterLimit | varchar |  |  | SI | Strict DiffCounter Limit |
| CTTS_Synonym | varchar |  |  | SI | Synonym |
| CTTS_Synonym2 | varchar |  |  | SI | Synonym 2 |
| CTTS_TI_Hidden | varchar |  |  | SI | TI Hidden |
| CTTS_TI_Optional | varchar |  |  | SI | TI Optional |
| CTTS_TS_LeftMargin | numeric |  |  | SI | T/S Left Margin |
| CTTS_TargetDiffCounter | numeric |  |  | SI | Target Diff Counter |
| CTTS_TestMessage | varchar |  |  | SI | Test Message |
| CTTS_TherapeuticDrug | varchar |  |  | SI | Therapeutic Drug |
| CTTS_UserSite_DR | varchar |  | FK | SI | User Site |
| CTTS_VerifQueues | varchar |  |  | SI | Verification Queues |
| CTTS_VerifQueuesAutomatic | varchar |  |  | SI | Automatic VQ |
| CTTS_VerifQueuesReferLimit | varchar |  |  | SI | Verification Queues Refer Limit |
| CTTS_Welcan | varchar |  |  | SI | Welcan units |
| CTTS_WidthDoctorReport | numeric |  |  | SI | TS Width for Doctor Report |
| CTTS_Word_MS_Result | varchar |  |  | SI | Word Result (MS) |
| CTTS_Word_MS_Template | varchar |  |  | SI | Word Template (MS) |
| CTTS_Word_RTF_Result | varchar |  |  | SI | Word Result (RTF) |
| CTTS_Word_RTF_Template | varchar |  |  | SI | Word Template (RTF) |
| CTTS_XM_Mode | varchar |  |  | SI | XM Mode |
| CTTS_XM_ModeDefault | varchar |  |  | SI | XM Mode Default |
| CTTS_XM_Test | varchar |  |  | SI | XM Test |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*