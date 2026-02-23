# TC_hmf_Adapter.Production

**Schema:** TC_hmf_Adapter
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Impresión/Reportes**. Generación de documentos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFADAP_Code | varchar |  |  | NO | Adapter production entry code <br>
Used for the g... |
| HMFADAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HMFADAP_CodeVersion | varchar |  |  | SI | Adapter archive version |
| HMFADAP_CreatedDate | date |  |  | SI | Created Date |
| HMFADAP_CreatedTime | time |  |  | SI | Created Time |
| HMFADAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HMFADAP_CustomExportStream | longvarchar |  |  | SI | Custom package Export stream |
| HMFADAP_DateFrom | date |  |  | SI | Date From |
| HMFADAP_DateTo | date |  |  | SI | Date To |
| HMFADAP_DeployProductionDR | bigint |  | FK | SI | DesRef To DeployedProduction used to generate adap... |
| HMFADAP_Desc | varchar |  |  | SI | Adapter production entry description <br>
Used fo... |
| HMFADAP_ExportStream | longvarchar |  |  | SI | Generated package Export stream |
| HMFADAP_GatewayCredentials | varchar |  |  | SI | Gateway SOAP credentials |
| HMFADAP_IncludeExportStream | longvarchar |  |  | SI | Include Export stream |
| HMFADAP_Owner | varchar |  |  | SI | Owner |
| HMFADAP_PathToGateway | varchar |  |  | SI | Path to gateway  |
| HMFADAP_System | varchar |  |  | SI | System created |
| HMFADAP_UpdateDate | date |  |  | SI | Updated Date |
| HMFADAP_UpdateTime | time |  |  | SI | Updated Time |
| HMFADAP_UpdateUserDR | bigint |  | FK | SI | Updated User |
| HMFADAP_Version | integer |  |  | SI | Adapter archive version |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*