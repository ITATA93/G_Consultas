# lab.CT_BugsAntiBiotics

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBUA_ParRef | varchar | PK |  | NO | CT_Bugs Parent Reference |
| CTBUA_Antibiotics_DR | varchar |  | FK | NO | Des Ref Antibiotics |
| CTBUA_Reported | varchar |  |  | SI | Reported |
| CTBUA_RowId | varchar |  |  | NO | - |
| CTBUA_Sequence | varchar |  |  | SI | Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*