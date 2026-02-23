# lab.CT_DBLabBlockTypeProced

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBD_ParRef | varchar | PK |  | NO | CT_DBLabBlockType Parent Reference |
| CTDBD_Level | varchar |  |  | SI | Level |
| CTDBD_Order | varchar |  |  | NO | Order |
| CTDBD_Pieces | double |  |  | SI | No Pieces |
| CTDBD_ProcedureCode | varchar |  |  | SI | Procedure Code |
| CTDBD_RowID | varchar |  |  | NO | - |
| CTDBD_StainCode | varchar |  |  | SI | Stain Code |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*