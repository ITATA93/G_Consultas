# Region_CLXX_Misc_Referral.Document

**Schema:** Region_CLXX_Misc_Referral
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Criteria | varchar |  |  | SI | - |
| DestinationFacility | bigint |  |  | NO | - |
| DestinationLocation | bigint |  |  | NO | - |
| OriginatingFacility | bigint |  |  | SI | - |
| OriginatingSpecialty | bigint |  |  | SI | - |
| Referral | bigint |  |  | SI | This will only exist if the referral came through ... |
| ReferralDocNumber | varchar |  |  | SI | - |
| ReferralNationalCode1 | varchar |  |  | SI | Código devuelto por el RNLE |
| ReferralNationalCode2 | varchar |  |  | SI | Folio SIGGES |
| Request | bigint |  |  | NO | This will always be present. Doesn't matter if thi... |
| Response | bigint |  |  | SI | Response that Trakcare send to Ensemble, only the ... |
| RoutedByReferralMap | bit |  |  | SI | - |
| WaitingListEntry | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*