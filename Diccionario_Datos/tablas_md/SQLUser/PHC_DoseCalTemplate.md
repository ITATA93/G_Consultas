# SQLUser.PHC_DoseCalTemplate

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCT_RowId | bigint | PK |  | NO | - |
| DCT_AdminRoute_DR | bigint |  | FK | SI | Des Ref AdminRoute |
| DCT_CTUOM_DR | bigint |  | FK | NO | Unit Of Measure |
| DCT_Code | varchar |  |  | NO | Code |
| DCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DCT_CreatedDate | date |  |  | SI | Created Date |
| DCT_CreatedTime | time |  |  | SI | Created Time |
| DCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DCT_DateFrom | date |  |  | SI | Date From |
| DCT_DateTo | date |  |  | SI | Date To |
| DCT_Desc | varchar |  |  | NO | Description |
| DCT_DurationUnit | varchar |  |  | SI | Duration Unit |
| DCT_DurationValue | integer |  |  | SI | Total Duration |
| DCT_FirstDetails | varchar |  |  | SI | First Details |
| DCT_Frequency | varchar |  |  | SI | Total Frequency |
| DCT_Generic_DR | bigint |  | FK | NO | Des Ref Generic |
| DCT_IVType | varchar |  |  | SI | IVType - NO LONGER USED - field numbers can be rep... |
| DCT_MaintenanceDetails | varchar |  |  | SI | Maintenance Details |
| DCT_Owner | varchar |  |  | SI | Owner |
| DCT_UpdatedDate | date |  |  | SI | Updated Date |
| DCT_UpdatedTime | time |  |  | SI | Updated Time |
| DCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*