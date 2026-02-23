# SQLUser.SS_UserLogin

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOG_RowId | bigint | PK |  | NO | - |
| LOG_ComputerName | varchar |  |  | SI | LOG_ComputerName  |
| LOG_CustomData1 | varchar |  |  | SI | - |
| LOG_CustomData2 | varchar |  |  | SI | - |
| LOG_CustomData3 | varchar |  |  | SI | - |
| LOG_CustomData4 | varchar |  |  | SI | - |
| LOG_CustomData5 | varchar |  |  | SI | - |
| LOG_LogoffDate | date |  |  | SI | Logoff Date |
| LOG_LogoffTime | time |  |  | SI | Logoff Time |
| LOG_LogonDate | date |  |  | SI | Logon Date |
| LOG_LogonTime | time |  |  | SI | Logon Time |
| LOG_SSOErrorDetails | varchar |  |  | SI | - |
| LOG_SpineDetails | varchar |  |  | SI | - |
| LOG_User_DR | bigint |  | FK | SI | Des Ref User |
| LOG_VBEX_DR | bigint |  | FK | SI | Des Ref VBEX |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*