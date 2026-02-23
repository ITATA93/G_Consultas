# websys.DSSActionItem

**Schema:** websys
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | varchar | PK |  | NO | - |
| ActionType | varchar |  |  | SI | - |
| ClassProperty | varchar |  |  | SI | - |
| CommandExecute | varchar |  |  | SI | - |
| ComponentItem | varchar |  |  | SI | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| EmailFrom | varchar |  |  | SI | - |
| EmailSubject | varchar |  |  | SI | - |
| EmailTo | varchar |  |  | SI | - |
| EpisodeRecipient | bigint |  |  | SI | - |
| EpisodeRecipientList | varchar |  |  | SI | - |
| FaxTo | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| MedTrakGroupID | varchar |  |  | SI | - |
| MedTrakRecipient | varchar |  |  | SI | - |
| MessageTo | varchar |  |  | SI | - |
| OrderItem | varchar |  |  | SI | - |
| PageTo | varchar |  |  | SI | - |
| PresentationType | varchar |  |  | NO | - |
| Recipient | varchar |  |  | SI | - |
| SetFieldType | varchar |  |  | SI | - |
| SetFieldValue | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*