# SQLUser.PHC_MedHisDurationType

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHDT_RowId | bigint | PK |  | NO | - |
| MHDT_Code | varchar |  |  | NO | Code |
| MHDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHDT_CreatedDate | date |  |  | SI | Created Date |
| MHDT_CreatedTime | time |  |  | SI | Created Time |
| MHDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHDT_DateFrom | date |  |  | SI | Date From |
| MHDT_DateTo | date |  |  | SI | Date To |
| MHDT_Desc | varchar |  |  | NO | Description |
| MHDT_Owner | varchar |  |  | SI | Owner |
| MHDT_UpdatedDate | date |  |  | SI | Updated Date |
| MHDT_UpdatedTime | time |  |  | SI | Updated Time |
| MHDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*