# SQLUser.PA_ORAnaestOperSnapshot

**Schema:** SQLUser
**Columnas:** 267
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAANOP_RowId | bigint | PK |  | NO | - |
| PAANOP_AnaestOperation_DR | varchar |  | FK | SI | Operation Des Ref to ORAnaestOperation Record |
| PAANOP_Anaesthetist_DR | varchar |  | FK | SI | Anaesthetist Des Ref to CTCP |
| PAANOP_AngBoxAnaesthetistCP_DR | varchar |  | FK | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxDeviceCat | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxDeviceExpiry | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxDeviceImpl | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxDeviceLot | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxDeviceVendor | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxMSALead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxMSLVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxMSVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxMVALead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxMVLVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxMVVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxOHMSALead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxOHMSComments | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Comme... |
| PAANOP_AngBoxOHMSConclusion | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Concl... |
| PAANOP_AngBoxOHMSDosage | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxOHMSLVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxOHMSScreenTime | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxOHMSVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxPerformingCP_DR | varchar |  | FK | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxProcIndications | varchar |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxProcedure_DR | bigint |  | FK | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxVALead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxVLVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngBoxVVLead | double |  |  | SI | Angio Box Change and Cardioversion Procedure Form ... |
| PAANOP_AngPainContrastVol | double |  |  | SI | Angio Pain Management Procedure Contrast Volume |
| PAANOP_AngPainContrast_DR | bigint |  | FK | SI | Angio Pain Management Procedure Contrast Used |
| PAANOP_AngPainEquipment_DR | bigint |  | FK | SI | Angio Pain Management Procedure Equipment |
| PAANOP_AngPainFollowUpDetails_DR | bigint |  | FK | SI | Angio Pain Management Procedure Follo Up Details |
| PAANOP_AngPainPostInstructions | varchar |  |  | SI | Angio Box Change and Cardioversion Pain Post Opera... |
| PAANOP_AngPainProcDetails | varchar |  |  | SI | Angio Box Change and Cardioversion Pain Procedure ... |
| PAANOP_AngPainProcedure_DR | bigint |  | FK | SI | Angio Pain Management Procedure Details Procedure |
| PAANOP_AngPainSiteLeft_DR | bigint |  | FK | SI | Angio Pain Management Procedure Site Left |
| PAANOP_AngPainSiteRight_DR | bigint |  | FK | SI | Angio Pain Management Procedure Site Right |
| PAANOP_AngPainTreatment_DR | bigint |  | FK | SI | Angio Pain Management Procedure Treatment |
| PAANOP_AngPostAmbulationTime | time |  |  | SI | Angio Post Procedure Instruction Form Ambulation T... |
| PAANOP_AngPostBedRestAt | time |  |  | SI | Angio Post Procedure Instruction Form Bed Rest At |
| PAANOP_AngPostBedRestAtFollowed | time |  |  | SI | Angio Post Procedure Instruction Form Bed Rest At |
| PAANOP_AngPostBedRestFor | double |  |  | SI | Angio Post Procedure Instruction Form Bed Rest For |
| PAANOP_AngPostBedRestForAnother | double |  |  | SI | Angio Post Procedure Instruction Form Bed Rest For... |
| PAANOP_AngPostDeploymentTime | time |  |  | SI | Angio Post Procedure Instruction Form Deployment T... |
| PAANOP_AngPostDeviceDressing | varchar |  |  | SI | Angio Post Procedure Instruction Form No Vascular ... |
| PAANOP_AngPostHaemostasisAt | double |  |  | SI | Angio Post Procedure Instruction Form Then Mobilis... |
| PAANOP_AngPostLegStraightFor | double |  |  | SI | Angio Post Procedure Instruction Form Leg Straight... |
| PAANOP_AngPostMaintainBedRest | varchar |  |  | SI | Angio Post Procedure Instruction Form Maintain Pat... |
| PAANOP_AngPostStraightLeg | varchar |  |  | SI | Angio Post Procedure Instruction Form With Leg Str... |
| PAANOP_AngPostVasSealingDevice | varchar |  |  | SI | Angio Post Procedure Instruction Form Vascular Sea... |
| PAANOP_AngPostVasSealingDeviceDressing | varchar |  |  | SI | Angio Post Procedure Instruction Form Vascular Sea... |
| PAANOP_AngRadBedrest | varchar |  |  | SI | Angio Radiology Procedure Bed Rest |
| PAANOP_AngRadContrastVol | double |  |  | SI | Angio Radiology Procedure Contrast Volume |
| PAANOP_AngRadContrast_DR | bigint |  | FK | SI | Angio Radiology Procedure Report Contrast Used |
| PAANOP_AngRadInstructions | varchar |  |  | SI | Angio Radiology Procedure Instructions |
| PAANOP_AngRadInstructionsOther | varchar |  |  | SI | Angio Radiology Procedure Other Instructions |
| PAANOP_AngRadLocalAnaestheticML | double |  |  | SI | Angio Radiology Procedure Report Local Anaesthetic... |
| PAANOP_AngRadLocalAnaesthetic_DR | bigint |  | FK | SI | Angio Radiology Procedure Report Local Anaesthetic |
| PAANOP_AngRadNoRuns | double |  |  | SI | Angio Radiology Procedure Report Number Of Runs |
| PAANOP_AngRadNoVessels | double |  |  | SI | Angio Radiology Procedure Report Number Of Vessels... |
| PAANOP_AngRadPerioDrugs | varchar |  |  | SI | Angio Radiology Procedure Drugs Given Perioperativ... |
| PAANOP_AngRadPrelReport | varchar |  |  | SI | Angio Radiology Procedure Preliminary Report |
| PAANOP_AngRadWoundCheck | varchar |  |  | SI | Angio Radiology Procedure Wound Check |
| PAANOP_AngTourniquetComplications | varchar |  |  | SI | Angio - Shealth/Tourniquet Variable/Complications |
| PAANOP_AngTourniquetHaemostasis | time |  |  | SI | Angio - Shealth/Tourniquet Haemostasis |
| PAANOP_AngTourniquetSheathInsitu | varchar |  |  | SI | Angio - Shealth/Tourniquet Tourniquet Sheath Insit... |
| PAANOP_AngTourniquetSheathRemoved | time |  |  | SI | Angio - Shealth/Tourniquet Sheath Removed/Tourniqu... |
| PAANOP_AngTourniquetTime30 | time |  |  | SI | Angio - Shealth/Tourniquet Time 30 |
| PAANOP_AngTourniquetTime60 | time |  |  | SI | Angio - Shealth/Tourniquet Time 60 |
| PAANOP_AngTourniquetTimeChair | time |  |  | SI | Angio - Shealth/Tourniquet Time Chair |
| PAANOP_AngTourniquetTimeMobilize | time |  |  | SI | Angio - Shealth/Tourniquet Time Mobilize |
| PAANOP_AreaInDate | date |  |  | SI | Area In Date |
| PAANOP_AreaInTime | time |  |  | SI | Area In Time |
| PAANOP_AreaOutDate | date |  |  | SI | Area Out Date |
| PAANOP_AreaOutTime | time |  |  | SI | Area Out Time |
| PAANOP_BiopsyPerformed | varchar |  |  | SI | Boipsy Performed |
| PAANOP_Blade_DR | bigint |  | FK | SI | Blade Des Ref to ORCBT |
| PAANOP_BodySite_DR | bigint |  | FK | SI | Des Ref OEC_BodySite_DR |
| PAANOP_CMBSCode | varchar |  |  | SI | CMBS Code |
| PAANOP_CTLOC_DR | bigint |  | FK | SI | Location of Operation(DR to CTLOC) |
| PAANOP_CancelReason | varchar |  |  | SI | Cancellation Reason |
| PAANOP_Circul_Nurse_DR | varchar |  | FK | SI | Circulating Nurse Des Ref to CTCP |
| PAANOP_Closure | varchar |  |  | SI | Closure |
| PAANOP_CountedItems | varchar |  |  | SI | Counted Items |
| PAANOP_CreatedDate | date |  |  | SI |  Date Created  |
| PAANOP_CreatedFlowSheetUpdated | varchar |  |  | SI | Created from Flow-sheet Updated from ORAnaOperatio... |
| PAANOP_CreatedTime | time |  |  | SI |  Time Created  |
| PAANOP_CreatedUser_DR | bigint |  | FK | SI | User Created  |
| PAANOP_CustomNumeric1 | double |  |  | SI | Custom Numeric Property 1 |
| PAANOP_CustomNumeric2 | double |  |  | SI | Custom Numeric Property 2 |
| PAANOP_CustomNumeric3 | double |  |  | SI | Custom Numeric Property 3 |
| PAANOP_CustomNumeric4 | double |  |  | SI | Custom Numeric Property 4 |
| PAANOP_CustomNumeric5 | double |  |  | SI | Custom Numeric Property 5 |
| PAANOP_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| PAANOP_DaySurgery | varchar |  |  | SI | Day Surgery |
| PAANOP_Depar_Oper_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PAANOP_Details | varchar |  |  | SI | Details |
| PAANOP_DiathermyBodySite_DR | bigint |  | FK | SI | Des Ref DiathermyBodySite |
| PAANOP_DoctorCommission | varchar |  |  | SI | DoctorCommission |
| PAANOP_DrainsInSitu | varchar |  |  | SI | DrainsInSitu  |
| PAANOP_EffectiveElective | varchar |  |  | SI | Effective Elective |
| PAANOP_EndoBronBronchoscope | varchar |  |  | SI | Endoscopy Report Bronchoscopy Bronchoscope |
| PAANOP_EndoBronCXR | varchar |  |  | SI | Endoscopy Report Bronchoscopy CXR |
| PAANOP_EndoBronComplications | varchar |  |  | SI | Endoscopy Report Bronchoscopy Complications |
| PAANOP_EndoBronFindings | varchar |  |  | SI | Endoscopy Report Bronchoscopy Findings |
| PAANOP_EndoBronHistory | varchar |  |  | SI | Endoscopy Report Bronchoscopy History |
| PAANOP_EndoBronIndications | varchar |  |  | SI | Endoscopy Report Bronchoscopy Indications |
| PAANOP_EndoBronPostInstruc | varchar |  |  | SI | Endoscopy Report Bronchoscopy Post Instructions |
| PAANOP_EndoBronSpecimen_DR | bigint |  | FK | SI | Endoscopy Report Bronchoscopy Specimen |
| PAANOP_EndoBronVideo_DR | bigint |  | FK | SI | Endoscopy Report Bronchoscopy Video |
| PAANOP_EndoColComments | varchar |  |  | SI | Endoscopy Report Colonoscopy Comments |
| PAANOP_EndoColFindings | varchar |  |  | SI | Endoscopy Report Colonoscopy Findings |
| PAANOP_EndoColIndications | varchar |  |  | SI | Endoscopy Report Colonoscopy Indications |
| PAANOP_EndoColPreDiagnosis | varchar |  |  | SI | Endoscopy Report Colonoscopy Preliminary Diagnosis |
| PAANOP_EndoERCPBiopsies | varchar |  |  | SI | Endoscopy Report ERCP Biopsies |
| PAANOP_EndoERCPComments | varchar |  |  | SI | Endoscopy Report ERCP Comments |
| PAANOP_EndoERCPFindings | varchar |  |  | SI | Endoscopy Report ERCP Findings |
| PAANOP_EndoERCPIndications | varchar |  |  | SI | Endoscopy Report ERCP Indications |
| PAANOP_EndoERCPPreDiagnosis | varchar |  |  | SI | Endoscopy Report ERCP Preliminary Diagnosis |
| PAANOP_EndoGastComments | varchar |  |  | SI | Endoscopy Report Gastroscopy Comments |
| PAANOP_EndoGastFindings | varchar |  |  | SI | Endoscopy Report Gastroscopy Findings |
| PAANOP_EndoGastIndications | varchar |  |  | SI | Endoscopy Report Gastroscopy Indications |
| PAANOP_EndoGastPreDiagnosis | varchar |  |  | SI | Endoscopy Report Gastroscopy Preliminary Diagnosis |
| PAANOP_EndoGenEndoscopist_DR | varchar |  | FK | SI | Endoscopy Report General Endoscopist |
| PAANOP_EndoGenFindings | varchar |  |  | SI | Endoscopy Report General Findings |
| PAANOP_EndoGenIndications | varchar |  |  | SI | Endoscopy Report General Indications |
| PAANOP_EndoGenOrders | varchar |  |  | SI | Endoscopy Report General Post-Op Orders |
| PAANOP_EndoGenPreliminiaryDiag | varchar |  |  | SI | Endoscopy Report General Preliminary Diagnosis |
| PAANOP_EndoGenRefGP_DR | bigint |  | FK | SI | Endoscopy Report General Referring GP |
| PAANOP_EndoSigColonBiopsies | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Colon Biopsies |
| PAANOP_EndoSigColonPolyps | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Colon Polyps |
| PAANOP_EndoSigComments | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Comments |
| PAANOP_EndoSigFindings | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Findings |
| PAANOP_EndoSigIndications | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Indications |
| PAANOP_EndoSigPreDiagnosis | varchar |  |  | SI | Endoscopy Report Sigmoidoscopy Preliminary Diagnos... |
| PAANOP_EndoSigType_DR | bigint |  | FK | SI | Endoscopy Report Sigmoidoscopy Type |
| PAANOP_Findings | varchar |  |  | SI | Findings |
| PAANOP_FlowSheetCreatedFlag | varchar |  |  | SI | Created from Flow-sheet flag |
| PAANOP_ForSignByCP | varchar |  |  | SI | For Sign By Care Provider |
| PAANOP_HTMLNotesPlainText_DR | bigint |  | FK | SI | Des Ref websys.Document - Plain text of PAANOPHTML... |
| PAANOP_HTMLNotes_DR | bigint |  | FK | SI | Des Ref websys.Document |
| PAANOP_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| PAANOP_ItemsCountedBy_DR | varchar |  | FK | SI | Des Ref CTCareProv Items Counted By |
| PAANOP_ItemsReCountedBy_DR | varchar |  | FK | SI | Des Ref ItemsReCountedBy |
| PAANOP_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| PAANOP_MBSCode | varchar |  |  | SI | MBS Code |
| PAANOP_MedAdrenaline | double |  |  | SI | Medications Adrenaline |
| PAANOP_MedBSS | double |  |  | SI | Medications BSS |
| PAANOP_MedBSSPlus | double |  |  | SI | Medications BSS Plus |
| PAANOP_MedBrilliantPeel | double |  |  | SI | Medications Brilliant Peel |
| PAANOP_MedCellugel | double |  |  | SI | Medications Cellugel |
| PAANOP_MedDexamethasone | double |  |  | SI | Medications Dexamethasone |
| PAANOP_MedGentamycin | double |  |  | SI | Medications Gentamycin |
| PAANOP_MedGlycerine | double |  |  | SI | Medications Glycerine |
| PAANOP_MedHeparin | double |  |  | SI | Medications Heparin |
| PAANOP_MedKeflin | double |  |  | SI | Medications Keflin |
| PAANOP_MedMarcain0p25 | double |  |  | SI | Medications Marcain 0.25% |
| PAANOP_MedMarcain0p25Adrenaline | double |  |  | SI | Medications Marcain 0.25% with Adrenaline |
| PAANOP_MedMarcain0p5 | double |  |  | SI | Medications Marcain 0.5% |
| PAANOP_MedMarcain0p5Adrenaline | double |  |  | SI | Medications Marcain 0.5% with Adrenaline |
| PAANOP_MedNaropin0p2 | double |  |  | SI | Medications Naropin 0.2% |
| PAANOP_MedNaropin0p75 | double |  |  | SI | Medications Naropin 0.75% |
| PAANOP_MedNaropin1 | double |  |  | SI | Medications Naropin 1% |
| PAANOP_MedOther | varchar |  |  | SI | Medications Other |
| PAANOP_MedPapaverine | double |  |  | SI | Medications Papaverine |
| PAANOP_MedRingersLactate | double |  |  | SI | Medications Ringers Lactate |
| PAANOP_MedSodiumChloride0p9 | double |  |  | SI | Medications Sodium Chloride 0.9% |
| PAANOP_MedSterileWater | double |  |  | SI | Medications Sterile Water |
| PAANOP_MedXylocaine1 | double |  |  | SI | Medications Xylocaine 1% |
| PAANOP_MedXylocaine1Adrenaline | double |  |  | SI | Medications Xylocaine 1% with Adrenaline |
| PAANOP_MedXylocaine2Adrenaline | double |  |  | SI | Medications Xylocaine 2% with Adrenaline |
| PAANOP_No | varchar |  |  | SI | Operation No |
| PAANOP_Notes | varchar |  |  | SI | Operation Notes |
| PAANOP_OPBIL_DR | bigint |  | FK | SI | Des Ref to OPBIL |
| PAANOP_OpEndDate | date |  |  | SI | Op End Date |
| PAANOP_OpEndTime | time |  |  | SI | Op End Time |
| PAANOP_OpStartDate | date |  |  | SI | Op Start Date |
| PAANOP_OpStartTime | time |  |  | SI | Op Start Time |
| PAANOP_OperCategory_DR | bigint |  | FK | SI | Des Ref OperCategory |
| PAANOP_OperType | varchar |  |  | SI | Operation Type |
| PAANOP_OperationComplication | varchar |  |  | SI | OperationComplication |
| PAANOP_OutcomeOfSurgery_DR | bigint |  | FK | SI | Des Ref OutcomeOfSurgery |
| PAANOP_PatholEsthetOper | varchar |  |  | SI | PatholEsthetOper |
| PAANOP_PathologySent | varchar |  |  | SI | PathologySent |
| PAANOP_PlannedSPPP_DR | bigint |  | FK | SI | Des Ref PrevSPPP |
| PAANOP_PostDiag_DR | bigint |  | FK | SI | Des REf Postoperation Diagnosis |
| PAANOP_PostFollowUpApptDate | date |  |  | SI | Post Operative Surgeon Follow-up Appointment Date |
| PAANOP_PostFollowUpApptPlace | varchar |  |  | SI | Post Operative Surgeon Follow-up Appointment Place |
| PAANOP_PostFollowUpApptReq | bit |  |  | SI | Post Operative Surgeon Follow-up Appointment Requi... |
| PAANOP_PostFollowUpApptTime | time |  |  | SI | Post Operative Surgeon Follow-up Appointment Time |
| PAANOP_PostOPDiagnosisDiff | varchar |  |  | SI | Post-Operative Diagnosis |
| PAANOP_PostOperInstructions | varchar |  |  | SI | PostOperInstructions |
| PAANOP_PostParticularsLeftInSitu | varchar |  |  | SI | Post Operative Particulars of Tubes / Drains / Cat... |
| PAANOP_PostPathologyProvOther | varchar |  |  | SI | Post Operative Instructions Pathology Provider Oth... |
| PAANOP_PostPathologyProvider_DR | bigint |  | FK | SI | Post Operative Pathology Provider |
| PAANOP_PostSpecToPathology | varchar |  |  | SI | Post Operative Specimens to Pathology |
| PAANOP_PostSpecimenDetails | varchar |  |  | SI | Post Operative Specimen Details |
| PAANOP_PreOPDiagnosis | varchar |  |  | SI | Pre-Operative Diagnosis |
| PAANOP_PreopDiag_DR | bigint |  | FK | SI | Des Ref Preoperation Diagnosis |
| PAANOP_PrevSPPP_DR | bigint |  | FK | SI | Des Ref PrevSPPP |
| PAANOP_PrevSurg_DR | varchar |  | FK | SI | Des Ref PrevSurg |
| PAANOP_PrevType_DR | bigint |  | FK | SI | Des Ref PrevType |
| PAANOP_ProceduralDetails | varchar |  |  | SI | Procedural Details of Operation |
| PAANOP_Procedure | varchar |  |  | SI | Procedure |
| PAANOP_ProperlyIncision | varchar |  |  | SI | ProperlyIncision |
| PAANOP_ProthesisUsed | varchar |  |  | SI | Prosthesis Used |
| PAANOP_Quantity | double |  |  | SI | Quantity |
| PAANOP_RBOPSecProc_DR | varchar |  | FK | SI | Des Ref RBOPSecProc |
| PAANOP_ReasonForProcVariance_DR | bigint |  | FK | SI | Des Ref OT Reason for Variance |
| PAANOP_ReportTemplate_DR | bigint |  | FK | SI | Des Ref ORCOperReportTemplate |
| PAANOP_Resource_DR | bigint |  | FK | SI | Des REf Resource |
| PAANOP_RobotUsed | varchar |  |  | SI | Robot Used |
| PAANOP_SSUSR_DR | bigint |  | FK | SI | Des Ref SSUSR |
| PAANOP_SecondSurgeon_DR | varchar |  | FK | SI | Second Surgeon |
| PAANOP_SnapshotDate | date |  |  | SI | Create Date |
| PAANOP_SnapshotTime | time |  |  | SI | Create Time |
| PAANOP_SnapshotUser_DR | bigint |  | FK | SI | Des Ref SSUSR |
| PAANOP_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PAANOP_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| PAANOP_StatePPP_DR | bigint |  | FK | SI | DR PACStatePPP |
| PAANOP_Status | varchar |  |  | SI | Status |
| PAANOP_SterPackBatchNo | varchar |  |  | SI | SterPackBatchNo |
| PAANOP_SurchCode_DR | bigint |  | FK | SI | Des Ref SurchCode |
| PAANOP_Surgeon_DR | varchar |  | FK | SI | Surgeon Des Ref to CTCP |
| PAANOP_SurgicalWoundStatus | varchar |  |  | SI | SurgicalWoundStatus  |
| PAANOP_Text1 | varchar |  |  | SI | Text1 |
| PAANOP_Text2 | varchar |  |  | SI | Text2 |
| PAANOP_TheatreInDate | date |  |  | SI | Theatre In Date |
| PAANOP_TheatreInTime | time |  |  | SI | Theatre In Time |
| PAANOP_TheatreOutDate | date |  |  | SI | Theatre Out Date |
| PAANOP_TheatreOutTime | time |  |  | SI | Theatre Out Time |
| PAANOP_Torniquet2BodySite_DR | bigint |  | FK | SI | Des Ref TorniquetBodySite |
| PAANOP_Torniquet2DateFrom | date |  |  | SI | TorniquetDateFrom |
| PAANOP_Torniquet2DateTo | date |  |  | SI | TorniquetDateTo |
| PAANOP_Torniquet2TimeFrom | time |  |  | SI | TorniquetTimeFrom |
| PAANOP_Torniquet2TimeTo | time |  |  | SI | TorniquetTimeTo |
| PAANOP_TorniquetBodySite_DR | bigint |  | FK | SI | Des Ref TorniquetBodySite |
| PAANOP_TorniquetDateFrom | date |  |  | SI | TorniquetDateFrom |
| PAANOP_TorniquetDateTo | date |  |  | SI | TorniquetDateTo |
| PAANOP_TorniquetTimeFrom | time |  |  | SI | TorniquetTimeFrom |
| PAANOP_TorniquetTimeTo | time |  |  | SI | TorniquetTimeTo |
| PAANOP_TourniquetPressure1M | double |  |  | SI | Tourniquet Pressure Observations Pressure 1 Measur... |
| PAANOP_TourniquetPressure1Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 1 Time |
| PAANOP_TourniquetPressure1_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 1 |
| PAANOP_TourniquetPressure2M | double |  |  | SI | Tourniquet Pressure Observations Pressure 2 Measur... |
| PAANOP_TourniquetPressure2Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 2 Time |
| PAANOP_TourniquetPressure2_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 2 |
| PAANOP_TourniquetPressure3M | double |  |  | SI | Tourniquet Pressure Observations Pressure 3 Measur... |
| PAANOP_TourniquetPressure3Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 3 Time |
| PAANOP_TourniquetPressure3_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 3 |
| PAANOP_TourniquetPressure4M | double |  |  | SI | Tourniquet Pressure Observations Pressure 4 Measur... |
| PAANOP_TourniquetPressure4Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 4 Time |
| PAANOP_TourniquetPressure4_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 4 |
| PAANOP_TourniquetPressure5M | double |  |  | SI | Tourniquet Pressure Observations Pressure 5 Measur... |
| PAANOP_TourniquetPressure5Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 5 Time |
| PAANOP_TourniquetPressure5_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 5 |
| PAANOP_TourniquetPressure6M | double |  |  | SI | Tourniquet Pressure Observations Pressure 6 Measur... |
| PAANOP_TourniquetPressure6Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 6 Time |
| PAANOP_TourniquetPressure6_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 6 |
| PAANOP_TourniquetPressure7M | double |  |  | SI | Tourniquet Pressure Observations Pressure 7 Measur... |
| PAANOP_TourniquetPressure7Time | time |  |  | SI | Tourniquet Pressure Observations Pressure 7 Time |
| PAANOP_TourniquetPressure7_DR | bigint |  | FK | SI | Tourniquet Pressure Observations Pressure 7 |
| PAANOP_TransferToLoc | bigint |  |  | SI | Transfer To Loc |
| PAANOP_Type_DR | bigint |  | FK | SI | Operations/Procedures Des Ref |
| PAANOP_UpdateDate | date |  |  | SI | Last Update Date |
| PAANOP_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital |
| PAANOP_UpdateTime | time |  |  | SI | Last Update Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*