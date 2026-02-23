# Tools_DrugUpload_Variation.Downloads

**Schema:** Tools_DrugUpload_Variation
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ConfigurationDR | bigint |  | FK | NO | Property that declares which Configuration this is... |
| DownloadDateTime | timestamp |  |  | SI | Start of download |
| DownloadStatus | integer |  |  | SI | Status for that Download Instance simply number (s... |
| UsedConfiguration | varchar |  |  | SI | Properties used history - internal use only (JSON ... |
| VariationEnd | timestamp |  |  | SI | Download Variation "TO" - if supported by vendor, ... |
| VariationStart | timestamp |  |  | SI | Download Variation "FROM" (Empty if full download) |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*