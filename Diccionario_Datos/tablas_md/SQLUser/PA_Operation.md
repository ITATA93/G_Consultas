# SQLUser.PA_Operation

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPER_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| OPER_Childsub | double |  |  | NO | Childsub |
| OPER_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| OPER_Date | date |  |  | SI | Operation Date |
| OPER_DateEntered | date |  |  | SI | Date Entered |
| OPER_Desc | varchar |  |  | SI | Description |
| OPER_Doctor_DR | varchar |  | FK | SI | Des Ref Doctor |
| OPER_DuratDays | double |  |  | SI | Duration in Days |
| OPER_DuratMonth | double |  |  | SI | Duration in Month |
| OPER_DuratYear | double |  |  | SI | Duration in Year |
| OPER_EndDate | date |  |  | SI | EndDate |
| OPER_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| OPER_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| OPER_InActive | varchar |  |  | SI | InActive |
| OPER_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| OPER_NoHistoryOf | varchar |  |  | SI | NoHistoryOf |
| OPER_ORCOper_DR | bigint |  | FK | SI | Des Ref to ORCOper |
| OPER_OnsetDate | date |  |  | SI | Onset Date |
| OPER_RowId | varchar |  |  | NO | - |
| OPER_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| OPER_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| OPER_TimeEntered | time |  |  | SI | Time Entered |
| OPER_UpdateDate | date |  |  | SI | UpdateDate |
| OPER_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| OPER_UpdateTime | time |  |  | SI | UpdateTime |
| OPER_UpdateUser_DR | bigint |  | FK | SI | Des REf User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*