# SQLUser.PHC_DrgFormEquivGrp

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EQGRP_ParRef | varchar | PK |  | NO | PHC_DrgForm Parent Reference |
| EQGRP_Childsub | double |  |  | NO | Childsub |
| EQGRP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EQGRP_CreatedDate | date |  |  | SI | Created Date |
| EQGRP_CreatedTime | time |  |  | SI | Created Time |
| EQGRP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EQGRP_DateFrom | date |  |  | SI | Date From |
| EQGRP_DateTo | date |  |  | SI | Date To |
| EQGRP_EquivGroup_DR | bigint |  | FK | SI | Des Ref PHCEquivalenceGroup |
| EQGRP_HCA_DR | bigint |  | FK | SI | Des Ref HealthCareArea |
| EQGRP_HCR_DR | bigint |  | FK | SI | Des Ref HealthCareRegion |
| EQGRP_National | varchar |  |  | SI | National  |
| EQGRP_RowId | varchar |  |  | NO | - |
| EQGRP_UpdatedDate | date |  |  | SI | Updated Date |
| EQGRP_UpdatedTime | time |  |  | SI | Updated Time |
| EQGRP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*