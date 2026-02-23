# SQLUser.OE_OrderReviewSession

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REVSESS_RowId | bigint | PK |  | NO | - |
| Q36Q1 | - |  |  | SI | Movement |
| Q36Q2 | - |  |  | SI | Strength - Right |
| Q36Q3 | - |  |  | SI | Strength - Left |
| Q36Q4 | - |  |  | SI | AROM - Right |
| Q36Q5 | - |  |  | SI | AROM - Left |
| Q36Q6 | - |  |  | SI | PROM - Right |
| Q36Q7 | - |  |  | SI | PROM - Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REVSESS_Adm_DR | bigint |  | FK | SI | Des Ref PAAdm |
| REVSESS_EndDate | date |  |  | SI | EndDate |
| REVSESS_EndTime | time |  |  | SI | EndTime |
| REVSESS_OffSetStartDate | date |  |  | SI | OffSetStartDate |
| REVSESS_OffSetStartTime | time |  |  | SI | StartTime |
| REVSESS_OverlapEndDate | date |  |  | SI | OverlapEndDate |
| REVSESS_OverlapEndTime | time |  |  | SI | EndTime |
| REVSESS_ReviewNumber | varchar |  |  | SI | ReviewNumber |
| REVSESS_StartDate | date |  |  | SI | StartDate |
| REVSESS_StartTime | time |  |  | SI | StartTime |
| REVSESS_Status | varchar |  |  | SI | Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*