# SQLUser.CT_Loc_SimilarDepartment

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEP_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| DEP_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DEP_Childsub | double |  |  | NO | Childsub |
| DEP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEP_CreatedDate | date |  |  | SI | Created Date |
| DEP_CreatedTime | time |  |  | SI | Created Time |
| DEP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEP_RowId | varchar |  |  | NO | - |
| DEP_UpdatedDate | date |  |  | SI | Updated Date |
| DEP_UpdatedTime | time |  |  | SI | Updated Time |
| DEP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q37Q1 | - |  |  | SI | Gestation |
| Q37Q2 | - |  |  | SI | Required and discussed |
| Q37Q3 | - |  |  | SI | Accepted |
| Q37Q4 | - |  |  | SI | Date given |
| Q37Q5 | - |  |  | SI | Batch number |
| Q37Q6 | - |  |  | SI | Dose |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*