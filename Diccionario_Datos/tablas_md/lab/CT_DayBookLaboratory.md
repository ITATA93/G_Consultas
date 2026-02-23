# lab.CT_DayBookLaboratory

**Schema:** lab
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDBL_RowId | varchar | PK |  | NO | - |
| CTDBL_AutoBlockNumberCreation | varchar |  |  | SI | Automatic Block Number Creation |
| CTDBL_CheckSingleAccessionPerTS | varchar |  |  | SI | Check Single Accession Per TS |
| CTDBL_DefaultCCR | varchar |  |  | SI | Default CCR |
| CTDBL_DefaultDBReview | varchar |  |  | SI | Default DayBook Review |
| CTDBL_DefaultPathologists | varchar |  |  | SI | Default Pathologists |
| CTDBL_DefaultPieces | double |  |  | SI | Default Pieces |
| CTDBL_DefaultPrintDBHistory | varchar |  |  | SI | Default Print DBHistory |
| CTDBL_DefaultPrintLabels | varchar |  |  | SI | Default Print Labels |
| CTDBL_DefaultStCutUp | varchar |  |  | SI | Default Standard CutUp |
| CTDBL_Department_DR | varchar |  | FK | SI | Des Ref Department |
| CTDBL_EnterAnatomicalSite | varchar |  |  | SI | Enter Anatomical Site |
| CTDBL_EnterBlock | varchar |  |  | SI | Enter Block |
| CTDBL_EnterSiteOfOrigin | varchar |  |  | SI | Enter Site of Origin |
| CTDBL_EnterTCode | varchar |  |  | SI | Enter TCode |
| CTDBL_EnterTest | varchar |  |  | SI | Enter Test |
| CTDBL_EnterVCCR | varchar |  |  | SI | Enter VCCR |
| CTDBL_LabCode | varchar |  |  | NO | LabCode |
| CTDBL_LabName | varchar |  |  | SI | Lab Name |
| CTDBL_LastNumber | varchar |  |  | SI | Last Number |
| CTDBL_NonSystemSequence | varchar |  |  | SI | Non System Sequence |
| CTDBL_PatternMatch | varchar |  |  | SI | Pattern match |
| CTDBL_ResetAccessionNumbers | varchar |  |  | SI | Reset Accession Numbers |
| CTDBL_Specimen_DR | varchar |  | FK | SI | Default Specimen |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*