# SQLUser.PAC_FdiuDiagnosis

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FDIUDIAG_RowId | bigint | PK |  | NO | - |
| FDIUDIAG_Active | varchar |  |  | SI | active |
| FDIUDIAG_Code | varchar |  |  | NO | Code |
| FDIUDIAG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FDIUDIAG_CreatedDate | date |  |  | SI | Created Date |
| FDIUDIAG_CreatedTime | time |  |  | SI | Created Time |
| FDIUDIAG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FDIUDIAG_DateFrom | date |  |  | SI | Date From |
| FDIUDIAG_DateTo | date |  |  | SI | Date To |
| FDIUDIAG_Desc | varchar |  |  | NO | Description |
| FDIUDIAG_NationalCode | varchar |  |  | SI | National code |
| FDIUDIAG_Owner | varchar |  |  | SI | Owner |
| FDIUDIAG_UpdatedDate | date |  |  | SI | Updated Date |
| FDIUDIAG_UpdatedTime | time |  |  | SI | Updated Time |
| FDIUDIAG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q06Q1 | - |  |  | SI | Medication |
| Q06Q2 | - |  |  | SI | Risk |
| Q06Q3 | - |  |  | SI | Nature of risk |
| Q06Q4 | - |  |  | SI | Other risks |
| Q06Q5 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*