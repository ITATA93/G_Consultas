# SQLUser.NRC_Problem

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NRCP_RowID | bigint | PK |  | NO | - |
| NRCP_Code | varchar |  |  | NO | Code  |
| NRCP_CodeTableTags | varchar |  |  | SI | List of code table tags |
| NRCP_DateFrom | date |  |  | NO | Effective date for the record |
| NRCP_DateTo | date |  |  | SI | Last day the record is active |
| NRCP_Definition | varchar |  |  | SI | Free Text Definition is a Long Description |
| NRCP_Desc | varchar |  |  | NO | Description |
| NRCP_Owner | varchar |  |  | SI | Owner |
| NRCP_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| NRCP_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| NRCP_Type | varchar |  |  | SI | Nursing Problem Type, standardType |
| Q40Q1 | - |  |  | SI | Baby number |
| Q40Q2 | - |  |  | SI | Fetal heart baseline |
| Q40Q3 | - |  |  | SI | 3 accelerators |
| Q40Q4 | - |  |  | SI | Unreactive |
| Q40Q5 | - |  |  | SI | Variability |
| Q40Q6 | - |  |  | SI | Decelerations |
| Q40Q7 | - |  |  | SI | Difficult to interpret |
| Q40Q8 | - |  |  | SI | Acceptable |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*