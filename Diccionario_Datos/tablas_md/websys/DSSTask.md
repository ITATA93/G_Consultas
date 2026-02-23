# websys.DSSTask

**Schema:** websys
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CmdExecute | varchar |  |  | SI | - |
| EpisodeID | varchar |  |  | SI | - |
| Event | bigint |  |  | SI | - |
| ExeDateOld | varchar |  |  | SI | - |
| ExeTimeOld | varchar |  |  | SI | - |
| PatientID | varchar |  |  | SI | - |
| Status | varchar |  |  | SI | - |
| exeDate | varchar |  |  | SI | Date store in $HOROLOG format |
| exeTime | varchar |  |  | SI | Time store in $HOROLOG format |
| reqDate | varchar |  |  | SI | Date store in $HOROLOG format |
| reqTime | varchar |  |  | SI | Time store in $HOROLOG format |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*