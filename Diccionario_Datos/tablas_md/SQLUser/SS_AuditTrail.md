# SQLUser.SS_AuditTrail

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AUD_RowId | bigint | PK |  | NO | - |
| AUD_Action | varchar |  |  | SI | Action |
| AUD_CacheUser | varchar |  |  | SI | Cache User |
| AUD_ClientIP | varchar |  |  | SI | Computer Identification IP Address. |
| AUD_ClientName | varchar |  |  | SI | Computer Identification Name. |
| AUD_Date | date |  |  | SI | Date |
| AUD_Group_DR | bigint |  | FK | SI | Des Ref Group |
| AUD_LogonLocation_DR | bigint |  | FK | SI | Des Ref LogonLocation |
| AUD_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| AUD_Table | varchar |  |  | SI | Table Name |
| AUD_TableRowId | varchar |  |  | SI | Record RowId |
| AUD_Time | time |  |  | SI | Time |
| AUD_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*