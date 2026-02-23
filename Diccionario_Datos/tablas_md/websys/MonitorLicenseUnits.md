# websys.MonitorLicenseUnits

**Schema:** websys
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| Active | integer |  |  | SI | Active is the time in seconds the UserId has been ... |
| CSPCon | integer |  |  | SI | CSPCon is the number of CSP sessions open to this ... |
| Connects | integer |  |  | SI | Connects is the number of connections to this Cach... |
| Grace | integer |  |  | SI | Grace is the amount of time this license unit will... |
| ID | varchar |  |  | NO | - |
| InactivityTimeout | integer |  |  | SI | InactivityTimeout (minutes) is the value configure... |
| LU | integer |  |  | SI | LU is the number of License Units consumed on this... |
| LicenseString | varchar |  |  | SI | License string is only used for Cache 5.0 - no lon... |
| MaxCon | integer |  |  | SI | MaxCon is the maximum number of concurrent connect... |
| Type | varchar |  |  | SI | The Type field contains the login type and is one ... |
| UserId | varchar |  |  | SI | The UserId field contains the License Login UserId... |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*