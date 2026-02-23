# SQLUser.RBC_ClinicPrintOption

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLPROPT_RowId | bigint | PK |  | NO | - |
| CLPROPT_Code | varchar |  |  | NO | Code |
| CLPROPT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CLPROPT_CreatedDate | date |  |  | SI | Created Date |
| CLPROPT_CreatedTime | time |  |  | SI | Created Time |
| CLPROPT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CLPROPT_DateFrom | date |  |  | SI | Date From |
| CLPROPT_DateTo | date |  |  | SI | Date To |
| CLPROPT_Desc | varchar |  |  | NO | Description |
| CLPROPT_Owner | varchar |  |  | SI | Owner |
| CLPROPT_UpdatedDate | date |  |  | SI | Updated Date |
| CLPROPT_UpdatedTime | time |  |  | SI | Updated Time |
| CLPROPT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*