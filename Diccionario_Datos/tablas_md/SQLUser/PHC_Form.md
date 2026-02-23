# SQLUser.PHC_Form

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCF_RowId | bigint | PK |  | NO | - |
| PHCF_Code | varchar |  |  | NO | Code |
| PHCF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCF_CodeTranslated | varchar |  |  | SI | - |
| PHCF_CreatedDate | date |  |  | SI | Created Date |
| PHCF_CreatedTime | time |  |  | SI | Created Time |
| PHCF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCF_Desc | varchar |  |  | NO | Description |
| PHCF_DescTranslated | varchar |  |  | SI | - |
| PHCF_Owner | varchar |  |  | SI | Owner |
| PHCF_RoundFactor | double |  |  | SI | Divisibility Factor for strength incremental round... |
| PHCF_RoundMethod | varchar |  |  | SI | Rounding Method |
| PHCF_SigFigs | integer |  |  | SI | Number for rounding to Significant Figures (RoundM... |
| PHCF_TIMSno | varchar |  |  | SI | TIMS No |
| PHCF_UpdatedDate | date |  |  | SI | Updated Date |
| PHCF_UpdatedTime | time |  |  | SI | Updated Time |
| PHCF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*