# SQLUser.PA_ProblemClinEpis

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CEP_ParRef | varchar | PK |  | NO | PA_VaccinationDesease Parent Reference |
| CEP_Childsub | double |  |  | NO | Childsub |
| CEP_EndDate | date |  |  | SI | End Date |
| CEP_EndTime | time |  |  | SI | End Time |
| CEP_RowId | varchar |  |  | NO | - |
| CEP_StartDate | date |  |  | SI | Start Date |
| CEP_StartTime | time |  |  | SI | Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*