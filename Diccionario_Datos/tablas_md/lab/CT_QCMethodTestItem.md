# lab.CT_QCMethodTestItem

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMTT_ParRef | varchar | PK |  | NO | CT_QCMethod Parent Reference |
| CTMTT_Method_DR | varchar |  | FK | SI | Method |
| CTMTT_RowID | varchar |  |  | NO | - |
| CTMTT_TestItem_DR | varchar |  | FK | NO | Test Item DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*