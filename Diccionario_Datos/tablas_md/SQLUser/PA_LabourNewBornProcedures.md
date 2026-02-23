# SQLUser.PA_LabourNewBornProcedures

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROC_ParRef | varchar | PK |  | NO | PA_LabourNewBorn Parent Reference |
| PROC_Childsub | double |  |  | NO | Childsub |
| PROC_Procedure_DR | bigint |  | FK | SI | Des Ref Procedure |
| PROC_RowId | varchar |  |  | NO | - |
| Q04Q1 | - |  |  | SI | Procedure |
| Q04Q10 | - |  |  | SI | No. on cleavage day 5 |
| Q04Q2 | - |  |  | SI | No. treated |
| Q04Q3 | - |  |  | SI | No. of mature |
| Q04Q4 | - |  |  | SI | No. injected |
| Q04Q5 | - |  |  | SI | No. of abnormal |
| Q04Q6 | - |  |  | SI | No. of normal |
| Q04Q7 | - |  |  | SI | No. on cleavage day 2 |
| Q04Q8 | - |  |  | SI | No. on cleavage day 3 |
| Q04Q9 | - |  |  | SI | No. on cleavage day 4 |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*