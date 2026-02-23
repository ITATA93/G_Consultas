# SQLUser.PHC_DispensingTime

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PHCDT_PHCFR_ParRef | bigint | PK |  | NO | PHCF Parent Reference |
| PHCDT_ChildSub | double |  |  | NO | ChildSub (New Key) |
| PHCDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PHCDT_CreatedDate | date |  |  | SI | Created Date |
| PHCDT_CreatedTime | time |  |  | SI | Created Time |
| PHCDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PHCDT_DayNumber | varchar |  |  | SI | Day Number |
| PHCDT_DayOfTheWeek | varchar |  |  | SI | Day of the week |
| PHCDT_RowId | varchar |  |  | NO | - |
| PHCDT_Time | time |  |  | SI | Dispensing Time |
| PHCDT_UpdatedDate | date |  |  | SI | Updated Date |
| PHCDT_UpdatedTime | time |  |  | SI | Updated Time |
| PHCDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*