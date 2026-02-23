# web_Msg.CT_ClinicalTimeline

**Schema:** web_Msg
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CTCTL_AutoRefreshInterval | varchar |  |  | SI | Auto-Refresh Interval |
| CTCTL_AutoRefreshOn | varchar |  |  | SI | Enable Auto-Refresh |
| CTCTL_EpisodeID | varchar |  |  | SI | - |
| CTCTL_Interval | varchar |  |  | SI | - |
| CTCTL_QueryTimeFrom | varchar |  |  | SI | - |
| CTCTL_QueryTimeTo | varchar |  |  | SI | - |
| CTCTL_ScrollY | varchar |  |  | SI | - |
| CTCTL_TimeFrom | varchar |  |  | SI | - |
| CTCTL_TimeTo | varchar |  |  | SI | - |
| CTCTL_TimelineID | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*