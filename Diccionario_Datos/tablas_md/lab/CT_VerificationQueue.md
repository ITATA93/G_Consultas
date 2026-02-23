# lab.CT_VerificationQueue

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTVQ_RowID | varchar | PK |  | NO | - |
| CTVQ_Code | varchar |  |  | NO | Code |
| CTVQ_Description | varchar |  |  | SI | Description |
| CTVQ_InstantPrint | varchar |  |  | SI | Instant Print |
| CTVQ_Printable | varchar |  |  | SI | Printable |
| CTVQ_QueueType | varchar |  |  | SI | Queue Type |
| CTVQ_ReadOnly | varchar |  |  | SI | Read Only |
| CTVQ_Viewable | varchar |  |  | SI | Viewable |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*