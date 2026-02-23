# SQLUser.PAC_ContMethod

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTMETH_RowId | bigint | PK |  | NO | - |
| CONTMETH_Code | varchar |  |  | NO | Code |
| CONTMETH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTMETH_CreatedDate | date |  |  | SI | Created Date |
| CONTMETH_CreatedTime | time |  |  | SI | Created Time |
| CONTMETH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTMETH_DateFrom | date |  |  | SI | Date From |
| CONTMETH_DateTo | date |  |  | SI | Date To |
| CONTMETH_Desc | varchar |  |  | NO | Description |
| CONTMETH_Owner | varchar |  |  | SI | Owner |
| CONTMETH_UpdatedDate | date |  |  | SI | Updated Date |
| CONTMETH_UpdatedTime | time |  |  | SI | Updated Time |
| CONTMETH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ118DR | - |  |  | SI | Child Reference: Catheter position corrected / wit... |
| Q117Q1 | - |  |  | SI | Is CVC Required |
| Q117Q2 | - |  |  | SI | Line Status |
| Q117Q3 | - |  |  | SI | Site Condition |
| Q117Q4 | - |  |  | SI | Dressing	 |
| Q117Q5 | - |  |  | SI | Care |
| Q117Q6 | - |  |  | SI | Drainage Description |
| Q117Q7 | - |  |  | SI | Limb Temperature	 |
| Q117Q8 | - |  |  | SI | Pulse Distal To Insertion Site	 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*