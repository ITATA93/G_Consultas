# lab.CT_ClinicalHistory

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCLH_RowId | varchar | PK |  | NO | - |
| CTCLH_Code | varchar |  |  | NO | Code |
| CTCLH_Description | varchar |  |  | SI | Description |
| CTCLH_ICD10_DR | varchar |  | FK | SI | ICD10 DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*