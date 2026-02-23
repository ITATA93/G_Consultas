# websys_MobileApp.PushLog

**Schema:** websys_MobileApp
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| IsError | bit |  |  | SI | - |
| Message | varchar |  |  | SI | - |
| PushToken | varchar |  |  | SI | - |
| PushType | varchar |  |  | SI | - |
| SentDate | date |  |  | SI | - |
| SentTime | time |  |  | SI | - |
| Server | varchar |  |  | SI | - |
| SourceID | varchar |  |  | SI | - |
| Status | varchar |  |  | SI | - |
| UserDR | bigint |  | FK | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*