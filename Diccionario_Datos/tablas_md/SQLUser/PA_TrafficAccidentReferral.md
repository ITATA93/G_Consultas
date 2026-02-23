# SQLUser.PA_TrafficAccidentReferral

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TARF_ParRef | bigint | PK |  | NO | PA_TrafficAccident Parent Reference |
| TARF_Childsub | double |  |  | NO | Childsub |
| TARF_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| TARF_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| TARF_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| TARF_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| TARF_ProviderType_DR | bigint |  | FK | SI | Referral Provider Type |
| TARF_ReferralReason | varchar |  |  | SI | Referral Reason |
| TARF_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*