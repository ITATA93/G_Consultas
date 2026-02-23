# SQLUser.LBC_TestSetRevisionClassificationRule

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRCR_ParRef | bigint | PK |  | NO | - |
| ChildQ27DR | - |  |  | SI | Child Reference: Información general |
| LBCTSRCR_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTSRCR_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical site |
| LBCTSRCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRCR_Container_DR | bigint |  | FK | SI | Container |
| LBCTSRCR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRCR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRCR_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRCR_RowID | varchar |  |  | NO | - |
| LBCTSRCR_Sequence | numeric |  |  | SI | Priority  Sequence |
| LBCTSRCR_SnomedTerm_DR | bigint |  | FK | SI | SNOMED Code |
| LBCTSRCR_Specimen_DR | bigint |  | FK | SI | Specimen |
| Q03Q1 | - |  |  | SI | Fecha |
| Q03Q2 | - |  |  | SI | Resultados |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*