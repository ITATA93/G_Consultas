# lab.DEB_DepartmentHistory

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEBDH_ParRef | varchar | PK |  | NO | DEB_Debtor Parent Reference |
| DEBDH_Department_DR | varchar |  | FK | NO | Department DR |
| DEBDH_Remarks | varchar |  |  | SI | Remarks |
| DEBDH_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*