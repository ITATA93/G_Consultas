# SQLUser.LBC_TestSetRevisionDefaultAliquot

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRDA_ParRef | bigint | PK |  | NO | Parent Revision |
| ChildQ35DR | - |  |  | SI | Child Reference: Estructura y dinámica familiar de... |
| LBCTSRDA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRDA_Container_DR | bigint |  | FK | NO | Container |
| LBCTSRDA_DateFrom | date |  |  | NO | Start date the record is active |
| LBCTSRDA_DateTo | date |  |  | SI | Last date the record is active  |
| LBCTSRDA_LabSite_DR | bigint |  | FK | SI | Lab Site Filter |
| LBCTSRDA_RowID | varchar |  |  | NO | - |
| LBCTSRDA_SpecimenAliquot_DR | varchar |  | FK | NO | Specimen Aliquot |
| LBCTSRDA_Specimen_DR | bigint |  | FK | NO | Specimen |
| Q27Q1 | - |  |  | SI | Objetivos del estudio |
| Q27Q2 | - |  |  | SI | Fecha |
| Q27Q3 | - |  |  | SI | Síntesis de la historia familiar |
| Q27Q4 | - |  |  | SI | Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*