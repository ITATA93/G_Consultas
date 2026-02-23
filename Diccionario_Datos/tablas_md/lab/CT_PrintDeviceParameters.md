# lab.CT_PrintDeviceParameters

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDV_RowId | varchar | PK |  | NO | - |
| CTDV_Code | varchar |  |  | NO | Code |
| CTDV_DeviceType | varchar |  |  | NO | Device Type |
| CTDV_Sequence | varchar |  |  | SI | Command/Control Sequence |
| CTDV_Subsystem | varchar |  |  | NO | Subsystem |
| CTDV_xxx | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*