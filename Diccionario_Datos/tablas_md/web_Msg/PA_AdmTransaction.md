# web_Msg.PA_AdmTransaction

**Schema:** web_Msg
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TRANS_AccomodationType_DR | bigint |  | FK | SI | Des Ref AccomodationType |
| TRANS_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| TRANS_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| TRANS_AuxInsType_DR | bigint |  | FK | SI | Des Ref to AuxInsType |
| TRANS_BedType_DR | bigint |  | FK | SI | Des Ref BedType |
| TRANS_Bed_DR | varchar |  | FK | SI | Des Ref Bed |
| TRANS_CTCP_DR | varchar |  | FK | SI | Des Ref to CTCP |
| TRANS_CTLOC_DR | bigint |  | FK | SI | Des REf CTLOC |
| TRANS_Childsub | double |  |  | SI | Childsub |
| TRANS_Closure | varchar |  |  | SI | Closure |
| TRANS_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| TRANS_Consultant_DR | varchar |  | FK | SI | Des Ref Consultant |
| TRANS_CreateDate | date |  |  | SI | Create Date |
| TRANS_CreateTime | time |  |  | SI | Create Time |
| TRANS_CreateUser_DR | bigint |  | FK | SI | Des Ref CreateUser |
| TRANS_DRG_DR | bigint |  | FK | SI | Des Ref TRANS_DRG_DR |
| TRANS_DateAccepted | date |  |  | SI | Date Accepted |
| TRANS_Dept_DR | bigint |  | FK | SI | Des Ref CTLOC |
| TRANS_EmbDayCase | varchar |  |  | SI | EmbDayCase |
| TRANS_EmergConsultant_DR | varchar |  | FK | SI | Des Ref Emergency Consultant |
| TRANS_EndDate | date |  |  | SI | End Date |
| TRANS_EndTime | time |  |  | SI | End Time |
| TRANS_ExpBedLengthOfStay | double |  |  | SI | Expected Bed Length Of Stay  |
| TRANS_ExpBedLengthOfStayUnit | varchar |  |  | SI | Expected Length Of Stay Unit |
| TRANS_ExpLengthOfStay | double |  |  | SI | Expected Length Of Stay  |
| TRANS_ExpLengthOfStayUnit | varchar |  |  | SI | Expected Length Of Stay Unit |
| TRANS_ExpectedBedOutDate | date |  |  | SI | Expected Bed Out Date |
| TRANS_ExpectedBedOutTime | time |  |  | SI | Expected Bed Out Time |
| TRANS_ExpectedBedVacancy | date |  |  | SI | ExpectedBedVacancy |
| TRANS_HRG_DR | bigint |  | FK | SI | Des Ref HRG |
| TRANS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| TRANS_ICUBedRequired | varchar |  |  | SI | ICU Bed Required |
| TRANS_InsType_DR | bigint |  | FK | SI | Des Ref to InsType |
| TRANS_IsolationRequired | varchar |  |  | SI | Isolation Required |
| TRANS_KeepOnDischarge | varchar |  |  | SI | TRANSKeepOnDischarge |
| TRANS_LikelihoodAdmit | varchar |  |  | SI | Likelihood to Admit
Put onto the Transaction as w... |
| TRANS_LinkedMovement_DR | varchar |  | FK | SI | Des Ref Linked Movement |
| TRANS_Main | varchar |  |  | SI | Main |
| TRANS_MoveMROnDischarge | varchar |  |  | SI | MoveMROnDischarge |
| TRANS_OnMedicalGrounds | varchar |  |  | SI | OnMedicalGrounds |
| TRANS_OverrideRoomType_DR | bigint |  | FK | SI | Des Ref OverrideRoomType |
| TRANS_ParRef | bigint |  |  | SI | PA_Adm Parent Reference
Required by User.PAAdmTra... |
| TRANS_PayByResult | varchar |  |  | SI | Payment By Result |
| TRANS_PostOpBedRequest | varchar |  |  | SI | Post Operative Bed Request |
| TRANS_RMCCareProv_DR | varchar |  | FK | SI | Rapid Management Clinician, des ref CTCareProv |
| TRANS_ReadyForBill | varchar |  |  | SI | ReadyForBill |
| TRANS_Reason_DR | bigint |  | FK | SI | Des Ref BedTransfer_Reason |
| TRANS_RejectReason_DR | bigint |  | FK | SI | Des Ref PACTransRejectReason |
| TRANS_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| TRANS_RoomType_DR | bigint |  | FK | SI | Des Ref PAC RoomType |
| TRANS_Room_DR | bigint |  | FK | SI | Des Ref to Room |
| TRANS_RowId | varchar |  |  | SI | - |
| TRANS_StartDate | date |  |  | SI | Start Date |
| TRANS_StartTime | time |  |  | SI | Start Time |
| TRANS_Status_DR | bigint |  | FK | SI | Des Ref PACTransfReqStatus |
| TRANS_TembTempLoc | varchar |  |  | SI | TembTempLoc |
| TRANS_TempLoc_DR | bigint |  | FK | SI | Des REf CTLOC |
| TRANS_TimeAccepted | time |  |  | SI | Time Accepted |
| TRANS_TransType_DR | bigint |  | FK | SI | Des Ref TransType |
| TRANS_UpdateDate | date |  |  | SI | Update Date |
| TRANS_UpdateTime | time |  |  | SI | Update Time |
| TRANS_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| TRANS_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| TRANS_Verified | varchar |  |  | SI | Verified |
| TRANS_WardRoom_DR | varchar |  | FK | SI | Des Ref to PACWardRoom - To be used in web.Msg.PAA... |
| TRANS_Ward_DR | bigint |  | FK | SI | Des Ref to Ward |
| TRANS_Warned | varchar |  |  | SI | Warned |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*