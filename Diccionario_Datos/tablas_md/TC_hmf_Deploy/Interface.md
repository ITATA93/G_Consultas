# TC_hmf_Deploy.Interface

**Schema:** TC_hmf_Deploy
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFDEPINT_ParRef | bigint | PK |  | NO | ProductionConfig Parent Reference |
| HMFDEPINT_AdapterInterfaceDR | varchar |  | FK | SI | DesRef To Adapter used to generate Interface |
| HMFDEPINT_Code | varchar |  |  | NO | Deployed gateway interface code
Used for the gene... |
| HMFDEPINT_Desc | varchar |  |  | SI | Deployed gateway interface description
Used for t... |
| HMFDEPINT_Direction | varchar |  |  | SI | Message direction - either Outbound, Inbound, Quer... |
| HMFDEPINT_Enabled | bit |  |  | SI | Interface enabled flag |
| HMFDEPINT_ExternalCredentials | varchar |  |  | SI | SOAP credentials to connect to external system for... |
| HMFDEPINT_ExternalMPI | bit |  |  | SI | Interface ExterrnalMPI flag |
| HMFDEPINT_FilePath | varchar |  |  | SI | Filepath for file interface |
| HMFDEPINT_FormatDR | bigint |  | FK | SI | Des Ref to message format eg. HL7 - each deployed ... |
| HMFDEPINT_IP | varchar |  |  | SI | IP address for server running deployed gateway int... |
| HMFDEPINT_InterfaceCodingSystem_DR | bigint |  | FK | SI | Coding system supported |
| HMFDEPINT_InterfaceWorkbenchDR | bigint |  | FK | SI | DesRef To IWB |
| HMFDEPINT_Port | varchar |  |  | SI | Port for deployed gateway interface - if protocol ... |
| HMFDEPINT_Protocol | varchar |  |  | SI | Deployed gateway interface message transport proto... |
| HMFDEPINT_ReceivingApplication | varchar |  |  | SI | Receiving application - used in HMF router rules t... |
| HMFDEPINT_ReceivingFacility | varchar |  |  | SI | Receiving facility - used in HMF router rules to d... |
| HMFDEPINT_RuleDR | varchar |  | FK | SI | Des Ref to message rule <br>
Applied to generated... |
| HMFDEPINT_SendingApplication | varchar |  |  | SI | Sending application - applied to outbound message ... |
| HMFDEPINT_SendingFacility | varchar |  |  | SI | Sending facility - applied to outbound message if ... |
| HMFDEPINT_URLPath | varchar |  |  | SI | HTTP application path for SOAP/REST interfaces 
e... |
| HMFDEPINT_VersionDR | varchar |  | FK | SI | Des Ref to message version supported for message f... |
| HMFDEPINT_WSClient | varchar |  |  | SI | WS client class |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*