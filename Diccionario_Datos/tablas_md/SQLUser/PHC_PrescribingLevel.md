# SQLUser.PHC_PrescribingLevel

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRESCLV_RowId | bigint | PK |  | NO | - |
| PRESCLV_CreatedDate | date |  |  | SI | Created Date |
| PRESCLV_CreatedTime | time |  |  | SI | Created Time |
| PRESCLV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRESCLV_Default | varchar |  |  | SI | Default |
| PRESCLV_EpisType | varchar |  |  | SI | EpisType |
| PRESCLV_PrescLevel | varchar |  |  | SI | Prescribing Level |
| PRESCLV_UpdatedDate | date |  |  | SI | Updated Date |
| PRESCLV_UpdatedTime | time |  |  | SI | Updated Time |
| PRESCLV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*