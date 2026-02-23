# lab.HI_HistDBVABlockOrder

**Schema:** lab
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIVAO_ParRef | varchar | PK |  | NO | HI_HistDayBookVisitAccessBlock Parent Reference |
| HIVAO_Checker_DR | varchar |  | FK | SI | Checker DR |
| HIVAO_Completed | varchar |  |  | SI | Completed |
| HIVAO_DBTest_Result | varchar |  |  | SI | DB Test - Result |
| HIVAO_DBTest_vtsRID_DR | varchar |  | FK | SI | DB Test - vts RID |
| HIVAO_Date | date |  |  | SI | Date |
| HIVAO_DateCompleted | date |  |  | SI | Date Completed |
| HIVAO_DateQCChange | date |  |  | SI | Date of QC Change |
| HIVAO_EPTest_TestItem_DR | varchar |  | FK | SI | EP Test - Result field DR |
| HIVAO_EPTest_vtsRID_DR | varchar |  | FK | SI | EP Test - vts RID |
| HIVAO_FailureCodes_DR | varchar |  | FK | SI | Failure Code DR |
| HIVAO_Level | varchar |  |  | SI | Level |
| HIVAO_MultipleStatus | varchar |  |  | SI | Multiple Status |
| HIVAO_Order | varchar |  |  | NO | Order |
| HIVAO_ParentProcedureOrder_DR | varchar |  | FK | SI | Parent Procedure Order DR |
| HIVAO_Pieces | double |  |  | SI | No Pieces |
| HIVAO_PrintedLabel | varchar |  |  | SI | Printed Label |
| HIVAO_ProcedureCode | varchar |  |  | SI | Procedure Code |
| HIVAO_ProcedureComments | varchar |  |  | SI | Procedure Comment |
| HIVAO_ProcedureLocation_DR | varchar |  | FK | SI | Procedure Location DR |
| HIVAO_ProcedureStatus_DR | varchar |  | FK | SI | Procedure Status DR |
| HIVAO_Remarks | varchar |  |  | SI | Remarks |
| HIVAO_ResponsibleUserGroup_DR | bigint |  | FK | SI | User Group DR - User Grou Responsible |
| HIVAO_ResponsibleUser_DR | varchar |  | FK | SI | User DR - User Responsible |
| HIVAO_Result | varchar |  |  | SI | Result |
| HIVAO_RowId | varchar |  |  | NO | - |
| HIVAO_StainCode | varchar |  |  | SI | Stain Code |
| HIVAO_StoragePosition_DR | varchar |  | FK | SI | Storage Position DR |
| HIVAO_Time | time |  |  | SI | Time |
| HIVAO_UserCompleted_DR | varchar |  | FK | SI | User Completed DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*