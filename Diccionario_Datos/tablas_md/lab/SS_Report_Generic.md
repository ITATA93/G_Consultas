# lab.SS_Report_Generic

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSRG_RowID | varchar | PK |  | NO | - |
| SSRG_Display | varchar |  |  | SI | Allow to Display |
| SSRG_Parameters | varchar |  |  | SI | Report Parameters |
| SSRG_Report_Code | varchar |  |  | NO | Report Code |
| SSRG_Report_Description | varchar |  |  | SI | Report Description |
| SSRG_Trak_ProgramName | varchar |  |  | SI | Trak Program Name |
| SSRG_Trak_StationeryFont_DR | varchar |  | FK | SI | Trak Stationary Font DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*