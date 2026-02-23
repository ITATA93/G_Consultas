# SQLUser.PHC_DoseCalTemplateDetails

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DCTD_ParRef | bigint | PK |  | NO | PHC_DoseCalTemplate Parent Reference |
| DCTD_AsPerProtocol | varchar |  |  | SI | As Per Protocol |
| DCTD_ChildSub | double |  |  | NO | PHC_DoseCalTemplate ChildSub |
| DCTD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DCTD_CreatedDate | date |  |  | SI | Created Date |
| DCTD_CreatedTime | time |  |  | SI | Created Time |
| DCTD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DCTD_Dose | double |  |  | NO | Dose |
| DCTD_DurationType | varchar |  |  | SI | DurationType |
| DCTD_DurationValue | double |  |  | SI | Duration Value |
| DCTD_Event | varchar |  |  | SI | Event |
| DCTD_IsDoseVariable | varchar |  |  | SI | Is Dose Variable |
| DCTD_IsMinDoseVariable | varchar |  |  | SI | Is MinDose Variable |
| DCTD_MaintenanceInstruction | varchar |  |  | SI | Maintenance Instruction |
| DCTD_MinDose | double |  |  | SI | Minimum Dose |
| DCTD_PHCFR_DR | bigint |  | FK | SI | Des Ref to PHCFR (Frequency) |
| DCTD_PrefParamsDosing_DR | varchar |  | FK | SI | Dosing Cycle |
| DCTD_RowId | varchar |  |  | NO | - |
| DCTD_Sequence | integer |  |  | SI | Sequence |
| DCTD_UpdatedDate | date |  |  | SI | Updated Date |
| DCTD_UpdatedTime | time |  |  | SI | Updated Time |
| DCTD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*