# SQLUser.OE_OrderCartExec

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CARTEX_ParRef | bigint | PK |  | NO | Parent Reference |
| CARTEX_Childsub | double |  |  | NO | Childsub |
| CARTEX_OffsetExecID | varchar |  |  | SI | OEOrdExec row ID to the offset order item in the s... |
| CARTEX_OffsetItemID | varchar |  |  | SI | OEOrdItem row ID to the offset order item in the s... |
| CARTEX_OffsetType | varchar |  |  | SI | Offset Type |
| CARTEX_OffsetUnit | varchar |  |  | SI | Offset Unit |
| CARTEX_OffsetValue | double |  |  | SI | Offset Value  |
| CARTEX_OriginalExecID | varchar |  |  | NO | OEOrdExec row ID that this object was originally c... |
| CARTEX_RowId | varchar |  |  | NO | - |
| ChildQ31DR | - |  |  | SI | Child Reference: Wrist |
| Q30Q1 | - |  |  | SI | Movement |
| Q30Q2 | - |  |  | SI | Strength - Right |
| Q30Q3 | - |  |  | SI | Strength - Left |
| Q30Q4 | - |  |  | SI | AROM - Right |
| Q30Q5 | - |  |  | SI | AROM - Left |
| Q30Q6 | - |  |  | SI | PROM - Right |
| Q30Q7 | - |  |  | SI | PROM - Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*