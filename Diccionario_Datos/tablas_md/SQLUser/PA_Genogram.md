# SQLUser.PA_Genogram

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAGEN_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| PAGEN_CanvasX | varchar |  |  | SI | SVG Canvas position X |
| PAGEN_CanvasY | varchar |  |  | SI | SVG Canvas position X |
| PAGEN_Childsub | double |  |  | NO | Childsub |
| PAGEN_CreatedByUser_DR | bigint |  | FK | SI | Des Ref User |
| PAGEN_CreatedDate | date |  |  | SI | CreatedDate |
| PAGEN_CreatedHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAGEN_CreatedTime | time |  |  | SI | CreatedTime |
| PAGEN_Document | bigint |  |  | SI | Document 
JSON string for diagram |
| PAGEN_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PAGEN_Family_DR | varchar |  | FK | SI | Des Ref PAFamily |
| PAGEN_Results | varchar |  |  | SI | Results |
| PAGEN_RowId | varchar |  |  | NO | - |
| PAGEN_UpdateDate | date |  |  | SI | UpdateDate |
| PAGEN_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| PAGEN_UpdateTime | time |  |  | SI | UpdateTime |
| PAGEN_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q56Q1 | - |  |  | SI | Scope type |
| Q56Q2 | - |  |  | SI | Scope number |
| Q56Q3 | - |  |  | SI | Insertion time |
| Q56Q4 | - |  |  | SI | Removal time |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*