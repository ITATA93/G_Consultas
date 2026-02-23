# SQLUser.MR_SubjectFindings

**Schema:** SQLUser
**Columnas:** 36
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBF_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| Q06Q1 | - |  |  | SI | Date |
| Q06Q2 | - |  |  | SI | Time |
| Q06Q3 | - |  |  | SI | Anesthesia |
| Q06Q4 | - |  |  | SI | Layer |
| Q06Q5 | - |  |  | SI | Material |
| Q06Q6 | - |  |  | SI | Note |
| Q06Q7 | - |  |  | SI | Size |
| Q06Q8 | - |  |  | SI | No. |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SUBF_ApproxOnsetDate | varchar |  |  | SI | ApproxOnsetDate |
| SUBF_BodySite_DR | bigint |  | FK | SI | Des Ref BodySite |
| SUBF_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| SUBF_Childsub | double |  |  | NO | Childsub |
| SUBF_Consult_DR | varchar |  | FK | SI | Des Ref Consult |
| SUBF_Date | date |  |  | SI | Date |
| SUBF_DiagnosSignSymptom_DR | bigint |  | FK | SI | Des Ref DiagnosSignSymptom |
| SUBF_DurationNum | varchar |  |  | SI | DurationNum |
| SUBF_DurationUnit | varchar |  |  | SI | DurationUnit |
| SUBF_EndDate | date |  |  | SI | EndDate |
| SUBF_EndTime | time |  |  | SI | EndTime |
| SUBF_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| SUBF_HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| SUBF_HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| SUBF_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| SUBF_OnsetDate | date |  |  | SI | OnsetDate |
| SUBF_OnsetTime | time |  |  | SI | OnsetTime |
| SUBF_RTFNotes | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| SUBF_RowId | varchar |  |  | NO | - |
| SUBF_Severity_DR | bigint |  | FK | SI | Des Ref Severity |
| SUBF_Text | varchar |  |  | SI | Text |
| SUBF_Time | time |  |  | SI | Time |
| SUBF_UpdateDate | date |  |  | SI | Update Date |
| SUBF_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| SUBF_UpdateTime | time |  |  | SI | Update Time |
| SUBF_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*