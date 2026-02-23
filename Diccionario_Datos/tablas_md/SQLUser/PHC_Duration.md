# SQLUser.PHC_Duration

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCDU_RowId | bigint | PK |  | NO | - |
| PHCDU_Code | varchar |  |  | NO | Code |
| PHCDU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCDU_CodeTranslated | varchar |  |  | SI | - |
| PHCDU_CreatedDate | date |  |  | SI | Created Date |
| PHCDU_CreatedTime | time |  |  | SI | Created Time |
| PHCDU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCDU_DateFrom | date |  |  | SI | DateFrom |
| PHCDU_DateTo | date |  |  | SI | DateTo |
| PHCDU_Desc1 | varchar |  |  | NO | Description (Local Language) |
| PHCDU_Desc1Translated | varchar |  |  | SI | - |
| PHCDU_Desc2 | varchar |  |  | SI | Description (Foreign Language) |
| PHCDU_ExcludeForED | varchar |  |  | SI | Exclude for Emergency |
| PHCDU_ExcludeForIP | varchar |  |  | SI | Exclude for Inpaitient |
| PHCDU_ExcludeForOP | varchar |  |  | SI | Exclude for Outpaitient |
| PHCDU_Factor | double |  |  | NO | Factor |
| PHCDU_IsOngoing | varchar |  |  | SI | IsOngoing |
| PHCDU_Owner | varchar |  |  | SI | Owner |
| PHCDU_STATDuration | varchar |  |  | SI | STATDuration |
| PHCDU_UpdatedDate | date |  |  | SI | Updated Date |
| PHCDU_UpdatedTime | time |  |  | SI | Updated Time |
| PHCDU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*