# lab.CTBB_PackStatus

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBST_RowID | varchar | PK |  | NO | - |
| BBST_ActiveFlag | varchar |  |  | SI | Active Flag |
| BBST_Code | varchar |  |  | NO | Code |
| BBST_Description | varchar |  |  | SI | Description |
| BBST_NormalLife | numeric |  |  | SI | Status Type |
| BBST_StatusStock | varchar |  |  | SI | Status of Stock |
| BBST_xxx1 | varchar |  |  | SI | Default |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*