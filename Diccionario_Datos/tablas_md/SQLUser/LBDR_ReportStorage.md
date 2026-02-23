# SQLUser.LBDR_ReportStorage

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRRS_RowID | bigint | PK |  | NO | - |
| ChildQ82DR | - |  |  | SI | Child Reference: Estado de Ánimo / Afecto |
| LBDRRS_Courier_DR | bigint |  | FK | SI | Courier |
| LBDRRS_EpisodeReportingInterface_DR | varchar |  | FK | SI | Episode Reporting Interface |
| LBDRRS_Episode_DR | bigint |  | FK | SI | Link to Lab Episode ID |
| LBDRRS_GenerationDate | date |  |  | SI | Generation Date of the Report |
| LBDRRS_GenerationTime | time |  |  | SI | Generation Time of the Report |
| LBDRRS_GenerationType | varchar |  |  | SI | Generation Type (Default: Courier) |
| LBDRRS_PDFStream | longvarbinary |  |  | SI | Report Data in PDF format |
| LBDRRS_RecipCareProvider_DR | varchar |  | FK | SI | Care Provider Recipient |
| LBDRRS_RecipLocation_DR | bigint |  | FK | SI | Location Recipient |
| LBDRRS_RecipReferringClinic_DR | bigint |  | FK | SI | Referring Clinic Recipient, only exists if Recipie... |
| LBDRRS_RecipReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor Recipient |
| LBDRRS_RecipThirdParty_DR | bigint |  | FK | SI | Third Party Recipient. |
| Q81Q1 | - |  |  | SI | Características |
| Q81Q2 | - |  |  | SI | Evaluación |
| Q81Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*