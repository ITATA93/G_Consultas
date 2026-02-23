# lab.CT_PatientWarnings

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPW_RowID | varchar | PK |  | NO | - |
| CTPW_Code | varchar |  |  | NO | Code |
| CTPW_DaysToExpiry | double |  |  | SI | Days to Expiry |
| CTPW_Description | varchar |  |  | SI | Description |
| CTPW_DisplayType | varchar |  |  | SI | Display Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*