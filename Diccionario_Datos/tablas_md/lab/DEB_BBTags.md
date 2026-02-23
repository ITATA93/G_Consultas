# lab.DEB_BBTags

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEBBT_ParRef | varchar | PK |  | NO | DEB_Debtor Parent Reference |
| DEBBT_Date | date |  |  | SI | Date |
| DEBBT_RowID | varchar |  |  | NO | - |
| DEBBT_Tag_DR | varchar |  | FK | NO | BB Tag DR |
| DEBBT_Time | time |  |  | SI | Time |
| DEBBT_User_DR | varchar |  | FK | SI | User DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*