# Report_JReport.Configuration

**Schema:** Report_JReport
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CredentialsToLogi | varchar |  |  | SI | Credentials to connect to JReport |
| CredentialsToTrak | varchar |  |  | SI | Credentials to connect to TrakCare database |
| Encoding | varchar |  |  | SI | Encoding code used to generate report |
| FilesVersion | varchar |  |  | SI | JReport Files version |
| ImageAccessTokenTimeout | integer |  |  | SI | Timeout for image access Tokens  |
| ImageWebServerBaseURL | varchar |  |  | SI | Image web server location |
| JSPTimeout | integer |  |  | SI | Timeout for JSP connection |
| JavaHotVMNumPingThreads | integer |  |  | SI | JReportServer Java HotVM number of Ping Threads |
| JavaHotVMNumThreads | integer |  |  | SI | JReportServer Java HotVM number of Threads |
| JavaHotVMPingPort | integer |  |  | SI | JReportServer Java App HotVM ping port |
| JavaHotVMPort | integer |  |  | SI | JReportServer Java App HotVM port |
| PathToConvertLog | varchar |  |  | SI | Path to conversion log |
| PathToJavaConverterScript | varchar |  |  | SI | Path to converter script |
| PathToJavaRenderApp | varchar |  |  | SI | Path to TrakCare Logi Report Java app script |
| PrefixResFolder | varchar |  |  | SI | JReport Resource Prefix |
| RenderJSPSSLConfig | varchar |  |  | SI | Use SSL to connect to JSP |
| RenderViaJSP | varchar |  |  | SI | Indicate if server-side printing use only JSP page... |
| RootLogiReportFolder | varchar |  |  | SI | Path to Logi Report root folder |
| ServerIPAddress | varchar |  |  | SI | JReport server IP address |
| ServerJDBCURL | varchar |  |  | SI | URL to JDBC connection to JReport |
| ServerVersion | varchar |  |  | SI | JReport Server version |
| SetRefererJSP | varchar |  |  | SI | Indicate that the referer should be set when conne... |
| URLToLogiReportServer | varchar |  |  | SI | URL to JReport Server |
| UsesExcelFormatXLSX | varchar |  |  | SI | Indicate if use Excel XLSX format for rendering of... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*