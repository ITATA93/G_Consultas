# TC_hmf_Deploy.TokenStore

**Schema:** TC_hmf_Deploy
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFTKN_Credentials | varchar |  |  | SI | Ens.Config.Credentials ID in TC namespace - links ... |
| HMFTKN_DateFrom | date |  |  | SI | Token valid start date |
| HMFTKN_DateTo | date |  |  | SI | Token expiry date |
| HMFTKN_Desc | varchar |  |  | NO | Token freetext description  |
| HMFTKN_ExternalInterfaceID | varchar |  |  | SI | FreeText Interface Identifier for external (non-HM... |
| HMFTKN_InterfaceDR | varchar |  | FK | SI | HMF Deployed interface supported by this token |
| HMFTKN_OauthClientID | varchar |  |  | SI | OAuth ClientID for %SYS namespace - this is the ID... |
| HMFTKN_Token | varchar |  |  | NO | Token string value  |
| HMFTKN_X509ID | varchar |  |  | SI | X509 Id for %SYS namepsace - this is the ID value ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*