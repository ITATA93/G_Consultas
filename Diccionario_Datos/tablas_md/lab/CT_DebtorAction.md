# lab.CT_DebtorAction

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDA_RowId | varchar | PK |  | NO | - |
| CTDA_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTDA_Code | varchar |  |  | NO | Code |
| CTDA_Desc | varchar |  |  | SI | Description |
| CTDA_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTDA_SuppressBilling | varchar |  |  | SI | Suppress Billing |
| CTDA_SuppressDays | numeric |  |  | SI | Suppress Days |
| CTDA_SuppressReminders | varchar |  |  | SI | Suppress Reminders |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*