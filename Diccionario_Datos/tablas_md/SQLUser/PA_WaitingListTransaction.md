# SQLUser.PA_WaitingListTransaction

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRANS_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| TRANS_AccomodationType_DR | bigint |  | FK | SI | Des Ref AccomodationType |
| TRANS_AdmVisitStatus | varchar |  |  | SI | AdmVisitStatus |
| TRANS_AuthUser_DR | bigint |  | FK | SI | Des Ref AuthUser |
| TRANS_BookingNumber | varchar |  |  | SI | Booking Number |
| TRANS_CareProvGroup_DR | bigint |  | FK | SI | Care Provider Group - Affiliation |
| TRANS_Childsub | double |  |  | NO | Childsub |
| TRANS_Date | date |  |  | SI | Date |
| TRANS_DateDelete | date |  |  | SI | DateDelete |
| TRANS_DateEffective | date |  |  | SI | Effective Date |
| TRANS_EstLengthOfStay | double |  |  | SI | Est Length Of Stay |
| TRANS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| TRANS_PriorityChanged | varchar |  |  | SI | Priority Changed |
| TRANS_ProcessFlag | varchar |  |  | SI | Process Flag (if changes are for future) |
| TRANS_ProgramFunding_DR | bigint |  | FK | SI | Des Ref ProgramFundingSource  |
| TRANS_ReasonForChange_DR | bigint |  | FK | SI | Des Ref Reason For Change |
| TRANS_ReasonNotAvail_DR | bigint |  | FK | SI | Des Ref ReasonNotAvail |
| TRANS_RefDepHospCareTypes | varchar |  |  | SI | Referring Hospital Care Types |
| TRANS_RefStatusReason_DR | bigint |  | FK | SI | Des Ref PACRefStatusReason  |
| TRANS_RemovalDesc | varchar |  |  | SI | Removal Desc |
| TRANS_RowId | varchar |  |  | NO | - |
| TRANS_StatePPP_DR | bigint |  | FK | SI | Des Ref StatePPP |
| TRANS_Status_DR | bigint |  | FK | SI | Status |
| TRANS_Surgeon_DR | varchar |  | FK | SI | Des Ref Surgeon |
| TRANS_TCIStatus | varchar |  |  | SI | TCI Status |
| TRANS_Time | time |  |  | SI | Time |
| TRANS_User_DR | bigint |  | FK | SI | Des Ref User |
| TRANS_WLNotAvail_DR | varchar |  | FK | SI | Des Ref WLNotAvail |
| TRANS_WaitListPriority_DR | bigint |  | FK | SI | Des Ref Wait List Priority |
| TRANS_WaitListType_DR | bigint |  | FK | SI | Des Ref Wait List Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*