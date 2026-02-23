# lab.WS_WorkSheet

**Schema:** lab
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Web Services**. Integración con sistemas externos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WKS_RowId | varchar | PK |  | NO | - |
| WKS_Active | varchar |  |  | SI | Active |
| WKS_AddTStoClosedWS | varchar |  |  | SI | Add TS to Episodes in Closed WS |
| WKS_AutomaticAllocation | varchar |  |  | SI | Automatic Allocation |
| WKS_ClinicalNotes | varchar |  |  | SI | Clinical Notes |
| WKS_CloseAfterPrinting | varchar |  |  | SI | Close WS After Printing |
| WKS_Code | varchar |  |  | NO | Code |
| WKS_ColumnWidthForEntry | numeric |  |  | SI | Column Width For Entry |
| WKS_ColumnWidthForPrinting | numeric |  |  | SI | Column Width For Printing |
| WKS_Comments | varchar |  |  | SI | Comments to print |
| WKS_Comments_Formatted | varchar |  |  | SI | Comments Formatted |
| WKS_Department_DR | varchar |  | FK | SI | Department |
| WKS_Flag_EntryMode | varchar |  |  | SI | Flag Entry Mode |
| WKS_Flag_ResultIndicators | varchar |  |  | SI | Flag Result Indicators |
| WKS_Flag_StatusIndicators | varchar |  |  | SI | Flag Status Indicators |
| WKS_ManualCreation | varchar |  |  | SI | Manual Creation |
| WKS_MaxVisits | double |  |  | SI | Max Visits |
| WKS_MaxVisitsOnPage | numeric |  |  | SI | Max Visits On Page |
| WKS_Name | varchar |  |  | SI | WS Name |
| WKS_OneSiteOnly | varchar |  |  | SI | One Site Only |
| WKS_PendingDays | double |  |  | SI | Pending Days |
| WKS_PendingToCurrent | varchar |  |  | SI | Move Pending patients to current WS |
| WKS_PreviousResults | varchar |  |  | SI | Display previous results |
| WKS_PrintAuthorisedPatients | varchar |  |  | SI | Print Authorised Patients |
| WKS_PrintCalculatedFields | varchar |  |  | SI | Print Calculated Fields |
| WKS_PrintDirection | varchar |  |  | SI | Print Direction |
| WKS_PrintDoctor | varchar |  |  | SI | Print Doctor |
| WKS_RearrangeWhenPrinting | varchar |  |  | SI | Rearrange When Printing |
| WKS_Stationary_DR | varchar |  | FK | SI | Stationary DR |
| WKS_UrgentsFirst | varchar |  |  | SI | Urgents First |
| WKS_UseSynonymsForTI | varchar |  |  | SI | Use Synonyms For Test Items |
| WKS_UseSynonymsForTS | varchar |  |  | SI | Use Synonyms For Test Sets |
| WKS_UserSite_DR | varchar |  | FK | SI | User Site DR |
| WKS_WorkSheetDataOrder | varchar |  |  | SI | WorkSheet Data Order |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*