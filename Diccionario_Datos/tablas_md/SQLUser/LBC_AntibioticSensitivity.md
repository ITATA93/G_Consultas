# SQLUser.LBC_AntibioticSensitivity

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCASI_RowID | bigint | PK |  | NO | - |
| ChildQ17DR | - |  |  | SI | Child Reference: Carbohydrate ratio (grams/Unit) |
| LBCASI_AntibioticPanel_DR | bigint |  | FK | SI | Antibiotics Panel
Des Ref Antibiotics Panel |
| LBCASI_Antibiotic_DR | bigint |  | FK | NO | Antibiotic
Des Ref Antibiotics |
| LBCASI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCASI_ObjectReference | varchar |  |  | SI | - |
| LBCASI_OperandETest | varchar |  |  | SI | Operand E Test |
| LBCASI_OperandMIC | varchar |  |  | SI | Operand MIC |
| LBCASI_Operandmm | varchar |  |  | SI | Operand mm |
| LBCASI_Owner | varchar |  |  | SI | Owner |
| LBCASI_PathogenGroup_DR | bigint |  | FK | SI | Pathogen Group
Des Ref Antibiotics |
| LBCASI_Pathogen_DR | bigint |  | FK | SI | Pathogen
Des Ref Pathogen |
| LBCASI_ResultETest | varchar |  |  | SI | Result E Test |
| LBCASI_ResultMIC | varchar |  |  | SI | Result MIC  |
| LBCASI_Resultmm | varchar |  |  | SI | Result mm |
| LBCASI_Sensitivity_DR | bigint |  | FK | SI | Sensitivity |
| LBCASI_Type | varchar |  |  | SI | Type |
| Q14Q1 | - |  |  | SI | Time from |
| Q14Q2 | - |  |  | SI | Time to |
| Q14Q3 | - |  |  | SI | Units / hour |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*