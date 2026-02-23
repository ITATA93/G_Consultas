# lab.WS_WorkSheetRows

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Web Services**. Integración con sistemas externos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WKSRW_ParRef | varchar | PK |  | NO | WS_WorkSheet Parent Reference |
| WKSRW_Description_1 | varchar |  |  | SI | Description 1 |
| WKSRW_Description_2 | varchar |  |  | SI | Description 2 |
| WKSRW_Number | double |  |  | NO | Number |
| WKSRW_QC_Group_DR | varchar |  | FK | SI | QC Group DR |
| WKSRW_QC_Level | numeric |  |  | SI | QC Level |
| WKSRW_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*