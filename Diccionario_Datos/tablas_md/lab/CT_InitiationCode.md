# lab.CT_InitiationCode

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTIC_RowId | varchar | PK |  | NO | - |
| CTIC_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTIC_BillingDescription | varchar |  |  | SI | Billing Description |
| CTIC_Code | varchar |  |  | NO | Code |
| CTIC_Desc | varchar |  |  | SI | Description |
| CTIC_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTIC_Inpatient | varchar |  |  | SI | Inpatient |
| CTIC_License | varchar |  |  | SI | License |
| CTIC_SCPType_DR | varchar |  | FK | SI | SCP Type DR |
| CTIC_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*