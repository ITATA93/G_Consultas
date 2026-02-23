# SQLUser.PAC_SnomedTernaryAssociation

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOTAC_RowId | bigint | PK |  | NO | - |
| ChildQ19DR | - |  |  | SI | Child Reference: Range of movement: passive |
| Q18Q1 | - |  |  | SI | Body location |
| Q18Q2 | - |  |  | SI | Range of movement: active |
| Q18Q3 | - |  |  | SI | Altered active ROM: degrees |
| Q18Q4 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNOTAC_AssoType | varchar |  |  | NO | Association Type |
| SNOTAC_Code | varchar |  |  | NO | Code |
| SNOTAC_ConceptX_DR | bigint |  | FK | NO | SNOMED Concept X DR |
| SNOTAC_ConceptY_DR | bigint |  | FK | NO | SNOMED Concept Y DR |
| SNOTAC_ConceptZ_DR | bigint |  | FK | NO | SNOMED Concept Z DR |
| SNOTAC_DateFrom | date |  |  | NO | Effective date for the record |
| SNOTAC_DateTo | date |  |  | SI | Last day the record is active |
| SNOTAC_Desc | varchar |  |  | NO | Description |
| SNOTAC_SDesc | varchar |  |  | SI | Short Description |
| SNOTAC_TermsX_DR | bigint |  | FK | NO | SNOMED TERMS X DR  |
| SNOTAC_TermsY_DR | bigint |  | FK | NO | SNOMED TERMS Y DR |
| SNOTAC_TermsZ_DR | bigint |  | FK | NO | SNOMED TERMS Z DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*