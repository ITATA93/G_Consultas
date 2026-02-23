# lab.BB_AntibodyRegister

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANTRG_RowId | varchar | PK |  | NO | - |
| ANTRG_AntigenDetected | varchar |  |  | SI | Antigen Detected |
| ANTRG_ClinicallySignificant | varchar |  |  | SI | Clinically Significant |
| ANTRG_Date | date |  |  | SI | Date |
| ANTRG_DonorID | varchar |  |  | SI | Donor ID |
| ANTRG_Episode_DR | varchar |  | FK | SI | Episode |
| ANTRG_Result | varchar |  |  | SI | Result |
| ANTRG_ResultCode_DR | varchar |  | FK | SI | Result Code DR |
| ANTRG_Sequence | varchar |  |  | NO | Sequence |
| ANTRG_TestItem_Comment_DR | varchar |  | FK | SI | Test Item Comment DR |
| ANTRG_TestItem_Result_DR | varchar |  | FK | SI | Test Item Result DR |
| ANTRG_TestSet_DR | varchar |  | FK | SI | Des Ref TestSet |
| ANTRG_Time | time |  |  | SI | Time |
| ANTRG_Type | varchar |  |  | NO | Type |
| ANTRG_User_DR | varchar |  | FK | SI | User |
| ANTRG_VisitTest_DR | varchar |  | FK | SI | Visit Test DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*