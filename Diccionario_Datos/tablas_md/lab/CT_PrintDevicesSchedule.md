# lab.CT_PrintDevicesSchedule

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDXS_ParRef | varchar | PK |  | NO | CT_PrintDevices Parent Reference |
| CTDXS_Order | numeric |  |  | NO | Order Number |
| CTDXS_PrintDestination_DR | varchar |  | FK | SI | Print Destination DR |
| CTDXS_RowID | varchar |  |  | NO | - |
| CTDXS_TimeEnd | time |  |  | SI | Time End |
| CTDXS_TimeStart | time |  |  | SI | Time Start |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*