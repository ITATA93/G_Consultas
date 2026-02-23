# lab.HI_HistDayBookVisAcc

**Schema:** lab
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIVAC_ParRef | varchar | PK |  | NO | HI_HistDayBookVisit Parent Reference |
| HIVAC_AccessionNo | varchar |  |  | NO | Accession No |
| HIVAC_AnatomicalSiteFT | varchar |  |  | SI | Anatomical Site FT |
| HIVAC_AnatomicalSite_DR | varchar |  | FK | SI | Anatomical Site |
| HIVAC_CalcAccession | varchar |  |  | SI | Accession |
| HIVAC_CalcLabCode_DR | varchar |  | FK | SI | Lab Code |
| HIVAC_CalcSite | varchar |  |  | SI | Day Book Laboratory Site |
| HIVAC_CalcTestSets | varchar |  |  | SI | Tests |
| HIVAC_CalcYear | varchar |  |  | SI | Year |
| HIVAC_Comments | varchar |  |  | SI | Comments |
| HIVAC_ConsentToCCR | varchar |  |  | SI | Consent To CCR |
| HIVAC_MethodOfCollection_DR | varchar |  | FK | SI | Method Of Collection DR |
| HIVAC_PathologistMacro_DR | varchar |  | FK | SI | Macro Pathologist DR |
| HIVAC_PathologistMicro_DR | varchar |  | FK | SI | Micro Pathologist DR |
| HIVAC_RetainSample | varchar |  |  | SI | Retain Sample |
| HIVAC_Review | varchar |  |  | SI | To Review |
| HIVAC_RowId | varchar |  |  | NO | - |
| HIVAC_Site_DR | varchar |  | FK | SI | Cut-Up Site_DR |
| HIVAC_SpecialistRegistrar_DR | varchar |  | FK | SI | Specialist Registrar DR |
| HIVAC_SpecimenUnlabelled | varchar |  |  | SI | Specimen Unlabelled |
| HIVAC_Specimen_DR | varchar |  | FK | SI | Specimen |
| HIVAC_TCode_DR | varchar |  | FK | SI | TCode |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*