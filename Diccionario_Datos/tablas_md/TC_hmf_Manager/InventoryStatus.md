# TC_hmf_Manager.InventoryStatus

**Schema:** TC_hmf_Manager
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFINV_CompletedCount | integer |  |  | SI | CompletedCount reported |
| HMFINV_Component | varchar |  |  | SI | Interface Component, can be Operation, Process, Se... |
| HMFINV_ComponentStatus | varchar |  |  | SI | This is the Status for the named component   |
| HMFINV_ConnectionStatus | varchar |  |  | SI | This is the Connection Status for the named compon... |
| HMFINV_HostType | varchar |  |  | SI | HostType reported (Ensemble 1=BS -> S, 2=BP -> P ,... |
| HMFINV_HostTypeStatus | varchar |  |  | SI | (HostType) Status from Ens (OK, ?) |
| HMFINV_Interface | varchar |  |  | NO | The logical interface |
| HMFINV_Interface_DR | varchar |  | FK | SI | Referenced ConfigItem (Interface) |
| HMFINV_LastActivity | varchar |  |  | SI | LastActivity reported |
| HMFINV_Production | varchar |  |  | NO | Production representing the hmf.Production (=Gatew... |
| HMFINV_ProductionStatus | varchar |  |  | SI | This is the Status for the named component or the ... |
| HMFINV_Production_DR | bigint |  | FK | SI | Referenced ConfigItem (Production) |
| HMFINV_QueueCount | integer |  |  | SI | QueueCount reported  |
| HMFINV_UpdateDate | date |  |  | SI | Update Date |
| HMFINV_UpdateTime | time |  |  | SI | Update Time |
| HMFINV_UpdateUser | varchar |  |  | SI | Update User as String - could be a non TrakCare (C... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*