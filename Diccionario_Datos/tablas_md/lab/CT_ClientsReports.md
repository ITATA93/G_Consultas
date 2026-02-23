# lab.CT_ClientsReports

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCLR_RowID | varchar | PK |  | NO | - |
| CTCLR_Client_ProgramName | varchar |  |  | SI | Client Program Name |
| CTCLR_Client_StationeryFont_DR | varchar |  | FK | SI | Client Stationery Font DR |
| CTCLR_CrystalReport | varchar |  |  | SI | Crystal Report |
| CTCLR_DLL | varchar |  |  | SI | DLL |
| CTCLR_Description | varchar |  |  | SI | Description |
| CTCLR_Display | varchar |  |  | SI | Display |
| CTCLR_EndOfReport | varchar |  |  | SI | End Of Report |
| CTCLR_ReportGroup_DR | varchar |  | FK | SI | Report Group DR |
| CTCLR_Report_DR | varchar |  | FK | NO | Generic Report DR |
| CTCLR_Suspend | varchar |  |  | SI | Suspend |
| CTCLR_do_Display | varchar |  |  | SI | Allow to display |
| CTCLR_do_Trak_ProgramName | varchar |  |  | SI | Trak Program Name |
| CTCLR_do_Trak_StationeryFont_DR | varchar |  | FK | SI | Trak Stationery Font DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*