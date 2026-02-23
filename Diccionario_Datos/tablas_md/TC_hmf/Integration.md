# TC_hmf.Integration

**Schema:** TC_hmf
**Columnas:** 53
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFINT_APIUser | bigint |  |  | SI | API User |
| HMFINT_AllowAddressCTUpdate | bit |  |  | SI | Flag to Allow the Address Code Table Updates |
| HMFINT_Authority | varchar |  |  | SI | Assigning Authority |
| HMFINT_AuthorityCode | varchar |  |  | SI | Assigning Authority Code |
| HMFINT_CodingStandard | varchar |  |  | SI | Coding Standard |
| HMFINT_DietOrderIgnoreMealType | bit |  |  | SI | Flag to ignore meal type requirement for outbound ... |
| HMFINT_DisableAPITINCLUDE | bit |  |  | SI | Flag to disable API TINCLUDE setting for building ... |
| HMFINT_DisableEncounterMatchForLocation | bit |  |  | SI | Flag to use block encounter matching for location |
| HMFINT_DisableEncounterUpdate | bit |  |  | SI | Flag to use block encounter updates from inbound m... |
| HMFINT_DisablePatientUpdate | bit |  |  | SI | Flag to use block demographic updates from inbound... |
| HMFINT_DisableSaveRetry | bit |  |  | SI | Flag to use block API save retry on error for inbo... |
| HMFINT_ERRORCUSTOMMETHOD | varchar |  |  | SI | Custom site specific error handling classmethod to... |
| HMFINT_EReferralEnabled | varchar |  |  | SI | If enabled indicete E-Referral processing for refe... |
| HMFINT_EnableSYSQAPI | bit |  |  | SI | Enable HMF-SYS Questionnaire API regenerate |
| HMFINT_Enabled | bit |  |  | SI | Enabled Flag |
| HMFINT_ExtSearchCustomFetchMethod | varchar |  |  | SI | TrakCare External Search Custom Fetch Method |
| HMFINT_ExtSearchCustomListMethod | varchar |  |  | SI | TrakCare External Search Custom List Method |
| HMFINT_ExternalDocSearchTarget | varchar |  |  | SI | TrakCare External Document Search Target Interface |
| HMFINT_ExternalHostName | varchar |  |  | SI | External Host Name |
| HMFINT_ExternalHostPort | varchar |  |  | SI | External Host Port |
| HMFINT_ExternalProviderSearchTarget | varchar |  |  | SI | TrakCare External Provider Search Target Interface |
| HMFINT_ExternalSearchTarget | varchar |  |  | SI | TrakCare External Search Target Interface |
| HMFINT_Facility | varchar |  |  | SI | Facility |
| HMFINT_FacilityCode | varchar |  |  | SI | Facility Code |
| HMFINT_GenerateInternalMRN | bit |  |  | SI | Flag to use internal generated MRN 
If flag set t... |
| HMFINT_HSRegistry | varchar |  |  | SI | TrakCare HIE Target Service Registry Entry |
| HMFINT_InboundCustomMethod | varchar |  |  | SI | Custom site specific inbound classmethod to be exe... |
| HMFINT_LabOrdCatList | varchar |  |  | SI | Lab order category - comma delimited list of codes... |
| HMFINT_LogLevel | varchar |  |  | SI | Logging Level  |
| HMFINT_MedOrdCatList | varchar |  |  | SI | Medication order category - comma delimited list o... |
| HMFINT_MedicationHistorySearchTarget | varchar |  |  | SI | TrakCare Medication History Search Interface |
| HMFINT_MultiThreadScheduler | bit |  |  | SI | HMF flag to enable MultiThread Scheduler for outbo... |
| HMFINT_NullHandlingFlag | bit |  |  | SI | Flag to enable active null handling for inbound HM... |
| HMFINT_OutboundCustomMethod | varchar |  |  | SI | Custom site specific outbound classmethod to be ex... |
| HMFINT_PAPERIDNumType | varchar |  |  | SI | If PAPERID used in TrakCare implementation allows ... |
| HMFINT_ProductionNS | varchar |  |  | SI | System Production namespace |
| HMFINT_ProfileSegmentData | varchar |  |  | SI | Custom Class to validate data for each SDA segment |
| HMFINT_QueryTimeOut | integer |  |  | SI | Set the timeout for Query Out Intefaces |
| HMFINT_RadOrdCatList | varchar |  |  | SI | Radiology order category - comma delimited list of... |
| HMFINT_RemoteDeploy | bit |  |  | SI | Deployment Flag |
| HMFINT_RouterCredentials | varchar |  |  | SI | Router Production SOAP Credentials |
| HMFINT_RouterPath | varchar |  |  | SI | Router Production Path |
| HMFINT_RouterRegenFlag | bit |  |  | SI | Router Regenerate flag |
| HMFINT_SMSTarget | varchar |  |  | SI | TrakCare SMS Target Interface |
| HMFINT_SchedulerQuerySize | integer |  |  | SI | HMF-SYS production scheduler service query pool si... |
| HMFINT_SystemCredentials | varchar |  |  | SI | System Production SOAP Credentials |
| HMFINT_SystemURL | varchar |  |  | SI | System Production URL  |
| HMFINT_Triggers | varchar |  |  | SI | Enabled Triggers |
| HMFINT_UpdateDate | date |  |  | SI | Update Date |
| HMFINT_UpdateProvinceWithState | bit |  |  | SI | Flag to update CTProvince with SDA State |
| HMFINT_UpdateTime | time |  |  | SI | Update Time |
| HMFINT_UpdateUser | varchar |  |  | SI | Des Ref Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*