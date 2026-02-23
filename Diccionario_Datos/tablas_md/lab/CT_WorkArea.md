# lab.CT_WorkArea

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTWA_RowID | varchar | PK |  | NO | - |
| CTWA_Code | varchar |  |  | NO | Code |
| CTWA_Description | varchar |  |  | SI | Description |
| CTWA_PatientLocation_DR | varchar |  | FK | SI | Patient Location DR |
| CTWA_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*