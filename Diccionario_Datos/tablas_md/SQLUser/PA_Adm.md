# SQLUser.PA_Adm

**Schema:** SQLUser
**Columnas:** 347
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla principal de **Admisiones de Pacientes**.

Registra cada episodio de atencion:
- Admisiones ambulatorias (consultas, urgencias)
- Admisiones hospitalarias (hospitalizacion)
- Admisiones de urgencia

**Campos clave:**
- PAADM_ADMNo: Numero de admision unico
- PAADM_PAPMI_DR: FK a PA_PatMas (paciente)
- PAADM_AdmDate/Time: Fecha y hora de admision
- PAADM_Type: Tipo de admision (I=Inpatient, O=Outpatient, E=Emergency)
- PAADM_CurrentMRADM_DR: FK a registro medico activo

**Relaciones principales:**
- PA_PatMas: Datos del paciente
- CT_Loc: Ubicacion/servicio
- CT_CarPrv: Medico responsable

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAADM_RowID | bigint | PK |  | NO | - |
| PAADM_ADMNo | varchar |  |  | SI | Admission No |
| PAADM_AEArrivalMode_DR | bigint |  | FK | SI | Des Ref AEArrivalMode |
| PAADM_ActivityInjured_DR | bigint |  | FK | SI | Des Ref Activity When Injured |
| PAADM_AdmCateg_DR | bigint |  | FK | SI | Des Ref to AdmCateg |
| PAADM_AdmDate | date |  |  | SI | Admission Date |
| PAADM_AdmDocCodeDR | varchar |  | FK | SI | Des Ref to CTPCP |
| PAADM_AdmMethod_DR | bigint |  | FK | SI | Des Ref AdmMethod |
| PAADM_AdmReadm | varchar |  |  | SI | Admission/Readmission |
| PAADM_AdmReason_DR | bigint |  | FK | SI | Des Ref AdmReason |
| PAADM_AdmRef | varchar |  |  | SI | Adm Reference |
| PAADM_AdmSrc_DR | bigint |  | FK | SI | Adm Source |
| PAADM_AdmTime | time |  |  | SI | Admission Time |
| PAADM_AdmissionFIM | varchar |  |  | SI | Admission FIM |
| PAADM_AgreedEDD | date |  |  | SI | Date of agreed EDD |
| PAADM_AppointBookingSystem_DR | bigint |  | FK | SI | Des Ref AppointBookingSystem |
| PAADM_AppointTransport_DR | bigint |  | FK | SI | Des Ref AppointTransport |
| PAADM_Appoint_DR | varchar |  | FK | SI | Des Ref RB_Appoint |
| PAADM_ApptMethod_DR | bigint |  | FK | SI | Des Ref to ApptMethod |
| PAADM_AuditLetterResponse | varchar |  |  | SI | Audit Letter Response |
| PAADM_AutocodeRequired | varchar |  |  | SI | Autocode Required |
| PAADM_BarthelScore | double |  |  | SI | Barthel Score |
| PAADM_BedMobility_DR | bigint |  | FK | SI | Des Ref BedMobility |
| PAADM_BillFlag | varchar |  |  | SI | To indicate admission is financially dischag |
| PAADM_BillingMethod_DR | bigint |  | FK | SI | Des Ref BillingMethod |
| PAADM_BookLocReady | varchar |  |  | SI | Book Loc Ready |
| PAADM_CClass | varchar |  |  | SI | C Class |
| PAADM_CancelReason_DR | bigint |  | FK | SI | Des Ref CancelReason |
| PAADM_CaseManager_DR | varchar |  | FK | SI | Des Ref CaseManager |
| PAADM_CauseInj_DR | bigint |  | FK | SI | Des Ref CauseInj |
| PAADM_ChaplainChurchAddress | varchar |  |  | SI | ChaplainChurchAddress |
| PAADM_ChaplainName | varchar |  |  | SI | Chaplain Name |
| PAADM_ChaplainPhone | varchar |  |  | SI | Chaplain Phone |
| PAADM_ClinicalSubProgram_DR | bigint |  | FK | SI | Des Ref ClinicalSubProgram |
| PAADM_CodingUpdateDate | date |  |  | SI | CodingUpdateDate |
| PAADM_CodingUpdateTime | time |  |  | SI | CodingUpdateTime |
| PAADM_CodingUpdateUser_DR | bigint |  | FK | SI | Des Ref CodingUpdateUser |
| PAADM_Completed | varchar |  |  | SI | Completed |
| PAADM_ConfidentMessage | varchar |  |  | SI | Confidential Message |
| PAADM_Confidential | varchar |  |  | SI | Confidential Flag |
| PAADM_ConfirmReferral | varchar |  |  | SI | Confirm Referral |
| PAADM_ConsentDVA | varchar |  |  | SI | Consent DVA |
| PAADM_ConsentDepOfDefence | varchar |  |  | SI | Consent Dep Of Defence |
| PAADM_ConsentFeedback | varchar |  |  | SI | Consent Feedback |
| PAADM_ConsentMotorVehicle | varchar |  |  | SI | Consent Motor Vehicle |
| PAADM_ConsentPatSatisfSurve | varchar |  |  | SI | Consent to undertake Pat Satisf Survey |
| PAADM_ConsentRecFundInfo | varchar |  |  | SI | Consent to Receive Fundrising Information |
| PAADM_ConsentWorkCompens | varchar |  |  | SI | Consent Work Compens |
| PAADM_ContractRole_DR | bigint |  | FK | SI | Des Ref ContractRole |
| PAADM_ContractSpoke_DR | bigint |  | FK | SI | Des Ref ContractSpoke |
| PAADM_ContractType_DR | bigint |  | FK | SI | Des Ref ContractType |
| PAADM_ConvertDate | date |  |  | SI | Convert Date |
| PAADM_ConvertTime | time |  |  | SI | Convert Time |
| PAADM_ConvertUser_DR | bigint |  | FK | SI | Des Ref ConvertUser |
| PAADM_ConvertedFromOut | varchar |  |  | SI | Converted From Out Patient Episode |
| PAADM_CreateDate | date |  |  | SI | Create Date |
| PAADM_CreatePreadmission | varchar |  |  | SI | Create Preadmission |
| PAADM_CreateTime | time |  |  | SI | Create Time |
| PAADM_CreateUser | bigint |  |  | SI | Create User |
| PAADM_Current | varchar |  |  | SI | Current |
| PAADM_CurrentBed_DR | varchar |  | FK | SI | Des Ref PAC Bed |
| PAADM_CurrentProcess_DR | bigint |  | FK | SI | Des Ref Process |
| PAADM_CurrentResource_DR | bigint |  | FK | SI | Des Ref Current Resource |
| PAADM_CurrentRoom_DR | bigint |  | FK | SI | Des Ref to Room |
| PAADM_CurrentWard_DR | bigint |  | FK | SI | Des Ref to Ward |
| PAADM_DNAReason | bigint |  |  | SI | Des Ref DNAReason |
| PAADM_DateAssessmentCompleted | date |  |  | SI | Date Assessment Completed |
| PAADM_DateDischHosp | date |  |  | SI | Date Disch Hosp |
| PAADM_DateFirstAppt | date |  |  | SI | Date First Appt |
| PAADM_DateHCPRequestSent | date |  |  | SI | Date HCP Request Sent |
| PAADM_DateHCPreceived | date |  |  | SI | DateHCPreceived |
| PAADM_DateOfEntry | date |  |  | SI | Date Of Entry |
| PAADM_DateOfInterview | date |  |  | SI | Date Of Interview |
| PAADM_DatePatRefferedAssess | date |  |  | SI | Date Pat Reffered for Assess |
| PAADM_DateReceived | date |  |  | SI | Date Received |
| PAADM_DateRefDecision | date |  |  | SI | Date of Decision to refer patient |
| PAADM_DateSocialWorkerAlloc | date |  |  | SI | Date Social Worker Alloc |
| PAADM_DateSocialWorkerCompleted | date |  |  | SI | Date Social Worker Completed |
| PAADM_DaySurgeryType | varchar |  |  | SI | Day Surgery Type |
| PAADM_DaysCarriedForward | double |  |  | SI | DaysCarriedForward |
| PAADM_DelayReason | varchar |  |  | SI | Delay Reason |
| PAADM_DepCode_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| PAADM_DietType_DR | bigint |  | FK | SI | Des Ref to DTCDietType(order subcat) |
| PAADM_DischComments | varchar |  |  | SI | Discharge Comments |
| PAADM_DischCond_DR | bigint |  | FK | SI | Des Ref to PACDischCond |
| PAADM_DischargeAppoint_DR | varchar |  | FK | SI | Discharge Appointment for in patients des ref |
| PAADM_DischargeBarthelScore | double |  |  | SI | Discharge Barthel Score |
| PAADM_DischargeFIM | varchar |  |  | SI | Discharge FIM |
| PAADM_DischgDate | date |  |  | SI | Discharge Date |
| PAADM_DischgDoc_DR | varchar |  | FK | SI | Des Ref to CTPCP |
| PAADM_DischgHospital | varchar |  |  | SI | DischgHospital |
| PAADM_DischgTime | time |  |  | SI | Discharge Time |
| PAADM_Dispos_DR | bigint |  | FK | SI | Des Ref to CTDSP |
| PAADM_DoctorLetterNotes | varchar |  |  | SI | Doctor Letter Notes |
| PAADM_EDDBasedOnLMP | date |  |  | SI | Date of estimated EDD based on LMP |
| PAADM_Eating_DR | bigint |  | FK | SI | Des Ref Eating |
| PAADM_EmergencyDate | date |  |  | SI | Emergency Date |
| PAADM_EmergencyNo | varchar |  |  | SI | Emergency Number |
| PAADM_EmergencyStatus | varchar |  |  | SI | Emergency Status |
| PAADM_EmergencyTime | time |  |  | SI | Emergency Time |
| PAADM_Epissubtype_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| PAADM_EstDischConfirmed | varchar |  |  | SI | Estimated Discharge Confirmed |
| PAADM_EstimDischargeDate | date |  |  | SI | Estimated Discharge Date |
| PAADM_EstimDischargeTime | time |  |  | SI | Estimated Discharge Time |
| PAADM_EstimOperDate | date |  |  | SI | Estimated Operation Date |
| PAADM_ExpAdmDate | date |  |  | SI | Expected Admission Date |
| PAADM_ExpLOS | double |  |  | SI | Expected Length Of Stay  |
| PAADM_FamilyDoctor | varchar |  |  | SI | FamilyDoctor |
| PAADM_FinDischDate | date |  |  | SI | FinDischDate |
| PAADM_FinDischTime | time |  |  | SI | Fin Disch Time |
| PAADM_FirstOrReadmis | varchar |  |  | SI | First Or Readmission flag |
| PAADM_FlaggedPatient | varchar |  |  | SI | Flagged Patient |
| PAADM_FrequentAdmissions | varchar |  |  | SI | Frequent Admissions |
| PAADM_FundingArrangement_DR | bigint |  | FK | SI | Des Ref FundingArrangement |
| PAADM_GuaranteeAdmDate | date |  |  | SI | Guarantee Adm Date |
| PAADM_HCA_DR | bigint |  | FK | SI | Des Ref HCA_DR |
| PAADM_HCPPriority_DR | bigint |  | FK | SI | Des Ref HCPPriority |
| PAADM_HCP_DR | bigint |  | FK | SI | Des Ref HCP |
| PAADM_HCR_DR | bigint |  | FK | SI | Des Ref HCR |
| PAADM_HasCommunSocWorker | varchar |  |  | SI | Has Commun Soc Worker |
| PAADM_HasFunding | varchar |  |  | SI | Has Funding |
| PAADM_HomerID | varchar |  |  | SI | Homer ID |
| PAADM_HospChaplainVisitReq | varchar |  |  | SI | Hosp Chaplain Visit Required |
| PAADM_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAADM_HumanIntent_DR | bigint |  | FK | SI | Des Ref Human Intent |
| PAADM_InPatAdmType_DR | bigint |  | FK | SI | Des Ref InPatAdmType |
| PAADM_InPatNo | varchar |  |  | SI | In Patient Number |
| PAADM_Infect_DR | bigint |  | FK | SI | Des Ref to PACInfect |
| PAADM_InjuryIncidentDate | date |  |  | SI | InjuryIncidentDate |
| PAADM_InpatBedReqDate | date |  |  | SI | Inpat Bed Request Date |
| PAADM_InpatBedReqTime | time |  |  | SI | Inpat Bed Req Time |
| PAADM_InternalRefDoc_DR | varchar |  | FK | SI | Des Ref CTPCP |
| PAADM_InternalRefLoc_DR | bigint |  | FK | SI | Des Ref InternalRefLoc |
| PAADM_InterviewRec | varchar |  |  | SI | Interview Rec |
| PAADM_InterviewedBy | varchar |  |  | SI | Interviewed By |
| PAADM_Isolate | varchar |  |  | SI | Isolate |
| PAADM_LMP | date |  |  | SI | Date of LMP |
| PAADM_LabClinicalCondition | varchar |  |  | SI | Lab Clinical Condition |
| PAADM_LabourAccident_DR | bigint |  | FK | SI | Des Ref LabourAccident |
| PAADM_LastContactFamily | date |  |  | SI | Last Contact Family |
| PAADM_LikelihoodAdmit | varchar |  |  | SI | Likelihood to Admit |
| PAADM_LikelyTransICU_DR | bigint |  | FK | SI | Des Ref LikelyTransICU |
| PAADM_LocalAuthority_DR | bigint |  | FK | SI | Des Ref LocalAuthority |
| PAADM_LocationAtTelehealth | bigint |  |  | SI | Patients Location at time of Telehealth presentati... |
| PAADM_LongStay | varchar |  |  | SI | Long Stay |
| PAADM_MainMRADM_DR | bigint |  | FK | SI | Des Ref to MRADM (Main) |
| PAADM_MajorIncident_DR | bigint |  | FK | SI | Des Ref MajorIncident |
| PAADM_MaritalStatus_DR | bigint |  | FK | SI | Des Ref Marital Status |
| PAADM_MaternityVisType_DR | bigint |  | FK | SI | Des Ref MaternityVisType |
| PAADM_MealPreference | varchar |  |  | SI | Meal Preference |
| PAADM_MedDischDate | date |  |  | SI | MedDischDate |
| PAADM_MedDischDoc_DR | varchar |  | FK | SI | Des REf CTCP |
| PAADM_MedDischTime | time |  |  | SI | MedDischTime |
| PAADM_MedicalDischarge | varchar |  |  | SI | Medical Discharge |
| PAADM_MethodRef_DR | bigint |  | FK | SI | Des Ref MethodRef |
| PAADM_MiniMentalAssScore | double |  |  | SI | Mini Mental Ass Score |
| PAADM_MotherAdm_DR | bigint |  | FK | SI | Des Ref MotherAdm_DR |
| PAADM_NonGovOrg_DR | bigint |  | FK | SI | Des Ref NonGovOrg |
| PAADM_NursingNotesFlag | varchar |  |  | SI | Nursing Notes Flag |
| PAADM_OESubCat_DR | bigint |  | FK | SI | Des Ref OESubCat |
| PAADM_OSVCountryFrom_DR | bigint |  | FK | SI | Des Ref OSVCountryFrom |
| PAADM_OSVisitStatus_DR | bigint |  | FK | SI | Des Ref OSVisitStatus |
| PAADM_Occupation_DR | bigint |  | FK | SI | Des Ref Occupation |
| PAADM_OnsetDate | date |  |  | SI | Onset Date |
| PAADM_Oper_DR | bigint |  | FK | SI | Des Ref to ORCOper |
| PAADM_OrderTime | time |  |  | SI | Order Time |
| PAADM_OriginalAdmissionDR | bigint |  | FK | SI | Original Admission |
| PAADM_OtherDischType | varchar |  |  | SI | Other Discharge Type |
| PAADM_OtherHospital | varchar |  |  | SI | Other Hospital |
| PAADM_OtherInfectType | varchar |  |  | SI | Other Infection Type |
| PAADM_OverseasVisitor | varchar |  |  | SI | Overseas Visitor |
| PAADM_OwnMinisterIndicator | varchar |  |  | SI | Own Minister Indicator |
| PAADM_PAAdm2_DR | bigint |  | FK | SI | Des Ref PAAdm2 |
| PAADM_PAPMI_DR | bigint |  | FK | NO | Des Ref to PAPMI |
| PAADM_PaidEmergencySurcharge | varchar |  |  | SI | Has the emergency surcharge been paid |
| PAADM_PalliativeCare_DR | bigint |  | FK | SI | Des Ref Palliative Care |
| PAADM_ParentWard_DR | bigint |  | FK | SI | Des Ref ParentWard |
| PAADM_PatAcuity_DR | bigint |  | FK | SI | Des Ref PatAcuity |
| PAADM_PatClassif_DR | bigint |  | FK | SI | Des Ref PatClassif |
| PAADM_PatDestination | varchar |  |  | SI | Pat Destination |
| PAADM_PatType_DR | varchar |  | FK | SI | Not Used Des Ref to CTPTC |
| PAADM_PatientContacted | varchar |  |  | SI | PatientContacted |
| PAADM_PatientLetterNotes | varchar |  |  | SI | PatientLetterNotes |
| PAADM_PermanentResident | varchar |  |  | SI | Permanent Resident |
| PAADM_PersonRespPayment | varchar |  |  | SI | Person Resp Payment |
| PAADM_PersonResponsiblePayment | bigint |  |  | SI | Des Ref Person Responsible Payment |
| PAADM_PlaceOfInj_DR | bigint |  | FK | SI | Des Ref PlaceOfInj |
| PAADM_PoliceDivision | varchar |  |  | SI | Police Division |
| PAADM_PostDischStatus_DR | bigint |  | FK | SI | Des Ref PostDischStatus |
| PAADM_PreAdmNo | varchar |  |  | SI | Pre Admission Number |
| PAADM_PreAdmitDate | date |  |  | SI | Pre Admit Date |
| PAADM_PreAdmitTime | time |  |  | SI | Pre Admit Time |
| PAADM_PreAdmitted | varchar |  |  | SI | Pre - Admitted |
| PAADM_Pregnancy_DR | bigint |  | FK | SI | Des Ref Pregnancy |
| PAADM_PrevInPatAdmPalliativeCare | varchar |  |  | SI | PrevInPatAdmPalliativeCare |
| PAADM_PrevNonInPatPalliativeCare | varchar |  |  | SI | PrevNonInPatPalliativeCare |
| PAADM_PreviousProcess_DR | bigint |  | FK | SI | Des Ref Process |
| PAADM_Priority_DR | bigint |  | FK | SI | Que Priority |
| PAADM_QualifStatus_DR | bigint |  | FK | SI | Des Ref QualifStatus |
| PAADM_RBCCancelReason_DR | bigint |  | FK | SI | Des Ref RBCCancelReason |
| PAADM_RUGTotal | double |  |  | SI | RUG Total |
| PAADM_ReadOnly | varchar |  |  | SI | Read Only |
| PAADM_ReadmToRehab_DR | bigint |  | FK | SI | Des Ref ReadmToRehab |
| PAADM_ReasonDelDisch_DR | bigint |  | FK | SI | Des Ref ReasonDelDisch |
| PAADM_ReasonNotRegFee | bigint |  |  | SI | Reason For Not Collect Reg Fee |
| PAADM_RefAdm_DR | bigint |  | FK | SI | Des Ref to RefAdm |
| PAADM_RefApprovNo | varchar |  |  | SI | Referral Approval Number |
| PAADM_RefClinTo_DR | bigint |  | FK | SI | Des Ref RefClinTo |
| PAADM_RefClinic_DR | bigint |  | FK | SI | Des Ref to CTRFC |
| PAADM_RefDate | date |  |  | SI | Referral Date |
| PAADM_RefDocClinic_DR | varchar |  | FK | SI | Des Ref RefDocClinic |
| PAADM_RefDocCodeDR | varchar |  | FK | SI | Ref Doctor Text |
| PAADM_RefDocList_DR | bigint |  | FK | SI | Des Ref RefDocList |
| PAADM_RefDrConsent | varchar |  |  | SI | Ref Dr Consent |
| PAADM_RefExpiryDate | date |  |  | SI | Referral Expiry Date |
| PAADM_RefOrgAddress | varchar |  |  | SI | RefOrgAddress |
| PAADM_RefPeriod_DR | bigint |  | FK | SI | Des Ref RefPeriod |
| PAADM_RefStat_DR | bigint |  | FK | SI | Des Ref RefStat |
| PAADM_RefToNGOContactName | varchar |  |  | SI | Ref To NGO Contact Name |
| PAADM_RefToNonGov_DR | bigint |  | FK | SI | Des Ref RefToNonGov |
| PAADM_ReferralPriority_DR | bigint |  | FK | SI | Des Ref Referral Priority |
| PAADM_ReferralType | bigint |  |  | SI | Referral Type |
| PAADM_Region_DR | bigint |  | FK | SI | Des Ref Region |
| PAADM_RegistrationFee | varchar |  |  | SI | Registration Fee Flag |
| PAADM_RejectionReason | varchar |  |  | SI | Rejection Reason |
| PAADM_Related | varchar |  |  | SI | Related |
| PAADM_Remark | varchar |  |  | SI | Comment |
| PAADM_ReportDate | date |  |  | SI | Report Date |
| PAADM_RequestMR | varchar |  |  | SI | Request MR |
| PAADM_RoomType_DR | bigint |  | FK | SI | Des Ref to PACRoomType |
| PAADM_SecondaryReason_DR | bigint |  | FK | SI | Des Ref SecondaryReason |
| PAADM_SeenDate | date |  |  | SI | Seen Date |
| PAADM_SeenTime | time |  |  | SI | Seen Time |
| PAADM_SeriousDisease | bigint |  |  | SI | PAADM_SeriousDisease |
| PAADM_ServiceTypeOutlet_DR | bigint |  | FK | SI | Service Type Outlet |
| PAADM_ShowInFutureEpisode | varchar |  |  | SI | Show In Future Episode |
| PAADM_SocialWorkerCentre_DR | bigint |  | FK | SI | Des Ref SocialWorkerCentre |
| PAADM_SocialWorkerName | varchar |  |  | SI | Social Worker Name |
| PAADM_SourceOfAttend_DR | bigint |  | FK | SI | Des Ref SourceOfAttend |
| PAADM_SourceRef_DR | bigint |  | FK | SI | Des Ref to PACAR |
| PAADM_SpecialCategory | varchar |  |  | SI | Special Category |
| PAADM_SpecialDocument | varchar |  |  | SI | Special Document |
| PAADM_Specialty_DR | varchar |  | FK | SI | Should the patient be charged for specialist |
| PAADM_SpecificLoc | varchar |  |  | SI | Specific Location |
| PAADM_StatePPP_DR | bigint |  | FK | SI | Des Ref StatePPP |
| PAADM_StudentMRADM_DR | bigint |  | FK | SI | Student Des Ref to MRADM |
| PAADM_SuspectCancerType_DR | bigint |  | FK | SI | Des Ref SuspectCancerType |
| PAADM_TelephoneActive | varchar |  |  | SI | Telephone Active |
| PAADM_TempLocDate | date |  |  | SI | TempLocDate |
| PAADM_TempLocTime | time |  |  | SI | TempLocTime |
| PAADM_TempLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PAADM_TermChiefComplaintCode | varchar |  |  | SI | Code - if Chief Complaint Terminology link was use... |
| PAADM_TermChiefComplaintDesc | varchar |  |  | SI | Description - if Chief Complaint Terminology link ... |
| PAADM_TermChiefComplaintSelected | varchar |  |  | SI | Selected Description - if Chief Complaint Terminol... |
| PAADM_TerminologyInjuryCode | varchar |  |  | SI | Code - if Injury Terminology link was used (e.g. E... |
| PAADM_TerminologyInjuryDesc | varchar |  |  | SI | Description - if Injury Terminology link was used ... |
| PAADM_TerminologyInjurySelected | varchar |  |  | SI | Selected Description - if Injury Terminology link ... |
| PAADM_Toileting_DR | bigint |  | FK | SI | Des Ref Toileting |
| PAADM_TrafficAccident_DR | bigint |  | FK | SI | TrafficAccident_DR |
| PAADM_TransferFacility | varchar |  |  | SI | Transfer Facility |
| PAADM_Transfer_DR | bigint |  | FK | SI | Des Ref Transfer |
| PAADM_TreatingDr_DR | varchar |  | FK | SI | Des Ref TreatingDr |
| PAADM_TriageDate | date |  |  | SI | Triage Date |
| PAADM_TriageNurse_DR | varchar |  | FK | SI | Des Ref CTPCP |
| PAADM_TriageTime | time |  |  | SI | Triage Time |
| PAADM_TumourSiteGroup_DR | bigint |  | FK | SI | Des Ref TumourSiteGroup |
| PAADM_Type | varchar |  |  | NO | Admission Type |
| PAADM_Type_of_Patient_Calc | varchar |  |  | SI | Type of Patient (Calculated) |
| PAADM_UpdateDate | date |  |  | SI | UpdateDate |
| PAADM_UpdateTime | time |  |  | SI | UpdateTime |
| PAADM_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PAADM_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| PAADM_Urgent | varchar |  |  | SI | Urgent |
| PAADM_UsualAccom_DR | bigint |  | FK | SI | Des Ref PACUsualAccomodation |
| PAADM_Verified | varchar |  |  | SI | Verified |
| PAADM_ViewablebyEpCareProv | varchar |  |  | SI | Only Viewable by Episode CareProv |
| PAADM_VisitStatus | varchar |  |  | SI | Visit Status |
| PAADM_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Overall impression |
| Q04 | - |  |  | SI | Diet |
| Q05 | - |  |  | SI | Recommended diet |
| Q06 | - |  |  | SI | Solids |
| Q07 | - |  |  | SI | Liquids |
| Q08 | - |  |  | SI | Diet comments |
| Q09 | - |  |  | SI | Precautions |
| Q10 | - |  |  | SI | Diet safety precautions |
| Q11 | - |  |  | SI | Diet safety precaution comments |
| Q12 | - |  |  | SI | General precautions |
| Q13 | - |  |  | SI | Review |
| Q14 | - |  |  | SI | Review in |
| Q15 | - |  |  | SI | Ear Nose Throat (ENT) investigation indicated? |
| Q16 | - |  |  | SI | Videofluoroscopy indicated? |
| Q17 | - |  |  | SI | Plan comments |
| Q18 | - |  |  | SI | Intervention program |
| Q19 | - |  |  | SI | Referrals |
| Q20 | - |  |  | SI | Referral orders placed in TrakCare? |
| Q21 | - |  |  | SI | Referral(s) external to TrakCare |
| Q22 | - |  |  | SI | Referral(s) external to TrakCare comment |
| Q23 | - |  |  | SI | Referral(s) external to TrakCare completed? |
| Q24 | - |  |  | SI | Referral detail |
| Q25 | - |  |  | SI | Education provided to |
| Q26 | - |  |  | SI | Education provided to - other |
| Q27 | - |  |  | SI | Type of education provided |
| Q28 | - |  |  | SI | Education details |
| Q29 | - |  |  | SI | General precaution comments |
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