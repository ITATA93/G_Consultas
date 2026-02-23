# SQLUser.ARC_InsTypeDiscount

**Schema:** SQLUser
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISC_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ46DR | - |  |  | SI | Child Reference: COLPOSCOPIA |
| DISC_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| DISC_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| DISC_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| DISC_Childsub | double |  |  | NO | Childsub |
| DISC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISC_CreatedDate | date |  |  | SI | Created Date |
| DISC_CreatedTime | time |  |  | SI | Created Time |
| DISC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISC_DateFrom | date |  |  | SI | Date From |
| DISC_DateTo | date |  |  | SI | Date To |
| DISC_DayFrom | double |  |  | SI | Day From |
| DISC_DayTo | double |  |  | SI | Day To |
| DISC_Discount | double |  |  | SI | % Discount |
| DISC_DiscountAmount | double |  |  | SI | DiscountAmount |
| DISC_DocSpec_DR | bigint |  | FK | SI | Des Ref DocSpec |
| DISC_EpisBill_DR | bigint |  | FK | SI | Des Ref EpisBill |
| DISC_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| DISC_EpisodeType | varchar |  |  | SI | EpisodeType |
| DISC_Hosp_DR | bigint |  | FK | SI | Des Ref Hospital |
| DISC_Location_DR | bigint |  | FK | SI | Des Ref Location |
| DISC_PayorOnly | varchar |  |  | SI | Payor Only |
| DISC_PayorShare | varchar |  |  | SI | PayorShare |
| DISC_RowId | varchar |  |  | NO | - |
| DISC_UpdatedDate | date |  |  | SI | Updated Date |
| DISC_UpdatedTime | time |  |  | SI | Updated Time |
| DISC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q45Q1 | - |  |  | SI | Hallazgos |
| Q45Q2 | - |  |  | SI | Ext. Superior |
| Q45Q3 | - |  |  | SI | Ext. Inferior |
| Q45Q4 | - |  |  | SI | Topografía |
| Q45Q5 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*