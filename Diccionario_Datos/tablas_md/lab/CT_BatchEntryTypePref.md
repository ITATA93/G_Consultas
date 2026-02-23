# lab.CT_BatchEntryTypePref

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBETA_ParRef | varchar | PK |  | NO | CT_BBAction Parent Reference |
| CTBETA_Field | varchar |  |  | SI | Field |
| CTBETA_FieldSelection | varchar |  |  | SI | Field Selection |
| CTBETA_Order | numeric |  |  | NO | Order |
| CTBETA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*