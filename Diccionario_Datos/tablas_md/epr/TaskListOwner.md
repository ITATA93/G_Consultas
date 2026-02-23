# epr.TaskListOwner

**Schema:** epr
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| Action | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| OwnerCareProvDR | varchar |  | FK | SI | - |
| OwnerUserDR | bigint |  | FK | SI | - |
| StartDate | date |  |  | SI | - |
| StartTime | date |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*