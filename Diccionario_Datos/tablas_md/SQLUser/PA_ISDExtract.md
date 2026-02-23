# SQLUser.PA_ISDExtract

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ISD_RowId | bigint | PK |  | NO | - |
| ISD_EndDate | date |  |  | SI | End Date |
| ISD_RunDate | date |  |  | SI | Run Date |
| ISD_RunTime | time |  |  | SI | Run Time |
| ISD_StartDate | date |  |  | SI | Start Date |
| ISD_Type | varchar |  |  | SI | Type |
| ISD_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*