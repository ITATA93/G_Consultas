# SQLUser.RB_Appointment

**Schema:** SQLUser
**Columnas:** 177
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPT_AS_ParRef | varchar | PK |  | NO | RBAS Par Ref |
| APPT_APPT_DR | varchar |  | FK | SI | Des Ref to Transfer Appt |
| APPT_ARCIM_DR | varchar |  | FK | SI | Des REf ARCIM |
| APPT_ASSI_DR | bigint |  | FK | SI | Des Ref ASSI |
| APPT_AT_DR | bigint |  | FK | SI | Des Ref to RBC_ApptType |
| APPT_Activity | varchar |  |  | SI | Activity |
| APPT_AdmType | varchar |  |  | SI | Admission Type |
| APPT_Adm_DR | bigint |  | FK | SI | Des Ref to PAADM (only after admit RB) |
| APPT_AdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| APPT_AppointLetter | varchar |  |  | SI | Appointment Letter |
| APPT_ArrivalDate | date |  |  | SI | ArrivalDate |
| APPT_ArrivalTime | time |  |  | SI | Arrival Time |
| APPT_ArrivalTimeCP1 | time |  |  | SI | ArrivalTimeCP1 |
| APPT_ArrivalTimeCP2 | time |  |  | SI | ArrivalTimeCP2 |
| APPT_Associated_Flag | bit |  |  | SI | Allows Appointment Status to Change from Cancelled... |
| APPT_AuthoriseUser_DR | bigint |  | FK | SI | Des Ref AuthoriseUser |
| APPT_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| APPT_BillDoctor_DR | varchar |  | FK | SI | Des Ref CTPCP |
| APPT_BillingMethod_DR | bigint |  | FK | SI | Des Ref BillingMethod |
| APPT_BookedBy_DR | bigint |  | FK | SI | Des Ref User |
| APPT_BookedDate | date |  |  | SI | BookedDate |
| APPT_BookedTime | time |  |  | SI | BookedTime |
| APPT_BookingSystem_DR | bigint |  | FK | SI | Des Ref BookingSystem |
| APPT_CancelDate | date |  |  | SI | CancelDate |
| APPT_CancelTime | time |  |  | SI | CancelTime |
| APPT_CancelledOnDischarge | varchar |  |  | SI | CancelledOnDischarge |
| APPT_CareProvGroup_DR | bigint |  | FK | SI | Care Provider Group - Affiliation  |
| APPT_CareProvType_DR | bigint |  | FK | SI | Des Ref CareProvType |
| APPT_CareProvider | varchar |  |  | SI | CareProvider |
| APPT_CareProvider2_DR | varchar |  | FK | SI | Des Ref CareProvider2 |
| APPT_ChildSub | double |  |  | NO | Child Sub (New Key) |
| APPT_CommReportedDate | date |  |  | SI | Commissioning Reported Date |
| APPT_Confirmation | varchar |  |  | SI | Confirmation |
| APPT_ConfirmationResponse_DR | bigint |  | FK | SI | Des Ref RBCConfirmationResponse |
| APPT_ConfirmedBy | varchar |  |  | SI | Confirmed By |
| APPT_ConfirmedDate | date |  |  | SI | Confirmed Date |
| APPT_ConsultCateg_DR | bigint |  | FK | SI | Des Ref ConsultCateg |
| APPT_ContClientPresStat_DR | bigint |  | FK | SI | Des Ref PACContClientPresStat |
| APPT_ContDelivMode_DR | bigint |  | FK | SI | Des Ref PACContDelivMode |
| APPT_ContDelivSetting_DR | bigint |  | FK | SI | Des Ref PACContDelivSetting |
| APPT_ContSessionType_DR | bigint |  | FK | SI | Des Ref PACContSessionType |
| APPT_CustomFlag1 | varchar |  |  | SI | CustomFlag1 |
| APPT_CustomFlag2 | varchar |  |  | SI | CustomFlag2 |
| APPT_CustomFlag3 | varchar |  |  | SI | CustomFlag3 |
| APPT_CustomText1 | varchar |  |  | SI | CustomText1 |
| APPT_CustomText2 | varchar |  |  | SI | CustomText2 |
| APPT_CustomText3 | varchar |  |  | SI | CustomText3 |
| APPT_DateComp | date |  |  | SI | Date Computed |
| APPT_DateSearch | date |  |  | SI | Date Search |
| APPT_DepartureDate | date |  |  | SI | DepartureDate |
| APPT_DepartureTime | time |  |  | SI | Departure Time |
| APPT_DepartureTimeCP1 | time |  |  | SI | DepartureTimeCP1 |
| APPT_DepartureTimeCP2 | time |  |  | SI | DepartureTimeCP2 |
| APPT_DocUpdatedOTOrderBill | varchar |  |  | SI | Free Text Doctor Updated OT Order Billed |
| APPT_DoctorLetterNotes | varchar |  |  | SI | Doctor Letter Notes |
| APPT_Duration | double |  |  | SI | Service Duration |
| APPT_EBEI | varchar |  |  | SI | External Booking Event Identifier |
| APPT_ETA | time |  |  | NO | Estimated Time of Arrival |
| APPT_EndDate | date |  |  | SI | EndDate |
| APPT_EndTime | time |  |  | SI | EndTime |
| APPT_Equipment_DR | bigint |  | FK | SI | Des Ref Equipment |
| APPT_Escort | double |  |  | SI | Escort |
| APPT_EventSubmitCP_DR | varchar |  | FK | SI | Des Ref Submitting Care Provider for the Event Tim... |
| APPT_ExecutedStatus | varchar |  |  | SI | Executed Status |
| APPT_ExternalDocFiscalCode | varchar |  |  | SI | External Doctor Fiscal Code |
| APPT_ExternalFillerNo | varchar |  |  | SI | External Filler Number |
| APPT_ExternalPaperPrescNo | varchar |  |  | SI | External PAPER Prescription Number |
| APPT_ExternalPlacerNo | varchar |  |  | SI | External Placer Number |
| APPT_ExternalPrescriptionID | varchar |  |  | SI | External Prescription Item Identifier |
| APPT_FamilyBooking | varchar |  |  | SI | Family Booking |
| APPT_FirstAppointFlag | varchar |  |  | SI | First Appoint Flag |
| APPT_FirstAvailableSched_DR | varchar |  | FK | SI | Des Ref RBApptSchedule |
| APPT_FollowUpApptDate | date |  |  | SI | Follow Up Appointment Date |
| APPT_FollowUpApptHospital_DR | bigint |  | FK | SI | Des Ref Follow Up Appointment Hospital |
| APPT_FreeTextReasonTTG | varchar |  |  | SI | Free Text Reason for Booking Past TTG |
| APPT_GroupDesc | varchar |  |  | SI | Free Text Group Description |
| APPT_HRG_DR | bigint |  | FK | SI | Des Ref HRG |
| APPT_InWithDoctorDate | date |  |  | SI | In With Doctor Date |
| APPT_InWithDoctorTime | time |  |  | SI | In With Doctor Time |
| APPT_InWithNurseDate | date |  |  | SI | In With Nurse Date |
| APPT_InWithNurseTime | time |  |  | SI | In With Nurse Time |
| APPT_Infectious | varchar |  |  | SI | Infectious |
| APPT_InpatientFlag | varchar |  |  | SI | InpatientFlag |
| APPT_InsurAssociation_DR | bigint |  | FK | SI | Des Ref ARCInsurAssociation |
| APPT_InterpreterConfirmed | varchar |  |  | SI | Interpreter Confirmed |
| APPT_InterpreterRequired | varchar |  |  | SI | Interpreter Required |
| APPT_Interpreter_DR | bigint |  | FK | SI | Des Ref Interpreter |
| APPT_Language_DR | bigint |  | FK | SI | Des Ref Language |
| APPT_LastStatusChangeDate | date |  |  | SI | LastStatusChangeDate |
| APPT_LastStatusChangeHospital_DR | bigint |  | FK | SI | Des Ref LastStatusChangeHospital |
| APPT_LastStatusChangeTime | time |  |  | SI | LastStatusChangeTime |
| APPT_LastStatusChangeUser_DR | bigint |  | FK | SI | Des Ref LastStatusChangeUser |
| APPT_LastUpdateDate | date |  |  | SI | Last Update Date |
| APPT_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| APPT_Loc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| APPT_MRPulled | varchar |  |  | SI | MR Pulled |
| APPT_MainAppointment_DR | varchar |  | FK | SI | Des Ref MainAppointment |
| APPT_MainGroupAppt_DR | varchar |  | FK | SI | Des Ref MainGroupAppt |
| APPT_MeetingLink | varchar |  |  | SI | Meeting Link |
| APPT_Method_DR | bigint |  | FK | SI | Method Des Ref to RBCAptMeth |
| APPT_MoveMedRec | varchar |  |  | SI | MoveMedRec |
| APPT_NextApptDate | date |  |  | SI | NextAppt Date |
| APPT_NotUsed | varchar |  |  | SI | Not used field |
| APPT_NursingNotesFlag | varchar |  |  | SI | Nursing Notes Flag |
| APPT_OEORI_DR | varchar |  | FK | SI | Des Ref OEORI |
| APPT_OPDRoom_DR | bigint |  | FK | SI | Des Ref OPDRoom |
| APPT_Outcome_DR | bigint |  | FK | SI | Des Ref Outcome of Appointment |
| APPT_PANok_DR | varchar |  | FK | SI | Des Ref PANok |
| APPT_PAPMI_DR | bigint |  | FK | SI | Des Ref to PAPMI |
| APPT_PARefPathwayStage_DR | varchar |  | FK | SI | Des Ref PARefPathwayStage |
| APPT_PPMSSearch_DR | bigint |  | FK | SI | PPMS Search results |
| APPT_PatientLetterNotes | varchar |  |  | SI | Patient Letter Notes |
| APPT_PatientNotAttending | varchar |  |  | SI | PatientNotAttending |
| APPT_PatientStatus | varchar |  |  | SI | PatientStatus |
| APPT_PayByResult | varchar |  |  | SI | Payment By Result |
| APPT_PayedFlag | varchar |  |  | SI | Payed Flag |
| APPT_PaymentLink | varchar |  |  | SI | Payment Link |
| APPT_PayorContactType_DR | bigint |  | FK | SI | Des Ref ARCPayorContactType |
| APPT_PersonResponsibleComments | varchar |  |  | SI | Person Responsible Comments |
| APPT_PersonScheduleItem_DR | varchar |  | FK | SI | Des Ref PersonScheduleItem |
| APPT_PreassAppRBOP_DR | bigint |  | FK | SI |  OT Booking of PreassApp usually Outpatient, can b... |
| APPT_Problem_DR | varchar |  | FK | SI | Des Ref Problem for the attached ACN Encounter |
| APPT_QueueNo | varchar |  |  | SI | Queue Number |
| APPT_RBAttendance_DR | bigint |  | FK | SI | Des Ref RBAttendance |
| APPT_RBCServ_DR | bigint |  | FK | SI | Des Ref RBC Service |
| APPT_RBEventTimes_DR | varchar |  | FK | SI | Des Ref Event Session |
| APPT_RBEvent_DR | bigint |  | FK | SI | Des Ref RBEvent |
| APPT_RBOP_DR | bigint |  | FK | SI | Des Ref RBOP |
| APPT_RBTR | varchar |  |  | SI | Not Used |
| APPT_RSVP | varchar |  |  | SI | RSVP |
| APPT_RTTCons_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| APPT_RTTHosp_DR | bigint |  | FK | SI | Des Ref Hospital |
| APPT_RTTReferPrior_DR | bigint |  | FK | SI | Des Ref PACReferralPriority |
| APPT_RTTSpec_DR | bigint |  | FK | SI | Des Ref CTLoc |
| APPT_ReasonBookPastTTG_DR | bigint |  | FK | SI | Reason for Booking Past TTG |
| APPT_ReasonForCancel_DR | bigint |  | FK | SI | Des Ref Reason For Cancel |
| APPT_ReasonForCancellation | varchar |  |  | SI | Reason For Cancellation |
| APPT_ReasonForTransfer_DR | bigint |  | FK | SI | Des Ref ReasonForTransfer |
| APPT_ReasonNotShow | bigint |  |  | SI | Des Ref Reason Not Show |
| APPT_ReasonOverBook_DR | bigint |  | FK | SI | Des Ref ReasonOverBook |
| APPT_Remarks | varchar |  |  | SI | Remarks |
| APPT_RequestCareProvider2_DR | varchar |  | FK | SI | Des Ref RequestCareProvider2 |
| APPT_RequestedCP_DR | varchar |  | FK | SI | Des Ref RequestedCP |
| APPT_ReviewPeriod_DR | bigint |  | FK | SI | Des Ref ReviewPeriod |
| APPT_RowId | varchar |  |  | NO | - |
| APPT_SMSConsent | varchar |  |  | SI | SMS Consent |
| APPT_SeenByNurseDate | date |  |  | SI | Seen by Nurse Date |
| APPT_SeenByNurseTime | time |  |  | SI | Seen by Nurse Time |
| APPT_SeenDate | date |  |  | SI | Seen Date |
| APPT_SeenDoctor_DR | varchar |  | FK | SI | Des Ref CTPCP |
| APPT_SeenTime | time |  |  | SI | Seen Time |
| APPT_ServiceSet_DR | bigint |  | FK | SI | Des Ref ServiceSet |
| APPT_SourceOfAttend_DR | bigint |  | FK | SI | Des Ref SourceOfAttend |
| APPT_Status | varchar |  |  | NO | Appointment Status |
| APPT_SystemSession | varchar |  |  | SI | SystemSession |
| APPT_SystemSessionHold | varchar |  |  | SI | SystemSessionHold |
| APPT_Technician | varchar |  |  | SI | Free Text Technician |
| APPT_TimeComp | time |  |  | SI | Time Computed |
| APPT_TransCount | double |  |  | SI | Hospital Initated Transfer Count |
| APPT_TransDate | date |  |  | SI | Transaction Date |
| APPT_TransTime | time |  |  | SI | Transaction Time |
| APPT_TransUser_DR | bigint |  | FK | SI | Transcation processed by |
| APPT_TransferDate | date |  |  | SI | Transfer Date |
| APPT_TransferTime | time |  |  | SI | Transfer Time |
| APPT_TransportComments | varchar |  |  | SI | TransportComments |
| APPT_TransportRequired | varchar |  |  | SI | Transport Required |
| APPT_Transport_DR | bigint |  | FK | SI | Des Ref Transport |
| APPT_TreatmentPlan_DR | bigint |  | FK | SI | Des Ref NRTreatmentPlan |
| APPT_UBRN | varchar |  |  | SI | UBRN number |
| APPT_USRN | varchar |  |  | SI | USRN number |
| APPT_Urgent | varchar |  |  | SI | Urgent |
| APPT_Verified | varchar |  |  | SI | Verified |
| APPT_View | varchar |  |  | SI | View |
| APPT_ViewableByEpCareProv | varchar |  |  | SI | ViewableByEpCareProv |
| APPT_WaitListStatus_DR | bigint |  | FK | SI | Des Ref WaitListStatus |
| APPT_WaitList_DR | bigint |  | FK | SI | Des Ref Waiting List |
| APPT_YesNo1 | varchar |  |  | SI | YesNo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*