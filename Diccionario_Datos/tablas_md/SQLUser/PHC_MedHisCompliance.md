# SQLUser.PHC_MedHisCompliance

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHC_RowId | bigint | PK |  | NO | - |
| MHC_Code | varchar |  |  | NO | Code |
| MHC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHC_CreatedDate | date |  |  | SI | Created Date |
| MHC_CreatedTime | time |  |  | SI | Created Time |
| MHC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHC_DateFrom | date |  |  | SI | Date From |
| MHC_DateTo | date |  |  | SI | Date To |
| MHC_Desc | varchar |  |  | NO | Description |
| MHC_Owner | varchar |  |  | SI | Owner |
| MHC_UpdatedDate | date |  |  | SI | Updated Date |
| MHC_UpdatedTime | time |  |  | SI | Updated Time |
| MHC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*