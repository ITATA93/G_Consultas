# SQLUser.PA_PMIUpdate

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PMI_RowId | bigint | PK |  | NO | - |
| PMI_Date | date |  |  | SI | Date |
| PMI_ErrorMessage | varchar |  |  | SI | Error Message |
| PMI_MergeData | varchar |  |  | SI | Merge Data |
| PMI_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| PMI_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| PMI_Rego | varchar |  |  | SI | Rego |
| PMI_Status | varchar |  |  | SI | Status |
| PMI_Time | time |  |  | SI | Time |
| PMI_TrafficAccident_DR | bigint |  | FK | SI | Des TrafficAccident |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*