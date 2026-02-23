# SQLUser.RT_ReqVol

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTREV_RTREQ_ParRef | varchar | PK |  | NO | Des Ref to RTREQ |
| RTREV_AckRequest | varchar |  |  | SI | AckRequest |
| RTREV_ChildSub | numeric |  |  | NO | Request Volume ChildSub |
| RTREV_DateComputed | date |  |  | SI | Request Date Computed |
| RTREV_Doctor_DR | varchar |  | FK | SI | Des Ref Doctor |
| RTREV_DueDate | date |  |  | SI | Due Date |
| RTREV_HomeLoc | varchar |  |  | SI | Home Loc |
| RTREV_IssBy | varchar |  |  | SI | Issue By : MR (O)ffice/(M)ovement/(T)ransfer |
| RTREV_LastRTMVT_DR | varchar |  | FK | SI | Last Transaction |
| RTREV_LengthOfUse | double |  |  | SI | Length Of Use |
| RTREV_MRReturnDate | date |  |  | SI | MRReturnDate |
| RTREV_MasVol_DR | varchar |  | FK | SI | Des Ref to RTMAV |
| RTREV_NextRTREV_DR | varchar |  | FK | SI | Next Req Volume (pass by Trf & Move) |
| RTREV_Priority | double |  |  | SI | Priority (Order of Transfer List) |
| RTREV_RTMAS_DR | bigint |  | FK | SI | Des Ref RTMAS |
| RTREV_ReasonForCancel_DR | bigint |  | FK | SI | Des Ref ReasonForCancel |
| RTREV_RespLoc | bigint |  |  | SI | Resp Loc(Calculate) |
| RTREV_ReturnLoc_DR | bigint |  | FK | SI | Return Location for record |
| RTREV_RowId | varchar |  |  | NO | - |
| RTREV_ShowInHomeLoc | varchar |  |  | SI | Show In Home Loc |
| RTREV_Status | varchar |  |  | NO | Request Volume Status |
| RTREV_TimeComputed | time |  |  | SI | Time Computed |
| RTREV_ViewLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| RTREV_xMasVol_DR | varchar |  | FK | SI | Des Ref to RTMAV |
| RTREV_xStatus | varchar |  |  | SI | Original Status before Misplace |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*