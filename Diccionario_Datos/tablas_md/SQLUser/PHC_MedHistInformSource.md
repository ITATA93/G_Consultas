# SQLUser.PHC_MedHistInformSource

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHINFSRC_RowId | bigint | PK |  | NO | - |
| MHINFSRC_Code | varchar |  |  | NO | Code |
| MHINFSRC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHINFSRC_CreatedDate | date |  |  | SI | Created Date |
| MHINFSRC_CreatedTime | time |  |  | SI | Created Time |
| MHINFSRC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHINFSRC_DateFrom | date |  |  | SI | Date From |
| MHINFSRC_DateTo | date |  |  | SI | Date To |
| MHINFSRC_Desc | varchar |  |  | NO | Description |
| MHINFSRC_Owner | varchar |  |  | SI | Owner |
| MHINFSRC_UpdatedDate | date |  |  | SI | Updated Date |
| MHINFSRC_UpdatedTime | time |  |  | SI | Updated Time |
| MHINFSRC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*