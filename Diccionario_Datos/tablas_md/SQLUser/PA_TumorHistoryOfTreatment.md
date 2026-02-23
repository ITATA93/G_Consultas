# SQLUser.PA_TumorHistoryOfTreatment

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIS_ParRef | bigint | PK |  | NO | PA_Tumor Parent Reference |
| HIS_Childsub | double |  |  | NO | Childsub |
| HIS_EndDate | date |  |  | SI | End Date |
| HIS_HistoryOfTreatment_DR | bigint |  | FK | SI | Des Ref HistoryOfTreatment |
| HIS_RowId | varchar |  |  | NO | - |
| HIS_StartDate | date |  |  | SI | Start Date |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*