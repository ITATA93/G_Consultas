# SQLUser.OE_OrdExecAdditFTBatch

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FTBT_ParRef | varchar | PK |  | NO | OE_OrdExec Parent Reference |
| ChildQ63DR | - |  |  | SI | Child Reference: Muscle Power |
| FTBT_BatchFTExpiryDate | date |  |  | SI | Free Text Batch Expiry Date |
| FTBT_BatchFreeText | varchar |  |  | SI | Batch Free Text |
| FTBT_Childsub | double |  |  | NO | Childsub |
| FTBT_RowId | varchar |  |  | NO | - |
| Q62Q1 | - |  |  | SI | Joint / Motion |
| Q62Q2 | - |  |  | SI | AROM left |
| Q62Q3 | - |  |  | SI | PROM left |
| Q62Q4 | - |  |  | SI | AROM right |
| Q62Q5 | - |  |  | SI | PROM right |
| Q62Q6 | - |  |  | SI | End feel |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*