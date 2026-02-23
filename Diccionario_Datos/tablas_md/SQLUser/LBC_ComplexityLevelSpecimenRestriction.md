# SQLUser.LBC_ComplexityLevelSpecimenRestriction

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCLSR_ParRef | bigint | PK |  | NO | Parent LBCComplexityLevel |
| ChildQ02DR | - |  |  | SI | Child Reference: Embryos |
| LBCCLSR_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCCLSR_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCCLSR_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCCLSR_CreatedDate | date |  |  | SI | Created Date |
| LBCCLSR_CreatedTime | time |  |  | SI | Created Time |
| LBCCLSR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCLSR_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCCLSR_RowID | varchar |  |  | NO | - |
| LBCCLSR_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCCLSR_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCCLSR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCLSR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCLSR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q09Q1 | - |  |  | SI | <50% surviving |
| Q09Q2 | - |  |  | SI | 51-99% surviving |
| Q09Q3 | - |  |  | SI | 100% surviving |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*