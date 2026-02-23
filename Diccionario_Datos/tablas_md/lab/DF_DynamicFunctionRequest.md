# lab.DF_DynamicFunctionRequest

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DFR_RowID | varchar | PK |  | NO | - |
| DFR_Closed | varchar |  |  | SI | Closed |
| DFR_Date | date |  |  | NO | Date |
| DFR_DateClosed | date |  |  | SI | Date Closed |
| DFR_Debtor_DR | varchar |  | FK | NO | Debtor DR |
| DFR_DynamicFunction_DR | varchar |  | FK | NO | Dynamic Function DR |
| DFR_Remarks | varchar |  |  | SI | Remarks |
| DFR_Time | time |  |  | NO | Time |
| DFR_TimeClosed | time |  |  | SI | Time Closed |
| DFR_UserClosed | varchar |  |  | SI | User Closed |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*