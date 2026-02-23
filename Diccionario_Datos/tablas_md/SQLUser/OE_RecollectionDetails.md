# SQLUser.OE_RecollectionDetails

**Schema:** SQLUser
**Columnas:** 34
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RECDET_RowId | bigint | PK |  | NO | - |
| ChildQ70DR | - |  |  | SI | Child Reference: Muscle Power |
| Q69Q1 | - |  |  | SI | Joint / Motion |
| Q69Q2 | - |  |  | SI | AROM Left |
| Q69Q3 | - |  |  | SI | PROM Left |
| Q69Q4 | - |  |  | SI | AROM Right |
| Q69Q5 | - |  |  | SI | PROM Right |
| Q69Q6 | - |  |  | SI | End Feel |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RECDET_Chemistry | varchar |  |  | SI | Chemistry   |
| RECDET_Citometry | varchar |  |  | SI | Citometry    |
| RECDET_ClottedSample | varchar |  |  | SI | ClottedSample   |
| RECDET_Comments | varchar |  |  | SI | Comments  |
| RECDET_CultureConfirmation | varchar |  |  | SI | CultureConfirmation   |
| RECDET_Date | date |  |  | SI | Date |
| RECDET_Genetic | varchar |  |  | SI | Genetic    |
| RECDET_HLA | varchar |  |  | SI | HLA    |
| RECDET_Haematology | varchar |  |  | SI | Haematology    |
| RECDET_Immunology | varchar |  |  | SI | Immunology    |
| RECDET_IncorrectCollection | varchar |  |  | SI | IncorrectCollection   |
| RECDET_IncorrectIdentification | varchar |  |  | SI | IncorrectIdentification   |
| RECDET_IncorrectSample | varchar |  |  | SI | IncorrectSample   |
| RECDET_InsufficientSample | varchar |  |  | SI | InsufficientSample  |
| RECDET_LaboratoryName | varchar |  |  | SI | LaboratoryName    |
| RECDET_Microbiology | varchar |  |  | SI | Mircobiology    |
| RECDET_MolecularBiology | varchar |  |  | SI | MolecularBiology    |
| RECDET_OrderMistake | varchar |  |  | SI | OrderMistake   |
| RECDET_PhoneNumber | varchar |  |  | SI | PhoneNumber     |
| RECDET_ReasonForVariance_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason |
| RECDET_RefLaboratory | varchar |  |  | SI | RefLaboratory    |
| RECDET_ResultConfirmation | varchar |  |  | SI | ResultConfirmation   |
| RECDET_SampleContamination | varchar |  |  | SI | SampleContamination   |
| RECDET_TalkTo | varchar |  |  | SI | TalkTo     |
| RECDET_Time | time |  |  | SI | Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*