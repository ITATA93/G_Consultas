# SQLUser.PHC_DrgFormPackDispensing

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DISP_ParRef | varchar | PK |  | NO | PHC_DrgFormPack Parent Reference |
| DISP_Childsub | double |  |  | NO | Childsub |
| DISP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DISP_ConvFactor | double |  |  | SI | ConvFactor |
| DISP_CreatedDate | date |  |  | SI | Created Date |
| DISP_CreatedTime | time |  |  | SI | Created Time |
| DISP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DISP_DateFrom | date |  |  | SI | DateFrom |
| DISP_DateTo | date |  |  | SI | DateTo |
| DISP_EpisodeType | varchar |  |  | SI | EpisodeType |
| DISP_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| DISP_RowId | varchar |  |  | NO | - |
| DISP_UOM_DR | bigint |  | FK | SI | Des Ref UOM |
| DISP_UpdatedDate | date |  |  | SI | Updated Date |
| DISP_UpdatedTime | time |  |  | SI | Updated Time |
| DISP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*