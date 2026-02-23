# Tools_DrugUpload.Conversion

**Schema:** Tools_DrugUpload
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ATCforAllergyGroup | varchar |  |  | SI | ATC Levels used for Allery Group (Italian Drug Dat... |
| Credential | varchar |  |  | SI | Optional IRIS/Ensemble Credentials (User) to be us... |
| DrgFormPackSplit | varchar |  |  | SI | Multiple Pack for DrgForm (Farmadati XML) |
| DrgMastDM | varchar |  |  | SI | Conversion splits DrgMast for Manufacturer & Distr... |
| FastTrack | varchar |  |  | SI | Flag if the conversion should extract the GUIDs fo... |
| IncludeForeignDrugs | varchar |  |  | SI | Flag if the conversion should include foreign drug... |
| PathFrom | varchar |  |  | NO | Path From (Files from Vendor) |
| PathTo | varchar |  |  | NO | PathTo (Files for TrakCare) |
| ReloadCSV | varchar |  |  | SI | Flag if the Data from CSV files should be reloaded... |
| ReloadData | varchar |  |  | SI | Flag if the Data from the files should be reloaded... |
| RestAppID | varchar |  |  | SI | REST API AppID |
| RestAppKey | varchar |  |  | SI | REST API Parameter |
| RestAppPath | varchar |  |  | SI | REST API Path |
| RestAppServer | varchar |  |  | SI | REST API Parameter
Server inclusive protocol http... |
| SchemaVersion | varchar |  |  | SI | Version of SQL Schema to be used for conversion (N... |
| SinglePack | varchar |  |  | SI | Flag if the conversion should use the Single Pack ... |
| UseTallMan | varchar |  |  | SI | Flag if the conversion should use TallMan (NZULM) |
| Vendor | varchar |  |  | NO | Property that declares which Vendor this is saved ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*