# SQLUser.PAC_RefReceiptMethod

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFMETH_RowId | bigint | PK |  | NO | - |
| ChildQ10DR | - |  |  | SI | Child Reference: Peritonitis |
| Q9Q1 | - |  |  | SI | Date |
| Q9Q2 | - |  |  | SI | Condition of the wound |
| Q9Q3 | - |  |  | SI | Culture taken |
| Q9Q4 | - |  |  | SI | Organism |
| Q9Q5 | - |  |  | SI | Treatment |
| Q9Q6 | - |  |  | SI | Comment |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFMETH_Code | varchar |  |  | NO | Code |
| REFMETH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFMETH_CreatedDate | date |  |  | SI | Created Date |
| REFMETH_CreatedTime | time |  |  | SI | Created Time |
| REFMETH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFMETH_DateFrom | date |  |  | SI | DateFrom |
| REFMETH_DateTo | date |  |  | SI | DateTo |
| REFMETH_Desc | varchar |  |  | NO | Description |
| REFMETH_Owner | varchar |  |  | SI | Owner |
| REFMETH_Subregion_DR | bigint |  | FK | SI | Subregion  |
| REFMETH_UpdatedDate | date |  |  | SI | Updated Date |
| REFMETH_UpdatedTime | time |  |  | SI | Updated Time |
| REFMETH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*