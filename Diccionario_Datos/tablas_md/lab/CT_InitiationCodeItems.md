# lab.CT_InitiationCodeItems

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTICI_ParRef | varchar | PK |  | NO | CT_InitiationCode Parent Reference |
| CTICI_BillItems | varchar |  |  | SI | BillItem |
| CTICI_Date | date |  |  | NO | Eff Date |
| CTICI_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*