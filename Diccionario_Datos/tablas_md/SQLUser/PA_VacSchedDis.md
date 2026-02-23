# SQLUser.PA_VacSchedDis

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DIS_ParRef | bigint | PK |  | NO | PA_VaccinationDesease Parent Reference |
| DIS_Childsub | double |  |  | NO | Childsub |
| DIS_DeclineEndDate | date |  |  | SI | DeclineEndDate |
| DIS_DeclineStartDate | date |  |  | SI | DeclineStartDate |
| DIS_Declined | varchar |  |  | SI | Declined |
| DIS_ImmunisationNotes | varchar |  |  | SI | ImmunisationNotes |
| DIS_RowId | varchar |  |  | NO | - |
| DIS_VacDeclineReason_DR | bigint |  | FK | SI | Des Ref PACVacDeclineReason |
| DIS_VacDisease_DR | bigint |  | FK | SI | Des Ref PACVacDis |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*