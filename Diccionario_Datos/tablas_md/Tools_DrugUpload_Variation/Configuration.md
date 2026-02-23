# Tools_DrugUpload_Variation.Configuration

**Schema:** Tools_DrugUpload_Variation
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ContinueAfterError | varchar |  |  | SI | Continue (Y) or Stop (N) downloads if one file/con... |
| Credential | varchar |  |  | SI | Optional IRIS/Ensemble Credentials (User) to be us... |
| DownloadBase | varchar |  |  | SI | Folder used for downloads, vendor dependend subfol... |
| OverwriteFiles | varchar |  |  | SI | Overwrite existing files / e.g. same day downloads... |
| PostDownload | varchar |  |  | SI | Optional: ClassMethod to be called after download ... |
| PreDownload | varchar |  |  | SI | Optional: ClassMethod to be called before download... |
| Vendor | varchar |  |  | NO | Property that declares which Vendor this is saved ... |
| WSPassword | varchar |  |  | SI | Webservice Password |
| WSProxyPassword | varchar |  |  | SI | Proxy server password |
| WSProxyPort | varchar |  |  | SI | Proxy server port if using a proxy to connect to w... |
| WSProxyServer | varchar |  |  | SI | Proxy server host name if using a proxy to connect... |
| WSProxyUser | varchar |  |  | SI | Proxy server user |
| WSSSLConfiguration | varchar |  |  | SI | IRIS - SSL Configuration to be used  |
| WSUser | varchar |  |  | SI | Webservice User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*