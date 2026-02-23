# SQLUser.PAC_InfectionType

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INFEC_RowId | bigint | PK |  | NO | - |
| ChildQ31DR | - |  |  | SI | Child Reference: Social assistant goals |
| INFEC_Code | varchar |  |  | NO | Code |
| INFEC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INFEC_CreatedDate | date |  |  | SI | Created Date |
| INFEC_CreatedTime | time |  |  | SI | Created Time |
| INFEC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INFEC_DateFrom | date |  |  | SI | Date From |
| INFEC_DateTo | date |  |  | SI | Date To |
| INFEC_Desc | varchar |  |  | NO | Description |
| INFEC_Owner | varchar |  |  | SI | Owner |
| INFEC_UpdatedDate | date |  |  | SI | Updated Date |
| INFEC_UpdatedTime | time |  |  | SI | Updated Time |
| INFEC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q29Q1 | - |  |  | SI | Goal |
| Q29Q2 | - |  |  | SI | Timing |
| Q29Q3 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*