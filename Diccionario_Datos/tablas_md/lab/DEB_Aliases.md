# lab.DEB_Aliases

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEBA_ParRef | varchar | PK |  | NO | DEB_Debtor Parent Reference |
| DEBA_Episode_DR | varchar |  | FK | SI | Episode DR |
| DEBA_GivenName | varchar |  |  | NO | Given Name |
| DEBA_RowID | varchar |  |  | NO | - |
| DEBA_Surname | varchar |  |  | NO | Surname |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*