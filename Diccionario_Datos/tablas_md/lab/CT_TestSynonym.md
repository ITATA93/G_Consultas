# lab.CT_TestSynonym

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSY_RowId | varchar | PK |  | NO | - |
| CTSY_Code | varchar |  |  | NO | Code |
| CTSY_TestSet_SuperSet | varchar |  |  | NO | TestSet or SuperSet |
| CTSY_Type | varchar |  |  | NO | Type |
| CTSY_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*