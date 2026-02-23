# SQLUser.OEC_UnitsCollected

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| UNITCOL_RowId | bigint | PK |  | NO | - |
| Q04Q1 | - |  |  | SI | Toxin |
| Q04Q2 | - |  |  | SI | Strength / concentration |
| Q04Q3 | - |  |  | SI | Quantity or volume |
| Q04Q4 | - |  |  | SI | Route of exposure |
| Q04Q5 | - |  |  | SI | Time of exposure |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| UNITCOL_Code | varchar |  |  | NO | Code |
| UNITCOL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| UNITCOL_CreatedDate | date |  |  | SI | Created Date |
| UNITCOL_CreatedTime | time |  |  | SI | Created Time |
| UNITCOL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| UNITCOL_Desc | varchar |  |  | NO | Description |
| UNITCOL_Owner | varchar |  |  | SI | Owner |
| UNITCOL_UpdatedDate | date |  |  | SI | Updated Date |
| UNITCOL_UpdatedTime | time |  |  | SI | Updated Time |
| UNITCOL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*