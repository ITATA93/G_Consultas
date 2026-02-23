# SQLUser.PA_Desease

**Schema:** SQLUser
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DES_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| ChildQ27DR | - |  |  | SI | Child Reference: Structured Treatment Plan |
| DES_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| DES_Childsub | double |  |  | NO | Childsub |
| DES_ContageousWarning_DR | bigint |  | FK | SI | des ref to contageous disease warning |
| DES_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| DES_Date | date |  |  | SI | Date |
| DES_Desc | varchar |  |  | SI | Description |
| DES_DuratDays | double |  |  | SI | Duration in Days |
| DES_DuratMonth | double |  |  | SI | Duration in Month |
| DES_DuratYear | double |  |  | SI | Duration in Year |
| DES_EndDate | date |  |  | SI | EndDate |
| DES_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| DES_InActive | varchar |  |  | SI | InActive |
| DES_MRCICDDx_DR | bigint |  | FK | SI | DES Ref to MRCICDDx |
| DES_OnsetDate | date |  |  | SI | Onset Date |
| DES_RowId | varchar |  |  | NO | - |
| DES_Time | time |  |  | SI | Time |
| DES_UpdateDate | date |  |  | SI | UpdateDate |
| DES_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| DES_UpdateTime | time |  |  | SI | UpdateTime |
| DES_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| Q75Q1 | - |  |  | SI | Date |
| Q75Q10 | - |  |  | SI | Entered by |
| Q75Q2 | - |  |  | SI | Treatment |
| Q75Q3 | - |  |  | SI | Treatment comments |
| Q75Q4 | - |  |  | SI | Primary dressing(s) |
| Q75Q5 | - |  |  | SI | Secondary dressing(s) |
| Q75Q6 | - |  |  | SI | Dressing comments |
| Q75Q7 | - |  |  | SI | Packing count - IN |
| Q75Q8 | - |  |  | SI | Packing count - OUT |
| Q75Q9 | - |  |  | SI | Pack comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*