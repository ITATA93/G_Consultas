# TC_hmf.IntegrationTriggers

**Schema:** TC_hmf
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFINTTRG_Enabled | bit |  |  | SI | - |
| HMFINTTRG_Trigger_DR | bigint |  | FK | SI | Trigger DesRef |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*