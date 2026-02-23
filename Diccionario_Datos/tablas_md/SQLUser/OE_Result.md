# SQLUser.OE_Result

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Resultados**. Respuestas a órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RES_RowId | bigint | PK |  | NO | - |
| Q71Q1 | - |  |  | SI | Test |
| Q71Q2 | - |  |  | SI | Left |
| Q71Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RES_AnaestOper_DR | varchar |  | FK | SI | Des Ref OR_Anaest_Operation |
| RES_AuthClin_DR | varchar |  | FK | SI | Des Ref CTPCP |
| RES_CTLOC2_DR | bigint |  | FK | SI | Des Ref CTLOC |
| RES_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| RES_CTPCP2_DR | varchar |  | FK | SI | Des Ref CTPCP |
| RES_CTPCP_DR | varchar |  | FK | SI | Des Ref CTPCP |
| RES_CreateDate | date |  |  | SI | CreateDate |
| RES_CreateTime | time |  |  | SI | CreateTime |
| RES_Date | date |  |  | NO | Date |
| RES_HandoverDoc_DR | varchar |  | FK | SI | Handover Doctor Des Ref CTPCP |
| RES_OrdItem_DR | varchar |  | FK | SI | Des Ref OrdItem |
| RES_OrdResult_DR | varchar |  | FK | SI | OrdResult |
| RES_OrderDoc_DR | varchar |  | FK | SI | Ordering Doctor Des Ref CTPCP |
| RES_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| RES_Read | varchar |  |  | SI | Read |
| RES_ResultDate | date |  |  | NO | Result Date - Result Date that matches the 'Result... |
| RES_ResultTime | time |  |  | SI | Result Time - Result Time that matches the 'Result... |
| RES_TextResult_DR | bigint |  | FK | SI | Des Ref TextResult |
| RES_Time | time |  |  | SI | Time |
| RES_Urgent | varchar |  |  | SI | Urgent |
| RES_Ward2_DR | bigint |  | FK | SI | Des Ref Ward |
| RES_Ward_DR | bigint |  | FK | SI | Des Ref Ward |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*