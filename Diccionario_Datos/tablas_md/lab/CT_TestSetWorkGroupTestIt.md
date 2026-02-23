# lab.CT_TestSetWorkGroupTestIt

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTWI_ParRef | varchar | PK |  | NO | CT_TestSet_WorkGroup Parent Reference |
| CTTWI_RowID | varchar |  |  | NO | - |
| CTTWI_Sequence | numeric |  |  | SI | Sequence No |
| CTTWI_TestItem_DR | varchar |  | FK | NO | Test Item DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*