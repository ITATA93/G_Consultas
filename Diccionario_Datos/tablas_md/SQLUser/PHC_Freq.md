# SQLUser.PHC_Freq

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCFR_RowId | bigint | PK |  | NO | - |
| PHCFR_Code | varchar |  |  | NO | Code |
| PHCFR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCFR_CodeTranslated | varchar |  |  | SI | - |
| PHCFR_CreatedDate | date |  |  | SI | Created Date |
| PHCFR_CreatedTime | time |  |  | SI | Created Time |
| PHCFR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCFR_DateFrom | date |  |  | NO | Date From |
| PHCFR_DateTo | date |  |  | SI | Date To |
| PHCFR_Days | double |  |  | SI | No of Days |
| PHCFR_DaysOfTheWeek | varchar |  |  | SI | Days of the week |
| PHCFR_DelayedFirstAdminAlertThreshold | integer |  |  | SI | Frequency Interval Percentage for Delayed First Ad... |
| PHCFR_Desc1 | varchar |  |  | SI | Description (Local Languange) |
| PHCFR_Desc1Translated | varchar |  |  | SI | - |
| PHCFR_Desc2 | varchar |  |  | SI | Description (Foreign Language) |
| PHCFR_ExcludeForED | varchar |  |  | SI | Exclude for Emergency |
| PHCFR_ExcludeForIP | varchar |  |  | SI | Exclude for Inpaitient |
| PHCFR_ExcludeForOP | varchar |  |  | SI | Exclude for Outpaitient |
| PHCFR_Factor | double |  |  | SI | Factor |
| PHCFR_OffsetMinutes | double |  |  | SI | OffsetMinutes  |
| PHCFR_OnceOnlyFrequency | varchar |  |  | SI | OnceOnlyFrequency |
| PHCFR_Owner | varchar |  |  | SI | Owner |
| PHCFR_STATFrequency | varchar |  |  | SI | STATFrequency |
| PHCFR_SeqOrder | integer |  |  | SI | Seq Order |
| PHCFR_UpdatedDate | date |  |  | SI | Updated Date |
| PHCFR_UpdatedTime | time |  |  | SI | Updated Time |
| PHCFR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*