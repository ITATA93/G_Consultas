# TC_hmf_Deploy.ProductionConfig

**Schema:** TC_hmf_Deploy
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Configuración del módulo.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFDEPPRD_Adapter | bit |  |  | SI | Adapter reload flag |
| HMFDEPPRD_AdapterDR | bigint |  | FK | SI | DesRef To Adapter used to generate production |
| HMFDEPPRD_Code | varchar |  |  | NO | Deployed production entry code <br>
Used for the ... |
| HMFDEPPRD_CustomExportStream | longvarchar |  |  | SI | Custom package Export stream |
| HMFDEPPRD_Desc | varchar |  |  | SI | Deployed production entry description <br>
Used f... |
| HMFDEPPRD_Enabled | bit |  |  | SI | Enabled flag |
| HMFDEPPRD_ExportStream | longvarchar |  |  | SI | Generated package Export stream |
| HMFDEPPRD_ExternalMPI | bit |  |  | SI | Flag to indicate production is flagged as an exter... |
| HMFDEPPRD_GatewayCredentials | varchar |  |  | SI | Gateway SOAP credentials |
| HMFDEPPRD_GeneratedDate | date |  |  | SI | Records last date production was generated  |
| HMFDEPPRD_GeneratedStatus | varchar |  |  | SI | Records last status when production was generated  |
| HMFDEPPRD_GeneratedTime | time |  |  | SI | Records last time production was generated  |
| HMFDEPPRD_GeneratorLock | bit |  |  | SI | Flag to indicate production is locked cannot be re... |
| HMFDEPPRD_PathToGateway | varchar |  |  | SI | Path to gateway  |
| HMFDEPPRD_RegionFlag | bit |  |  | SI | Flag to indicate Region classes supported and will... |
| HMFDEPPRD_Sequence | integer |  |  | SI | Sequence <br>
When production configuration is up... |
| HMFDEPPRD_UpdateDate | date |  |  | SI | Update date |
| HMFDEPPRD_UpdateTime | time |  |  | SI | Update time |
| HMFDEPPRD_UpdateUserDR | bigint |  | FK | SI | Des Ref to update user |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*