# SQLUser.ARC_InitiationBillingItem

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCINIBI_ParRef | bigint | PK |  | NO | Parent Initiation |
| ARCINIBI_BillingItem_DR | bigint |  | FK | SI | Billing Item |
| ARCINIBI_BulkBillingIncentive | varchar |  |  | SI | Bulk Billing Incentive |
| ARCINIBI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCINIBI_CreatedDate | date |  |  | SI | Created Date |
| ARCINIBI_CreatedTime | time |  |  | SI | Created Time |
| ARCINIBI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCINIBI_DateFrom | date |  |  | SI | Effective date for the record |
| ARCINIBI_DateTo | date |  |  | SI | Last day the record is active |
| ARCINIBI_RowID | varchar |  |  | NO | - |
| ARCINIBI_UpdatedDate | date |  |  | SI | Updated Date |
| ARCINIBI_UpdatedTime | time |  |  | SI | Updated Time |
| ARCINIBI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ58DR | - |  |  | SI | Child Reference: Abdomen y dorso |
| Q51Q1 | - |  |  | SI | Percusión |
| Q51Q2 | - |  |  | SI | Auscultación |
| Q51Q3 | - |  |  | SI | Localización |
| Q51Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*