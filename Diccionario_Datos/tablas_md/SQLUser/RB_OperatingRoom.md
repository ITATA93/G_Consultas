# SQLUser.RB_OperatingRoom

**Schema:** SQLUser
**Columnas:** 132
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RBOP_RowId | bigint | PK |  | NO | - |
| RBOP_ASA_DR | bigint |  | FK | SI | Des Ref to ORC ASA |
| RBOP_ActualPreassDate | date |  |  | SI | Preassessment Date – date preadm appt booked, when... |
| RBOP_AdmDaysBeforeOper | double |  |  | SI | Number of Admission Days before Operation |
| RBOP_AdmDiagnosis | varchar |  |  | SI | AdmDiagnosis |
| RBOP_AnaestMethod_DR | bigint |  | FK | SI | Des Ref AnaestMethod |
| RBOP_Anaesthetist_DR | varchar |  | FK | SI | Des Ref CTCP |
| RBOP_Appoint_DR | varchar |  | FK | SI | Des REf Appoint |
| RBOP_ApproxTimeOper | time |  |  | SI | ApproxTimeOper |
| RBOP_Arrived | varchar |  |  | SI | Arrived |
| RBOP_AuthoriseUser_DR | bigint |  | FK | SI | Des Ref AuthoriseUser |
| RBOP_AuthorisedForInvoice | varchar |  |  | SI | Theatre Authorised for Invoicing |
| RBOP_AutologousTransfusion | varchar |  |  | SI | Autologous Transfusion Required |
| RBOP_Bed_DR | varchar |  | FK | SI | Des Ref PACBed |
| RBOP_BiopsyNeed | varchar |  |  | SI | Biopsy Need |
| RBOP_BloodRequired | varchar |  |  | SI | Blood Required |
| RBOP_BodySite_DR | bigint |  | FK | SI | Des Ref OEC_BodySite |
| RBOP_BookDoctor_DR | varchar |  | FK | SI | Des Ref to CTCP |
| RBOP_BookingNumber | varchar |  |  | SI | BookingNumber |
| RBOP_BookingType | varchar |  |  | SI | Booking Type |
| RBOP_BypassLoc_DR | bigint |  | FK | SI | Bypass Location |
| RBOP_BypassRec | varchar |  |  | SI | Bypass Recovery |
| RBOP_CancelReason | varchar |  |  | SI | Cancel Reason |
| RBOP_CreateDate | date |  |  | SI | Created Date |
| RBOP_CreateTime | time |  |  | SI | Created Time |
| RBOP_CstmText1 | varchar |  |  | SI | CstmText1 |
| RBOP_CstmText2 | varchar |  |  | SI | CstmText2 |
| RBOP_CstmText3 | varchar |  |  | SI | CstmText3 |
| RBOP_DateArrived | date |  |  | SI | Date Arrived |
| RBOP_DateBook | date |  |  | SI | Date of Booking |
| RBOP_DateOper | date |  |  | SI | Date of Operation |
| RBOP_DaySurgery | varchar |  |  | SI | Day Surgery |
| RBOP_DisplayChangedIcon | varchar |  |  | SI | Booking changed after 1pm before surgery |
| RBOP_Endoscopy | varchar |  |  | SI | Endoscopy |
| RBOP_EpisodeType | varchar |  |  | SI | EpisodeType |
| RBOP_EstimEpisLOS | double |  |  | SI | Estimated Episode Length of Stay  |
| RBOP_EstimatedTime | varchar |  |  | SI | Estimated Time |
| RBOP_ExpectedBedInDate | date |  |  | SI | Expected Bed In Date |
| RBOP_ExpectedBedInTime | time |  |  | SI | Expected Bed In Time |
| RBOP_ExpectedBedOutDate | date |  |  | SI | Expected Bed Out Date |
| RBOP_ExpectedBedOutTime | time |  |  | SI | Expected Bed Out Time |
| RBOP_FollowUpDone | varchar |  |  | SI | FollowUpDone |
| RBOP_FollowUpRequired | varchar |  |  | SI | FollowUpRequired |
| RBOP_FreeTextReasonTTG | varchar |  |  | SI | Free Text Reason for Booking Past TTG |
| RBOP_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| RBOP_ICUBedRequired | varchar |  |  | SI | ICU Bed Required |
| RBOP_Infect | varchar |  |  | SI | Infect |
| RBOP_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| RBOP_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| RBOP_ListingDoc_DR | varchar |  | FK | SI | Des Ref CTCareProv Listing Doctor |
| RBOP_Loc_DR | bigint |  | FK | SI | Theatre Location for OT Request |
| RBOP_MortalityFreeText | varchar |  |  | SI | Mortality Risk Free Text |
| RBOP_MortalityRiskPerc | double |  |  | SI | Mortality Risk Percentage |
| RBOP_NOKPostOpCallDone | varchar |  |  | SI | NOKPostOpCallDone |
| RBOP_NOKPostOpCallRequired | varchar |  |  | SI | NOKPostOpCallRequired |
| RBOP_OTConsultant_DR | varchar |  | FK | SI | OT Consultant (owner) Des Ref  |
| RBOP_OperDepartment_DR | bigint |  | FK | SI | Des Ref OperDepartment |
| RBOP_Operation_DR | bigint |  | FK | SI | Des Ref to ORC_Operation |
| RBOP_OtherOTSpec | varchar |  |  | SI | Booked in Another OT Specialty Session |
| RBOP_PAADM_DR | bigint |  | FK | SI | Des Ref to PAADM |
| RBOP_Person_DR | bigint |  | FK | SI | Des Ref Person |
| RBOP_PlanAnaesTime | double |  |  | SI | Average planned Anaesthetic Time (minutes) |
| RBOP_PlanAveAnaesTime | double |  |  | SI | Average planned Anaesthetic Time (minutes) |
| RBOP_PlanCleanUpTime | double |  |  | SI | Planned Clean up time (minutes) needed after the p... |
| RBOP_PlanPatTheatreTime | double |  |  | SI | Planned Patient Theatre Time (minutes) |
| RBOP_PlanPreSetupTime | double |  |  | SI | Pre/Set up time (minutes), planned setup time need... |
| RBOP_PlanSurgicalTime | double |  |  | SI | Planned Surgical Time (minutes)  |
| RBOP_PreOpCallDate | date |  |  | SI | Pre-Op Call Date |
| RBOP_PreOpCallDone | varchar |  |  | SI | Pre-Op Call Done |
| RBOP_PreOpCallReq | varchar |  |  | SI | Pre-Op Call Required |
| RBOP_PreOpCallTime | time |  |  | SI | Pre-Op Call Time |
| RBOP_PreOpCheckDate | date |  |  | SI | Pre-Op Check Date |
| RBOP_PreOpCheckDone | varchar |  |  | SI | Pre-Op Check Done |
| RBOP_PreOpCheckReq | varchar |  |  | SI | Pre-Op Check Required |
| RBOP_PreOpCheckTime | time |  |  | SI | Pre-Op Check Time |
| RBOP_PreOpDiagnosis | varchar |  |  | SI | PreOpDiagnosis |
| RBOP_PreassAPPT_DR | varchar |  | FK | SI | Preassessment Appointment ID |
| RBOP_PreopDate | date |  |  | SI | Preop Date |
| RBOP_PreopDiagn_DR | bigint |  | FK | SI | Des Ref to MRCICDx |
| RBOP_PreopTestDone | varchar |  |  | SI | Preop Test Done |
| RBOP_Priority_DR | bigint |  | FK | SI | Des Ref ORC_Priority |
| RBOP_Problem_DR | varchar |  | FK | SI | Patient Problem |
| RBOP_Procedure | varchar |  |  | SI | Procedure |
| RBOP_ProcedureEndTime | time |  |  | SI | ProcedureEndTime |
| RBOP_ProcedureStartTime | time |  |  | SI | ProcedureStartTime |
| RBOP_ProcsOpers | varchar |  |  | SI | ProcsOpers |
| RBOP_ProstheticsRequired | varchar |  |  | SI | Prosthetics Required |
| RBOP_ReasonBookPastTTG_DR | bigint |  | FK | SI | Reason for Booking Past TTG |
| RBOP_ReasonNotReady_DR | bigint |  | FK | SI | Des Ref ReasonNotReady |
| RBOP_ReasonReturn_DR | bigint |  | FK | SI | Des Ref ReasonReturn |
| RBOP_ReasonSuspend_DR | bigint |  | FK | SI | Des Ref ReasonSuspend |
| RBOP_RefDep_DR | bigint |  | FK | SI | Des Ref RefDep |
| RBOP_Remarks | varchar |  |  | SI | Remarks |
| RBOP_ReqPreassDate | date |  |  | SI | Preassessment Request Date – date preadm appt need... |
| RBOP_RequestApprovalDate | date |  |  | SI | Request Approval Date |
| RBOP_RequestApprovalTime | time |  |  | SI | Request Approval Time |
| RBOP_RequestMadeDate | date |  |  | SI | Request Made Date  |
| RBOP_RequestMadeTime | time |  |  | SI | Request Made Time |
| RBOP_RequestedDateOper | date |  |  | SI | RequestedDateOper |
| RBOP_RequestedTimeOper | time |  |  | SI | RequestedTimeOper |
| RBOP_RequiresFasting | varchar |  |  | SI | Fasting Required |
| RBOP_Resource_DR | bigint |  | FK | SI | Des Ref to Resource |
| RBOP_SentFor | varchar |  |  | SI | Pt Sent For  |
| RBOP_SentForAck | varchar |  |  | SI | Sent For Ack |
| RBOP_SentForAckDate | date |  |  | SI | Sent For Ack Date |
| RBOP_SentForAckTime | time |  |  | SI | Sent For Ack Time |
| RBOP_SentForDate | date |  |  | SI | Sent For Date |
| RBOP_SentForTime | time |  |  | SI | Sent For Time |
| RBOP_SequenceNo | varchar |  |  | SI | Sequence No |
| RBOP_SetupComplete | varchar |  |  | SI | Operating Theatre Setup Completed |
| RBOP_StatePPP_DR | bigint |  | FK | SI | Des Ref StatePPP |
| RBOP_Status | varchar |  |  | SI | Status |
| RBOP_SurgeonAssist_DR | varchar |  | FK | SI | Des Ref Surgeon Assistant |
| RBOP_Surgeon_DR | varchar |  | FK | SI | Des Ref to CTCP |
| RBOP_TempOTLocANA_DR | bigint |  | FK | SI | Temporary OT Location Anaesthetic |
| RBOP_TempOTLocREC_DR | bigint |  | FK | SI | Temporary OT Location Recovery |
| RBOP_TempOTLocWA_DR | bigint |  | FK | SI | Temporary OT Location Waiting Area |
| RBOP_TempOTLoc_DR | bigint |  | FK | SI | Temporary OT Location Calculated in web.RBOperatin... |
| RBOP_TimeArrived | time |  |  | SI | Time Arrived |
| RBOP_TimeOper | time |  |  | SI | Time of Operation |
| RBOP_TimeSurgery | time |  |  | SI | Time of Surgery |
| RBOP_TotalPlanTheatreTime | double |  |  | SI | Total Planned Theatre Time (minutes) |
| RBOP_TypeOfProcedure_DR | bigint |  | FK | SI | Des Ref Type Of Procedure |
| RBOP_UpdateDate | date |  |  | SI | Update Date |
| RBOP_UpdateTime | time |  |  | SI | Update Time |
| RBOP_UpdateUser | bigint |  |  | SI | Last Update User |
| RBOP_WaitList_DR | bigint |  | FK | SI | Des Ref Wait List |
| RBOP_WaitingRoom_DR | bigint |  | FK | SI | Waiting Room (Arrived Area) Des Ref |
| RBOP_Ward_DR | bigint |  | FK | SI | Des Ref PACWard |
| RBOP_YesNo1 | varchar |  |  | SI | YesNo1 |
| RBOP_YesNo2 | varchar |  |  | SI | YesNo2 |
| RBOP_YesNo3 | varchar |  |  | SI | YesNo3 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*