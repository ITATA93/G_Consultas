# SQLUser.PHC_MedHistStopRea

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHSR_RowId | bigint | PK |  | NO | - |
| MHSR_Code | varchar |  |  | NO | Code |
| MHSR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHSR_CreatedDate | date |  |  | SI | Created Date |
| MHSR_CreatedTime | time |  |  | SI | Created Time |
| MHSR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHSR_DateFrom | date |  |  | SI | Date From |
| MHSR_DateTo | date |  |  | SI | Date To |
| MHSR_Desc | varchar |  |  | NO | Description |
| MHSR_Owner | varchar |  |  | SI | Owner |
| MHSR_UpdatedDate | date |  |  | SI | Updated Date |
| MHSR_UpdatedTime | time |  |  | SI | Updated Time |
| MHSR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*