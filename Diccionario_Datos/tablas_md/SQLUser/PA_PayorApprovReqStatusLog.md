# SQLUser.PA_PayorApprovReqStatusLog

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STLOG_ParRef | bigint | PK |  | NO | PA_PayorApprovalRequest Parent Reference |
| STLOG_AmendInitiator | varchar |  |  | SI | Approval Request Amending Initiator |
| STLOG_ApprReqStat_DR | bigint |  | FK | SI | Des Ref BLCApprovalRequestStatus |
| STLOG_ApprovReqDate | date |  |  | SI | Approval Request Date |
| STLOG_Childsub | double |  |  | NO | Childsub |
| STLOG_Initiator | varchar |  |  | SI | Approval Request Initiator |
| STLOG_RowId | varchar |  |  | NO | - |
| STLOG_UpdateDate | date |  |  | SI | Update Date |
| STLOG_UpdateHospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| STLOG_UpdateTime | time |  |  | SI | Update Time |
| STLOG_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*