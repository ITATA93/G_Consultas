# SQLUser.HPC_DiscountReason

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración Hosp/Paciente**. Parámetros hospital-paciente.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISCR_RowId | bigint | PK |  | NO | - |
| ChildQ51DR | - |  |  | SI | Child Reference: Central venous catheter line care... |
| DISCR_Code | varchar |  |  | NO | Code |
| DISCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISCR_CreatedDate | date |  |  | SI | Created Date |
| DISCR_CreatedTime | time |  |  | SI | Created Time |
| DISCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISCR_Desc | varchar |  |  | NO | Description |
| DISCR_Owner | varchar |  |  | SI | Owner |
| DISCR_UpdatedDate | date |  |  | SI | Updated Date |
| DISCR_UpdatedTime | time |  |  | SI | Updated Time |
| DISCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q49Q1 | - |  |  | SI | Drainage present |
| Q49Q2 | - |  |  | SI | Drainage description |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*