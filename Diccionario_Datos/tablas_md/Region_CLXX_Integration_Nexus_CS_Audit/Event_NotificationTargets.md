# Region_CLXX_Integration_Nexus_CS_Audit.Event_NotificationTargets

**Schema:** Region_CLXX_Integration_Nexus_CS_Audit
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Integración Nexus**. Conexión con sistema externo Nexus.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| Event | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| NotificationTargets | varchar |  |  | SI | NotificationTargets |
| element_key | varchar |  |  | NO | NotificationTargets array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*