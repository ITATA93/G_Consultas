# lab.EP_VisitDayBook

**Schema:** lab
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISDB_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISDB_Accession | varchar |  |  | SI | Accession |
| VISDB_AnatomicalSiteFT | varchar |  |  | SI | Anatomical Site FT |
| VISDB_AnatomicalSite_DR | varchar |  | FK | SI | Anatomical Site DR |
| VISDB_Comments | varchar |  |  | SI | Level |
| VISDB_DBAccession_DR | varchar |  | FK | SI | DB Accession DR |
| VISDB_DBLaboratory_DR | varchar |  | FK | SI | DB Laboratory DR |
| VISDB_DBSiteOfOrigin_DR | varchar |  | FK | SI | DB Site Of Origin DR |
| VISDB_MethodOfCollection_DR | varchar |  | FK | SI | Method Of Collection DR |
| VISDB_PrintDBHistory | varchar |  |  | SI | Print DB History |
| VISDB_PrintLabels | varchar |  |  | SI | Print Labels |
| VISDB_RowID | varchar |  |  | NO | - |
| VISDB_Sequence | numeric |  |  | NO | Sequence |
| VISDB_SpecimenGroup_DR | varchar |  | FK | SI | Specimen Group DR |
| VISDB_Specimen_DR | varchar |  | FK | SI | Specimen DR |
| VISDB_StandardCutUp | varchar |  |  | SI | Standard CutUp |
| VISDB_TCode_DR | varchar |  | FK | SI | T-Code DR |
| VISDB_Tests | varchar |  |  | SI | Tests |
| VISDB_xxx2 | varchar |  |  | SI | DB Stain DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*