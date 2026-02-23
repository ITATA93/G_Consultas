# lab.CT_BugGroupAntActions

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBGF_ParRef | varchar | PK |  | NO | CT_Bugs_Group_Antibiotics Parent Reference |
| CTBGF_ActionType | varchar |  |  | SI | Action Type |
| CTBGF_Group | varchar |  |  | SI | Group |
| CTBGF_InfoText | varchar |  |  | SI | Info Text |
| CTBGF_Order | double |  |  | NO | Order number |
| CTBGF_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*