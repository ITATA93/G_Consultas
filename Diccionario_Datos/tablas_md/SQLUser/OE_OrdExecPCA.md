# SQLUser.OE_OrdExecPCA

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PCA_ParRef | varchar | PK |  | NO | OE_OrdExec Parent Reference |
| PCA_Childsub | double |  |  | NO | Childsub |
| PCA_Date | date |  |  | SI | Date |
| PCA_DeleteComment | varchar |  |  | SI | Delete Reason Comment |
| PCA_DeleteReason | varchar |  |  | SI | Delete Reason |
| PCA_NoBolusAdmin | double |  |  | SI | NoBolusAdministered |
| PCA_NoBolusRequested | double |  |  | SI | NoBolusRequested |
| PCA_RowId | varchar |  |  | NO | - |
| PCA_Text1 | varchar |  |  | SI | Text1 |
| PCA_Time | time |  |  | SI | Time |
| PCA_TotalAdmin | double |  |  | SI | TotalAdministered |
| PCA_TotalAdminUOM_DR | bigint |  | FK | SI | Des Ref CTUOM |
| PCA_TotalVolInfused | double |  |  | SI | Volume Infused |
| PCA_UserDelete_DR | bigint |  | FK | SI | Des Ref SSUser |
| PCA_User_DR | bigint |  | FK | SI | Des Ref SSUser |
| PCA_VolumeRemainMls | double |  |  | SI | VolumeRemainMls |
| Q64Q1 | - |  |  | SI | Test |
| Q64Q2 | - |  |  | SI | Left |
| Q64Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*