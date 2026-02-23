# SQLUser.RT_MasVol

**Schema:** SQLUser
**Columnas:** 36
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Tiempo Real**. Procesamiento en tiempo real.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTMAV_RTMAS_ParRef | bigint | PK |  | NO | Des Ref to RTMAS |
| RTMAV_ActiveFlag | varchar |  |  | NO | Active Flag |
| RTMAV_BoxNumber | varchar |  |  | SI | Box Number |
| RTMAV_CancelReason_DR | bigint |  | FK | SI | Des Ref CancelReason |
| RTMAV_ChildSub | numeric |  |  | NO | RTMAV ChildSub |
| RTMAV_CreateLoc_DR | bigint |  | FK | SI | Des Ref Create Loc |
| RTMAV_CreatedByUser_DR | bigint |  | FK | SI | Created By User |
| RTMAV_CurrentLoc_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| RTMAV_DateArchived | date |  |  | SI | Date Archived |
| RTMAV_DateArrived | date |  |  | SI | Date Arrived |
| RTMAV_DateCancelled | date |  |  | SI | DateCancelled |
| RTMAV_DateCreated | date |  |  | SI | Date Created |
| RTMAV_DateIssued | date |  |  | SI | Date Issued |
| RTMAV_DateRequiredBy | date |  |  | SI | DateRequiredBy |
| RTMAV_DateToBeReturned | date |  |  | SI | DateToBeReturned |
| RTMAV_EarliestDesctruction | date |  |  | SI | EarliestDesctruction |
| RTMAV_EpisApptDate | date |  |  | SI | Episode/Appt Date |
| RTMAV_ExpDays | double |  |  | SI | Expected Number of Use Day |
| RTMAV_HomeLoc_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| RTMAV_MRStatus | varchar |  |  | NO | MRStatus |
| RTMAV_MRType_Vol_DR | varchar |  | FK | SI | Des Ref MRType_Vol |
| RTMAV_Notes | varchar |  |  | SI | Notes |
| RTMAV_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| RTMAV_Parts_DR | bigint |  | FK | SI | Des Ref to RTCParts |
| RTMAV_PositionNumber | varchar |  |  | SI | Position Number |
| RTMAV_ProcStatus | varchar |  |  | SI | Process Status |
| RTMAV_Request_DR | varchar |  | FK | SI | Do Not Use - Not Relevent |
| RTMAV_RetentionStatus | varchar |  |  | SI | RetentionStatus |
| RTMAV_RollNumber | varchar |  |  | SI | RollNumber |
| RTMAV_RowId | varchar |  |  | NO | - |
| RTMAV_TempHomeLoc_DR | bigint |  | FK | SI | Des Ref TempHomeLoc |
| RTMAV_TimeCreated | time |  |  | SI | Time Created |
| RTMAV_VolDesc | varchar |  |  | SI | RT Volume Description |
| RTMAV_VolumeNotes | varchar |  |  | SI | Volume Notes |
| RTMAV_VolumeNumber | varchar |  |  | SI | Volume Number |
| RTMAV_VolumeNumber1 | varchar |  |  | SI | VolumeNumber1 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*