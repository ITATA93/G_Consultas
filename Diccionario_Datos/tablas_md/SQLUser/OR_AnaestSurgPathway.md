# SQLUser.OR_AnaestSurgPathway

**Schema:** SQLUser
**Columnas:** 260
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SURPW_ParRef | varchar | PK |  | NO | OR_Anaesthesia Parent Reference |
| ChildQ16DR | - |  |  | SI | Child Reference: Interpreters present |
| Q01Q1 | - |  |  | SI | Name |
| Q01Q2 | - |  |  | SI | Relationship |
| Q01Q3 | - |  |  | SI | Relationship |
| Q01Q4 | - |  |  | SI | Location |
| Q01Q5 | - |  |  | SI | Time arrived |
| Q01Q6 | - |  |  | SI | Time departed |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SURPW_AdditionOfCountCorrect | varchar |  |  | SI | Addition of Count Correct |
| SURPW_AdditionalComments | varchar |  |  | SI | AdditionalComments |
| SURPW_Adrenaline | varchar |  |  | SI | Adrenaline |
| SURPW_Allergy | varchar |  |  | SI | Allergy |
| SURPW_AnaestMachineChecked | varchar |  |  | SI | AnaestheticMachineChecked |
| SURPW_AnaestOperation_DR | varchar |  | FK | SI | Des Ref ORAnaestOperation |
| SURPW_AnaesthDurat | double |  |  | SI | AnaestheticDuration  |
| SURPW_AnaestheticAssistant_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_AnaestheticFinishDate | date |  |  | SI | AnaestheticFinishDate |
| SURPW_AnaestheticFinishTime | time |  |  | SI | AnaestheticFinishTime |
| SURPW_AnaestheticStartDate | date |  |  | SI | AnaestheticStartDate |
| SURPW_AnaestheticStartTime | time |  |  | SI | AnaestheticStartTime |
| SURPW_AnaesthetistStatus_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffStatus |
| SURPW_Anaesthetist_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_AntibGivenLast60 | varchar |  |  | SI | Antibiotic prophylaxis given in the last 60mins |
| SURPW_AntibioticGiven | varchar |  |  | SI | AntibioticGiven |
| SURPW_AppMonPulseOximeter | varchar |  |  | SI | Appropriate monitoring including pulse oximeter |
| SURPW_AreaDurat | double |  |  | SI | AreaDuration |
| SURPW_AreaInDate | date |  |  | SI | AreaInDate |
| SURPW_AreaInTime | time |  |  | SI | AreaInTime |
| SURPW_AreaOutDate | date |  |  | SI | AreaOutDate |
| SURPW_AreaOutTime | time |  |  | SI | AreaOutTime |
| SURPW_Bacterial | varchar |  |  | SI | Bacterial |
| SURPW_BandOrInject | varchar |  |  | SI | Banding or Injection |
| SURPW_Biopsy | varchar |  |  | SI | Biopsy |
| SURPW_BloodAvail_DR | bigint |  | FK | SI | Des Ref BloodAvailability |
| SURPW_BrilliantPeel | varchar |  |  | SI | BrilliantPeel |
| SURPW_Bronchoscopy | varchar |  |  | SI | Bronchoscopy |
| SURPW_ByPassLocation_DR | bigint |  | FK | SI | Des Ref CTLoc |
| SURPW_ByPassRecovery | varchar |  |  | SI | ByPassRecovery |
| SURPW_Cellugel | varchar |  |  | SI | Cellugel |
| SURPW_ChangeOverCount | varchar |  |  | SI | Change Over Count |
| SURPW_ChangeOverCountCompletedBy_DR | varchar |  | FK | SI | Change Over Count Completed By |
| SURPW_ChangeOverCountDate | date |  |  | SI | Change Over Count Date |
| SURPW_ChangeOverCountTime | time |  |  | SI | Change Over Count Time |
| SURPW_ChildSub | numeric |  |  | NO | ChildSub |
| SURPW_ChkOther | varchar |  |  | SI | Other |
| SURPW_ClampOffDate | date |  |  | SI | Requested field for clamp off date |
| SURPW_ClampOnDate | date |  |  | SI | Requested field for clamp on date |
| SURPW_ClampSite1 | varchar |  |  | SI | Clamp Site 1 |
| SURPW_ClampSite2 | varchar |  |  | SI | Clamp Site 2 |
| SURPW_ClampSite3 | varchar |  |  | SI | Clamp Site 3 |
| SURPW_ClampSite4 | varchar |  |  | SI | Clamp Site 4 |
| SURPW_ClampTimeOff1 | time |  |  | SI | Clamp 1 Time Off |
| SURPW_ClampTimeOff2 | time |  |  | SI | Clamp 2 Time Off |
| SURPW_ClampTimeOff3 | time |  |  | SI | Clamp 3 Time Off |
| SURPW_ClampTimeOff4 | time |  |  | SI | Clamp 4 Time Off |
| SURPW_ClampTimeOn1 | time |  |  | SI | Clamp 1 Time On |
| SURPW_ClampTimeOn2 | time |  |  | SI | Clamp 2 Time On |
| SURPW_ClampTimeOn3 | time |  |  | SI | Clamp 3 Time On |
| SURPW_ClampTimeOn4 | time |  |  | SI | Clamp 4 Time On |
| SURPW_ClampType1_DR | bigint |  | FK | SI | Des ref Clamp 1 Type |
| SURPW_ClampType2_DR | bigint |  | FK | SI | Des ref Clamp 2 Type |
| SURPW_ClampType3_DR | bigint |  | FK | SI | Des ref Clamp 3 Type |
| SURPW_ClampType4_DR | bigint |  | FK | SI | Des ref Clamp 4 Type |
| SURPW_CleaningStartedDate | date |  |  | SI | CleaningStartedDate |
| SURPW_CleaningStartedTime | time |  |  | SI | CleaningStartedTime |
| SURPW_Colonoscopy | varchar |  |  | SI | Colonoscopy |
| SURPW_Comments | varchar |  |  | SI | Comments |
| SURPW_ConfAllTeamListed | varchar |  |  | SI | ConfirmAllTeamListed |
| SURPW_ConfirmsWithTeamOnSignOut | varchar |  |  | SI | ConfirmsWithTeamOnSignOut |
| SURPW_ConsultingAnaesthetistStatus_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffStatus |
| SURPW_ConsultingAnaesthetist_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_CorrectImagingChecked | varchar |  |  | SI | CorrectImagingChecked |
| SURPW_CorrectPatient | varchar |  |  | SI | CorrectPatient |
| SURPW_CreateDate | date |  |  | SI | CreateDate |
| SURPW_CreateTime | time |  |  | SI | CreateTime |
| SURPW_Cytology | varchar |  |  | SI | Cytology |
| SURPW_CytologyComments | varchar |  |  | SI | Cytology Comments |
| SURPW_Dexamethasone | varchar |  |  | SI | Dexamethasone |
| SURPW_DiathermyAppliedBy_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_DiathermyRemovedBy_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_DifficultyAirway | varchar |  |  | SI | DifficultyAirway |
| SURPW_Dilatation | varchar |  |  | SI | Dilatation |
| SURPW_Duodenoscope | varchar |  |  | SI | Duodenoscope |
| SURPW_ERCP | varchar |  |  | SI | ERCP |
| SURPW_EndoscopicText1 | varchar |  |  | SI | Endoscopic TextArea 1 |
| SURPW_EndoscopicText2 | varchar |  |  | SI | Endoscopic TextArea 2 |
| SURPW_EndoscopicText3 | varchar |  |  | SI | Endoscopic TextArea 3 |
| SURPW_EndoscopicText4 | varchar |  |  | SI | Endoscopic TextArea 4 |
| SURPW_EndoscopicText5 | varchar |  |  | SI | Endoscopic TextArea 5 |
| SURPW_EndoscopicText6 | varchar |  |  | SI | Endoscopic TextArea 6 |
| SURPW_FemoralHeadDonation | varchar |  |  | SI | FemoralHeadDonation |
| SURPW_FrozenSection | varchar |  |  | SI | FrozenSection |
| SURPW_FrozenSectionComments | varchar |  |  | SI | Frozen Section Comments |
| SURPW_Gastroscopy | varchar |  |  | SI | Gastroscopy |
| SURPW_Gentamycin | varchar |  |  | SI | Gentamycin |
| SURPW_GradComprStockings | varchar |  |  | SI | Graduated Compression Stockings |
| SURPW_Haematology | varchar |  |  | SI | Haematology |
| SURPW_HaematologyComments | varchar |  |  | SI | Haematology Comments |
| SURPW_Heparin | varchar |  |  | SI | Heparin |
| SURPW_Histology | varchar |  |  | SI | Histology |
| SURPW_HistopathologyComments | varchar |  |  | SI | Histopathology Comments |
| SURPW_ImplantsChecked | varchar |  |  | SI | ImplantsChecked |
| SURPW_Infusion1 | varchar |  |  | SI | Infusion1  |
| SURPW_Infusion2 | varchar |  |  | SI | Infusion2 |
| SURPW_Infusion3 | varchar |  |  | SI | Infusion3  |
| SURPW_Infusion4 | varchar |  |  | SI | Infusion4  |
| SURPW_Infusion5 | varchar |  |  | SI | Infusion5  |
| SURPW_InstrumentID1 | varchar |  |  | SI | Instrument ID 1 |
| SURPW_InstrumentID2 | varchar |  |  | SI | Instrument ID 2 |
| SURPW_InstrumentID3 | varchar |  |  | SI | Instrument ID 3 |
| SURPW_InstrumentID4 | varchar |  |  | SI | Instrument ID 4 |
| SURPW_InstrumentID5 | varchar |  |  | SI | Instrument ID 5 |
| SURPW_InstrumentID6 | varchar |  |  | SI | Instrument ID 6 |
| SURPW_ItemsCounted | varchar |  |  | SI | ItemsCounted |
| SURPW_ItemsCountedBy_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_ItemsLeftInSitu | varchar |  |  | SI | Items left in Situ |
| SURPW_ItemsRecountedBy_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_Keflin | varchar |  |  | SI | Keflin |
| SURPW_Marcain0p25 | varchar |  |  | SI | Marcain0p25 |
| SURPW_Marcain0p25WithAdrenaline | varchar |  |  | SI | Marcain0p25WithAdrenaline |
| SURPW_Marcain0p50 | varchar |  |  | SI | Marcain0p50 |
| SURPW_Marcain0p50WithAdrenaline | varchar |  |  | SI | Marcain0p50WithAdrenaline |
| SURPW_MicrobiologyComments | varchar |  |  | SI | Microbiology Comments |
| SURPW_Naropin0p20 | varchar |  |  | SI | Naropin0p20 |
| SURPW_Naropin0p75 | varchar |  |  | SI | Naropin0p75 |
| SURPW_Naropin1 | varchar |  |  | SI | Naropin1 |
| SURPW_NoteEquipmentNotAvailable | varchar |  |  | SI | NoteEquipmentNotAvailable |
| SURPW_NumSpecCol | varchar |  |  | SI | Number of Specimen(s) Collected |
| SURPW_NurseProcSignOut1 | varchar |  |  | SI | Nurse Procedure Sign Out Check 1 |
| SURPW_NurseProcSignOut2 | varchar |  |  | SI | Nurse Procedure Sign Out Check 2 |
| SURPW_NurseProcSignOut3 | varchar |  |  | SI | Nurse Procedure Sign Out Check 3 |
| SURPW_NurseProcSignOut4 | varchar |  |  | SI | Nurse Procedure Sign Out Check 4 |
| SURPW_NurseProcSignOut5 | varchar |  |  | SI | Nurse Procedure Sign Out Check 5 |
| SURPW_NurseProcSignOut6 | varchar |  |  | SI | Nurse Procedure Sign Out Check 6 |
| SURPW_OTConsultantOwnerStatus_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffStatus |
| SURPW_OTConsultantOwner_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_OTStaff1_DR | varchar |  | FK | SI | OT Staff 1 - Des Ref CTCareProv |
| SURPW_OTStaff2_DR | varchar |  | FK | SI | OT Staff 2 - Des Ref CTCareProv |
| SURPW_OTStaff3_DR | varchar |  | FK | SI | OT Staff 3 - Des Ref CTCareProv |
| SURPW_OTStaff4_DR | varchar |  | FK | SI | OT Staff 4 - Des Ref CTCareProv |
| SURPW_OTStaff5_DR | varchar |  | FK | SI | OT Staff 5 - Des Ref CTCareProv |
| SURPW_OTStaff6_DR | varchar |  | FK | SI | OT Staff 6 - Des Ref CTCareProv |
| SURPW_OperationDurat | double |  |  | SI | OperationDuration |
| SURPW_OperationEndDate | date |  |  | SI | OperationEndDate |
| SURPW_OperationEndTime | time |  |  | SI | OperationEndTime |
| SURPW_OperationStartDate | date |  |  | SI | OperationStartDate |
| SURPW_OperationStartTime | time |  |  | SI | OperationStartTime |
| SURPW_OtherMedication | varchar |  |  | SI | OtherMedication |
| SURPW_OtherSpecimens | varchar |  |  | SI | Other Specimens |
| SURPW_OtherSpecimensComments | varchar |  |  | SI | Other Specimens Comments |
| SURPW_PACUFinishDate | date |  |  | SI | PACUFinishDate |
| SURPW_PACUFinishTime | time |  |  | SI | PACUFinishTime |
| SURPW_PACUReadyToLeaveDate | date |  |  | SI | PACUReadyToLeaveDate |
| SURPW_PACUReadyToLeaveTime | time |  |  | SI | PACUReadyToLeaveTime |
| SURPW_PACUStartDate | date |  |  | SI | PACUStartDate |
| SURPW_PACUStartTime | time |  |  | SI | PACUStartTime |
| SURPW_Papaverine | varchar |  |  | SI | Papaverine |
| SURPW_ParticularsLeftInSitu | varchar |  |  | SI | ParticularsLeftInSitu |
| SURPW_PathologyProviderOther | varchar |  |  | SI | PathologyProviderOther |
| SURPW_PathologyProvider_DR | bigint |  | FK | SI | Des Ref PACNonGovOrg |
| SURPW_PathologyProviders | varchar |  |  | SI | Pathology Providers as List of Non Gov Organisatio... |
| SURPW_PatientAwakeDate | date |  |  | SI | PatientAwakeDate |
| SURPW_PatientAwakeTime | time |  |  | SI | PatientAwakeTime |
| SURPW_PatientCalledDate | date |  |  | SI | PatientCalledDate |
| SURPW_PatientCalledTime | time |  |  | SI | PatientCalledTime |
| SURPW_PatientChecked | varchar |  |  | SI | PatientChecked |
| SURPW_PatientIVC | varchar |  |  | SI | Patient IVC |
| SURPW_PhosEnemaGiven | varchar |  |  | SI | Phosphate Enema Given |
| SURPW_PlateSiteIntact | varchar |  |  | SI | PlateSiteIntact |
| SURPW_PneumaticCompr | varchar |  |  | SI | Pneumatic Compression |
| SURPW_Polypectomy | varchar |  |  | SI | Polypectomy |
| SURPW_PositioningComments | varchar |  |  | SI | PositioningComments |
| SURPW_PostOpReviewDate | date |  |  | SI | PostOpReviewDate |
| SURPW_PostOpReviewTime | time |  |  | SI | PostOpReviewTime |
| SURPW_Pressure1 | varchar |  |  | SI | Tourniquet 1 Pressure |
| SURPW_Pressure2 | varchar |  |  | SI | Tourniquet 2 Pressure |
| SURPW_Pressure3 | varchar |  |  | SI | Tourniquet 3 Pressure |
| SURPW_Pressure4 | varchar |  |  | SI | Tourniquet 4 Pressure |
| SURPW_ProcedureCheck | varchar |  |  | SI | ProcedureCheck |
| SURPW_ProcedureCheck2 | varchar |  |  | SI | ProcedureCheck2 |
| SURPW_Quantity | double |  |  | SI | Quantity |
| SURPW_ReadyForSurgeryDate | date |  |  | SI | ReadyForSurgeryDate |
| SURPW_ReadyForSurgeryTime | time |  |  | SI | ReadyForSurgeryTime |
| SURPW_ReasonForDisperancy | varchar |  |  | SI | ReasonForDisperancy |
| SURPW_RecordReviewed | varchar |  |  | SI | RecordReviewed |
| SURPW_Remarks | varchar |  |  | SI | Remarks |
| SURPW_Risk500BloodLoss | varchar |  |  | SI | Risk of >500ml Blood loss |
| SURPW_RoomPreparationDate | date |  |  | SI | RoomPreparationDate |
| SURPW_RoomPreparationTime | time |  |  | SI | RoomPreparationTime |
| SURPW_RowId | varchar |  |  | NO | - |
| SURPW_ScopeExpDChecked | varchar |  |  | SI | Scope Expiry Date checked |
| SURPW_Sigmoidoscopy | varchar |  |  | SI | Sigmoidoscopy |
| SURPW_SipTestmls | double |  |  | SI | Sip Test (mls) |
| SURPW_SiteAndSideChecked | varchar |  |  | SI | SiteAndSideChecked |
| SURPW_SiteMarket | varchar |  |  | SI | SiteMarket |
| SURPW_SkinIntegrity | varchar |  |  | SI | SkinIntegrity |
| SURPW_SpecColDetls | varchar |  |  | SI | Specimen(s) Collected Details |
| SURPW_SpecLabelCorrect | varchar |  |  | SI | Specimens are correctly labelled |
| SURPW_SpecimenCollected | varchar |  |  | SI | SpecimenCollected |
| SURPW_SpecimenType | varchar |  |  | SI | SpecimenType |
| SURPW_Spincterotomy | varchar |  |  | SI | Spincterotomy |
| SURPW_Stent | varchar |  |  | SI | Stent |
| SURPW_SterPackConfirmed | varchar |  |  | SI | Sterility of packaging confirmed |
| SURPW_SurgeonStatus_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffStatus |
| SURPW_Surgeon_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_SurgicalAssistant_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| SURPW_TeamReviewACV | varchar |  |  | SI | Team review of anticipated critical events |
| SURPW_TheatreDurat | double |  |  | SI | TheatreDuration |
| SURPW_TheatreInDate | date |  |  | SI | TheatreInDate |
| SURPW_TheatreInTime | time |  |  | SI | TheatreInTime |
| SURPW_TheatreOutDate | date |  |  | SI | TheatreOutDate |
| SURPW_TheatreOutTime | time |  |  | SI | TheatreOutTime |
| SURPW_TissueStored | varchar |  |  | SI | Tissue Stored |
| SURPW_TissueStoredDtls | varchar |  |  | SI | Tissue Stored Details |
| SURPW_TourniquetBodySite1_DR | bigint |  | FK | SI | Des Ref Tourniquet 1 Body Site |
| SURPW_TourniquetBodySite2_DR | bigint |  | FK | SI | Des Ref Tourniquet 2 Body Site |
| SURPW_TourniquetBodySite3_DR | bigint |  | FK | SI | Des Ref Tourniquet 3 Body Site |
| SURPW_TourniquetBodySite4_DR | bigint |  | FK | SI | Des Ref Tourniquet 4 Body Site |
| SURPW_TourniquetClampComments | varchar |  |  | SI | Tourniquet/Clamp Comments |
| SURPW_TourniquetDateFrom1 | date |  |  | SI | Tourniquet 1 Date From |
| SURPW_TourniquetDateFrom2 | date |  |  | SI | Tourniquet 2 Date From |
| SURPW_TourniquetDateFrom3 | date |  |  | SI | Tourniquet 3 Date From |
| SURPW_TourniquetDateFrom4 | date |  |  | SI | Tourniquet 4 Date From |
| SURPW_TourniquetDateTo1 | date |  |  | SI | Tourniquet 1 Date To |
| SURPW_TourniquetDateTo2 | date |  |  | SI | Tourniquet 2 Date To |
| SURPW_TourniquetDateTo3 | date |  |  | SI | Tourniquet 3 Date To |
| SURPW_TourniquetDateTo4 | date |  |  | SI | Tourniquet 4 Date To |
| SURPW_TourniquetSite1 | varchar |  |  | SI | Tourniquet 1 Site |
| SURPW_TourniquetSite2 | varchar |  |  | SI | Tourniquet 2 Site |
| SURPW_TourniquetSite3 | varchar |  |  | SI | Tourniquet 3 Site |
| SURPW_TourniquetSite4 | varchar |  |  | SI | Tourniquet 4 Site |
| SURPW_TourniquetTimeOff1 | time |  |  | SI | Tourniquet 1 Time Off |
| SURPW_TourniquetTimeOff2 | time |  |  | SI | Tourniquet 2 Time Off |
| SURPW_TourniquetTimeOff3 | time |  |  | SI | Tourniquet 3 Time Off |
| SURPW_TourniquetTimeOff4 | time |  |  | SI | Tourniquet 4 Time Off |
| SURPW_TourniquetTimeOn1 | time |  |  | SI | Tourniquet 1 Time On |
| SURPW_TourniquetTimeOn2 | time |  |  | SI | Tourniquet 2 Time On |
| SURPW_TourniquetTimeOn3 | time |  |  | SI | Tourniquet 3 Time On |
| SURPW_TourniquetTimeOn4 | time |  |  | SI | Tourniquet 4 Time On |
| SURPW_TourniquetType1_DR | bigint |  | FK | SI | Des Ref Tourniquet 1 Type |
| SURPW_TourniquetType2_DR | bigint |  | FK | SI | Des Ref Tourniquet 2 Type |
| SURPW_TourniquetType3_DR | bigint |  | FK | SI | Des Ref Tourniquet 3 Type |
| SURPW_TourniquetType4_DR | bigint |  | FK | SI | Des Ref Tourniquet 4 Type |
| SURPW_UpdateDate | date |  |  | SI | UpdateDate |
| SURPW_UpdateLoc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| SURPW_UpdateTime | time |  |  | SI | UpdateTime |
| SURPW_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| SURPW_ValidConsent | varchar |  |  | SI | ValidConsent |
| SURPW_ValidConsent2 | varchar |  |  | SI | ValidConsent2 |
| SURPW_WearingOfPPE | varchar |  |  | SI | WearingOfPPE |
| SURPW_WoundClassif2 | varchar |  |  | SI | WoundClassification2  |
| SURPW_WoundClassification_DR | bigint |  | FK | SI | Des Ref MRCWoundType |
| SURPW_WoundDressing | varchar |  |  | SI | Wound Dressing |
| SURPW_XRayUsed | varchar |  |  | SI | XRayUsed |
| SURPW_Xylocaine1 | varchar |  |  | SI | Xylocaine1 |
| SURPW_Xylocaine1WithAdrenaline | varchar |  |  | SI | Xylocaine1WithAdrenaline |
| SURPW_Xylocaine2 | varchar |  |  | SI | Xylocaine2 |
| SURPW_Xylocaine2WithAdrenaline | varchar |  |  | SI | Xylocaine2WithAdrenaline |
| SURPW_XylocaineSpray | varchar |  |  | SI | Xylocaine Spray |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*