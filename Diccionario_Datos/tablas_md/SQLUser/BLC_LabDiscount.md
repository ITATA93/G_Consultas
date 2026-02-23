# SQLUser.BLC_LabDiscount

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LABD_RowID | bigint | PK |  | NO | - |
| ChildQ05DR | - |  |  | SI | Child Reference: RED SOCIAL Y COMUNITARIO |
| LABD_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| LABD_CreatedDate | date |  |  | SI | Created Date |
| LABD_CreatedTime | time |  |  | SI | Created Time |
| LABD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LABD_UpdatedDate | date |  |  | SI | Updated Date |
| LABD_UpdatedTime | time |  |  | SI | Updated Time |
| LABD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02Q1 | - |  |  | SI | Metas |
| Q02Q2 | - |  |  | SI | Logro |
| Q02Q3 | - |  |  | SI | Cumplimiento |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*