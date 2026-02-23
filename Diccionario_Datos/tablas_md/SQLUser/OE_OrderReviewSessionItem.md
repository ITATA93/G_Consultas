# SQLUser.OE_OrderReviewSessionItem

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | bigint | PK |  | NO | OE_OrderReviewSession Parent Reference |
| ChildQ32DR | - |  |  | SI | Child Reference: Hip Outcome Score (HOS) Sports su... |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| ITM_PhOrdRevAuthClin_DR | varchar |  | FK | SI | Des Ref AuthoriseClinician |
| ITM_PhOrdRevDate | date |  |  | SI | ITMphOrdReviewDate |
| ITM_PhOrdRevSignOffDate | date |  |  | SI | ITMPhOrdReviewDate |
| ITM_PhOrdRevSignOffTime | time |  |  | SI | ITMPhOrdReviewTime |
| ITM_PhOrdRevSignOffUser_DR | bigint |  | FK | SI | Des Ref AuthoriseClinician |
| ITM_PhOrdRevTime | time |  |  | SI | ITMPhOrdReviewTime |
| ITM_PhOrdRevUser_DR | bigint |  | FK | SI | Des Ref SSUSR |
| ITM_PhOrdReviewFlag | varchar |  |  | SI | ITMPhOrdReviewFlag |
| ITM_RowId | varchar |  |  | NO | - |
| Q31Q1 | - |  |  | SI | Activity |
| Q31Q2 | - |  |  | SI | Condition |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*