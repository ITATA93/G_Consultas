# SQLUser.SS_ObservationBuffer

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBSBUF_RowId | bigint | PK |  | NO | - |
| OBSBUF_Date | date |  |  | SI | Date |
| OBSBUF_Device_DR | bigint |  | FK | SI | Des Ref CTMonitoringDevice |
| OBSBUF_Message | longvarchar |  |  | SI | Message Stream |
| OBSBUF_Time | time |  |  | SI | Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*