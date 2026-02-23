# SQLUser.PAC_RefStatusReason

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFSTREA_RowId | bigint | PK |  | NO | - |
| ChildQ12DR | - |  |  | SI | Child Reference: Bowel movements |
| Q11Q1 | - |  |  | SI | Date |
| Q11Q2 | - |  |  | SI | Status |
| Q11Q3 | - |  |  | SI | Comment |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFSTREA_Code | varchar |  |  | NO | Code |
| REFSTREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFSTREA_CreatedDate | date |  |  | SI | Created Date |
| REFSTREA_CreatedTime | time |  |  | SI | Created Time |
| REFSTREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFSTREA_DateFrom | date |  |  | SI | Date From |
| REFSTREA_DateTo | date |  |  | SI | Date To |
| REFSTREA_Desc | varchar |  |  | NO | Description |
| REFSTREA_Owner | varchar |  |  | SI | Owner |
| REFSTREA_UpdatedDate | date |  |  | SI | Updated Date |
| REFSTREA_UpdatedTime | time |  |  | SI | Updated Time |
| REFSTREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*