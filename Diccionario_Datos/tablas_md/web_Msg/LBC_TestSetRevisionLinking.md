# web_Msg.LBC_TestSetRevisionLinking

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRL_ClinicalConditions | varchar |  |  | SI | Clinical Condition(s) - may be multiple |
| LBCTSRL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRL_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRL_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRL_Interval | integer |  |  | SI | Interval |
| LBCTSRL_IntervalUnit | varchar |  |  | SI | Interval Unit  |
| LBCTSRL_LastSpecimen | varchar |  |  | SI | Last Sample Only |
| LBCTSRL_ParRef | bigint |  |  | SI | Parent Reference LBCTestSetRevisionDR |
| LBCTSRL_RowID | varchar |  |  | SI | - |
| LBCTSRL_SamePatient | varchar |  |  | SI | Same Patient |
| LBCTSRL_SameSpecimen | varchar |  |  | SI | Same Specimen |
| LBCTSRL_SameTestSet | varchar |  |  | SI | Same Test Set |
| LBCTSRL_Sequence | double |  |  | SI | Priority  Sequence |
| LBCTSRL_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRL_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRL_TestSets | varchar |  |  | SI | Test sets for link
List of possible test sets tha... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*