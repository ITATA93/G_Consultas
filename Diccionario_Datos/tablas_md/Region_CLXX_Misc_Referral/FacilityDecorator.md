# Region_CLXX_Misc_Referral.FacilityDecorator

**Schema:** Region_CLXX_Misc_Referral
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AllowReferralInfoReq | bit |  |  | SI | Indica si el establecimiento puede contestar un pe... |
| AllowSkipLEMatch | bit |  |  | SI | Indica si el establecimiento permite saltar la est... |
| AllowSkipMap | bit |  |  | SI | - |
| DefaultSpecialtyService | varchar |  |  | SI | En la UI, se elige desde la User.RBCService.
wl.W... |
| Facility | bigint |  |  | NO | - |
| PrimaryPeerReviewDoneInTC | bit |  |  | SI | - |
| RecReferralsEnabled | bit |  |  | SI | - |
| SecondaryPeerReviewDoneInTC | bit |  |  | SI | - |
| SendReferralsEnabled | bit |  |  | SI | - |
| System | bigint |  |  | SI | Referencia a Systema al cual el hospital está asoc... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*