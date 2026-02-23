# SQLUser.PA_PregHistoryofCare

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOC_ParRef | bigint | PK |  | NO | PA_Pregnancy Parent Reference |
| HOC_AntenatalCare_DR | bigint |  | FK | SI | Des Ref PACTypeOfAntenatalCare |
| HOC_BookingChangeManag_DR | bigint |  | FK | SI | Des Ref PACBookingChangeManag |
| HOC_BookingChangePlace_DR | bigint |  | FK | SI | Des Ref PACBookingChangePlace |
| HOC_CareChangeReason_DR | bigint |  | FK | SI | Des Ref PAC_AntenatalCareChangeReason |
| HOC_Childsub | double |  |  | NO | Childsub |
| HOC_Consultant_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| HOC_DelivPlanManagement_DR | bigint |  | FK | SI | Des Ref PACDelivPlanManag |
| HOC_GestationAtTimeOfChange | varchar |  |  | SI | GestationAtTimeOfChange  |
| HOC_IntendedDelivPlace_DR | bigint |  | FK | SI | Des Ref PACDeliveryPlace |
| HOC_MidCommTeam_DR | bigint |  | FK | SI | Des Ref PACMidwifeCommTeam |
| HOC_ReasTypeAntenatalCare | varchar |  |  | SI | CareProviderName
Property HOCCareProviderName As ... |
| HOC_RowId | varchar |  |  | NO | - |
| HOC_UpdateDate | date |  |  | SI | UpdateDate   |
| HOC_UpdateTime | time |  |  | SI | UpdateTime   |
| HOC_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*