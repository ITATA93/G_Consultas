# SQLUser.ARC_InsuranceStatus

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCIS_RowId | bigint | PK |  | NO | - |
| ARCIS_Code | varchar |  |  | NO | Code |
| ARCIS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCIS_CreatedDate | date |  |  | SI | Created Date |
| ARCIS_CreatedTime | time |  |  | SI | Created Time |
| ARCIS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCIS_DateFrom | date |  |  | SI | Date From |
| ARCIS_DateTo | date |  |  | SI | Date To |
| ARCIS_Desc | varchar |  |  | NO | Description |
| ARCIS_Owner | varchar |  |  | SI | Owner |
| ARCIS_UpdatedDate | date |  |  | SI | Updated Date |
| ARCIS_UpdatedTime | time |  |  | SI | Updated Time |
| ARCIS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ80DR | - |  |  | SI | Child Reference: Sensopercepción |
| Q79Q1 | - |  |  | SI | Área |
| Q79Q2 | - |  |  | SI | Evaluación |
| Q79Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*