# SQLUser.SS_ProfilePatientLocation

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPPL_ParRef | bigint | PK |  | NO | Parent table |
| SSPPL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSPPL_DateFrom | date |  |  | SI | Date From |
| SSPPL_DateTo | date |  |  | SI | Date To |
| SSPPL_PatientLocation_DR | bigint |  | FK | SI | Patient Location |
| SSPPL_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*