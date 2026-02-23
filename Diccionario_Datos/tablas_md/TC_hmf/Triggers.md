# TC_hmf.Triggers

**Schema:** TC_hmf
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFTRG_Class | varchar |  |  | SI | TrakCare Class |
| HMFTRG_DateFrom | date |  |  | SI | Date From |
| HMFTRG_DateTo | date |  |  | SI | Date To |
| HMFTRG_Desc | varchar |  |  | SI | Trigger description (optional) |
| HMFTRG_DisplayName | varchar |  |  | SI | - |
| HMFTRG_Enabled | bit |  |  | SI | - |
| HMFTRG_Group_DR | bigint |  | FK | SI | - |
| HMFTRG_LowPriority | bit |  |  | SI | Set trigger to low priority for outbound messaging... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*