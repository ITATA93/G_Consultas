# epr.Task

**Schema:** epr
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Code | varchar |  |  | SI | - |
| CodeTableTags | varchar |  |  | SI | - |
| Color | varchar |  |  | SI | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| EscalateAfter | varchar |  |  | SI | - |
| EscalateTimeUnit | varchar |  |  | SI | - |
| GenerateTask | varchar |  |  | SI | - |
| LinkComponent | bigint |  |  | SI | - |
| LinkExpression | varchar |  |  | SI | - |
| OutstandingBalance | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | - |
| PriorityDR | bigint |  | FK | SI | - |
| Sensitive | varchar |  |  | SI | - |
| TaskCategory | bigint |  |  | SI | - |
| WorkflowDR | bigint |  | FK | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*