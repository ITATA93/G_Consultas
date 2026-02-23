# lab.BB_EDN

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBEDN_RowID | varchar | PK |  | NO | - |
| BBEDN_DateDispatch | date |  |  | SI | Date of Dispatch |
| BBEDN_DateReceive | date |  |  | SI | Date of Receive |
| BBEDN_Number | varchar |  |  | NO | EDN Number |
| BBEDN_Supplier_DR | varchar |  | FK | SI | Supplier |
| BBEDN_TimeDispatch | time |  |  | SI | Time of Dispatch |
| BBEDN_TimeReceive | time |  |  | SI | Time of Receive |
| BBEDN_UserSIte_DR | varchar |  | FK | SI | User Site |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*