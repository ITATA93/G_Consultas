# SQLUser.PAC_RefTemplate

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFTMP_RowId | bigint | PK |  | NO | - |
| ChildQ13DR | - |  |  | SI | Child Reference: Peritoneal dialysis training |
| Q12Q1 | - |  |  | SI | Date |
| Q12Q2 | - |  |  | SI | Status |
| Q12Q3 | - |  |  | SI | Comment |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RFTMP_BreachAllowed | varchar |  |  | SI | Breach Allowed |
| RFTMP_CancerReferral | varchar |  |  | SI | Cancer Referral |
| RFTMP_Code | varchar |  |  | NO | Code |
| RFTMP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RFTMP_CreatedDate | date |  |  | SI | Created Date |
| RFTMP_CreatedTime | time |  |  | SI | Created Time |
| RFTMP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFTMP_DateFrom | date |  |  | SI | Date From |
| RFTMP_DateTo | date |  |  | SI | Date To |
| RFTMP_Desc | varchar |  |  | NO | Description |
| RFTMP_Duration | double |  |  | SI | Duration |
| RFTMP_GES | varchar |  |  | SI | GES |
| RFTMP_Owner | varchar |  |  | SI | Owner |
| RFTMP_ProjWarning | double |  |  | SI | Projected End Date Warning |
| RFTMP_UpdatedDate | date |  |  | SI | Updated Date |
| RFTMP_UpdatedTime | time |  |  | SI | Updated Time |
| RFTMP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*