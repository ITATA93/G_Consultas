# SQLUser.PAC_SkinClosure

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SKNCL_RowId | bigint | PK |  | NO | - |
| ChildQ62DR | - |  |  | SI | Child Reference: Continuous Passive Motion |
| Q27Q1 | - |  |  | SI | Joint |
| Q27Q2 | - |  |  | SI | Side |
| Q27Q3 | - |  |  | SI | Range of Motion (ROM) |
| Q27Q4 | - |  |  | SI | Strength |
| Q27Q5 | - |  |  | SI | Straight Leg Raise (SLR) |
| Q27Q6 | - |  |  | SI | Quadriceps lag |
| Q27Q7 | - |  |  | SI | Inner range quadriceps |
| Q27Q8 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SKNCL_Code | varchar |  |  | NO | Code |
| SKNCL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SKNCL_CreatedDate | date |  |  | SI | Created Date |
| SKNCL_CreatedTime | time |  |  | SI | Created Time |
| SKNCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SKNCL_DateFrom | date |  |  | SI | Date From |
| SKNCL_DateTo | date |  |  | SI | Date To |
| SKNCL_Desc | varchar |  |  | NO | Description |
| SKNCL_Owner | varchar |  |  | SI | Owner |
| SKNCL_UpdatedDate | date |  |  | SI | Updated Date |
| SKNCL_UpdatedTime | time |  |  | SI | Updated Time |
| SKNCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*