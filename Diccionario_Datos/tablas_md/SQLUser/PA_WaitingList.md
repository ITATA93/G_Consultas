# SQLUser.PA_WaitingList

**Schema:** SQLUser
**Columnas:** 264
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WL_RowId | bigint | PK |  | NO | - |
| WL_ASA_DR | bigint |  | FK | SI | Des Ref to ORC ASA |
| WL_AccomodationType_DR | bigint |  | FK | SI | Des Ref AccomodationType |
| WL_ActiveMonitoring | varchar |  |  | SI | Active Monitoring |
| WL_ActualAmountPaid | double |  |  | SI | Actual Amount Paid |
| WL_AdmBookingSystem_DR | bigint |  | FK | SI | Des Ref AdmBookingSystem |
| WL_AdmDateOtherHosp | date |  |  | SI | Adm Date in Other Hosp |
| WL_AdmDaysBeforeOper | double |  |  | SI | Number of Admission Days before Operation |
| WL_AdminCategory_DR | bigint |  | FK | SI | Des Ref PACAccountClass |
| WL_AdmissionCategory_DR | bigint |  | FK | SI | Des Ref AdmissionCategory |
| WL_Advised | varchar |  |  | SI | Advised |
| WL_AgencyPref_DR | bigint |  | FK | SI | Des Ref PACNonGovOrg |
| WL_AnaestMethod_DR | bigint |  | FK | SI | Des Ref AnaestMethod |
| WL_Anaesthetist_DR | varchar |  | FK | SI | Des Ref CTCP |
| WL_AppointMethod_DR | bigint |  | FK | SI | Des Ref AppointMethod |
| WL_ApptDate | date |  |  | SI | Appt Date |
| WL_ApptLoc_DR | bigint |  | FK | SI | Appointment Location  |
| WL_ApptOutcome_DR | bigint |  | FK | SI | Des Ref ApptOutcome |
| WL_ApptTime | time |  |  | SI | Appt Time |
| WL_AssignedGroup_DR | varchar |  | FK | SI | Hospital - Assigned Group |
| WL_AssignedUser_DR | bigint |  | FK | SI | Assigned User |
| WL_AutoAssignedFlg | varchar |  |  | SI | Auto Assigned Flag |
| WL_AuxilInsurType_DR | bigint |  | FK | SI | Des Ref ARCAuxilInsurType  |
| WL_BillingMethod_DR | bigint |  | FK | SI | Des Ref BillingMethod |
| WL_BloodDonation | varchar |  |  | SI | Blood Donation |
| WL_BloodDonationText | varchar |  |  | SI | Blood Donation Text |
| WL_BloodRequired | varchar |  |  | SI | Blood Required |
| WL_BodySitePrimaryProc_DR | bigint |  | FK | SI | Des Ref OECBodySite  |
| WL_BookSystem_DR | bigint |  | FK | SI | Des Ref BookSystem |
| WL_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WL_CancerSite_DR | bigint |  | FK | SI | Des Ref PACSuspectCancerType  |
| WL_CareProvGroup_DR | bigint |  | FK | SI | Care Provider Group - Affiliation |
| WL_CareType_DR | bigint |  | FK | SI | Care Type |
| WL_CaseManager_DR | varchar |  | FK | SI | Des Ref CaseManager |
| WL_ClinicalRegistrationDate | date |  |  | SI | ClinicalRegistrationDate |
| WL_CommunicationPreference | varchar |  |  | SI | Communication Preference |
| WL_ComplexNeeds | varchar |  |  | SI | Complex Needs Notes |
| WL_ConsultCateg_DR | bigint |  | FK | SI | Des Ref ConsultCateg |
| WL_Consult_DR | varchar |  | FK | SI | Des Ref Consult |
| WL_ContDelivMode_DR | bigint |  | FK | SI | Des Ref PACContDelivMode |
| WL_ContTreatStoppedPathway | varchar |  |  | SI | Contining Treatment for Stopped Pathway |
| WL_ContinuationActivePathway | varchar |  |  | SI | Continuation ActivePathway |
| WL_ContractRemarks | varchar |  |  | SI | ContractRemarks |
| WL_CreatingAdmission_DR | bigint |  | FK | SI | Des Ref CreatingAdmission |
| WL_CurrWaitTime | double |  |  | SI | Current WaitTime |
| WL_DNACountPMS | double |  |  | SI | Count of not arrived appointments for PMS definiti... |
| WL_DRGCode_DR | bigint |  | FK | SI | Des Ref MRCDRGCodes |
| WL_Date | date |  |  | SI | Date |
| WL_DateAcknowLetterSent | date |  |  | SI | Date Acknowledgement Letter Sent |
| WL_DateConsultRequestSent | date |  |  | SI | DateConsultRequestSent |
| WL_DateContactLetterSent | date |  |  | SI | Date Contact Letter Sent |
| WL_DateDecidedToAdmit | date |  |  | SI | Date Decided To Admit |
| WL_DateDecisionRefer | date |  |  | SI | Date of Decisionto Refer |
| WL_DateGuaranteed | date |  |  | SI | Date Guaranteed |
| WL_DateMinusExcludeDays | date |  |  | SI | Date Minus Excl Days |
| WL_DateOfList | date |  |  | SI | Date Off List |
| WL_DateReceivedBack | date |  |  | SI | DateReceivedBack |
| WL_DateRefLetter | date |  |  | SI | DateRefLetter |
| WL_DateReminderLetterSent | date |  |  | SI | Date Reminder Letter Sent |
| WL_DayInAdvToAdmit | double |  |  | SI | Days in Advance to Admit |
| WL_DaySurgery | varchar |  |  | SI | Day Surgery |
| WL_DaysExclude | double |  |  | SI | Days Exclude |
| WL_DaysOfWeek | varchar |  |  | SI | Days Of Week |
| WL_DaysOnList | double |  |  | SI | DaysOnList |
| WL_DaysWaiting | double |  |  | SI | Days Waiting |
| WL_DefCancTreatByHosp | varchar |  |  | SI | Deferred/Cancelled Treatment by hospital |
| WL_DefCancTreatByHospDate | date |  |  | SI | Deferred/Cancelled Treatment by hospital Date  |
| WL_DeferredDate | date |  |  | SI | Deferred Date |
| WL_DeferredDaysWaiting | double |  |  | SI | Deferred Days Waiting |
| WL_DeftTreatInit_DR | bigint |  | FK | SI | Des Ref DeftTreatInit |
| WL_DeleteFlag | varchar |  |  | SI | Delete Flag |
| WL_DesiredTheatreTime | time |  |  | SI | DesiredTheatreTime |
| WL_DiagnosticTestOnly | varchar |  |  | SI | Diagnostic TestOnly |
| WL_Doctor | varchar |  |  | SI | Doctor |
| WL_DoctorNotes | varchar |  |  | SI | Doctor Notes |
| WL_Doctor_DR | varchar |  | FK | SI | Des Ref Doctor |
| WL_DonationDate | date |  |  | SI | Donation Date |
| WL_EDDBasedOnLMP | date |  |  | SI | Date of estimated EDD based on LMP |
| WL_ERefLinkedWaitlist_DR | bigint |  | FK | SI | Des Ref WaitList |
| WL_ESISResubmissionDate | date |  |  | SI | ESIS Resubmission Date |
| WL_EarliestOfferDate | date |  |  | SI | Earliest Reasonable Offer Date  |
| WL_EdcAgreedDate | date |  |  | SI | EdcAgreedDate |
| WL_EffectiveDate | date |  |  | SI | Effective Date |
| WL_EffectiveRemovalDate | date |  |  | SI | Date entry is reported to have been removed |
| WL_Eligibility | varchar |  |  | SI | Eligibility |
| WL_EndTime | time |  |  | SI | End Time of Waiting List |
| WL_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| WL_EstLengOp | double |  |  | SI | Estimate Length of Operation |
| WL_EstLengthOfStay | double |  |  | SI | Estimated LengthOfStay |
| WL_EstOperDate | date |  |  | SI | Estimated operation date |
| WL_EstOperTime | time |  |  | SI | Estimated operation time |
| WL_EstimatedCostOfCare | double |  |  | SI | Estimated Cost of Care |
| WL_ExpectedAdmDate | date |  |  | SI | Expected Adm Date |
| WL_ExternalReferralID | varchar |  |  | SI | External Prescription Item Identifier |
| WL_FamilyDoc_DR | bigint |  | FK | SI | Des Ref FamilyDoc |
| WL_FamilyDoctor | varchar |  |  | SI | FamilyDoctor |
| WL_GDayToOver | double |  |  | SI | GDayToOver |
| WL_GPConsent | varchar |  |  | SI | GPConsent |
| WL_GenderPref_DR | bigint |  | FK | SI | Des Ref CTSex |
| WL_GuaranteeExcCode_DR | bigint |  | FK | SI | Des Ref Guarantee Exception Code |
| WL_HIPs | varchar |  |  | SI | Hosp Initiated Postponements |
| WL_HospChaplainVisitReq | varchar |  |  | SI | Not used |
| WL_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| WL_ICD_DR | bigint |  | FK | SI | diagnosis |
| WL_ICUBedRequired | varchar |  |  | SI | ICU Bed Required |
| WL_InUK12Months | varchar |  |  | SI | In UK last 12 Months |
| WL_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| WL_IntendedWard_DR | bigint |  | FK | SI | Des Ref IntendedWard |
| WL_LMP | date |  |  | SI | Date of LMP |
| WL_LastAuditReviewDate | date |  |  | SI | Last Audit Review Date |
| WL_LastReviewedDate | date |  |  | SI | Last Reviewed Date |
| WL_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| WL_LeafLetType_DR | bigint |  | FK | SI | Des Ref LeafLetType |
| WL_LegalStatus_DR | bigint |  | FK | SI | Des Ref PACLegalStatusIndicator |
| WL_LinkedPAReferral_DR | bigint |  | FK | SI | Des Ref PAReferralPathway |
| WL_LinkedRBReferral_DR | bigint |  | FK | SI | Des Ref RBReferral |
| WL_ListingDoc_DR | varchar |  | FK | SI | Des Ref CTCareProv Listing Doctor |
| WL_LocPref_DR | bigint |  | FK | SI | Des Ref CTLoc |
| WL_MaxWaitingPeriod | varchar |  |  | SI | Max Waiting Period |
| WL_Minutes | integer |  |  | SI | Duration of Waiting |
| WL_MortalityFreeText | varchar |  |  | SI | Mortality Risk Free Text |
| WL_MortalityRiskPerc | double |  |  | SI | Mortality Risk Percentage |
| WL_NFMICategDepart_DR | varchar |  | FK | SI | Des Ref CTNFMICategDepart  |
| WL_NO | varchar |  |  | SI | Number |
| WL_NWPatientType_DR | bigint |  | FK | SI | Des Ref PACNWPatientType   |
| WL_NamedCP | varchar |  |  | SI | Named Care Provider |
| WL_NationalPPP_DR | bigint |  | FK | SI | Des Ref PACNationalPPP |
| WL_NumberOfDNAs | double |  |  | SI | Number of not attended appointments |
| WL_Nurse_DR | varchar |  | FK | SI | Desref Nurse |
| WL_OPOTBookingRequired | varchar |  |  | SI | OPOTBookingRequired |
| WL_OSVisitorStatus_DR | bigint |  | FK | SI | Des Ref OSVisitorStatus |
| WL_OTRoomBookPriority_DR | bigint |  | FK | SI | Des Ref ORC_Priority |
| WL_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| WL_OperativeEpisode | varchar |  |  | SI | Operative Episode |
| WL_OpinionOnly | varchar |  |  | SI | Opinion Only |
| WL_OrderingOfficer_DR | bigint |  | FK | SI | Ordering Officer |
| WL_OwnMinisterIndicator | varchar |  |  | SI | Not used |
| WL_PACLegalStatus_DR | bigint |  | FK | SI | Legal Status |
| WL_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| WL_PPMSSearch_DR | bigint |  | FK | SI | PPMS Search results |
| WL_PackageDet_DR | varchar |  | FK | SI | Des Ref PAPersonPackage |
| WL_Package_DR | varchar |  | FK | SI | Des Ref PAPersonPackage |
| WL_PatWillChangeClinician | varchar |  |  | SI | PatWillChangeClinician |
| WL_PatWillChangeNHSBoard | varchar |  |  | SI | PatWillChangeNHSBoard |
| WL_PatientCategory_DR | bigint |  | FK | SI | Des Ref PatientCategory |
| WL_PatientOn18wRTT | varchar |  |  | SI | Patient On 18wRTT |
| WL_PatientType_DR | bigint |  | FK | SI | PatientType |
| WL_PersonScheduleItem_DR | varchar |  | FK | SI | Des Ref PersonScheduleItem |
| WL_PlannedSameDay | varchar |  |  | SI | PlannedSameDay |
| WL_PositionNumber | varchar |  |  | SI | PositionNumber |
| WL_PreAdmission_DR | bigint |  | FK | SI | Pre Admission DR |
| WL_PrefAdmFacility_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WL_Pregnancy_DR | bigint |  | FK | SI | Des Ref Pregnancy |
| WL_PreopDate | date |  |  | SI | Preop Date |
| WL_PreopTime | time |  |  | SI | Preop Time |
| WL_PresentComplaint | varchar |  |  | SI | Present Complaint |
| WL_PreviousDaysWaiting | double |  |  | SI | Previous Days Waiting |
| WL_Primary | varchar |  |  | SI | Primary |
| WL_Private | varchar |  |  | SI | Private |
| WL_Procedure2_DR | bigint |  | FK | SI | Des Ref Procedure2 |
| WL_Procedure3_DR | bigint |  | FK | SI | Des Ref Procedure3 |
| WL_ProcedureFreeText | varchar |  |  | SI | Procedure Free Text |
| WL_ProcessingGroup | varchar |  |  | SI | Checkbox for Processing Group |
| WL_ProgramFunding_DR | bigint |  | FK | SI | Des Ref ProgramFundingSource  |
| WL_ProstheticsRequired | varchar |  |  | SI | Prosthetics Required |
| WL_ProvisionalDiagnosis | varchar |  |  | SI | Provisional Diagnosis |
| WL_QualifPrimaryProc_DR | varchar |  | FK | SI | Des Ref ORCProcedureQualifier  |
| WL_RBCTransport_DR | bigint |  | FK | SI | Des Ref RBC Transport |
| WL_RBOP_DR | bigint |  | FK | SI | Des Ref RB OperTheatre |
| WL_RTTFromOtherBoard | varchar |  |  | SI | RTTFromOtherBoard |
| WL_RTTStartDate | date |  |  | SI | RTT StartDate |
| WL_RadiologyFlag | varchar |  |  | SI | RadiologyFlag |
| WL_ReasonForChange_DR | bigint |  | FK | SI | Des Ref Reason For Change |
| WL_ReasonForList_DR | bigint |  | FK | SI | Des Ref ReasonForList |
| WL_ReasonForTransfer_DR | bigint |  | FK | SI | Des Ref ReasonForTransfer |
| WL_ReasonLinkUnlink_DR | bigint |  | FK | SI | Des Ref ReasonLinkUnlink |
| WL_RecallDate | date |  |  | SI | RecallDate |
| WL_RefCTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC Referrer Speciality |
| WL_RefClinIndicator | bigint |  |  | SI | Des Ref Clinical Indicator for Referral |
| WL_RefClinTo_DR | bigint |  | FK | SI | Des Ref CTRefClin |
| WL_RefDepHospCareTypes | varchar |  |  | SI | Referring Hospital Care Types |
| WL_RefDepHosp_DR | bigint |  | FK | SI | Referral Department Hospital |
| WL_RefDep_DR | bigint |  | FK | SI | Des Ref CTLOC |
| WL_RefDocClinc_DR | varchar |  | FK | SI | Des Ref RefDocClinc |
| WL_RefDocInt_DR | varchar |  | FK | SI | Des Ref RefDocInt |
| WL_RefDocTo_DR | bigint |  | FK | SI | Des Ref RefDocTo |
| WL_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| WL_RefExpiryDate | date |  |  | SI | RefExpiryDate |
| WL_RefHospTo_DR | bigint |  | FK | SI | Des Ref Ref HospTo |
| WL_RefHosp_DR | bigint |  | FK | SI | Des Ref RefHosp |
| WL_RefOrg_DR | bigint |  | FK | SI | Des Ref PACNonGovOrg |
| WL_RefReceiptMethod_DR | bigint |  | FK | SI | Des Ref PACRefReceiptMethod |
| WL_RefStatusReason_DR | bigint |  | FK | SI | Des Ref PACRefStatusReason  |
| WL_RefToNGOContactName | varchar |  |  | SI | RefToNGOContactName |
| WL_ReferralFrom_DR | bigint |  | FK | SI | Des Ref Health Care Area |
| WL_ReferralPeriod_DR | bigint |  | FK | SI | Des Ref PACReferralPeriod |
| WL_ReferralPriority_DR | bigint |  | FK | SI | Des Ref ReferralPriority |
| WL_ReferralReason_DR | bigint |  | FK | SI | Des Ref PACReferralReason |
| WL_ReferralType_DR | bigint |  | FK | SI | Des Ref PACReferralType |
| WL_ReferralUniqueID | varchar |  |  | SI | Referral Unique ID |
| WL_Remarks | varchar |  |  | SI | Remarks |
| WL_RemoveComments | varchar |  |  | SI | Remove Comments |
| WL_RemovedRemainOnList | varchar |  |  | SI | RemovedRemainOnList |
| WL_RequestingEpisNo | varchar |  |  | SI | Requesting Episode Number |
| WL_Resource_DR | bigint |  | FK | SI | Des REf Resource_DR |
| WL_Responded | varchar |  |  | SI | Responded |
| WL_ResponsibleUnit_DR | bigint |  | FK | SI | Des Ref CTResponsibleUnit  |
| WL_SecondAuxilInsurType_DR | bigint |  | FK | SI | Second Des Ref ARCAuxilInsurType  |
| WL_SecondInsType_DR | bigint |  | FK | SI | Second Des Ref InsType |
| WL_SendingApplication | varchar |  |  | SI | Sending Application |
| WL_ServiceGroup_DR | bigint |  | FK | SI | Des Ref ServiceGroup |
| WL_ServiceGuaranteedDate | date |  |  | SI | Service Guaranteed Date |
| WL_ServiceKey | varchar |  |  | SI | ServiceKey |
| WL_ServiceSet_DR | bigint |  | FK | SI | Des Ref RBCServiceSet  |
| WL_Service_DR | bigint |  | FK | SI | Des Ref Service |
| WL_SessionType | varchar |  |  | SI | SessionType |
| WL_ShortNotice | varchar |  |  | SI | Short Notice |
| WL_SnomedTerms_DR | bigint |  | FK | SI | SNOMED |
| WL_SourceAttend_DR | bigint |  | FK | SI | Des Ref SourceAttend |
| WL_SourceOfAddit_DR | bigint |  | FK | SI | Des Ref Source of addition |
| WL_SourceRefQualif_DR | bigint |  | FK | SI | Des Ref Source of RefQualifier |
| WL_SpecialCatFlag | varchar |  |  | SI | Special Categ Flag |
| WL_SpecialProject_DR | bigint |  | FK | SI | Des Ref SpecialProject |
| WL_SpecialRequirements | varchar |  |  | SI | Special Requirements |
| WL_StandbyStatus_DR | bigint |  | FK | SI | Des Ref StandbyStatus |
| WL_StartNewPathway | varchar |  |  | SI | Start New Pathway |
| WL_StartTime | time |  |  | SI | StartTime |
| WL_StateProc_DR | bigint |  | FK | SI | Des Ref StateProc |
| WL_StayingPermanently | varchar |  |  | SI | Staying Permanently |
| WL_SuitabilityOfPatient | varchar |  |  | SI | SuitabilityOfPatient |
| WL_SurgeonAssist_DR | varchar |  | FK | SI | Des Ref Surgeon Assistant |
| WL_Surgeon_DR | varchar |  | FK | SI | Des Ref Surgeon |
| WL_TCIsCancelledByHosp | varchar |  |  | SI | Linked PreAdmissions Cancelled with Cancel Reason ... |
| WL_TCIsCancelledByPat | varchar |  |  | SI | Linked PreAdmissions Cancelled with Cancel Reason ... |
| WL_TTGGuaranteedDate | date |  |  | SI | TTG Guaranteed Date |
| WL_TTGLetterDate | date |  |  | SI | TTG Letter Date |
| WL_Time | time |  |  | SI | Time |
| WL_TimeInTriage | double |  |  | SI | Time spent on Triage |
| WL_TotDaysOnList | double |  |  | SI | Total  Days On List |
| WL_TransDest_DR | bigint |  | FK | SI | Desref TransDest |
| WL_TransSource_DR | bigint |  | FK | SI | Des Ref TransSource |
| WL_TransferOfPatientCare | varchar |  |  | SI | Transfer Of PatientCare |
| WL_TreatmentID | varchar |  |  | SI | TreatmentID |
| WL_TreatmentStartDate | date |  |  | SI | Treatment Start Date |
| WL_TriageClinIndicator | bigint |  |  | SI | Des Ref Clinical Indicator for Triage |
| WL_TriageConsultant_DR | varchar |  | FK | SI | Des Ref TriageConsultant |
| WL_TriageDate | date |  |  | SI | TriageDate  |
| WL_TriageNotes | varchar |  |  | SI | Triage Notes |
| WL_TriageOutcome_DR | bigint |  | FK | SI | Des Ref WLTriageOutcome |
| WL_Trust_DR | bigint |  | FK | SI | Des Ref PACTrust  |
| WL_TypeOfProcedure_DR | bigint |  | FK | SI | Des Ref Type Of Procedure |
| WL_UpdateDate | date |  |  | SI | Update Date |
| WL_UpdateTime | time |  |  | SI | Update Time |
| WL_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| WL_UpdateUser_DR | bigint |  | FK | SI | Update User |
| WL_UserDefWindow_DR | varchar |  | FK | SI | Des Ref SSUserDefWindow  |
| WL_User_DR | bigint |  | FK | SI | Des Ref User |
| WL_Verified | varchar |  |  | SI | Intended Procedure Status(Verified) |
| WL_WaitListPrior_DR | bigint |  | FK | SI | Des Ref Wait List Prior |
| WL_WaitListStatus_DR | bigint |  | FK | SI | Des Ref Wait List Status |
| WL_WaitListType_DR | bigint |  | FK | SI | Des Ref Wait ListType |
| WL_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |
| WL_WaitingTimeStandard_DR | bigint |  | FK | SI | Des Ref WaitingTimeStandard |
| WL_YesNo1 | varchar |  |  | SI | YesNo |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*