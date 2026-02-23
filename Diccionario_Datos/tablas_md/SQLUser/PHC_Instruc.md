# SQLUser.PHC_Instruc

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCIN_RowId | bigint | PK |  | NO | - |
| PHCIN_Code | varchar |  |  | NO | Instruction Code |
| PHCIN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCIN_CodeTranslated | varchar |  |  | SI | - |
| PHCIN_CreatedDate | date |  |  | SI | Created Date |
| PHCIN_CreatedTime | time |  |  | SI | Created Time |
| PHCIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCIN_DateFrom | date |  |  | SI | DateFrom |
| PHCIN_DateTo | date |  |  | SI | DateTo |
| PHCIN_Desc1 | varchar |  |  | NO | Description(Local Language) |
| PHCIN_Desc1Translated | varchar |  |  | SI | - |
| PHCIN_Desc2 | varchar |  |  | SI | Description(Foreign Language) |
| PHCIN_DisplayOnLabel | varchar |  |  | SI | Display on Label |
| PHCIN_OfficialCode | varchar |  |  | SI | Official Code |
| PHCIN_Owner | varchar |  |  | SI | Owner |
| PHCIN_Type | varchar |  |  | SI | Type |
| PHCIN_UpdatedDate | date |  |  | SI | Updated Date |
| PHCIN_UpdatedTime | time |  |  | SI | Updated Time |
| PHCIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*