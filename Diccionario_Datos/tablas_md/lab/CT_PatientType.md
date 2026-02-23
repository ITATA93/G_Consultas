# lab.CT_PatientType

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPAT_RowID | varchar | PK |  | NO | - |
| CTPAT_Active | varchar |  |  | SI | Active Y/N |
| CTPAT_Code | varchar |  |  | NO | Code |
| CTPAT_Description | varchar |  |  | SI | Description |
| CTPAT_InPatient | varchar |  |  | SI | Inpatient Y/N |
| CTPAT_PatientFlag | varchar |  |  | SI | Patient Flag Y/N |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*