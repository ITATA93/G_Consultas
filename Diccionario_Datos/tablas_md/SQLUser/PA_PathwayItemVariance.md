# SQLUser.PA_PathwayItemVariance

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PATHIV_ParRef | varchar | PK |  | NO | Parent Reference |
| PATHIV_AccessProfile_DR | bigint |  | FK | SI | Access Profile |
| PATHIV_ChangedBy_DR | bigint |  | FK | SI | Changed By |
| PATHIV_Childsub | double |  |  | NO | Childsub |
| PATHIV_DateChanged | date |  |  | SI | Date Changed |
| PATHIV_ReasonForVariance_DR | bigint |  | FK | SI | Reason for Variance |
| PATHIV_RowId | varchar |  |  | NO | - |
| PATHIV_TimeChanged | time |  |  | SI | Time Changed |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*