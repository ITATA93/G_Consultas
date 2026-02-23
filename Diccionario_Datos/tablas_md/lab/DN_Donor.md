# lab.DN_Donor

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DN_RowID | varchar | PK |  | NO | - |
| DN_ActiveFlag | varchar |  |  | SI | Active Flag |
| DN_AllowAutologousCollection | varchar |  |  | SI | Allow Autologous Collection |
| DN_DeferUntillDate | date |  |  | SI | Defer untill Date |
| DN_DeferalType | varchar |  |  | SI | Deferal Type |
| DN_DonorID | varchar |  |  | NO | Donor ID |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*