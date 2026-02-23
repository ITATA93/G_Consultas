# lab.CT_StorageContainersTestSet

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSTCT_ParRef | varchar | PK |  | NO | - |
| CTSTCT_RowID | varchar |  |  | NO | - |
| CTSTCT_TestSet_DR | varchar |  | FK | NO | Test Set DR |
| CTSTCT_Warnings | varchar |  |  | SI | Warnings |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*