# lab.CT_Sections

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDS_RowID | varchar | PK |  | NO | - |
| CTDS_Code | varchar |  |  | NO | Code |
| CTDS_Department_DR | varchar |  | FK | SI | Department DR |
| CTDS_Description | varchar |  |  | SI | Description |
| CTDS_PrintFooter | varchar |  |  | SI | Print Footer |
| CTDS_PrintHeader | varchar |  |  | SI | Print Header |
| CTDS_PrintSequence | double |  |  | SI | Print Sequence |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*