# lab.CT_WebEnquiryTI

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTWEBTI_ParRef | varchar | PK |  | NO | CT_WebEnquiry Parent Reference |
| CTWEBTI_RowID | varchar |  |  | NO | - |
| CTWEBTI_Sequence | integer |  |  | SI | Sequence |
| CTWEBTI_TestItem_DR | varchar |  | FK | NO | Test Item DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*