# Region_CLXX_Reports_REMManager.Audit

**Schema:** Region_CLXX_Reports_REMManager
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AUDDate | date |  |  | SI | - |
| AUDHospitalLocation | varchar |  |  | SI | - |
| AUDObject | varchar |  |  | SI | - |
| AUDObjectType | varchar |  |  | SI | - |
| AUDSourceView | varchar |  |  | SI | - |
| AUDTableRowId | varchar |  |  | SI | - |
| AUDTime | time |  |  | SI | - |
| AUDUser | varchar |  |  | SI | - |
| AUDViewType | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*