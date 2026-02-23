# Tools_DataMover_Process_GetOnePatient.Context

**Schema:** Tools_DataMover_Process_GetOnePatient
**Columnas:** 25
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
| AllMaternityRefsResolved | bit |  |  | SI | - |
| ErrorMessage | varchar |  |  | SI | - |
| MapName | varchar |  |  | SI | - |
| MapVersion | varchar |  |  | SI | - |
| MaternityReloadRespID | varchar |  |  | SI | - |
| MaternityReloadResponseIDs | varchar |  |  | SI | - |
| MaternityResolveRefsResponse | bigint |  |  | SI | - |
| PatientDataRespID | varchar |  |  | SI | - |
| PendingToReload | bit |  |  | SI | - |
| RegistrationNumber | varchar |  |  | SI | - |
| ReloadErrorMsg | varchar |  |  | SI | - |
| ReloadErrorsIndex | varchar |  |  | SI | - |
| ReloadPatientErrorMsgCount | integer |  |  | SI | - |
| ReloadRegNumber | varchar |  |  | SI | - |
| TrakProcessGUID | varchar |  |  | SI | - |
| matIndex | integer |  |  | SI | - |
| patientOKResponsesIDs | varchar |  |  | SI | - |
| patientResolveNOKResponse | bigint |  |  | SI | - |
| patientResolveResponse | bigint |  |  | SI | - |
| processLogIndex | integer |  |  | SI | - |
| remoteClientHostName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*