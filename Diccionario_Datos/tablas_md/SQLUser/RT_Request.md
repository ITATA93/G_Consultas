# SQLUser.RT_Request

**Schema:** SQLUser
**Columnas:** 35
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTREQ_RowId1 | varchar | PK |  | NO | - |
| RTREQ_AckRequest | varchar |  |  | SI | Acknowledge requests |
| RTREQ_Appt_DR | varchar |  | FK | SI | Des Ref Appt |
| RTREQ_Area_DR | bigint |  | FK | SI | Des Ref Area |
| RTREQ_Automatic | varchar |  |  | SI | Automatic |
| RTREQ_BatchID | varchar |  |  | SI | BatchID |
| RTREQ_Comments | varchar |  |  | SI | Comments |
| RTREQ_ContactPerson | varchar |  |  | SI | Contact Person |
| RTREQ_Date | date |  |  | NO | Request Date |
| RTREQ_Doctor_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| RTREQ_FHResident_DR | bigint |  | FK | SI | Des Ref MicroArea |
| RTREQ_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| RTREQ_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| RTREQ_MRNo_DR | bigint |  | FK | NO | Des Ref to RTMAS |
| RTREQ_MatchRTREV_DR | varchar |  | FK | SI | Matching field |
| RTREQ_MicroArea_DR | bigint |  | FK | SI | Des Ref MicroArea |
| RTREQ_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| RTREQ_PagerNo | varchar |  |  | SI | Pager No |
| RTREQ_PatientAttending | varchar |  |  | SI | Patient Attending |
| RTREQ_PullingDate | date |  |  | SI | Pulling Date |
| RTREQ_ReasonForMove_DR | bigint |  | FK | SI | Des Ref ReasonForMove |
| RTREQ_ReqLoc_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| RTREQ_ReqReason_DR | bigint |  | FK | SI | Request Reason |
| RTREQ_ReqTelExt | varchar |  |  | SI | ReqTelExt |
| RTREQ_ReqTelNo | varchar |  |  | SI | Request Telephone Number |
| RTREQ_ReqUser_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| RTREQ_RespLoc_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| RTREQ_RespUser_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| RTREQ_RowId | varchar |  |  | NO | RTREQ Row ID |
| RTREQ_Segment_DR | bigint |  | FK | SI | Des Ref Segment |
| RTREQ_Session_DR | varchar |  | FK | SI | Des Ref Session |
| RTREQ_Status | varchar |  |  | NO | Request Status |
| RTREQ_Time | time |  |  | NO | Request Time |
| RTREQ_TransDate | date |  |  | NO | Transcation Date |
| RTREQ_TransTime | time |  |  | SI | Transaction Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*