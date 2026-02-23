# SQLUser.OE_AdmixSnapshot

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AMS_ParRef | bigint | PK |  | NO | OE_OrdAdmix Parent Reference |
| AMS_Childsub | double |  |  | NO | Childsub |
| AMS_Date | date |  |  | SI | Date |
| AMS_ItemChange_DR | bigint |  | FK | NO | Order Item Change ID |
| AMS_PCALoadingVolume | double |  |  | SI | PCA Loading Volume |
| AMS_PCALoadingVolumeUOM_DR | bigint |  | FK | SI | PCA Loading Volume UOM |
| AMS_Quantity | double |  |  | SI | Quantity |
| AMS_RowId | varchar |  |  | NO | - |
| AMS_Solvent_DR | varchar |  | FK | SI | Solvent |
| AMS_Time | time |  |  | SI | Time |
| AMS_TotalFlowRate | double |  |  | SI | Total Flow Rate |
| AMS_TotalFlowRatePerUOM | varchar |  |  | SI | Total Flow Rate Per UOM |
| AMS_TotalFlowRateUOM_DR | bigint |  | FK | SI | Total Flow Rate UOM |
| AMS_UOM_DR | bigint |  | FK | SI | UOM |
| ChildQ63DR | - |  |  | SI | Child Reference: Wound Physical Assessment |
| Q62Q1 | - |  |  | SI | Requested |
| Q62Q2 | - |  |  | SI | Request date |
| Q62Q3 | - |  |  | SI | Completed |
| Q62Q4 | - |  |  | SI | Completed date |
| Q62Q5 | - |  |  | SI | Review notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*