# TC_hmf_Adapter.Interface

**Schema:** TC_hmf_Adapter
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFADAPINT_ParRef | bigint | PK |  | NO | ProductionConfig Parent Reference |
| HMFADAPINT_Code | varchar |  |  | NO | Adapter interface code
Used for the generated Gat... |
| HMFADAPINT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HMFADAPINT_DeployInterfaceDR | varchar |  | FK | SI | DesRef To Deployed Interface used to generate adap... |
| HMFADAPINT_Desc | varchar |  |  | SI | Adapter interface description
Used for the genera... |
| HMFADAPINT_Direction | varchar |  |  | SI | Message direction - either Outbound, Inbound, Quer... |
| HMFADAPINT_ExternalCredentials | varchar |  |  | SI | SOAP credentials to connect to external system for... |
| HMFADAPINT_FilePath | varchar |  |  | SI | Filepath for file interface |
| HMFADAPINT_FormatDR | bigint |  | FK | SI | Des Ref to message format eg. HL7 - each deployed ... |
| HMFADAPINT_IP | varchar |  |  | SI | IP address for server running deployed gateway int... |
| HMFADAPINT_IWBLinkDR | bigint |  | FK | SI | Link to IWB Interface |
| HMFADAPINT_InterfaceCodingSystem_DR | bigint |  | FK | SI | Coding system supported |
| HMFADAPINT_Port | varchar |  |  | SI | Port for deployed gateway interface - if protocol ... |
| HMFADAPINT_Protocol | varchar |  |  | SI | Adapter interface message transport protocol |
| HMFADAPINT_ReceivingApplication | varchar |  |  | SI | Receiving application - used in HMF router rules t... |
| HMFADAPINT_ReceivingFacility | varchar |  |  | SI | Receiving facility - used in HMF router rules to d... |
| HMFADAPINT_RuleDR | varchar |  | FK | SI | Des Ref to message rule <br>
Applied to generated... |
| HMFADAPINT_SendingApplication | varchar |  |  | SI | Sending application - applied to outbound message ... |
| HMFADAPINT_SendingFacility | varchar |  |  | SI | Sending facility - applied to outbound message if ... |
| HMFADAPINT_System | varchar |  |  | SI | System |
| HMFADAPINT_URLPath | varchar |  |  | SI | HTTP application path for SOAP/REST interfaces 
e... |
| HMFADAPINT_VersionDR | varchar |  | FK | SI | Des Ref to message version supported for message f... |
| HMFADAPINT_WSClient | varchar |  |  | SI | WS client class |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*