# lab.CT_Bugs_Group_Antibiotics

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBGA_ParRef | varchar | PK |  | NO | CT_Bugs_Group Parent Reference |
| CTBGA_Antibiotics_DR | varchar |  | FK | NO | Des Ref Antibiotics |
| CTBGA_Reported | varchar |  |  | SI | Reported |
| CTBGA_RowID | varchar |  |  | NO | - |
| CTBGA_Sequence | varchar |  |  | SI | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*