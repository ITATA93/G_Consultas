# SQLUser.PA_PayorApprovGroupReqStatusLog

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STLOG_ParRef | bigint | PK |  | NO | PA_PayorApprovalGroupRequest Parent Reference |
| STLOG_ApprBatchReqStatus_DR | bigint |  | FK | SI | Des Ref BLCApprGroupRequestStatus |
| STLOG_Childsub | double |  |  | NO | Childsub |
| STLOG_RequestDate | date |  |  | SI | Request Date |
| STLOG_ResponseDate | date |  |  | SI | Response Date |
| STLOG_RowId | varchar |  |  | NO | - |
| STLOG_UpdateDate | date |  |  | SI | Update Date |
| STLOG_UpdateHospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| STLOG_UpdateTime | time |  |  | SI | Update Time |
| STLOG_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*