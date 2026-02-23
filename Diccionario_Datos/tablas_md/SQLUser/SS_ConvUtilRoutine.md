# SQLUser.SS_ConvUtilRoutine

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTN_ParRef | bigint | PK |  | NO | SS_ConversionUtility Parent Reference |
| RTN_Childsub | double |  |  | NO | Childsub |
| RTN_FinishDate | date |  |  | SI | Finish Date |
| RTN_FinishTime | time |  |  | SI | Finish Time |
| RTN_RoutineToRun | varchar |  |  | NO | Routine To Run |
| RTN_RowId | varchar |  |  | NO | - |
| RTN_RunMultipleTimes | varchar |  |  | NO | Run Multiple Times |
| RTN_StartDate | date |  |  | SI | Start Date |
| RTN_StartTime | time |  |  | SI | Start Time |
| RTN_Tag | varchar |  |  | NO | Tag |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*