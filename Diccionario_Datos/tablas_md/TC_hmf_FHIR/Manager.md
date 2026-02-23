# TC_hmf_FHIR.Manager

**Schema:** TC_hmf_FHIR
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFFHIRMGR_CTTransformClass | varchar |  |  | SI | FHIR CodeTable Transform Class |
| HMFFHIRMGR_CareProvSyncDate | varchar |  |  | SI | FHIR CareProv CodeTable Sync datetime $horlog stri... |
| HMFFHIRMGR_CustomDTLPackage | varchar |  |  | SI | Custom DTL Package |
| HMFFHIRMGR_DisableExternalID | bit |  |  | SI | FHIR requires a specific ID format for resource - ... |
| HMFFHIRMGR_DisableQueryLocalRepository | bit |  |  | SI | Disable Inbound FHIR Query using Local FHIR Reposi... |
| HMFFHIRMGR_EnableHMFService | bit |  |  | SI | Enable HMF-SYS FHIR Service for Inbound FHIR Reque... |
| HMFFHIRMGR_Enabled | bit |  |  | SI | Enabled Flag |
| HMFFHIRMGR_Format | varchar |  |  | SI | FHIR Format XML/JSON |
| HMFFHIRMGR_HMFSYSPath | varchar |  |  | SI | FHIR HMF-SYS URL Path Production REST Endpoint - h... |
| HMFFHIRMGR_InteractionsAPI | varchar |  |  | SI | API for FHIR Interactions class |
| HMFFHIRMGR_InteractionsStrategyAPI | varchar |  |  | SI | API for FHIR InteractionsStrategy class |
| HMFFHIRMGR_LocSyncDate | varchar |  |  | SI | FHIR Location CodeTable Sync datetime $horlog stri... |
| HMFFHIRMGR_Namespace | varchar |  |  | SI | FHIR Repository Production namespace |
| HMFFHIRMGR_PatientSyncDate | varchar |  |  | SI | FHIR Location CodeTable Sync datetime $horlog stri... |
| HMFFHIRMGR_ProfileSegmentData | varchar |  |  | SI | Custom Class to validate data for each SDA segment |
| HMFFHIRMGR_RemoteCredentials | varchar |  |  | SI | FHIR Remote Credentials |
| HMFFHIRMGR_RemoteDeploy | bit |  |  | SI | FHIR Repository Deployment Flag |
| HMFFHIRMGR_RemoteHost | varchar |  |  | SI | FHIR Remote Respoitory Host  |
| HMFFHIRMGR_RemotePath | varchar |  |  | SI | FHIR Remote Repository URL PathProduction Endpoint |
| HMFFHIRMGR_RemotePort | varchar |  |  | SI | FHIR Remote Repository Port  |
| HMFFHIRMGR_RemoteServiceRegistry | varchar |  |  | SI | FHIR Remote Service Registry Entry |
| HMFFHIRMGR_ServiceCredentials | varchar |  |  | SI | FHIR Production Credentials |
| HMFFHIRMGR_ServicePath | varchar |  |  | SI | FHIR Production Path |
| HMFFHIRMGR_ServiceRegistry | varchar |  |  | SI | FHIR Service Registry Entry |
| HMFFHIRMGR_SessionTimeout | integer |  |  | SI | TC FHIR Session Timeout for repository data
- def... |
| HMFFHIRMGR_TimeOut | integer |  |  | SI | Set the timeout for FHIR messages |
| HMFFHIRMGR_TransformClass | varchar |  |  | SI | FHIR Transform Class |
| HMFFHIRMGR_Triggers | varchar |  |  | SI | Enabled Triggers |
| HMFFHIRMGR_Version | varchar |  |  | SI | FHIR Version |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*