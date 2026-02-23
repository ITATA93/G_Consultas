# SQLUser.ARC_InsTypeBGLimits

**Schema:** SQLUser
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LIM_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| LIM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| LIM_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| LIM_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| LIM_Childsub | double |  |  | NO | Childsub |
| LIM_CoPaymentPercentage | double |  |  | SI | Co-Payment Percentage |
| LIM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LIM_CreatedDate | date |  |  | SI | Created Date |
| LIM_CreatedTime | time |  |  | SI | Created Time |
| LIM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LIM_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| LIM_EpisodeType | varchar |  |  | SI | EpisodeType |
| LIM_MaxAmountAllowed | double |  |  | SI | Maximum Amount Allowed |
| LIM_MaxCoPayAmountBeforeTax | double |  |  | SI | Maximum Co-Payment Amount Before Tax |
| LIM_MaxCoPaymentAmount | double |  |  | SI | Maximum Co-Payment Amount |
| LIM_MaxCoverage | double |  |  | SI | Max Coverage |
| LIM_MinCoPaymentAmount | double |  |  | SI | Minimum Co-Payment Amount |
| LIM_OrderStatus_DR | bigint |  | FK | SI | Des Ref OrderStatus |
| LIM_PatShareDiscountAmount | double |  |  | SI | Patient Share Discount Amount |
| LIM_PatShareDiscountPerc | double |  |  | SI | Patient Share Discount Percentage |
| LIM_PatientAmount | double |  |  | SI | Patient Amount |
| LIM_PayorPercent | double |  |  | SI | Payor Percent |
| LIM_Priority_DR | bigint |  | FK | SI | Des Ref OECPriority |
| LIM_Qty | double |  |  | SI | Qty |
| LIM_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| LIM_RowId | varchar |  |  | NO | - |
| LIM_UpdatedDate | date |  |  | SI | Updated Date |
| LIM_UpdatedTime | time |  |  | SI | Updated Time |
| LIM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q14Q1 | - |  |  | SI | Área |
| Q14Q2 | - |  |  | SI | Resultados |
| Q14Q3 | - |  |  | SI | Observaciones |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*