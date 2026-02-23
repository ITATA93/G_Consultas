# SQLUser.PA_Adm2

**Schema:** SQLUser
**Columnas:** 296
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAADM2_RowId | bigint | PK |  | NO | - |
| PAADM2_APPTLoc_DR | bigint |  | FK | SI | Des Ref APPTLoc |
| PAADM2_AccomSetting_DR | bigint |  | FK | SI | Des Ref Accom Setting |
| PAADM2_Action | varchar |  |  | SI | Action |
| PAADM2_ActualArrivalDate | date |  |  | SI | ActualArrivalDate |
| PAADM2_ActualArrivalTime | time |  |  | SI | ActualArrivalTime |
| PAADM2_ActualPreassDate | date |  |  | SI | Actual preassessment date |
| PAADM2_AdmDate | date |  |  | SI | AdmDate |
| PAADM2_AdmLabourStatus_DR | bigint |  | FK | SI | Des Ref AdmLabourStatus |
| PAADM2_AdmPointLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PAADM2_AdmTime | time |  |  | SI | AdmTime |
| PAADM2_AdminCategory_DR | bigint |  | FK | SI | Des Ref PACAccountClass |
| PAADM2_AdmissionPoint_DR | bigint |  | FK | SI | Des Ref AdmissionPoint |
| PAADM2_AlcoholDrugInvolve_DR | bigint |  | FK | SI | Des Ref PACAlcoholOrDrugInvolvement |
| PAADM2_AltFinDischDate | date |  |  | SI | AltFinDischDate |
| PAADM2_AltFinDischTime | time |  |  | SI | AltFinDischTime |
| PAADM2_AmbulCompDeparture_DR | bigint |  | FK | SI | Des Ref PACAmbulanceCompany |
| PAADM2_AmbulHandoverCompDate | date |  |  | SI | Ambulance Handover Complete Date |
| PAADM2_AmbulHandoverCompTime | time |  |  | SI | Ambulance Handover Complete Time |
| PAADM2_AmbulanceCompany_DR | bigint |  | FK | SI | Des Ref PACAmbulanceCompany |
| PAADM2_AssessmentReviewDate | date |  |  | SI | AssessmentReviewDate |
| PAADM2_AutoConverted | varchar |  |  | SI | Indicates whether an episode is the result of an a... |
| PAADM2_AutomaticEpisodeLinkage | varchar |  |  | SI | Indicates that, during the creation of this episod... |
| PAADM2_BillAdm_DR | bigint |  | FK | SI | Des Ref BillAdm |
| PAADM2_BillingLang_DR | bigint |  | FK | SI | Des Ref BillingLang |
| PAADM2_CheckECF | varchar |  |  | SI | Eligibility Check Fund |
| PAADM2_ClergyVisit | varchar |  |  | SI | ClergyVisit |
| PAADM2_ClinSumCompleted | varchar |  |  | SI | ClinSumCompleted |
| PAADM2_CodingUpdateHospital | bigint |  |  | SI | Des Ref CodingUpdateHospital |
| PAADM2_Comments | varchar |  |  | SI | Comments |
| PAADM2_ConfidentialityCode_DR | bigint |  | FK | SI | Des Ref PACConfidentialityCode |
| PAADM2_Consultant_DR | varchar |  | FK | SI | Des Ref Consultant |
| PAADM2_ContDelivMode_DR | bigint |  | FK | SI | Des Ref PACContDelivMode |
| PAADM2_ConversionOrig_DR | bigint |  | FK | SI | Des Ref PAAdm |
| PAADM2_ConversionTarget_DR | bigint |  | FK | SI | Des Ref PAADM |
| PAADM2_CriteriaTypeC | varchar |  |  | SI | CriteriaTypeC |
| PAADM2_DRGBillingEndDate | date |  |  | SI | DRG Billing End Date |
| PAADM2_DRGBillingEndTime | time |  |  | SI | DRG Billing End Time |
| PAADM2_DefaultEDtoIP | varchar |  |  | SI | DefaultEDtoIP |
| PAADM2_DeftTreatInit_DR | bigint |  | FK | SI | Des Ref DeftTreatInit |
| PAADM2_DesUsualHCConsent | varchar |  |  | SI | Designated Usual Health Centre Consent |
| PAADM2_DetentionType_DR | bigint |  | FK | SI | Des Ref MHCDetentionType |
| PAADM2_DischFeeding_DR | bigint |  | FK | SI | Des REf DischFeeding |
| PAADM2_DischHeadCircumfer | double |  |  | SI | Disch Head Circumfer |
| PAADM2_DischIntentOnAdm_DR | bigint |  | FK | SI | Des Ref PACDischIntentOnAdm |
| PAADM2_DischSumNotRequired | varchar |  |  | SI | DischSumNotRequired |
| PAADM2_DischSumRequired | varchar |  |  | SI | DischSumRequired |
| PAADM2_DischWeight | double |  |  | SI | DischWeight |
| PAADM2_EDIOverride | varchar |  |  | SI | EDIOverride |
| PAADM2_EdcAgreedDate | date |  |  | SI | EdcAgreedDate |
| PAADM2_EmergConsultant_DR | varchar |  | FK | SI | Des Ref Emergency Consultant |
| PAADM2_EmploymentStat_DR | bigint |  | FK | SI | Des Ref EmploymentStat |
| PAADM2_EpisCheckCompleted | varchar |  |  | SI | Episode Check Completed standard type YesNoInProgr... |
| PAADM2_EstimateDateInjury | varchar |  |  | SI | EstimateDateInjury |
| PAADM2_ExpAdmTime | time |  |  | SI | Expected AdmTime |
| PAADM2_ExpBedLengthOfStay | double |  |  | SI | Expected Bed Length Of Stay  |
| PAADM2_ExpBedLengthOfStayUnit | varchar |  |  | SI | Expected Length Of Stay Unit |
| PAADM2_ExpDateLegalStatClassif | date |  |  | SI | Expiry Date Legal Status Classification Assignment... |
| PAADM2_ExpLengthOfStay | double |  |  | SI | Expected Length Of Stay  |
| PAADM2_ExpLengthOfStayUnit | varchar |  |  | SI | Expected Length Of Stay Unit |
| PAADM2_ExpTimeLegalStatClassif | time |  |  | SI | Expiry Time Legal Status Classification Assignment... |
| PAADM2_ExpectDate | date |  |  | SI | ExpectDate |
| PAADM2_ExpectTime | time |  |  | SI | ExpecTime |
| PAADM2_ExpectedBedOutDate | date |  |  | SI | Expected Bed Out Date |
| PAADM2_ExpectedBedOutTime | time |  |  | SI | Expected Bed Out Time |
| PAADM2_FinIntrDisclosure | varchar |  |  | SI | Financial Interest Disclosure |
| PAADM2_FinalDischUser_DR | bigint |  | FK | SI | Des Ref FinalDischUser |
| PAADM2_FinancialDischUser_DR | bigint |  | FK | SI | Des Ref FinancialDischUser |
| PAADM2_FreeText1 | varchar |  |  | SI | FreeText1 |
| PAADM2_FreeText2 | varchar |  |  | SI | FreeText2 |
| PAADM2_FreeText3 | varchar |  |  | SI | FreeText3 |
| PAADM2_FreqAttendComments | varchar |  |  | SI | FreqAttendComments |
| PAADM2_FreqAttendConcernLev_DR | bigint |  | FK | SI | Des Ref FreqAttendConcernLev |
| PAADM2_FreqAttendUpdateDate | date |  |  | SI | FreqAttendUpdateDate |
| PAADM2_FreqAttendUpdateTime | time |  |  | SI | FreqAttendUpdateTime |
| PAADM2_FreqAttendUpdateUser_DR | bigint |  | FK | SI | Des Ref FreqAttendUpdateUser |
| PAADM2_FuncAssessDateAdm | date |  |  | SI | Functional Assessment Date on Admisson |
| PAADM2_FuncAssessDateDisch | date |  |  | SI | Functional Assessment Date on Discharge |
| PAADM2_GESReview | varchar |  |  | SI | GESReview |
| PAADM2_GPConsent | varchar |  |  | SI | GP Consent |
| PAADM2_GracePeriod | varchar |  |  | SI | Grace Period |
| PAADM2_GracePeriodReason | varchar |  |  | SI | Grace Period Reason |
| PAADM2_Guarantor_DR | varchar |  | FK | SI | Des Ref to PANok |
| PAADM2_HandedOverDoc_DR | varchar |  | FK | SI | Des Ref HandedOverDoc |
| PAADM2_HandedOverNurse_DR | varchar |  | FK | SI | Des Ref HandedOverNurse |
| PAADM2_HandoverDate | date |  |  | SI | HandoverDate |
| PAADM2_HandoverNotes | varchar |  |  | SI | HandoverNotes |
| PAADM2_HandoverTime | time |  |  | SI | HandoverTime |
| PAADM2_HospitalInsurance | varchar |  |  | SI | HospitalInsurance |
| PAADM2_ICUBedRequired | varchar |  |  | SI | ICU Bed Required |
| PAADM2_IndigLiasionVisit | varchar |  |  | SI | IndigLiasionVisit |
| PAADM2_InfFinConsent | varchar |  |  | SI | Informed Financial Consent |
| PAADM2_Injury | varchar |  |  | SI | Injury |
| PAADM2_InjuryActivityStatus_DR | bigint |  | FK | SI | Des Ref PACInjuryActivityStatus |
| PAADM2_InjuryMechanism_DR | bigint |  | FK | SI | Des Ref PACInjuryMechanism |
| PAADM2_IntendedDelivPlace_DR | bigint |  | FK | SI | Des Ref PAC_DeliveryPlace  |
| PAADM2_Latitude | varchar |  |  | SI | Latitude |
| PAADM2_LegalStatus_DR | bigint |  | FK | SI | Des Ref PACLegalStatusIndicator |
| PAADM2_Longitude | varchar |  |  | SI | Longitude |
| PAADM2_MHRConsent | varchar |  |  | SI | MHR Consent |
| PAADM2_MHRConsentEmergency | varchar |  |  | SI | MHR Consent |
| PAADM2_MedHisComments | varchar |  |  | SI | FreqAttendComments |
| PAADM2_MedHisStatus | varchar |  |  | SI | Medication History Status |
| PAADM2_MultiAppt | varchar |  |  | SI | MultiAppt |
| PAADM2_NFMICategDepart_DR | varchar |  | FK | SI | Des Ref CTNFMICategDepart  |
| PAADM2_Name | varchar |  |  | SI | Name |
| PAADM2_Name2 | varchar |  |  | SI | Name2 |
| PAADM2_Name3 | varchar |  |  | SI | Name3 |
| PAADM2_Name4 | varchar |  |  | SI | Name4 |
| PAADM2_NamedMidwife_DR | varchar |  | FK | SI | Des Ref NamedMidwife |
| PAADM2_NumberOfDNAs | double |  |  | SI | Number of not attended appointments |
| PAADM2_OTReg | varchar |  |  | SI | OT Registration |
| PAADM2_ObjectiveOutcomePat_DR | bigint |  | FK | SI | Des Ref ObjectiveOutcomePat  |
| PAADM2_ObjectiveOutcome_DR | bigint |  | FK | SI | Des Ref ObjectiveOutcome  |
| PAADM2_OnHold | varchar |  |  | SI | OnHold |
| PAADM2_OnHoldReason | varchar |  |  | SI | OnHoldReason |
| PAADM2_OnHoldReasonIDs | varchar |  |  | SI | OnHoldReasonFreeText |
| PAADM2_OnHoldReasons | varchar |  |  | SI | OnHoldReasons |
| PAADM2_OperationDate | date |  |  | SI | OperationDate |
| PAADM2_OperationTime | time |  |  | SI | OperationTime |
| PAADM2_OrderAdm_DR | bigint |  | FK | SI | Des Ref PAAdm - Original Admission in Ordering Hos... |
| PAADM2_OtherHospAdmNo | varchar |  |  | SI | Other Hospital Episode Number |
| PAADM2_OutstandingTasks | varchar |  |  | SI | OutstandingTasks |
| PAADM2_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| PAADM2_PANOK_DR | varchar |  | FK | SI | Des Ref PANOK |
| PAADM2_PAPersonPatMas_DR | bigint |  | FK | SI | Des Ref PAPersonPatMas |
| PAADM2_PARefPathwayStage_DR | varchar |  | FK | SI | Link to a patient referral pathway stage (REPORTIN... |
| PAADM2_PEARequestInd | varchar |  |  | SI | Pre-existing ailment |
| PAADM2_PalliativeCarePatDays | double |  |  | SI | PalliativeCarePatDays |
| PAADM2_ParentConsent | varchar |  |  | SI | Parent Consent |
| PAADM2_PatType_DR | bigint |  | FK | SI | Des Ref PatType |
| PAADM2_PractFCareProv_DR | varchar |  | FK | SI | Pract F Care Provider Des Ref |
| PAADM2_PractFSeenDate | date |  |  | SI | Pract F Seen Date |
| PAADM2_PractFSeenTime | time |  |  | SI | Pract F Seen Time |
| PAADM2_PreConversionStatus | varchar |  |  | SI | If episode is result of a conversion, keeps track ... |
| PAADM2_PreConversionType | varchar |  |  | SI | If episode is result of a conversion, keeps track ... |
| PAADM2_PreRegDate | date |  |  | SI | PreRegDate |
| PAADM2_PreRegTime | time |  |  | SI | PreRegTime |
| PAADM2_PrefAdmFacility_DR | bigint |  | FK | SI | Des Ref CTLoc |
| PAADM2_PrefGenderOfCareProvDR | bigint |  | FK | SI | Des Ref CTSex |
| PAADM2_PregnancyBeforeError_DR | bigint |  | FK | SI | Des Ref Pregnancy Before Pregnancy Was Marked Ente... |
| PAADM2_PresentingIllnessCode | varchar |  |  | SI | Presenting Illness Code |
| PAADM2_PresentingIllnessItemNum | varchar |  |  | SI | Presenting Illness Item Numbe |
| PAADM2_PrevSpecialTreatment_DR | bigint |  | FK | SI | Des Ref PrevSpecTreatment |
| PAADM2_PreviousProviderDays | double |  |  | SI | Number of days under the care of the previous prov... |
| PAADM2_PreviousProviderHrs | double |  |  | SI | Number of hours under the care of the previous pro... |
| PAADM2_PriorityHandover | varchar |  |  | SI | PriorityHandover |
| PAADM2_ProposedPriority_DR | bigint |  | FK | SI | Proposed Priority |
| PAADM2_ProvisionalDRG_DR | bigint |  | FK | SI | Des Ref MRCDRGCodes |
| PAADM2_RMCFCareProv_DR | varchar |  | FK | SI | First Seen By Rapid Management Clinician, des ref ... |
| PAADM2_Readmission | varchar |  |  | SI | Readmission |
| PAADM2_RefCareProvConsent | varchar |  |  | SI | Referring Care Provider Consent |
| PAADM2_RefOverrideType | varchar |  |  | SI | Referral Override Type Code |
| PAADM2_RefStatusReason_DR | bigint |  | FK | SI | Des Ref RefStatusReason |
| PAADM2_ReferralReason_DR | bigint |  | FK | SI | Des Ref PACReferralReason |
| PAADM2_ReferredToHospital_DR | bigint |  | FK | SI | Des Ref ReferredToHospital |
| PAADM2_ReqPreassDate | date |  |  | SI | Requested preassessment date |
| PAADM2_RequiredCoding | varchar |  |  | SI | Required Coding |
| PAADM2_SMSConsent | varchar |  |  | SI | SMS Consent |
| PAADM2_SelfGuarantor | varchar |  |  | SI | Self Guarantor |
| PAADM2_ServTax_DR | bigint |  | FK | SI | Des Ref ServTax |
| PAADM2_Service_DR | bigint |  | FK | SI | Des Ref Service |
| PAADM2_ShortStayComments | varchar |  |  | SI | Short Stay Comments |
| PAADM2_ShortStayIntent | varchar |  |  | SI | Short Stay Intent |
| PAADM2_ShortStayReason_DR | bigint |  | FK | SI | Des Ref to MRCShortStayReason |
| PAADM2_SignificantInstructions | varchar |  |  | SI | SignificantInstructions |
| PAADM2_SpecialProject_DR | bigint |  | FK | SI | Des Ref PACSpecialProject |
| PAADM2_StDateLegalStatClassif | date |  |  | SI | Start Date Legal Status Classification Assignment ... |
| PAADM2_StTimeLegalStatClassif | time |  |  | SI | Start Time Legal Status Classification Assignment ... |
| PAADM2_SystemSession | varchar |  |  | SI | SystemSession |
| PAADM2_TaskGroup_DR | bigint |  | FK | SI | Des Ref CTTaskAssignGroup  |
| PAADM2_Text1 | varchar |  |  | SI | Text1 |
| PAADM2_Text2 | varchar |  |  | SI | Text2 |
| PAADM2_TreatmentStream_DR | bigint |  | FK | SI | Des Ref PAC_TreatmentStream |
| PAADM2_TriageCatChReaComments | varchar |  |  | SI | TriageCategoryChangeReasonComment |
| PAADM2_TriageCatChangeReason_DR | bigint |  | FK | SI | Des Ref PACTriageCatChangeReason |
| PAADM2_TriageSympSum | varchar |  |  | SI | TriageSympSum |
| PAADM2_UserDefDate1 | date |  |  | SI | User Defined Date 1 |
| PAADM2_UserDefTime1 | time |  |  | SI | User Defined Time 1 |
| PAADM2_VerifiedCoding | varchar |  |  | SI | VerifiedCoding |
| PAADM2_ViewablebyEpLoc | varchar |  |  | SI | ViewablebyEpLoc |
| PAADM2_WalkIn | varchar |  |  | SI | WalkIn |
| Q01 | - |  |  | SI | Date of examination |
| Q02 | - |  |  | SI | Time of examination |
| Q03 | - |  |  | SI | Patient's level of alertness |
| Q04 | - |  |  | SI | Level of education |
| Q05 | - |  |  | SI | 1. Does the patient know the correct day of the we... |
| Q06 | - |  |  | SI | 2. Does the patient know what the correct year is? |
| Q07 | - |  |  | SI | 3. Does the patient know what city / town / countr... |
| Q08 | - |  |  | SI | 4. Please remember these five objects. I will ask ... |
| Q09 | - |  |  | SI | Apple. Pen. Tie. House. Car |
| Q10 | - |  |  | SI | 5. You have $100 and you go to the store and buy a... |
| Q11 | - |  |  | SI | Does the patient know the correct answer to the qu... |
| Q12 | - |  |  | SI | Does the patient know the correct answer to the qu... |
| Q13 | - |  |  | SI | 6. Please name as many animals as you can in one m... |
| Q14 | - |  |  | SI | 7. How many objects from Question #4 does the pati... |
| Q15 | - |  |  | SI | 8. I am going to give you a series of numbers and ... |
| Q16 | - |  |  | SI | Does the patient know the backward number for '87'... |
| Q17 | - |  |  | SI | Does the patient know the backward number for '648... |
| Q18 | - |  |  | SI | Does the patient know the backward number for '853... |
| Q19 | - |  |  | SI | Please provide image to patient and document accor... |
| Q20 | - |  |  | SI | 9. This is a clock face image - Please put in the ... |
| Q21 | - |  |  | SI | Does the patient put the hours marker okay? |
| Q22 | - |  |  | SI | Does the patient put the time correct? |
| Q23 | - |  |  | SI | 10. Object image - Does the patient put an 'X' in ... |
| Q24 | - |  |  | SI | Object image - Does the patient know which of the ... |
| Q25 | - |  |  | SI | 11. I am going to tell you a story. Please listen ... |
| Q26 | - |  |  | SI | Jill was a very successful stockbroker. She made a... |
| Q27 | - |  |  | SI | She married him and had three children. They lived... |
| Q28 | - |  |  | SI | Does the patient know what the female's name was? |
| Q29 | - |  |  | SI | Does the patient know what work did she do? |
| Q30 | - |  |  | SI | Does the patient know when did she go back to work... |
| Q31 | - |  |  | SI | Does the patient know what state did she live in? |
| Q32 | - |  |  | SI | SLUMS form is used to screen individuals to look f... |
| Q33 | - |  |  | SI | Begin by asking the patient the following: “Do you... |
| Q34 | - |  |  | SI | is by asking you some questions.” You may need to ... |
| Q35 | - |  |  | SI | What this tool does is check the amount of memory ... |
| Q36 | - |  |  | SI | Read the questions aloud clearly and slowly to the... |
| Q37 | - |  |  | SI | Score the questions as indicated on the examinatio... |
| Q38 | - |  |  | SI | a. On question No. 4, read the statement as listed... |
| Q39 | - |  |  | SI | that the patient heard and understood what you sai... |
| Q40 | - |  |  | SI | b. On question  No. 5, make sure the patient is fo... |
| Q41 | - |  |  | SI | you have left?”).  Do not prompt or give hints, bu... |
| Q42 | - |  |  | SI | c. Redirect the patient’s attention if necessary b... |
| Q43 | - |  |  | SI | d. On question No. 8, state each number by its ind... |
| Q44 | - |  |  | SI | On question No. 9, either draw a large circle on t... |
| Q45 | - |  |  | SI | When scoring, give full credit for either all 12 n... |
| Q46 | - |  |  | SI | for full credit. When scoring the correct time, ma... |
| Q47 | - |  |  | SI | You may also provide a separate sheet with larger ... |
| Q48 | - |  |  | SI | be created by enlarging the figures on the examina... |
| Q49 | - |  |  | SI | Read question No. 11 as written, and provide ample... |
| Q50 | - |  |  | SI | read it to them. Do not prompt or give hints. The ... |
| Q51 | - |  |  | SI | Score |
| Q52 | - |  |  | SI | Classification |
| Q53 | - |  |  | SI | The answer of Chicago as the state she lives in ge... |
| Q54 | - |  |  | SI | High school education |
| Q55 | - |  |  | SI | 27 - 30 |
| Q56 | - |  |  | SI | 21 - 26 |
| Q57 | - |  |  | SI | 1 - 20 |
| Q58 | - |  |  | SI | Less than high school education |
| Q59 | - |  |  | SI | 25 - 30 |
| Q60 | - |  |  | SI | 20 - 24 |
| Q61 | - |  |  | SI | 1 - 19 |
| Q62 | - |  |  | SI | The Saint Louis University Mental Status exam is a... |
| Q63 | - |  |  | SI | . |
| Q64 | - |  |  | SI | • |
| Q65 | - |  |  | SI | For example, if I say 42, you would say 24. |
| Q66 | - |  |  | SI | When they were teenagers, she went back to work. S... |
| Q67 | - |  |  | SI | The purpose of the form is to screen individuals t... |
| Q68 | - |  |  | SI | : |
| Q69 | - |  |  | SI | Normal |
| Q70 | - |  |  | SI | Mild Neurocognitive Disorder |
| Q71 | - |  |  | SI | Dementia |
| Q72 | - |  |  | SI | Normal |
| Q73 | - |  |  | SI | Mild Neurocognitive Disorder |
| Q74 | - |  |  | SI | Dementia |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*