# lab.CT_MedicareSettings

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMED_RowID | bigint | PK |  | NO | - |
| CTMED_LocationID | varchar |  |  | SI | Location ID |
| CTMED_PKIPassword | varchar |  |  | SI | PKI Password |
| CTMED_PKIPath | varchar |  |  | SI | PKI Path |
| CTMED_ProxyPassword | varchar |  |  | SI | Proxy Password |
| CTMED_ProxyUser | varchar |  |  | SI | Proxy User |
| CTMED_Recipient | varchar |  |  | SI | Recipient |
| CTMED_Server | varchar |  |  | SI | Server |
| CTMED_TimeOut | integer |  |  | SI | Time Out |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*