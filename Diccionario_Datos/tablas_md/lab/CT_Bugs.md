# lab.CT_Bugs

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBUG_RowId | varchar | PK |  | NO | - |
| CTBUG_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTBUG_AutoCommentsRules | varchar |  |  | SI | Auto Comments Rules |
| CTBUG_AutoCommentsSelection | varchar |  |  | SI | Auto Comments Selection |
| CTBUG_Classification | varchar |  |  | SI | Classification |
| CTBUG_Code | varchar |  |  | NO | Code |
| CTBUG_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTBUG_Name | varchar |  |  | SI | Name |
| CTBUG_National_ID | varchar |  |  | SI | National ID |
| CTBUG_PathogenGroup_DR | varchar |  | FK | SI | Pathogen group |
| CTBUG_ReportTemplate_DR | varchar |  | FK | SI | Report Template DR |
| CTBUG_Reported | varchar |  |  | SI | Reported |
| CTBUG_ReportedTime | numeric |  |  | SI | Reported Time |
| CTBUG_Synonym | varchar |  |  | SI | Synonym |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*