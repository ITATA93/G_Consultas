# lab.MR_Property

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRP_RowID | varchar | PK |  | NO | - |
| MRP_CaseNumber | varchar |  |  | SI | Case Number |
| MRP_Code | varchar |  |  | NO | Code |
| MRP_Comments | varchar |  |  | SI | Comments |
| MRP_DateOfRelease | date |  |  | SI | Date Of Release |
| MRP_Depositor | varchar |  |  | SI | Depositor |
| MRP_Description | varchar |  |  | SI | Description |
| MRP_Location | varchar |  |  | SI | Location |
| MRP_Property_DR | varchar |  | FK | SI | Property DR |
| MRP_TimeOfRelease | varchar |  |  | SI | Time Of Release |
| MRP_UserReceived | varchar |  |  | SI | User Received |
| MRP_UserReleased_DR | varchar |  | FK | SI | User Released |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*