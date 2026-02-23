# SQLUser.SS_Audit

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUD_RowId | bigint | PK |  | NO | - |
| AUD_Date | date |  |  | SI | Date |
| AUD_Reason_DR | bigint |  | FK | SI | Des Ref Reason |
| AUD_TableName | varchar |  |  | SI | Table Name |
| AUD_TableRowId | varchar |  |  | SI | Table RowId |
| AUD_Time | time |  |  | SI | Time |
| AUD_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*