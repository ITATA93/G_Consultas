# SQLUser.PA_ObservationLink

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBSLINK_RowId | bigint | PK |  | NO | - |
| OBSLINK_MRPictures_DR | varchar |  | FK | SI | Des Ref MRPictures |
| OBSLINK_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| OBSLINK_PatBillGrpChargeObs_DR | varchar |  | FK | SI | Des Ref ARPatBillGroupChargeObserv |
| OBSLINK_PatBillObs_DR | varchar |  | FK | SI | Des Ref ARPatBillObservation |
| OBSLINK_PayorApprGrpReqObs_DR | varchar |  | FK | SI | Des Ref PAPayorApprovGroupReqObservation |
| OBSLINK_PayorApprReqObs_DR | varchar |  | FK | SI | Des Ref PAPayorApprovReqObservation |
| OBSLINK_PersonPictures_DR | varchar |  | FK | SI | Des Ref PAPersonPictures |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*