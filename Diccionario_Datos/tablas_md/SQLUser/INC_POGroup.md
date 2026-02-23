# SQLUser.INC_POGroup

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCPO_RowId | bigint | PK |  | NO | - |
| INCPO_Code | varchar |  |  | NO | Stock Type |
| INCPO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCPO_CreatedDate | date |  |  | SI | Created Date |
| INCPO_CreatedTime | time |  |  | SI | Created Time |
| INCPO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCPO_Desc | varchar |  |  | NO | Description |
| INCPO_Owner | varchar |  |  | SI | Owner |
| INCPO_UpdatedDate | date |  |  | SI | Updated Date |
| INCPO_UpdatedTime | time |  |  | SI | Updated Time |
| INCPO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q52Q1 | - |  |  | SI | Date |
| Q52Q2 | - |  |  | SI | Time |
| Q52Q3 | - |  |  | SI | Staff name |
| Q52Q4 | - |  |  | SI | Check |
| Q52Q5 | - |  |  | SI | Actions |
| Q52Q6 | - |  |  | SI | Daily assessment notes |
| Q52Q7 | - |  |  | SI | Drain location |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*