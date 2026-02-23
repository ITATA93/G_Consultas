# TC_hmf_System_Process_TrakOutbound.Thread1__PendingResponses

**Schema:** TC_hmf_System_Process_TrakOutbound
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Thread1 | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| _PendingResponses | varchar |  |  | SI | _PendingResponses |
| element_key | varchar |  |  | NO | %PendingResponses array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*