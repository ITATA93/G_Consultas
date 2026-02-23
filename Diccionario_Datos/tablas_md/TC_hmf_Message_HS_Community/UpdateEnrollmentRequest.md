# TC_hmf_Message_HS_Community.UpdateEnrollmentRequest

**Schema:** TC_hmf_Message_HS_Community
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AssigningAuthority | varchar |  |  | SI | Assigning Authority for the MRN |
| EnrollmentComment | varchar |  |  | SI | Enrollment Comment |
| EnrollmentStatus | varchar |  |  | SI | Enrollment Status |
| MPIID | varchar |  |  | SI | Patient MPI ID |
| MRN | varchar |  |  | SI | Patient MRN / Identitifier |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*