# websys.MonitorPerformanceLine

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | varchar | PK |  | NO | - |
| LineNumber | integer |  |  | NO | - |
| MonitorID | integer |  |  | NO | - |
| RoutineName | varchar |  |  | NO | - |
| pGlobals | integer |  |  | SI | - |
| pLines | integer |  |  | SI | - |
| pTime | double |  |  | SI | - |
| pTotalTime | double |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*