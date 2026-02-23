# SQLUser.PA_PersonEnrollmentHistory

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIST_ParRef | bigint | PK |  | NO | PA_Person Parent Reference |
| HIST_Childsub | double |  |  | NO | Childsub |
| HIST_Comment | varchar |  |  | SI | Comment |
| HIST_Date | date |  |  | NO | Date |
| HIST_EnrollmentAction | varchar |  |  | SI | Enrollment Action |
| HIST_EnrollmentStatus | varchar |  |  | SI | Personal Community Enrollment Status |
| HIST_RowId | varchar |  |  | NO | - |
| HIST_Time | time |  |  | NO | Time |
| HIST_UserDR | bigint |  | FK | SI | Last Action User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*