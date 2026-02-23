# websys.DSSAuditAction

**Schema:** websys
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Auditoría de modificaciones.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ActionDate | date |  |  | SI | - |
| ActionEpisode | bigint |  |  | SI | - |
| ActionEvent | bigint |  |  | SI | - |
| ActionHospital | bigint |  |  | SI | - |
| ActionID | varchar |  |  | SI | - |
| ActionItem | varchar |  |  | SI | - |
| ActionPatient | bigint |  |  | SI | - |
| ActionTime | time |  |  | SI | - |
| ActionUser | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*