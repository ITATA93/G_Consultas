# lab.CT_VisitAction

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTVA_RowId | varchar | PK |  | NO | - |
| CTVA_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTVA_Code | varchar |  |  | NO | Code |
| CTVA_CommentsRequired | varchar |  |  | SI | Comments Required |
| CTVA_Desc | varchar |  |  | SI | Description |
| CTVA_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTVA_Message | varchar |  |  | SI | Message to print on Pathology claims |
| CTVA_SuppressBilling | varchar |  |  | SI | Suppress Billing |
| CTVA_SuppressReport | varchar |  |  | SI | Suppress Report |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*