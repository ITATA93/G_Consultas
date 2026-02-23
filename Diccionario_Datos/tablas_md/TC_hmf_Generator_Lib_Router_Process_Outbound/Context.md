# TC_hmf_Generator_Lib_Router_Process_Outbound.Context

**Schema:** TC_hmf_Generator_Lib_Router_Process_Outbound
**Columnas:** 21
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
| ErrorList | varchar |  |  | SI | - |
| GatewayReceivingApplication | varchar |  |  | SI | - |
| GatewayReceivingFacility | varchar |  |  | SI | - |
| Iterator | varchar |  |  | SI | - |
| OpArray | varchar |  |  | SI | - |
| Operation | varchar |  |  | SI | - |
| SDAReceivingApplication | varchar |  |  | SI | - |
| SDAReceivingFacility | varchar |  |  | SI | - |
| SendToGateway | bit |  |  | SI | - |
| allCallNames | varchar |  |  | SI | - |
| callArray | varchar |  |  | SI | - |
| callIterator | varchar |  |  | SI | - |
| callName | varchar |  |  | SI | - |
| callResponse | bigint |  |  | SI | - |
| gwResponse | bigint |  |  | SI | - |
| responseTimeout | varchar |  |  | SI | - |
| syncTimedOut | bit |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*