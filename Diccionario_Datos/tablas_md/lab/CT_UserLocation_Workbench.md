# lab.CT_UserLocation_Workbench

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTUSW_ParRef | varchar | PK |  | NO | CT_UserLocation Parent Reference |
| CTUSW_Instrument_DR | varchar |  | FK | NO | Instrument DR |
| CTUSW_Order | double |  |  | SI | Order |
| CTUSW_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*