# lab.CT_Department

**Schema:** lab
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDEP_RowId | varchar | PK |  | NO | - |
| CTDEP_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTDEP_Code | varchar |  |  | NO | Code |
| CTDEP_DefaultPathologist_DR | varchar |  | FK | SI | Default Pathologist |
| CTDEP_DisplaySequence | numeric |  |  | NO | Display Sequence |
| CTDEP_DocCourierRun_DR | varchar |  | FK | SI | Courier Run for Doctors |
| CTDEP_Footer | varchar |  |  | SI | Footer |
| CTDEP_InterimWardReport | varchar |  |  | SI | Interim Ward Report |
| CTDEP_LocCourierRun_DR | varchar |  | FK | SI | Courier Run for Locations |
| CTDEP_Manager | varchar |  |  | SI | Manager |
| CTDEP_ManualPrint | varchar |  |  | SI | Manual Print |
| CTDEP_Name | varchar |  |  | SI | Department Name |
| CTDEP_PrintDepartmentHeading | varchar |  |  | SI | Print Department Heading |
| CTDEP_PrintSeparatePage | varchar |  |  | SI | Print on Separate Page |
| CTDEP_PrintSequence | varchar |  |  | SI | Print Sequence |
| CTDEP_ReadOnlyStaffNotes | varchar |  |  | SI | Read Only Staff Notes |
| CTDEP_ReportableComments | varchar |  |  | SI | Reportable Comments in Cummulative |
| CTDEP_ReportableResults | varchar |  |  | SI | Reportable Results |
| CTDEP_TS_LeftMargin | numeric |  |  | SI | T/S Left Margin |
| CTDEP_TS_WidthDoctorReport | numeric |  |  | SI | TS Width for Doctor Report |
| CTDEP_UserBasedPrinting | varchar |  |  | SI | User Based Printing |
| CTDEP_Welcan_Minute | varchar |  |  | SI | Welcan / Minute Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*