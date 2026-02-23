# lab.MIF_MachineParameters

**Schema:** lab
**Columnas:** 52
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**MIF Module**. Interfaz de mensajería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MIMP_RowId | varchar | PK |  | NO | - |
| MIMP_AATimeSlot | double |  |  | SI | AA Time Slot |
| MIMP_AAenabled | varchar |  |  | SI | AA enabled |
| MIMP_AutoAuthoriseVQ | varchar |  |  | SI | Auto Authorise VQ |
| MIMP_AutoPurgeResults | double |  |  | SI | Auto Purge Results |
| MIMP_CheckQCForAA | varchar |  |  | SI | Check QC for AA |
| MIMP_Code | varchar |  |  | NO | Code |
| MIMP_ColumnWidth | numeric |  |  | SI | Column Width |
| MIMP_DefaultRowSelection | varchar |  |  | SI | Default Row Selection |
| MIMP_DelimiterForCommentsAnt | varchar |  |  | SI | Delimiter For Comments and AntiBiotics |
| MIMP_DelimiterForResults | varchar |  |  | SI | Delimiter For Results |
| MIMP_DelimiterForSensitivities | varchar |  |  | SI | Delimiter For Sensitivities |
| MIMP_DelimiterForTests | varchar |  |  | SI | Delimiter For Tests |
| MIMP_Department_DR | varchar |  | FK | SI | Des Ref Department |
| MIMP_DisableAutoAuthorise | varchar |  |  | SI | Disable Auto Authorise |
| MIMP_DisplayAntiBiotics | varchar |  |  | SI | Display AntiBiotics |
| MIMP_DisplayMessageOnAuthorise | varchar |  |  | SI | Display Info Message On Authorise |
| MIMP_DisplayPatientLocation | varchar |  |  | SI | Display Patient Location |
| MIMP_DisplayResultFlag | varchar |  |  | SI | Display Result Flag |
| MIMP_DisplayResultIndicator | varchar |  |  | SI | Display Result Indicator |
| MIMP_DisplayScatterPlot | varchar |  |  | SI | Display Scatter Plot |
| MIMP_DisplayToFollow | varchar |  |  | SI | Display To Follow Indicators |
| MIMP_DisplayTotals | varchar |  |  | SI | Display Totals |
| MIMP_GroupOfMachines | varchar |  |  | SI | Group Of Machines |
| MIMP_IF_Programme | varchar |  |  | SI | IF Programme |
| MIMP_IP_Address | varchar |  |  | SI | IP Address |
| MIMP_JoinResult | varchar |  |  | SI | Join result |
| MIMP_LW_PreviousYears | double |  |  | SI | LW Previous Years |
| MIMP_LW_TimeDelay | double |  |  | SI | LW Time Delay |
| MIMP_LW_VerificationQueue | varchar |  |  | SI | LW Verification Queue |
| MIMP_LoadListSpecimen | varchar |  |  | SI | Load List Specimen |
| MIMP_MUMPS_Device | varchar |  |  | SI | MUMPS Device |
| MIMP_MachineName | varchar |  |  | SI | Machine Name |
| MIMP_MaxLoadList | double |  |  | SI | Max Number of patients on loadlist |
| MIMP_MaxLog | numeric |  |  | SI | Max number of records in a log file |
| MIMP_Message | varchar |  |  | SI | Message |
| MIMP_NextTray | varchar |  |  | SI | Next Tray |
| MIMP_OverwriteResult | varchar |  |  | SI | Overwrite Result |
| MIMP_QCAssociationFrom | double |  |  | SI | QC Association From (Hours) |
| MIMP_QCAssociationTo | double |  |  | SI | QC Association To (Hours) |
| MIMP_QCTimeForAA | double |  |  | SI | QC Time for AA (Minutes) |
| MIMP_QCTimeSlot | double |  |  | SI | QC Time Slot |
| MIMP_QueryType | varchar |  |  | SI | Query Type |
| MIMP_ResultEntryMode | varchar |  |  | SI | Result Entry Mode |
| MIMP_Shutdown | varchar |  |  | SI | Shutdown |
| MIMP_StopAAforMultipleResults | varchar |  |  | SI | Stop AA for Multiple Results |
| MIMP_StopAAforStaffNotes | varchar |  |  | SI | Stop AA for Staff Notes |
| MIMP_Uni_Bi_Direct | varchar |  |  | SI | Uni Bi Direct |
| MIMP_UrgentFirst | varchar |  |  | SI | UrgentFirst |
| MIMP_UseParam | varchar |  |  | SI | Use Param |
| MIMP_UserSite_DR | varchar |  | FK | SI | User Site DR |
| MIMP_traceFolder | varchar |  |  | SI | trace folder |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*