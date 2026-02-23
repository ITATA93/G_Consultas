# lab.CT_MicrobiologyPanelItems

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMPI_ParRef | varchar | PK |  | NO | CT_MicrobiologyPanel Parent Reference |
| CTMPI_Antibiotics_DR | varchar |  | FK | NO | Des Ref Antibiotics |
| CTMPI_Reported | varchar |  |  | SI | Reported |
| CTMPI_RowID | varchar |  |  | NO | - |
| CTMPI_Sequence | double |  |  | SI | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*