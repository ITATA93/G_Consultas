# SQLUser.SS_InvalidUserLogin

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INVLOG_RowId | bigint | PK |  | NO | - |
| INVLOG_ComputerName | varchar |  |  | SI | Computer Name |
| INVLOG_CustomData1 | varchar |  |  | SI | - |
| INVLOG_CustomData2 | varchar |  |  | SI | - |
| INVLOG_CustomData3 | varchar |  |  | SI | - |
| INVLOG_CustomData4 | varchar |  |  | SI | - |
| INVLOG_CustomData5 | varchar |  |  | SI | - |
| INVLOG_Date | date |  |  | SI | Date |
| INVLOG_SpineDetails | varchar |  |  | SI | - |
| INVLOG_Time | time |  |  | SI | Time |
| INVLOG_UserName | varchar |  |  | SI | - |
| INVLOG_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*