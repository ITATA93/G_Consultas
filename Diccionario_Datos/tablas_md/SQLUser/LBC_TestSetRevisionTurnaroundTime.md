# SQLUser.LBC_TestSetRevisionTurnaroundTime

**Schema:** SQLUser
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRTT_ParRef | bigint | PK |  | NO | Parent Reference LBCTestSetRevisionDR |
| ChildQ52DR | - |  |  | SI | Child Reference: Abdomen Alterado |
| LBCTSRTT_AlertTurnaroundTime | integer |  |  | SI | Alert Turnaround Time (minutes)  |
| LBCTSRTT_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTSRTT_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRTT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRTT_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRTT_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRTT_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRTT_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRTT_MaxOutlierTime | integer |  |  | SI | Max Outlier Time  (minutes) |
| LBCTSRTT_Priority_DR | bigint |  | FK | SI | Priority |
| LBCTSRTT_RowID | varchar |  |  | NO | - |
| LBCTSRTT_Sequence | double |  |  | SI | Rule Sequence |
| LBCTSRTT_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTSRTT_Species_DR | bigint |  | FK | SI | Species |
| LBCTSRTT_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRTT_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRTT_SubjectType_DR | bigint |  | FK | SI | Subject Type |
| LBCTSRTT_TargetTurnaroundTime | integer |  |  | SI | Target Turnaround Time (minutes) |
| Q42Q1 | - |  |  | SI | Ritmo |
| Q42Q2 | - |  |  | SI | Ruidos |
| Q42Q3 | - |  |  | SI | Soplos |
| Q42Q4 | - |  |  | SI | Grado (soplos) |
| Q42Q5 | - |  |  | SI | Ubicación |
| Q42Q6 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*