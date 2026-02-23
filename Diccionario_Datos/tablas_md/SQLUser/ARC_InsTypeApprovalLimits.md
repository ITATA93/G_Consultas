# SQLUser.ARC_InsTypeApprovalLimits

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPRLIM_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| APPRLIM_ApprovalLimit | double |  |  | SI | Approval Limit |
| APPRLIM_Childsub | double |  |  | NO | Childsub |
| APPRLIM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APPRLIM_Contract_DR | bigint |  | FK | SI | Des Ref Contract |
| APPRLIM_CreatedDate | date |  |  | SI | Created Date |
| APPRLIM_CreatedTime | time |  |  | SI | Created Time |
| APPRLIM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPRLIM_DateFrom | date |  |  | SI | DateFrom |
| APPRLIM_DateTo | date |  |  | SI | DateTo |
| APPRLIM_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| APPRLIM_EpisodeType | varchar |  |  | SI | Episode Type |
| APPRLIM_OrdItmStatusList | varchar |  |  | SI | Exempt Order Item Status List |
| APPRLIM_Rank | double |  |  | SI | Rank |
| APPRLIM_RowId | varchar |  |  | NO | - |
| APPRLIM_UpdatedDate | date |  |  | SI | Updated Date |
| APPRLIM_UpdatedTime | time |  |  | SI | Updated Time |
| APPRLIM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ14DR | - |  |  | SI | Child Reference: Desarrollo Psicomotor |
| Q69Q1 | - |  |  | SI | Pulso |
| Q69Q2 | - |  |  | SI | Lateralidad |
| Q69Q3 | - |  |  | SI | Hallazgos |
| Q69Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*