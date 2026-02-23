# Region_CLXX_Integration_Nexus_CS.EventLog

**Schema:** Region_CLXX_Integration_Nexus_CS
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Category | varchar |  |  | SI | - |
| ErrorStatus | varchar |  |  | SI | - |
| ErrorStatus2 | varchar |  |  | SI | - |
| JobNumber | varchar |  |  | SI | - |
| Location | varchar |  |  | SI | - |
| LogDate | timestamp |  |  | SI | - |
| Message | varchar |  |  | SI | - |
| OID | varbinary |  |  | SI | - |
| Type | varchar |  |  | NO | - |
| WasSentByEMail | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*