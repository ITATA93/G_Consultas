# lab.CT_SuperSetItems

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSSI_ParRef | varchar | PK |  | NO | CT_SuperSet Parent Reference |
| CTSSI_Childsub | double |  |  | NO | Childsub |
| CTSSI_Default | varchar |  |  | SI | Default |
| CTSSI_RowId | varchar |  |  | NO | - |
| CTSSI_TestSet_DR | varchar |  | FK | SI | Des Ref TestSet |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*