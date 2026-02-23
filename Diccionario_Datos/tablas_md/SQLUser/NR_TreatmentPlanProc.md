# SQLUser.NR_TreatmentPlanProc

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROC_ParRef | bigint | PK |  | NO | NR_TreatmentPlan Parent Reference |
| PROC_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| PROC_Childsub | double |  |  | NO | Childsub |
| PROC_Days | varchar |  |  | SI | Days |
| PROC_DiscontDate | date |  |  | SI | Discontinued Date |
| PROC_NoOfDays | double |  |  | SI | No of Days |
| PROC_OverProcDur | double |  |  | SI | Override Procedure Duration |
| PROC_Remarks | varchar |  |  | SI | Remarks |
| PROC_RowId | varchar |  |  | NO | - |
| PROC_SupplyTime | double |  |  | SI | SupplyTime |
| PROC_SupplyTimeUnit | varchar |  |  | SI | SupplyTimeUnit |
| Q01Q1 | - |  |  | SI | Date |
| Q01Q10 | - |  |  | SI | Procedure |
| Q01Q2 | - |  |  | SI | Time |
| Q01Q3 | - |  |  | SI | Procedure |
| Q01Q4 | - |  |  | SI | Indication |
| Q01Q5 | - |  |  | SI | Benefits and risks explained to patient |
| Q01Q6 | - |  |  | SI | Discussed procedure with mother |
| Q01Q7 | - |  |  | SI | Consent obtained |
| Q01Q8 | - |  |  | SI | Discussed procedure with mother |
| Q01Q9 | - |  |  | SI | Consent obtained |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*