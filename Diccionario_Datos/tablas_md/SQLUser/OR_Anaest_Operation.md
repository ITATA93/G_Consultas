# SQLUser.OR_Anaest_Operation

**Schema:** SQLUser
**Columnas:** 359
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANAOP_Par_Ref | varchar | PK |  | NO | OR_Anaesthesia Parent Reference |
| ANAOP_Anaesthetist_DR | varchar |  | FK | SI | Anaesthetist Des Ref to CTCP |
| ANAOP_AngBoxAnaesthetistCP_DR | varchar |  | FK | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxDeviceCat | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxDeviceExpiry | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxDeviceImpl | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxDeviceLot | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxDeviceVendor | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxMSALead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxMSLVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxMSVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxMVALead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxMVLVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxMVVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxOHMSALead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxOHMSComments | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Comme... |
| ANAOP_AngBoxOHMSConclusion | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Concl... |
| ANAOP_AngBoxOHMSDosage | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxOHMSLVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxOHMSScreenTime | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxOHMSVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxPerformingCP_DR | varchar |  | FK | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxProcIndications | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxProcedure_DR | bigint |  | FK | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxVALead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxVLVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngBoxVVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| ANAOP_AngPainContrastVol | double |  |  | SI | Angio Pain Management Procedure Contrast Volume |
| ANAOP_AngPainContrast_DR | bigint |  | FK | SI | Angio Pain Management Procedure Contrast Used |
| ANAOP_AngPainEquipment_DR | bigint |  | FK | SI | Angio Pain Management Procedure Equipment |
| ANAOP_AngPainFollowUpDetails_DR | bigint |  | FK | SI | Angio Pain Management Procedure Follo Up Details |
| ANAOP_AngPainPostInstructions | varchar |  |  | SI | Angio Box Change and Cardioversion Pain Post Opera... |
| ANAOP_AngPainProcDetails | varchar |  |  | SI | Angio Box Change and Cardioversion Pain Procedure ... |
| ANAOP_AngPainProcedure_DR | bigint |  | FK | SI | Angio Pain Management Procedure Details Procedure |
| ANAOP_AngPainSiteLeft_DR | bigint |  | FK | SI | Angio Pain Management Procedure Site Left |
| ANAOP_AngPainSiteRight_DR | bigint |  | FK | SI | Angio Pain Management Procedure Site Right |
| ANAOP_AngPainTreatment_DR | bigint |  | FK | SI | Angio Pain Management Procedure Treatment |
| ANAOP_AngPostAmbulationTime | time |  |  | SI | Angio Post Procedure Instruction Form Ambulation T... |
| ANAOP_AngPostBedRestAt | time |  |  | SI | Angio Post Procedure Instruction Form Bed Rest At |
| ANAOP_AngPostBedRestAtFollowed | time |  |  | SI | Angio Post Procedure Instruction Form Bed Rest At |
| ANAOP_AngPostBedRestFor | double |  |  | SI | Angio Post Procedure Instruction Form Bed Rest For |
| ANAOP_AngPostBedRestForAnother | double |  |  | SI | Angio Post Procedure Instruction Form Bed Rest For... |
| ANAOP_AngPostDeploymentTime | time |  |  | SI | Angio Post Procedure Instruction Form Deployment T... |
| ANAOP_AngPostDeviceDressing | varchar |  |  | SI | Angio Post Procedure Instruction Form No Vascular ... |
| ANAOP_AngPostHaemostasisAt | double |  |  | SI | Angio Post Procedure Instruction Form Then Mobilis... |
| ANAOP_AngPostLegStraightFor | double |  |  | SI | Angio Post Procedure Instruction Form Leg Straight... |
| ANAOP_AngPostMaintainBedRest | varchar |  |  | SI | Angio Post Procedure Instruction Form Maintain Pat... |
| ANAOP_AngPostStraightLeg | varchar |  |  | SI | Angio Post Procedure Instruction Form With Leg Str... |
| ANAOP_AngPostVasSealingDevice | varchar |  |  | SI | Angio Post Procedure Instruction Form Vascular Sea... |
| ANAOP_AngPostVasSealingDeviceDressing | varchar |  |  | SI | Angio Post Procedure Instruction Form Vascular Sea... |
| ANAOP_AngRadBedrest | varchar |  |  | SI | Angio Radiology Procedure Bed Rest |
| ANAOP_AngRadContrastVol | double |  |  | SI | Angio Radiology Procedure Contrast Volume |
| ANAOP_AngRadContrast_DR | bigint |  | FK | SI | Angio Radiology Procedure Report Contrast Used |
| ANAOP_AngRadInstructions | varchar |  |  | SI | Angio Radiology Procedure Instructions |
| ANAOP_AngRadInstructionsOther | varchar |  |  | SI | Angio Radiology Procedure Other Instructions |
| ANAOP_AngRadLocalAnaestheticML | double |  |  | SI | Angio Radiology Procedure Report Local Anaesthetic... |
| ANAOP_AngRadLocalAnaesthetic_DR | bigint |  | FK | SI | Angio Radiology Procedure Report Local Anaesthetic |
| ANAOP_AngRadNoRuns | double |  |  | SI | Angio Radiology Procedure Report Number Of Runs |
| ANAOP_AngRadNoVessels | double |  |  | SI | Angio Radiology Procedure Report Number Of Vessels... |
| ANAOP_AngRadPerioDrugs | varchar |  |  | SI | Angio Radiology Procedure Drugs Given Perioperativ... |
| ANAOP_AngRadPrelReport | varchar |  |  | SI | Angio Radiology Procedure Preliminary Report |
| ANAOP_AngRadWoundCheck | varchar |  |  | SI | Angio Radiology Procedure Wound Check |
| ANAOP_AngTourniquetComplications | varchar |  |  | SI | Angio - Shealth/Tourniquet Variable/Complications |
| ANAOP_AngTourniquetHaemostasis | time |  |  | SI | Angio - Shealth/Tourniquet Haemostasis |
| ANAOP_AngTourniquetSheathInsitu | varchar |  |  | SI | Angio - Shealth/Tourniquet Tourniquet Sheath Insit... |
| ANAOP_AngTourniquetSheathRemoved | time |  |  | SI | Angio - Shealth/Tourniquet Sheath Removed/Tourniqu... |
| ANAOP_AngTourniquetTime30 | time |  |  | SI | Angio - Shealth/Tourniquet Time 30 |
| ANAOP_AngTourniquetTime60 | time |  |  | SI | Angio - Shealth/Tourniquet Time 60 |
| ANAOP_AngTourniquetTimeChair | time |  |  | SI | Angio - Shealth/Tourniquet Time Chair |
| ANAOP_AngTourniquetTimeMobilize | time |  |  | SI | Angio - Shealth/Tourniquet Time Mobilize |
| ANAOP_AreaInDate | date |  |  | SI | Area In Date |
| ANAOP_AreaInTime | time |  |  | SI | Area In Time |
| ANAOP_AreaOutDate | date |  |  | SI | Area Out Date |
| ANAOP_AreaOutTime | time |  |  | SI | Area Out Time |
| ANAOP_BiopsyPerformed | varchar |  |  | SI | Boipsy Performed |
| ANAOP_Blade_DR | bigint |  | FK | SI | Blade Des Ref to ORCBT |
| ANAOP_BodySite_DR | bigint |  | FK | SI | Des Ref OEC_BodySite_DR |
| ANAOP_CMBSCode | varchar |  |  | SI | CMBS Code |
| ANAOP_CTLOC_DR | bigint |  | FK | SI | Location of Operation(DR to CTLOC) |
| ANAOP_CancelReason | varchar |  |  | SI | Cancellation Reason |
| ANAOP_Childsub | numeric |  |  | NO | Childsub |
| ANAOP_Circul_Nurse_DR | varchar |  | FK | SI | Circulating Nurse Des Ref to CTCP |
| ANAOP_Closure | varchar |  |  | SI | Closure |
| ANAOP_CountedItems | varchar |  |  | SI | Counted Items |
| ANAOP_CreatedDate | date |  |  | SI |  Date Created  |
| ANAOP_CreatedFlowSheetUpdated | varchar |  |  | SI | Created from Flow-sheet Updated from ORAnaOperatio... |
| ANAOP_CreatedTime | time |  |  | SI |  Time Created  |
| ANAOP_CreatedUser_DR | bigint |  | FK | SI | User Created  |
| ANAOP_CustomNumeric1 | double |  |  | SI | Custom Numeric Property 1 |
| ANAOP_CustomNumeric2 | double |  |  | SI | Custom Numeric Property 2 |
| ANAOP_CustomNumeric3 | double |  |  | SI | Custom Numeric Property 3 |
| ANAOP_CustomNumeric4 | double |  |  | SI | Custom Numeric Property 4 |
| ANAOP_CustomNumeric5 | double |  |  | SI | Custom Numeric Property 5 |
| ANAOP_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| ANAOP_DaySurgery | varchar |  |  | SI | Day Surgery |
| ANAOP_Depar_Oper_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ANAOP_Details | varchar |  |  | SI | Details |
| ANAOP_DiathermyBodySite_DR | bigint |  | FK | SI | Des Ref DiathermyBodySite |
| ANAOP_DoctorCommission | varchar |  |  | SI | DoctorCommission |
| ANAOP_DrainsInSitu | varchar |  |  | SI | DrainsInSitu  |
| ANAOP_EffectiveElective | varchar |  |  | SI | Effective Elective |
| ANAOP_EndoBronBronchoscope | varchar |  |  | SI | Endoscopy Report Bronchoscopy Bronchoscope |
| ANAOP_EndoBronCXR | varchar |  |  | SI | Endoscopy Report Bronchoscopy CXR |
| ANAOP_EndoBronComplications | varchar |  |  | SI | Endoscopy Report Bronchoscopy Complications |
| ANAOP_EndoBronFindings | varchar |  |  | SI | Endoscopy Report Bronchoscopy Findings |
| ANAOP_EndoBronHistory | varchar |  |  | SI | Endoscopy Report Bronchoscopy History |
| ANAOP_EndoBronIndications | varchar |  |  | SI | Endoscopy Report Bronchoscopy Indications |
| ANAOP_EndoBronPostInstruc | varchar |  |  | SI | Endoscopy Report Bronchoscopy Post Instructions |
| ANAOP_EndoBronSpecimen_DR | bigint |  | FK | SI | Endoscopy Report Bronchoscopy Specimen |
| ANAOP_EndoBronVideo_DR | bigint |  | FK | SI | Endoscopy Report Bronchoscopy Video |
| ANAOP_EndoColComments | varchar |  |  | SI | Endoscopy Report Colonoscopy Comments |
| ANAOP_EndoColFindings | varchar |  |  | SI | Endoscopy Report Colonoscopy Findings |
| ANAOP_EndoColIndications | varchar |  |  | SI | Endoscopy Report Colonoscopy Indications |
| ANAOP_EndoColPreDiagnosis | varchar |  |  | SI | Endoscopy Report Colonoscopy Preliminary Diagnosis |
| ANAOP_EndoERCPBiopsies | varchar |  |  | SI | Endoscopy Report ERCP Biopsies |
| ANAOP_EndoERCPComments | varchar |  |  | SI | Endoscopy Report ERCP Comments |
| ANAOP_EndoERCPFindings | varchar |  |  | SI | Endoscopy Report ERCP Findings |
| ANAOP_EndoERCPIndications | varchar |  |  | SI | Endoscopy Report ERCP Indications |
| ANAOP_EndoERCPPreDiagnosis | varchar |  |  | SI | Endoscopy Report ERCP Preliminary Diagnosis |
| ANAOP_EndoGastComments | varchar |  |  | SI | Endoscopy Report Gastroscopy Comments |
| ANAOP_EndoGastFindings | varchar |  |  | SI | Endoscopy Report Gastroscopy Findings |
| ANAOP_EndoGastIndications | varchar |  |  | SI | Endoscopy Report Gastroscopy Indications |
| ANAOP_EndoGastPreDiagnosis | varchar |  |  | SI | Endoscopy Report Gastroscopy Preliminary Diagnosis |
| ANAOP_EndoGenEndoscopist_DR | varchar |  | FK | SI | Endoscopy Report General Endoscopist |
| ANAOP_EndoGenFindings | varchar |  |  | SI | Endoscopy Report General Findings |
| ANAOP_EndoGenIndications | varchar |  |  | SI | Endoscopy Report General Indications |
| ANAOP_EndoGenOrders | varchar |  |  | SI | Endoscopy Report General Post-Op Orders |
| ANAOP_EndoGenPreliminiaryDiag | varchar |  |  | SI | Endoscopy Report General Preliminary Diagnosis |
| ANAOP_EndoGenRefGP_DR | bigint |  | FK | SI | Endoscopy Report General Referring GP |
| ANAOP_EndoSigColonBiopsies | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Colon Biopsies |
| ANAOP_EndoSigColonPolyps | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Colon Polyps |
| ANAOP_EndoSigComments | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Comments |
| ANAOP_EndoSigFindings | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Findings |
| ANAOP_EndoSigIndications | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Indications |
| ANAOP_EndoSigPreDiagnosis | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Preliminary Diagnos... |
| ANAOP_EndoSigType_DR | bigint |  | FK | SI | Endoscopy Report Sigmoidoscopy Type |
| ANAOP_FinalCountCorrect | varchar |  |  | SI | Final Count Correct |
| ANAOP_FinalInstrCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Final Instruments C... |
| ANAOP_FinalItemsCntByRole_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffRole Final Items Counted ... |
| ANAOP_FinalItemsCntDate | date |  |  | SI | Des Ref CTCareProv Final Items Counted Date |
| ANAOP_FinalItemsCntTime | time |  |  | SI | Des Ref CTCareProv Final Items Counted Time |
| ANAOP_FinalItemsCountedBy_DR | varchar |  | FK | SI | Des Ref CTCareProv Final Items Counted by |
| ANAOP_FinalItemsRecntByRole_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffRole Final Items Recounte... |
| ANAOP_FinalItemsRecntBy_DR | varchar |  | FK | SI | Des Ref CTCareProv Final Items Recounted by |
| ANAOP_FinalItemsRecntDate | date |  |  | SI | Des Ref CTCareProv Final Items Recounted Date |
| ANAOP_FinalItemsRecntTime | time |  |  | SI | Des Ref CTCareProv Final Items Recounted Time |
| ANAOP_FinalSharpsCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Final Sharps Count ... |
| ANAOP_FinalSwabCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Final Swab Count St... |
| ANAOP_Findings | varchar |  |  | SI | Findings |
| ANAOP_FlowSheetCreatedFlag | varchar |  |  | SI | Created from Flow-sheet flag |
| ANAOP_ForSignByCP | varchar |  |  | SI | For Sign By Care Provider |
| ANAOP_HTMLNotesPlainText_DR | bigint |  | FK | SI | Des Ref websys.Document - Plain text of ANAOPHTMLN... |
| ANAOP_HTMLNotes_DR | bigint |  | FK | SI | Des Ref websys.Document |
| ANAOP_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| ANAOP_InitInstrCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Inital Instruments ... |
| ANAOP_InitItemsCntByRole_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffRole Inital Items Counted... |
| ANAOP_InitItemsCntDate | date |  |  | SI | Des Ref CTCareProv Inital Items Counted Date |
| ANAOP_InitItemsCntTime | time |  |  | SI | Des Ref CTCareProv Inital Items Counted Time |
| ANAOP_InitItemsRecntByRole_DR | bigint |  | FK | SI | Des Ref ORCOperatingStaffRole Inital Items Recount... |
| ANAOP_InitItemsRecntDate | date |  |  | SI | Des Ref CTCareProv Inital Items Recounted Date |
| ANAOP_InitItemsRecntTime | time |  |  | SI | Des Ref CTCareProv Inital Items Recounted Time |
| ANAOP_InitSharpsCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Inital Sharps Count... |
| ANAOP_InitSwabCntStat_DR | bigint |  | FK | SI | Des Ref ORCSurgicalCountStatus Inital Swab Count S... |
| ANAOP_InitialCountCorrect | varchar |  |  | SI | Initial Count Correct |
| ANAOP_ItemsCountedBy_DR | varchar |  | FK | SI | Des Ref CTCareProv Items Counted By |
| ANAOP_ItemsReCountedBy_DR | varchar |  | FK | SI | Des Ref ItemsReCountedBy |
| ANAOP_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| ANAOP_MBSCode | varchar |  |  | SI | MBS Code |
| ANAOP_MedAdrenaline | double |  |  | SI | Medications Adrenaline |
| ANAOP_MedBSS | double |  |  | SI | Medications BSS |
| ANAOP_MedBSSPlus | double |  |  | SI | Medications BSS Plus |
| ANAOP_MedBrilliantPeel | double |  |  | SI | Medications Brilliant Peel |
| ANAOP_MedCellugel | double |  |  | SI | Medications Cellugel |
| ANAOP_MedDexamethasone | double |  |  | SI | Medications Dexamethasone |
| ANAOP_MedGentamycin | double |  |  | SI | Medications Gentamycin |
| ANAOP_MedGlycerine | double |  |  | SI | Medications Glycerine |
| ANAOP_MedHeparin | double |  |  | SI | Medications Heparin |
| ANAOP_MedKeflin | double |  |  | SI | Medications Keflin |
| ANAOP_MedMarcain0p25 | double |  |  | SI | Medications Marcain 0.25% |
| ANAOP_MedMarcain0p25Adrenaline | double |  |  | SI | Medications Marcain 0.25% with Adrenaline |
| ANAOP_MedMarcain0p5 | double |  |  | SI | Medications Marcain 0.5% |
| ANAOP_MedMarcain0p5Adrenaline | double |  |  | SI | Medications Marcain 0.5% with Adrenaline |
| ANAOP_MedNaropin0p2 | double |  |  | SI | Medications Naropin 0.2% |
| ANAOP_MedNaropin0p75 | double |  |  | SI | Medications Naropin 0.75% |
| ANAOP_MedNaropin1 | double |  |  | SI | Medications Naropin 1% |
| ANAOP_MedOther | varchar |  |  | SI | Medications Other |
| ANAOP_MedPapaverine | double |  |  | SI | Medications Papaverine |
| ANAOP_MedRingersLactate | double |  |  | SI | Medications Ringers Lactate |
| ANAOP_MedSodiumChloride0p9 | double |  |  | SI | Medications Sodium Chloride 0.9% |
| ANAOP_MedSterileWater | double |  |  | SI | Medications Sterile Water |
| ANAOP_MedXylocaine1 | double |  |  | SI | Medications Xylocaine 1% |
| ANAOP_MedXylocaine1Adrenaline | double |  |  | SI | Medications Xylocaine 1% with Adrenaline |
| ANAOP_MedXylocaine2Adrenaline | double |  |  | SI | Medications Xylocaine 2% with Adrenaline |
| ANAOP_No | varchar |  |  | SI | Operation No |
| ANAOP_Notes | varchar |  |  | SI | Operation Notes |
| ANAOP_OPBIL_DR | bigint |  | FK | SI | Des Ref to OPBIL |
| ANAOP_OpEndDate | date |  |  | SI | Op End Date |
| ANAOP_OpEndTime | time |  |  | SI | Op End Time |
| ANAOP_OpStartDate | date |  |  | SI | Op Start Date |
| ANAOP_OpStartTime | time |  |  | SI | Op Start Time |
| ANAOP_OperCategory_DR | bigint |  | FK | SI | Des Ref OperCategory |
| ANAOP_OperType | varchar |  |  | SI | Operation Type |
| ANAOP_OperationComplication | varchar |  |  | SI | OperationComplication |
| ANAOP_OutcomeOfSurgery_DR | bigint |  | FK | SI | Des Ref OutcomeOfSurgery |
| ANAOP_PatholEsthetOper | varchar |  |  | SI | PatholEsthetOper |
| ANAOP_PathologySent | varchar |  |  | SI | PathologySent |
| ANAOP_PlannedSPPP_DR | bigint |  | FK | SI | Des Ref PrevSPPP |
| ANAOP_PostDiag_DR | bigint |  | FK | SI | Des REf Postoperation Diagnosis |
| ANAOP_PostFollowUpApptDate | date |  |  | SI | Post Operative Surgeon Follow-up Appointment Date |
| ANAOP_PostFollowUpApptPlace | varchar |  |  | SI | Post Operative Surgeon Follow-up Appointment Place |
| ANAOP_PostFollowUpApptReq | bit |  |  | SI | Post Operative Surgeon Follow-up Appointment Requi... |
| ANAOP_PostFollowUpApptTime | time |  |  | SI | Post Operative Surgeon Follow-up Appointment Time |
| ANAOP_PostOPDiagnosisDiff | varchar |  |  | SI | Post-Operative Diagnosis |
| ANAOP_PostOperInstructions | varchar |  |  | SI | PostOperInstructions |
| ANAOP_PostParticularsLeftInSitu | varchar |  |  | SI | Post Operative Particulars of Tubes / Drains / Cat... |
| ANAOP_PostPathologyProvOther | varchar |  |  | SI | Post Operative Instructions Pathology Provider Oth... |
| ANAOP_PostPathologyProvider_DR | bigint |  | FK | SI | Post Operative Pathology Provider |
| ANAOP_PostSpecToPathology | varchar |  |  | SI | Post Operative Specimens to Pathology |
| ANAOP_PostSpecimenDetails | varchar |  |  | SI | Post Operative Specimen Details |
| ANAOP_PreOPDiagnosis | varchar |  |  | SI | Pre-Operative Diagnosis |
| ANAOP_PreopDiag_DR | bigint |  | FK | SI | Des Ref Preoperation Diagnosis |
| ANAOP_PrevSPPP_DR | bigint |  | FK | SI | Des Ref PrevSPPP |
| ANAOP_PrevSurg_DR | varchar |  | FK | SI | Des Ref PrevSurg |
| ANAOP_PrevType_DR | bigint |  | FK | SI | Des Ref PrevType |
| ANAOP_ProceduralDetails | varchar |  |  | SI | Procedural Details of Operation |
| ANAOP_Procedure | varchar |  |  | SI | Procedure |
| ANAOP_ProperlyIncision | varchar |  |  | SI | ProperlyIncision |
| ANAOP_ProthesisUsed | varchar |  |  | SI | Prosthesis Used |
| ANAOP_Quantity | double |  |  | SI | Quantity |
| ANAOP_RBOPSecProc_DR | varchar |  | FK | SI | Des Ref RBOPSecProc |
| ANAOP_ReasonForProcVariance_DR | bigint |  | FK | SI | Des Ref OT Reason for Variance |
| ANAOP_ReportTemplate_DR | bigint |  | FK | SI | Des Ref ORCOperReportTemplate |
| ANAOP_Resource_DR | bigint |  | FK | SI | Des REf Resource |
| ANAOP_RobotUsed | varchar |  |  | SI | Robot Used |
| ANAOP_RowId | varchar |  |  | NO | - |
| ANAOP_SSUSR_DR | bigint |  | FK | SI | Des Ref SSUSR |
| ANAOP_SecondSurgeon_DR | varchar |  | FK | SI | Second Surgeon |
| ANAOP_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| ANAOP_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| ANAOP_StatePPP_DR | bigint |  | FK | SI | DR PACStatePPP |
| ANAOP_Status | varchar |  |  | SI | Status |
| ANAOP_SterPackBatchNo | varchar |  |  | SI | SterPackBatchNo |
| ANAOP_SurchCode_DR | bigint |  | FK | SI | Des Ref SurchCode |
| ANAOP_SurgCountNote | varchar |  |  | SI | Surgical Items Notes |
| ANAOP_SurgeonAssist_DR | varchar |  | FK | SI | Des Ref Surgeon Assistant |
| ANAOP_SurgeonNotified | varchar |  |  | SI | Surgeon Notified |
| ANAOP_Surgeon_DR | varchar |  | FK | SI | Surgeon Des Ref to CTCP |
| ANAOP_SurgicalWoundStatus | varchar |  |  | SI | SurgicalWoundStatus  |
| ANAOP_Text1 | varchar |  |  | SI | Text1 |
| ANAOP_Text2 | varchar |  |  | SI | Text2 |
| ANAOP_TheatreInDate | date |  |  | SI | Theatre In Date |
| ANAOP_TheatreInTime | time |  |  | SI | Theatre In Time |
| ANAOP_TheatreOutDate | date |  |  | SI | Theatre Out Date |
| ANAOP_TheatreOutTime | time |  |  | SI | Theatre Out Time |
| ANAOP_Torniquet2BodySite_DR | bigint |  | FK | SI | Des Ref TorniquetBodySite |
| ANAOP_Torniquet2DateFrom | date |  |  | SI | TorniquetDateFrom |
| ANAOP_Torniquet2DateTo | date |  |  | SI | TorniquetDateTo |
| ANAOP_Torniquet2TimeFrom | time |  |  | SI | TorniquetTimeFrom |
| ANAOP_Torniquet2TimeTo | time |  |  | SI | TorniquetTimeTo |
| ANAOP_TorniquetBodySite_DR | bigint |  | FK | SI | Des Ref TorniquetBodySite |
| ANAOP_TorniquetDateFrom | date |  |  | SI | TorniquetDateFrom |
| ANAOP_TorniquetDateTo | date |  |  | SI | TorniquetDateTo |
| ANAOP_TorniquetTimeFrom | time |  |  | SI | TorniquetTimeFrom |
| ANAOP_TorniquetTimeTo | time |  |  | SI | TorniquetTimeTo |
| ANAOP_TourniquetPressure1M | double |  |  | SI | Tourniquet Pressure Observations Pressure 1 Measur... |
| ANAOP_TourniquetPressure1Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 1 Time |
| ANAOP_TourniquetPressure1_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 1 |
| ANAOP_TourniquetPressure2M | double |  |  | SI | Tourniquet Pressure Observations Pressure 2 Measur... |
| ANAOP_TourniquetPressure2Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 2 Time |
| ANAOP_TourniquetPressure2_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 2 |
| ANAOP_TourniquetPressure3M | double |  |  | SI | Tourniquet Pressure Observations Pressure 3 Measur... |
| ANAOP_TourniquetPressure3Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 3 Time |
| ANAOP_TourniquetPressure3_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 3 |
| ANAOP_TourniquetPressure4M | double |  |  | SI | Tourniquet Pressure Observations Pressure 4 Measur... |
| ANAOP_TourniquetPressure4Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 4 Time |
| ANAOP_TourniquetPressure4_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 4 |
| ANAOP_TourniquetPressure5M | double |  |  | SI | Tourniquet Pressure Observations Pressure 5 Measur... |
| ANAOP_TourniquetPressure5Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 5 Time |
| ANAOP_TourniquetPressure5_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 5 |
| ANAOP_TourniquetPressure6M | double |  |  | SI | Tourniquet Pressure Observations Pressure 6 Measur... |
| ANAOP_TourniquetPressure6Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 6 Time |
| ANAOP_TourniquetPressure6_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 6 |
| ANAOP_TourniquetPressure7M | double |  |  | SI | Tourniquet Pressure Observations Pressure 7 Measur... |
| ANAOP_TourniquetPressure7Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 7 Time |
| ANAOP_TourniquetPressure7_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 7 |
| ANAOP_TransferToLoc | bigint |  |  | SI | Transfer To Loc |
| ANAOP_Type_DR | bigint |  | FK | SI | Operations/Procedures Des Ref |
| ANAOP_UpdateDate | date |  |  | SI | Last Update Date |
| ANAOP_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital |
| ANAOP_UpdateTime | time |  |  | SI | Last Update Time |
| ANAOP_XRayTaken | varchar |  |  | SI | X-Ray Taken |
| Q01 | - |  |  | SI | How soon after you wake up do you smoke your first... |
| Q02 | - |  |  | SI | Do you find it difficult to refrain from smoking i... |
| Q03 | - |  |  | SI | Which cigarette would you hate to give up most? |
| Q04 | - |  |  | SI | How many cigarettes per day do you smoke? |
| Q05 | - |  |  | SI | Do you smoke more frequently during the first hour... |
| Q06 | - |  |  | SI | Do you smoke if you are so ill that you are in bed... |
| Q07 | - |  |  | SI | Score |
| Q08 | - |  |  | SI | Classification |
| Q09 | - |  |  | SI | 0 ‐ 2 |
| Q10 | - |  |  | SI | Low dependence |
| Q11 | - |  |  | SI | 3 - 4 |
| Q12 | - |  |  | SI | Low to mod dependence |
| Q13 | - |  |  | SI | 5 |
| Q14 | - |  |  | SI | Moderate dependence |
| Q15 | - |  |  | SI | 6 - 7 |
| Q16 | - |  |  | SI | High dependence |
| Q17 | - |  |  | SI | 8 + |
| Q18 | - |  |  | SI | Very high dependence |
| Q19 | - |  |  | SI | 0 ‐ 2: Low dependence |
| Q20 | - |  |  | SI | 3 ‐ 4: Low to mod dependence |
| Q21 | - |  |  | SI | 5: Moderate dependence |
| Q22 | - |  |  | SI | 6 - 7: High dependence |
| Q23 | - |  |  | SI | 8 +: Very high dependence |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Time |
| Q26 | - |  |  | SI | The Fagerstroem Test for Nicotine Dependence (FTND... |
| Q27 | - |  |  | SI | The test was designed to provide an ordinal measur... |
| Q28 | - |  |  | SI | It contains six items that evaluate the quantity o... |
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