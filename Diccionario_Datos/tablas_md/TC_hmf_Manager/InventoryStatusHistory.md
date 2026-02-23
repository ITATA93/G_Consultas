# TC_hmf_Manager.InventoryStatusHistory

**Schema:** TC_hmf_Manager
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFINVH_CompletedCount | integer |  |  | SI | CompletedCount reported |
| HMFINVH_Component | varchar |  |  | SI | Interface Component, can be Operation, Process, Se... |
| HMFINVH_ComponentStatus | varchar |  |  | SI | This is the Status for the named component   |
| HMFINVH_ConnectionStatus | varchar |  |  | SI | This is the Connection Status for the named compon... |
| HMFINVH_HostType | varchar |  |  | SI | HostType reported (Ensemble 1=BS -> S, 2=BP -> P ,... |
| HMFINVH_HostTypeStatus | varchar |  |  | SI | (HostType) Status from Ens (OK, ?) |
| HMFINVH_Interface | varchar |  |  | NO | The logical interface |
| HMFINVH_Interface_DR | varchar |  | FK | SI | Referenced ConfigItem (Interface) |
| HMFINVH_LastActivity | varchar |  |  | SI | LastActivity reported |
| HMFINVH_Production | varchar |  |  | NO | Production representing the hmf.Production (=Gatew... |
| HMFINVH_ProductionStatus | varchar |  |  | SI | This is the Status for the named component or the ... |
| HMFINVH_Production_DR | bigint |  | FK | SI | Referenced ConfigItem (Production) |
| HMFINVH_QueueCount | integer |  |  | SI | QueueCount reported  |
| HMFINVH_UpdateDate | date |  |  | SI | Update Date |
| HMFINVH_UpdateTime | time |  |  | SI | Update Time |
| HMFINVH_UpdateUser | varchar |  |  | SI | Update User as String - could be a non TrakCare (C... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*