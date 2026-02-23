# SQLUser.PHC_GenericRtFormsTherCat

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| THC_ParRef | varchar | PK |  | NO | PHC_GenericRtForms Parent Reference |
| THC_Childsub | double |  |  | NO | Childsub |
| THC_CreatedDate | date |  |  | SI | Created Date |
| THC_CreatedTime | time |  |  | SI | Created Time |
| THC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| THC_RowId | varchar |  |  | NO | - |
| THC_TherCateg_DR | bigint |  | FK | SI | Des Ref TherCateg |
| THC_UpdatedDate | date |  |  | SI | Updated Date |
| THC_UpdatedTime | time |  |  | SI | Updated Time |
| THC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*