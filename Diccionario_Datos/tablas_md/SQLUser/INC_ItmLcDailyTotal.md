# SQLUser.INC_ItmLcDailyTotal

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DAY_ParRef | varchar | PK |  | NO | INC_ItmLoc Parent Reference |
| ChildQ66DR | - |  |  | SI | Child Reference: Deep Tendon Reflexes |
| DAY_CreatedDate | date |  |  | SI | Created Date |
| DAY_CreatedTime | time |  |  | SI | Created Time |
| DAY_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DAY_Date | date |  |  | NO | Date |
| DAY_PriceBeg | double |  |  | SI | Price at the Beginning of day |
| DAY_PriceEnd | double |  |  | SI | Price at the End of the day |
| DAY_QtyBeg | double |  |  | SI | Qty at the Beginning of day |
| DAY_QtyEnd | double |  |  | SI | Qty at the End of the day |
| DAY_RowId | varchar |  |  | NO | - |
| DAY_UpdatedDate | date |  |  | SI | Updated Date |
| DAY_UpdatedTime | time |  |  | SI | Updated Time |
| DAY_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q68Q1 | - |  |  | SI | Movement |
| Q68Q2 | - |  |  | SI | Major |
| Q68Q3 | - |  |  | SI | Moderate |
| Q68Q4 | - |  |  | SI | Minimum |
| Q68Q5 | - |  |  | SI | Nil |
| Q68Q6 | - |  |  | SI | Pain |
| Q68Q7 | - |  |  | SI | Muscle  power /5 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*