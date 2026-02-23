# Tools_Upload_OrderSet.Document

**Schema:** Tools_Upload_OrderSet
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CreatedDate | date |  |  | SI | Date this record was created |
| CreatedTime | time |  |  | SI | Time this record was created |
| DataSourceDR | bigint |  | FK | SI | - |
| LinkedDocDR | bigint |  | FK | SI | Reference for an Document representing a new Versi... |
| MapClassName | varchar |  |  | SI | - |
| ReReadDate | date |  |  | SI | Date this record was re-read |
| ReReadTime | time |  |  | SI | Time this record was re-read |
| SourceFileName | varchar |  |  | SI | Source file name of xml file data was loaded from |
| Vendor | varchar |  |  | SI | Properties from Vendor |
| VendorDocCategory | varchar |  |  | SI | - |
| VendorDocDateTime | varchar |  |  | SI | - |
| VendorDocIdentifier | varchar |  |  | SI | - |
| VendorDocName | varchar |  |  | SI | - |
| VendorDocPatType | varchar |  |  | SI | Adult, Pediatric etc. |
| VendorDocRevision | varchar |  |  | SI | - |
| VendorDocSetType | varchar |  |  | SI | - |
| VendorDocVersion | varchar |  |  | SI | - |
| WebsysDocumentDR | bigint |  | FK | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*