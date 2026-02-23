# SQLUser.PA_PendingRequest

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PENDREQ_RowId | bigint | PK |  | NO | - |
| PENDREQ_Appointment_DR | varchar |  | FK | SI | Des Ref RBAppointment |
| PENDREQ_Date | date |  |  | SI | Date |
| PENDREQ_DeletionFlag | varchar |  |  | SI | DeletionFlag |
| PENDREQ_Loc_DR | bigint |  | FK | SI | Des Ref PACWard |
| PENDREQ_MRTypes | varchar |  |  | SI | MRTypes |
| PENDREQ_PAADM_DR | bigint |  | FK | SI | Des Ref PAAdm |
| PENDREQ_RequestStatus | varchar |  |  | SI | RequestStatus |
| PENDREQ_RequestType | varchar |  |  | SI | RequestType |
| PENDREQ_WaitListAdm_DR | varchar |  | FK | SI | Des Ref PACWaitingListType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*