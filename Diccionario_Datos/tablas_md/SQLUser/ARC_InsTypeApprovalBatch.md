# SQLUser.ARC_InsTypeApprovalBatch

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPRBCH_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| APPRBCH_BillingGroups | varchar |  |  | SI | Billing Groups |
| APPRBCH_BillingSubgroups | varchar |  |  | SI | Billing Subgroups |
| APPRBCH_Childsub | double |  |  | NO | Childsub |
| APPRBCH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APPRBCH_CreatedDate | date |  |  | SI | Created Date |
| APPRBCH_CreatedTime | time |  |  | SI | Created Time |
| APPRBCH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPRBCH_DateFrom | date |  |  | SI | Date From |
| APPRBCH_DateTo | date |  |  | SI | Date To |
| APPRBCH_EpisodeType | varchar |  |  | SI | Episode Type |
| APPRBCH_GroupRequestDesc_DR | bigint |  | FK | NO | Des Ref BLCApprGroupRequestDescription - Approval ... |
| APPRBCH_Rank | double |  |  | SI | Rank |
| APPRBCH_RowId | varchar |  |  | NO | - |
| APPRBCH_UpdatedDate | date |  |  | SI | Updated Date |
| APPRBCH_UpdatedTime | time |  |  | SI | Updated Time |
| APPRBCH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ69DR | - |  |  | SI | Child Reference: Pulsos periféricos |
| Q65Q1 | - |  |  | SI | Hallazgos |
| Q65Q2 | - |  |  | SI | Extremidad superior |
| Q65Q3 | - |  |  | SI | Extremidad inferior |
| Q65Q4 | - |  |  | SI | Topografía |
| Q65Q5 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*