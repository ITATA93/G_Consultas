# SQLUser.PAC_RTTPathway

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTTPW_RowId | bigint | PK |  | NO | - |
| ChildQ02DR | - |  |  | SI | Child Reference: Tourniquet |
| Q03Q1 | - |  |  | SI | Body site |
| Q03Q2 | - |  |  | SI | Side |
| Q03Q3 | - |  |  | SI | Time on |
| Q03Q4 | - |  |  | SI | Time off |
| Q03Q5 | - |  |  | SI | Comment |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RTTPW_Code | varchar |  |  | NO | Code |
| RTTPW_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RTTPW_CreatedDate | date |  |  | SI | Created Date |
| RTTPW_CreatedTime | time |  |  | SI | Created Time |
| RTTPW_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RTTPW_DateFrom | date |  |  | SI | Date From |
| RTTPW_DateTo | date |  |  | SI | DateTo |
| RTTPW_Desc | varchar |  |  | NO | Description |
| RTTPW_Owner | varchar |  |  | SI | Owner |
| RTTPW_UpdatedDate | date |  |  | SI | Updated Date |
| RTTPW_UpdatedTime | time |  |  | SI | Updated Time |
| RTTPW_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*