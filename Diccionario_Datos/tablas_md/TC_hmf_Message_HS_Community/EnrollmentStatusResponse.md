# TC_hmf_Message_HS_Community.EnrollmentStatusResponse

**Schema:** TC_hmf_Message_HS_Community
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| PCEnrollmentStatusCode | varchar |  |  | SI | PC Enrollment Status Code |
| PCEnrollmentStatusDisplay | varchar |  |  | SI | PC Enrollment Status Display |
| TCActionStatusCode | varchar |  |  | SI | Status to be used for deciding which action to tak... |
| TCActionStatusDisplay | varchar |  |  | SI | Status to be used for deciding which action to tak... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*