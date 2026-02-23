# TC_hmf_Manager.ProductionStatus

**Schema:** TC_hmf_Manager
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFPST_CompStatSum | varchar |  |  | SI | Component Status Summary as numbers OK, Inactive, ... |
| HMFPST_NeedsUpdate | integer |  |  | SI | Monitor Matrix reports also NeedsUpdate 0/1 |
| HMFPST_Production | varchar |  |  | NO | Production representing the hmf.Production (=Gatew... |
| HMFPST_ProductionStatus | varchar |  |  | SI | This is the Status for the named component or the ... |
| HMFPST_Production_DR | bigint |  | FK | SI | Referenced ConfigItem (Production) |
| HMFPST_StatusDerived_DR | bigint |  | FK | SI | Status from Active Call to the Production (false) ... |
| HMFPST_StatusErrorString | varchar |  |  | SI | Status from Active Call to the Production (false) ... |
| HMFPST_UpdateDate | date |  |  | SI | Update Date |
| HMFPST_UpdateTime | time |  |  | SI | Update Time |
| HMFPST_UpdateUser | varchar |  |  | SI | Des Ref Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*