# SQLUser.PA_ProblemCancerStage

**Schema:** SQLUser
**Columnas:** 36
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STAGE_ParRef | varchar | PK |  | NO | PA_Problem Parent Reference |
| STAGE_AfterPathExam | varchar |  |  | SI | After pathological exam |
| STAGE_CancerSite_DR | bigint |  | FK | SI | Main cancer site |
| STAGE_CancerType_DR | bigint |  | FK | SI | Cancer Type |
| STAGE_CareProvider_DR | varchar |  | FK | SI | Update Care Provider |
| STAGE_CertaintyOfV | double |  |  | SI | C (Certainty of V) |
| STAGE_Childsub | double |  |  | NO | Childsub |
| STAGE_Desc | varchar |  |  | SI | Cancer Stage description either based on default T... |
| STAGE_ECOG_DR | bigint |  | FK | SI | [DEPRECATED]TC-39565: Eliminating ECOG Status[/DEP... |
| STAGE_Extranodal | varchar |  |  | SI | Extranodal |
| STAGE_HistologicalGrade | double |  |  | SI | G (Histological grade) |
| STAGE_LymphNode_DR | varchar |  | FK | SI | N (Lymph Node) |
| STAGE_LymphaticInvasion | double |  |  | SI | L (Lymphatic vessel invasion) |
| STAGE_MAfterAdjuv | varchar |  |  | SI | M After Adjuv |
| STAGE_MAfterPath | varchar |  |  | SI | M After Path |
| STAGE_MRecurrent | varchar |  |  | SI | M Recurrent |
| STAGE_Metastasis_DR | varchar |  | FK | SI | M (Metastasis) |
| STAGE_NAfterAdjuv | varchar |  |  | SI | N After Adjuv |
| STAGE_NAfterPath | varchar |  |  | SI | N After Path |
| STAGE_NRecurrent | varchar |  |  | SI | N Recurrent |
| STAGE_OtherStage_DR | varchar |  | FK | SI | Other Stage |
| STAGE_ResidualTumourStage | double |  |  | SI | R (Residual Tumour stage) |
| STAGE_RowId | varchar |  |  | NO | - |
| STAGE_SFlag | varchar |  |  | SI | S flag |
| STAGE_SerumMarkers | double |  |  | SI | S (Elevation of Serum Tumour Markers) |
| STAGE_StageDate | date |  |  | SI | Stage Date |
| STAGE_StageTime | time |  |  | SI | Stage Time |
| STAGE_SymptomsPresent | varchar |  |  | SI | B symptoms present |
| STAGE_TAfterAdjuv | varchar |  |  | SI | T After Adjuv |
| STAGE_TAfterPath | varchar |  |  | SI | T After Path |
| STAGE_TNMDescriptor | varchar |  |  | SI | TNM Descriptor either based on default TNM descrip... |
| STAGE_TRecurrent | varchar |  |  | SI | T Recurrent |
| STAGE_TumourSize_DR | varchar |  | FK | SI | T (Tumour size) |
| STAGE_Type | varchar |  |  | SI | Cancer Stage Type |
| STAGE_VenousInvasion | double |  |  | SI | V (Venous invasion) |
| STAGE_XFlag | varchar |  |  | SI | X flag |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*