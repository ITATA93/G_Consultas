# SQLUser.OE_OrderItemChangeAdmLineItems

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITMAL_ParRef | bigint | PK |  | NO | OE_OrderItemChange Parent Reference |
| ChildQ33DR | - |  |  | SI | Child Reference: Hip |
| ITMAL_Childsub | double |  |  | NO | Childsub |
| ITMAL_FieldName | varchar |  |  | SI | FieldName   |
| ITMAL_NewValue | varchar |  |  | SI | NewValue    |
| ITMAL_OldValue | varchar |  |  | SI | OldValue    |
| ITMAL_RowId | varchar |  |  | NO | - |
| Q32Q1 | - |  |  | SI | Movement |
| Q32Q2 | - |  |  | SI | Strength - Right |
| Q32Q3 | - |  |  | SI | Strength - Left |
| Q32Q4 | - |  |  | SI | AROM - Right |
| Q32Q5 | - |  |  | SI | AROM - Left |
| Q32Q6 | - |  |  | SI | PROM - Right |
| Q32Q7 | - |  |  | SI | PROM - Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*