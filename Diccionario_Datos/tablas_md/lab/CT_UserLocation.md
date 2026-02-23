# lab.CT_UserLocation

**Schema:** lab
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTUSL_RowId | varchar | PK |  | NO | - |
| CTUSL_AccreditationNumber | varchar |  |  | SI | Accreditation Number |
| CTUSL_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTUSL_Address | varchar |  |  | SI | Address |
| CTUSL_Address1 | varchar |  |  | SI | Address 1 |
| CTUSL_Address2 | varchar |  |  | SI | Address 2 |
| CTUSL_Address3_Suburb | varchar |  |  | SI | Suburb |
| CTUSL_Address4_State_DR | varchar |  | FK | SI | State |
| CTUSL_Address5_PostCode | varchar |  |  | SI | PostCode |
| CTUSL_Code | varchar |  |  | NO | Code |
| CTUSL_DefaultNID | varchar |  |  | SI | Default National ID |
| CTUSL_Desc | varchar |  |  | SI | Description |
| CTUSL_Destination_DR | varchar |  | FK | SI | Des Ref Print Destination |
| CTUSL_DisplaySequence | double |  |  | SI | Display Sequence |
| CTUSL_DocCourierRun_DR | varchar |  | FK | SI | Default Courier Run for Doctors |
| CTUSL_Fax | varchar |  |  | SI | Fax |
| CTUSL_LocCourierRun_DR | varchar |  | FK | SI | Default Courier Run for Location |
| CTUSL_MoveDirectory | varchar |  |  | SI | Database Movements Directory |
| CTUSL_PFforBatchEntry | varchar |  |  | SI | Patient Fields for Batch Entry |
| CTUSL_Phone | varchar |  |  | SI | Phone |
| CTUSL_RegionCode | varchar |  |  | SI | Region Code |
| CTUSL_StructuredCode | varchar |  |  | SI | Structured code |
| CTUSL_StructuredCodeLength | double |  |  | SI | Structured code length |
| CTUSL_StructuredCodeLevel | varchar |  |  | SI | Structured code level |
| CTUSL_UniqueSite | varchar |  |  | SI | Unique Site |
| CTUSL_UnixMoveDirectory | varchar |  |  | SI | Database Movements Directory (Unix) |
| CTUSL_WebReportFooter | varchar |  |  | SI | Web Report Footer |
| CTUSL_email | varchar |  |  | SI | Email |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*