# epr.TaskListGroup

**Schema:** epr
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| AdminStatus | varchar |  |  | SI | - |
| CareProvDR | varchar |  | FK | SI | - |
| ID | varchar |  |  | NO | - |
| ScheduledDate | date |  |  | SI | - |
| ScheduledTime | date |  |  | SI | - |
| UserDR | bigint |  | FK | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*