# SQLUser.ARC_InsTypeOrdItemApproval

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OIAPPR_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ86DR | - |  |  | SI | Child Reference: Actividades de la Vida Diaria y T... |
| OIAPPR_BillingGroups | varchar |  |  | SI | Billing Groups |
| OIAPPR_BillingSubgroups | varchar |  |  | SI | Billing Subgroups |
| OIAPPR_Childsub | double |  |  | NO | Childsub |
| OIAPPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OIAPPR_CreatedDate | date |  |  | SI | Created Date |
| OIAPPR_CreatedTime | time |  |  | SI | Created Time |
| OIAPPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OIAPPR_DateFrom | date |  |  | SI | Date From |
| OIAPPR_DateTo | date |  |  | SI | Date To |
| OIAPPR_DischBillingGroups | varchar |  |  | SI | Discharge Billing Groups |
| OIAPPR_DischBillingSubgroups | varchar |  |  | SI | Discharge Billing Subgroups |
| OIAPPR_EpisodeType | varchar |  |  | SI | Episode Type |
| OIAPPR_MinimumDuration | integer |  |  | SI | Minimum Duration (Days) |
| OIAPPR_OrderSet | varchar |  |  | SI | Order Set |
| OIAPPR_Rank | double |  |  | SI | Rank |
| OIAPPR_RowId | varchar |  |  | NO | - |
| OIAPPR_UpdatedDate | date |  |  | SI | Updated Date |
| OIAPPR_UpdatedTime | time |  |  | SI | Updated Time |
| OIAPPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q83Q1 | - |  |  | SI | Evaluación |
| Q83Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*