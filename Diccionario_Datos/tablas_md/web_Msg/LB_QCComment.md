# web_Msg.LB_QCComment

**Schema:** web_Msg
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBQCC_Comments | varchar |  |  | SI | Comments |
| LBQCC_Date | date |  |  | SI | Comment date |
| LBQCC_ReviewCorrectiveAction_DR | bigint |  | FK | SI | Review Corrective Action (if source is Review) |
| LBQCC_ReviewRootCause_DR | bigint |  | FK | SI | Review Root Cause (if source is Review) |
| LBQCC_ReviewType_DR | bigint |  | FK | SI | Review Type (if source is Review) |
| LBQCC_RowNumber | varchar |  |  | SI | Row sequence number |
| LBQCC_TestItem_DR | bigint |  | FK | SI | Test Item |
| LBQCC_Time | varchar |  |  | SI | Comment time |
| LBQCC_Type | varchar |  |  | SI | Comment type (labeled source in UI to reduce confu... |
| LBQCC_User_DR | bigint |  | FK | SI | Comment user |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*