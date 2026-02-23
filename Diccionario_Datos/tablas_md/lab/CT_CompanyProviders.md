# lab.CT_CompanyProviders

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTCOP_ParRef | varchar | PK |  | NO | CT_Company Parent Reference |
| CTCOP_Date | date |  |  | NO | Date |
| CTCOP_Pathologist_DR | varchar |  | FK | SI | Pathologist |
| CTCOP_ProviderNumber | varchar |  |  | SI | Provider Number |
| CTCOP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*