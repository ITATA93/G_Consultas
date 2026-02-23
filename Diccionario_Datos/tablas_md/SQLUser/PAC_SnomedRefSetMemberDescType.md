# SQLUser.PAC_SnomedRefSetMemberDescType

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNORFSDST_RowId | bigint | PK |  | NO | - |
| ChildQ10DR | - |  |  | SI | Child Reference: Add action(s) for amniotic fluid ... |
| Q09Q1 | - |  |  | SI | Action order number |
| Q09Q2 | - |  |  | SI | Time stamp |
| Q09Q3 | - |  |  | SI | Action type |
| Q09Q4 | - |  |  | SI | Other (specify) |
| Q09Q5 | - |  |  | SI | By whom |
| Q09Q6 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNORFSDST_CreatedDate | date |  |  | SI | Created Date |
| SNORFSDST_CreatedTime | time |  |  | SI | Created Time |
| SNORFSDST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNORFSDST_DescFormat_DR | bigint |  | FK | SI | Description Format |
| SNORFSDST_DescLength | integer |  |  | SI | Description Length |
| SNORFSDST_RefSetMember_DR | bigint |  | FK | SI | Des Ref PACSnomedRefSetMember |
| SNORFSDST_UpdatedDate | date |  |  | SI | Updated Date |
| SNORFSDST_UpdatedTime | time |  |  | SI | Updated Time |
| SNORFSDST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*