# epr.TaskExec

**Schema:** epr
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AdminStatus | varchar |  |  | SI | - |
| ExecNotes | varchar |  |  | SI | - |
| ExecutedBy | varchar |  |  | SI | - |
| ExecutionDate | date |  |  | SI | - |
| ExecutionTime | time |  |  | SI | - |
| ReasonNotComplete | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*