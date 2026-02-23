# lab.CT_PrintDestination

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPD_RowID | varchar | PK |  | NO | - |
| CTPD_Active | varchar |  |  | SI | Active |
| CTPD_Code | varchar |  |  | NO | Code |
| CTPD_CurrentStationery_DR | varchar |  | FK | SI | Stationery |
| CTPD_Description | varchar |  |  | SI | Description |
| CTPD_Device | varchar |  |  | SI | Device |
| CTPD_Message | varchar |  |  | SI | Message |
| CTPD_ModeEnd | varchar |  |  | SI | End mode |
| CTPD_ModeStart | varchar |  |  | SI | Start mode |
| CTPD_ModemNumber | varchar |  |  | SI | Modem Number |
| CTPD_NumberOfRetries | varchar |  |  | SI | Number Of Retries |
| CTPD_Parameters | varchar |  |  | SI | Open Parameters |
| CTPD_PrinterType_DR | varchar |  | FK | SI | Printer Type |
| CTPD_Site_DR | varchar |  | FK | SI | Site |
| CTPD_Type | varchar |  |  | SI | Destination Type |
| CTPD_WindowsDevice | varchar |  |  | SI | Windows Device |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*