# SQLUser.RT_MVTrans

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTMVT_RTMAV_ParRef | varchar | PK |  | NO | Des Ref to RTMAV |
| RTMVT_AddUser_DR | bigint |  | FK | SI | Des Ref to SSUser |
| RTMVT_BatchID | varchar |  |  | SI | BatchID |
| RTMVT_ChildSub | numeric |  |  | NO | RTMVT Childsub (Newkey) |
| RTMVT_Comments | varchar |  |  | SI | Comments |
| RTMVT_ContactPerson | varchar |  |  | SI | ContactPerson |
| RTMVT_Date | date |  |  | SI | Transaction Date |
| RTMVT_Doctor_DR | varchar |  | FK | SI | Des Ref to CTCP |
| RTMVT_Extension | varchar |  |  | SI | Extension |
| RTMVT_LocFrom_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| RTMVT_LocTo_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| RTMVT_RTMAVMerge_DR | varchar |  | FK | SI | Des Ref RTMAVMerge |
| RTMVT_ReasonForMove_DR | bigint |  | FK | SI | Des Ref ReasonForMove |
| RTMVT_ReasonRequest_DR | bigint |  | FK | SI | Des Ref ReasonForRequest |
| RTMVT_ReqTelNo | varchar |  |  | SI | ReqTelNo |
| RTMVT_ReqVol_DR | varchar |  | FK | SI | Des Ref to RTREV |
| RTMVT_RowId | varchar |  |  | NO | - |
| RTMVT_Time | time |  |  | SI | Transaction Time |
| RTMVT_TransComments | varchar |  |  | SI | TransComments |
| RTMVT_Type | varchar |  |  | NO | Transaction Type |
| RTMVT_UpdateDate | date |  |  | SI | Update Date |
| RTMVT_UpdateTime | time |  |  | SI | Update Time |
| RTMVT_UpdateUser_DR | bigint |  | FK | SI | Des Ref to SSUser |
| RTMVT_UserIdFrom_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| RTMVT_UserIdTo_DR | bigint |  | FK | SI | Des Ref to SSU |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*