# lab.CT_DBLabProcedures

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBP_ParRef | varchar | PK |  | NO | CT_DayBookLaboratory Parent Reference |
| CTDBP_ActiveFlag | varchar |  |  | SI | Active |
| CTDBP_Activity_DR | varchar |  | FK | SI | Activity DR |
| CTDBP_AddLevels | varchar |  |  | SI | Add Levels |
| CTDBP_AdditionalLabels | double |  |  | SI | Additional Labels |
| CTDBP_Code | varchar |  |  | NO | Code |
| CTDBP_DayBookTestSet_DR | varchar |  | FK | SI | Day Book Test Set DR |
| CTDBP_Desc | varchar |  |  | SI | Description |
| CTDBP_DisplaySequence | varchar |  |  | SI | Display Sequence |
| CTDBP_FavouriteColour | varchar |  |  | SI | Favourite Colour |
| CTDBP_PrintLabels | varchar |  |  | SI | Print Labels |
| CTDBP_ResultFormat | varchar |  |  | SI | Result Format |
| CTDBP_RowId | varchar |  |  | NO | - |
| CTDBP_SOPFile | varchar |  |  | SI | SOP File |
| CTDBP_SOPShort | varchar |  |  | SI | SOP Short |
| CTDBP_Welcan_Minute | varchar |  |  | SI | Welcan / Minute Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*