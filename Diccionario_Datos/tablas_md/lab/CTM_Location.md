# lab.CTM_Location

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMRL_RowID | varchar | PK |  | NO | - |
| CTMRL_Code | varchar |  |  | NO | Code |
| CTMRL_Description | varchar |  |  | SI | Description |
| CTMRL_External | varchar |  |  | SI | External |
| CTMRL_LocationAddress1 | varchar |  |  | SI | Location Address1 |
| CTMRL_LocationAddress2 | varchar |  |  | SI | Location Address2 |
| CTMRL_LocationAddress3_Suburb | varchar |  |  | SI | Location Suburb |
| CTMRL_LocationAddress4_State | varchar |  |  | SI | Location State |
| CTMRL_LocationAddress5_PostCode | varchar |  |  | SI | Location Post Code |
| CTMRL_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*