# TC_hmf_Message_HS_Community.EnrollmentRequest

**Schema:** TC_hmf_Message_HS_Community
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Encuentro**. Episodios de atención.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AssigningAuthority | varchar |  |  | SI | - |
| CommunicationPreference | integer |  |  | SI | - |
| Email | varchar |  |  | SI | - |
| MPIID | varchar |  |  | SI | - |
| MRN | varchar |  |  | SI | - |
| MobilePhone | varchar |  |  | SI | - |
| Mode | varchar |  |  | NO | - |
| Passphrase | varchar |  |  | SI | - |
| PhoneProvider | varchar |  |  | SI | - |
| PreferredCommunicationLanguageCode | varchar |  |  | SI | - |
| PreferredUILanguageCode | varchar |  |  | SI | - |
| ProxyOnly | bit |  |  | SI | - |
| _User | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*