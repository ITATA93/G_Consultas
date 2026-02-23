# SQLUser.PAC_ReferralCategory

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFCAT_RowId | bigint | PK |  | NO | - |
| ChildQ30DR | - |  |  | SI | Child Reference: Strength |
| Q29Q1 | - |  |  | SI | Mobility assessment for |
| Q29Q2 | - |  |  | SI | Walking aids |
| Q29Q3 | - |  |  | SI | Amputation |
| Q29Q4 | - |  |  | SI | Location of amputation (if applicable) |
| Q29Q5 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFCAT_Code | varchar |  |  | NO | Code |
| REFCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFCAT_CreatedDate | date |  |  | SI | Created Date |
| REFCAT_CreatedTime | time |  |  | SI | Created Time |
| REFCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFCAT_DateFrom | date |  |  | SI | DateFrom |
| REFCAT_DateTo | date |  |  | SI | DateTo |
| REFCAT_Desc | varchar |  |  | NO | Description |
| REFCAT_Owner | varchar |  |  | SI | Owner |
| REFCAT_UpdatedDate | date |  |  | SI | Updated Date |
| REFCAT_UpdatedTime | time |  |  | SI | Updated Time |
| REFCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*