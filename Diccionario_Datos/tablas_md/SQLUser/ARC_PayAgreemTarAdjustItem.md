# SQLUser.ARC_PayAgreemTarAdjustItem

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | ARC_PayAgreemTarAdjBillSub Parent Reference |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ITM_Adjustment | double |  |  | SI | Adjustment |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_CreatedDate | date |  |  | SI | Created Date |
| ITM_CreatedTime | time |  |  | SI | Created Time |
| ITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITM_DateFrom | date |  |  | SI | Date From |
| ITM_DateTo | date |  |  | SI | Date To |
| ITM_MultFactor | double |  |  | SI | Multiplier Factor |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_Type | varchar |  |  | SI | Type |
| ITM_UpdatedDate | date |  |  | SI | Updated Date |
| ITM_UpdatedTime | time |  |  | SI | Updated Time |
| ITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01Q1 | - |  |  | SI | Listado de Evaluaciones |
| Q01Q2 | - |  |  | SI | Resultado 1 |
| Q01Q3 | - |  |  | SI | Resultado 2 |
| Q01Q4 | - |  |  | SI | Resultado 3 |
| Q01Q5 | - |  |  | SI | Resultado 4 |
| Q01Q6 | - |  |  | SI | Observaciones Adicionles |
| Q01Q7 | - |  |  | SI | Otra Medición |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*