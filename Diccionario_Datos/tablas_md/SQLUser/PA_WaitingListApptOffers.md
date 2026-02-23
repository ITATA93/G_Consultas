# SQLUser.PA_WaitingListApptOffers

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APTOF_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| APTOF_Appointment_DR | varchar |  | FK | SI | Des Ref Appointment |
| APTOF_ApptCancelDate | date |  |  | SI | ApptCancelDate |
| APTOF_ApptDate | date |  |  | SI | ApptDate |
| APTOF_ApptTransferDate | date |  |  | SI | ApptTransferDate |
| APTOF_Childsub | double |  |  | NO | Childsub |
| APTOF_Date | date |  |  | SI | Date |
| APTOF_Outcome_DR | bigint |  | FK | SI | Des Ref Outcome |
| APTOF_RBAS_DR | varchar |  | FK | SI | Des Ref RBAS |
| APTOF_ResponseComments | varchar |  |  | SI | ResponseComments |
| APTOF_ResponseDate | date |  |  | SI | ResponseDate |
| APTOF_RowId | varchar |  |  | NO | - |
| APTOF_WLOfferType_DR | bigint |  | FK | SI | Des Ref WLOfferType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*