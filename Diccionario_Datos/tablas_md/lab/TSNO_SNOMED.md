# lab.TSNO_SNOMED

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TSNO_ROWID | varchar | PK |  | NO | - |
| TSNO_ALPHAUPSynonym | varchar |  |  | SI | ALPHAUP Synonym |
| TSNO_ALPHAUPSynonym2 | varchar |  |  | SI | ALPHAUP Synonym 2 |
| TSNO_ALPHAUPSynonym3 | varchar |  |  | SI | ALPHAUP Synonym 3 |
| TSNO_Class | varchar |  |  | SI | Class |
| TSNO_Code | varchar |  |  | NO | Code |
| TSNO_Description | varchar |  |  | SI | Description |
| TSNO_ICD10_DR | varchar |  | FK | SI | ICD10 code DR |
| TSNO_IUB | varchar |  |  | SI | IUB code |
| TSNO_Specimen_DR | varchar |  | FK | SI | Specimen DR |
| TSNO_Synonym | varchar |  |  | SI | Synonym |
| TSNO_Synonym2 | varchar |  |  | SI | Synonym 2 |
| TSNO_Synonym3 | varchar |  |  | SI | Synonym 3 |
| TSNO_Template | varchar |  |  | SI | Word Template |
| TSNO_Type_DR | varchar |  | FK | SI | Type DR |
| TSNO_WordTemplate | varchar |  |  | SI | RTF Template |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*