# SQLUser.PA_CancerReg

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACR_RowId | bigint | PK |  | NO | - |
| PACR_Active | varchar |  |  | SI | Active |
| PACR_AutopsyHeld | varchar |  |  | SI | Autopsy Held |
| PACR_CauseOfDeath | varchar |  |  | SI | Cause Of Death |
| PACR_Description | varchar |  |  | SI | Description |
| PACR_ExtractDate | date |  |  | SI | Extract Date |
| PACR_ExtractNeeded | varchar |  |  | SI | Extract Needed |
| PACR_LifetimeOccupation | varchar |  |  | SI | LifetimeOccupation |
| PACR_Person_DR | bigint |  | FK | SI | Des Ref Person |
| PACR_RegDate | date |  |  | SI | RegDate |
| PACR_RegNumber | varchar |  |  | SI | RegNumber |
| PACR_UpdateDate | date |  |  | SI | UpdateDate |
| PACR_UpdateTime | time |  |  | SI | UpdateTime |
| PACR_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| PACR_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q28Q1 | - |  |  | SI | Assessment date |
| Q28Q10 | - |  |  | SI | Due date for catheter bag change |
| Q28Q2 | - |  |  | SI | Assessment time |
| Q28Q3 | - |  |  | SI | Can urinary catheter be removed? |
| Q28Q4 | - |  |  | SI | Indication for continued catheter |
| Q28Q5 | - |  |  | SI | Insertion site  check |
| Q28Q6 | - |  |  | SI | Catheter check |
| Q28Q7 | - |  |  | SI | Actions performed |
| Q28Q8 | - |  |  | SI | Assessment notes |
| Q28Q9 | - |  |  | SI | Assessment performed by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*