# Tools_DrugUpload_Variation.TableStatus

**Schema:** Tools_DrugUpload_Variation
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AddedRecords | integer |  |  | SI | Number of records merged (Insert) - only after Var... |
| ConvertedDateTime | timestamp |  |  | SI | TimeStamps for Processing |
| DataFileName | varchar |  |  | SI | Path&FileName unzip |
| DownloadDR | bigint |  | FK | NO | - |
| DownloadDateTime | timestamp |  |  | SI | TimeStamp |
| FilteredRecords | integer |  |  | SI | Number of records after filter -> Updated from Var... |
| MergedDateTime | timestamp |  |  | SI | TimeStamps for Processing |
| MergedRecords | integer |  |  | SI | Number of records merged (Update) - only after Var... |
| NumberOfRecords | integer |  |  | NO | Numer of records received |
| PageFiles | integer |  |  | SI | Number of Pages/Files  |
| TableName | varchar |  |  | NO | Table / Vendor File Name |
| UnZipOK | bit |  |  | SI | UnZip Status  |
| VendorCode | varchar |  |  | NO | Vendor Core |
| XMLLoadDateTime | timestamp |  |  | SI | TimeStamps for Processing |
| XMLVariationDel | integer |  |  | SI | Numer of records received via XML (not filtered) f... |
| XMLVariationIns | integer |  |  | SI | Numer of records received via XML (not filtered) f... |
| XMLVariationUpd | integer |  |  | SI | Numer of records received via XML (not filtered) f... |
| ZipFileName | varchar |  |  | SI | Path&FileName zip - if zip is used |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*