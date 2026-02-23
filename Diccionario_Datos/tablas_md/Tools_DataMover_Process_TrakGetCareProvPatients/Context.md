# Tools_DataMover_Process_TrakGetCareProvPatients.Context

**Schema:** Tools_DataMover_Process_TrakGetCareProvPatients
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Contexto**. Datos de contexto de sesión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %LastError | varchar |  |  | SI | This holds last exception |
| %LastFault | varchar |  |  | SI | This holds the last thrown fault |
| %Process | bigint |  |  | SI | This holds the reference to the process object |
| checkCTAndLoadStatus | varchar |  |  | SI | - |
| checkCTGUIDsMissingGUIDs | varchar |  |  | SI | - |
| checkCTGUIDsPatientError | varchar |  |  | SI | - |
| checkCTGUIDsPatientResult | varchar |  |  | SI | - |
| checkCTGUIDsToLoad | varchar |  |  | SI | - |
| checkNOKAndLoadStatus | varchar |  |  | SI | - |
| clearDBErrorMessage | varchar |  |  | SI | - |
| countPatientsNoImported | integer |  |  | SI | - |
| countPatientsToImport | integer |  |  | SI | - |
| currentSyncOK | bit |  |  | SI | - |
| endDownloadStatus | varchar |  |  | SI | - |
| getCTDataXMLLoadStatus | varchar |  |  | SI | - |
| getCTDataXMLResponse | bigint |  |  | SI | - |
| getPatientCallNames | varchar |  |  | SI | - |
| gotPatientDataMsgError | varchar |  |  | SI | - |
| guidInfo | bigint |  |  | SI | - |
| hasMissingGUID | bit |  |  | SI | - |
| importPatientMsgError | varchar |  |  | SI | - |
| importPatientNumber | varchar |  |  | SI | - |
| importResultOnePatMsg | varchar |  |  | SI | - |
| index | varchar |  |  | SI | - |
| initialProcessGUID | varchar |  |  | SI | - |
| loadCTErrorCount | integer |  |  | SI | - |
| loadCTErrorStatus | varchar |  |  | SI | - |
| loadCTInfo | varchar |  |  | SI | - |
| loadNOKErrorCount | integer |  |  | SI | - |
| loadOneResponseID | varchar |  |  | SI | - |
| loadPatientsStatus | varchar |  |  | SI | - |
| mapName | varchar |  |  | SI | - |
| mapVersion | varchar |  |  | SI | - |
| missingGUIDIndex | varchar |  |  | SI | - |
| missingGuidByPatient | varchar |  |  | SI | - |
| missingGuidPatientList | varchar |  |  | SI | - |
| noImportPatientNumber | varchar |  |  | SI | - |
| patientERRORResponseIndex | varchar |  |  | SI | - |
| patientERRORResponsesIDs | varchar |  |  | SI | - |
| patientNumbers | varchar |  |  | SI | - |
| patientOKResponseIds | varchar |  |  | SI | - |
| patientOKResponseIndex | varchar |  |  | SI | - |
| patientResolveCTGuids | bit |  |  | SI | - |
| patientResponseID | varchar |  |  | SI | - |
| patientStreamIDs | varchar |  |  | SI | - |
| patientsListString | varchar |  |  | SI | - |
| pendingCTGuids | varchar |  |  | SI | - |
| processLogIndex | integer |  |  | SI | - |
| remoteClientHostName | varchar |  |  | SI | - |
| requireSyncPatients | bit |  |  | SI | - |
| syncCallsString | varchar |  |  | SI | - |
| syncPatientsNumbers | varchar |  |  | SI | - |
| syncPatientsResultMsg | varchar |  |  | SI | - |
| tmpCallName | varchar |  |  | SI | - |
| tmpPatientLoadReq | bigint |  |  | SI | - |
| tmpPatientNumber | varchar |  |  | SI | - |
| trakProcessGUID | varchar |  |  | SI | - |
| trakSessionID | varchar |  |  | SI | - |
| waitCallNames | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*