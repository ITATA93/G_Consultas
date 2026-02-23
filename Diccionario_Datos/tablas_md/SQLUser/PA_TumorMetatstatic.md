# SQLUser.PA_TumorMetatstatic

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MET_ParRef | bigint | PK |  | NO | PA_Tumor Parent Reference |
| MET_AbstractedFrom | varchar |  |  | SI | AbstractedFrom |
| MET_Childsub | double |  |  | NO | Childsub |
| MET_MetastaticSite | varchar |  |  | SI | Metastatic Site |
| MET_Metastatic_DR | bigint |  | FK | SI | Des Ref ICD |
| MET_RowId | varchar |  |  | NO | - |
| MET_SourceDate | date |  |  | SI | SourceDate |
| MET_UpdateDate | date |  |  | SI | UpdateDate |
| MET_UpdateTime | time |  |  | SI | UpdateTime |
| MET_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| MET_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*