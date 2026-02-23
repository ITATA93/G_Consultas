# SQLUser.OE_OrdStatus

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ST_ParRef | varchar | PK |  | NO | OE_OrdItem Parent Reference |
| ChildQ25DR | - |  |  | SI | Child Reference: Deep Sensation |
| Q24Q1 | - |  |  | SI | Location |
| Q24Q2 | - |  |  | SI | Criteria |
| Q24Q3 | - |  |  | SI | Score |
| Q24Q4 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| ST_Childsub | double |  |  | NO | Childsub |
| ST_Date | date |  |  | SI | Date |
| ST_OrdExecStatus_DR | varchar |  | FK | SI | Des Ref OEOrdExecStatus |
| ST_Reason | varchar |  |  | SI | Reason |
| ST_RowId | varchar |  |  | NO | - |
| ST_Status_DR | bigint |  | FK | SI | Des Ref Status |
| ST_TextStatus | varchar |  |  | SI | Text Status |
| ST_Time | time |  |  | SI | Time |
| ST_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*