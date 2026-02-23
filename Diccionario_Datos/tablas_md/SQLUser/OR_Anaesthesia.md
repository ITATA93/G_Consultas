# SQLUser.OR_Anaesthesia

**Schema:** SQLUser
**Columnas:** 325
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANA_PAADM_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| ANA_ASA_DR | bigint |  | FK | SI | Des Ref to ORC ASA |
| ANA_AdminAnaOutOTRoomDate | date |  |  | SI | Administration of Anaesthesia Outside OT Room Date |
| ANA_AdminAnaOutOTRoomTime | time |  |  | SI | Administration of Anaesthesia Outside OT Room Time |
| ANA_AirwayMgtAirway_DR | bigint |  | FK | SI | Airway management technique |
| ANA_AirwayMgtComments | varchar |  |  | SI | Airway management comments |
| ANA_AirwayMgtDrugsDiscarded | varchar |  |  | SI | Airway management drugs discarded |
| ANA_AirwayMgtETTSize_DR | bigint |  | FK | SI | Airway management ETT size |
| ANA_AirwayMgtLMASize_DR | bigint |  | FK | SI | Airway management LMA size |
| ANA_AirwayMgtLaryngoView_DR | bigint |  | FK | SI | Airway management Laryngoscopic View |
| ANA_AirwayMgtMaskVentilation | varchar |  |  | SI | Airway management mask ventilation |
| ANA_AirwayMgtPEEP | integer |  |  | SI | Airway management PEEP |
| ANA_AirwayMgtThroatPkInserted | bit |  |  | SI | Airway management throat pack inserted |
| ANA_AirwayMgtThroatPkInsertedDate | date |  |  | SI | Airway management throat pack inserted date |
| ANA_AirwayMgtThroatPkInsertedTime | time |  |  | SI | Airway management throat pack inserted time |
| ANA_AirwayMgtThroatPkRemoved | bit |  |  | SI | Airway management throat pack removed |
| ANA_AirwayMgtThroatPkRemovedDate | date |  |  | SI | Airway management throat pack removed date |
| ANA_AirwayMgtThroatPkRemovedTime | time |  |  | SI | Airway management throat pack removed time |
| ANA_AirwayMgtVentPressure | double |  |  | SI | Airway management ventilation pressure |
| ANA_AirwayMgtVentRate | integer |  |  | SI | Airway management ventilation rate |
| ANA_AmtBloodLoss | double |  |  | SI | Amount of Blood Loss |
| ANA_AmtBloodTranfused | double |  |  | SI | Amount of Blood Tranfused |
| ANA_AmtFluidInfused | double |  |  | SI | Amount of Fluid Infused |
| ANA_AmtUrineOutput | double |  |  | SI | Amount of Urine Output |
| ANA_AnaFinishTime | time |  |  | SI | Anaest. Finish Time |
| ANA_AnaStartTime | time |  |  | SI | Anaest. Start Time |
| ANA_AnaestMethods | varchar |  |  | SI | List of Anaesthetic Methods |
| ANA_Anaesthetist_DR | varchar |  | FK | SI | Anaesthetist Des Ref to CTCP |
| ANA_Anest_Duration | double |  |  | SI | Duration of Anesthesia |
| ANA_AreaInDate | date |  |  | SI | Area In Date |
| ANA_AreaInTime | time |  |  | SI | Area In Time |
| ANA_AreaOutDate | date |  |  | SI | Area Out Date |
| ANA_AreaOutTime | time |  |  | SI | Area Out Time |
| ANA_BagMaskVent_DR | bigint |  | FK | SI | Bag-Mask Ventilation |
| ANA_BldtType_DR | bigint |  | FK | SI | Des Ref BldtType |
| ANA_BolusDrugsUsed | varchar |  |  | SI | Initial Bolus/Drugs Used |
| ANA_BypassLoc_DR | bigint |  | FK | SI | Bypass Location |
| ANA_BypassRec | varchar |  |  | SI | Bypass Recovery |
| ANA_COMP_DR | bigint |  | FK | SI | Des Ref to ORANCOMP |
| ANA_Childsub | numeric |  |  | NO | Childsub |
| ANA_Colloids | varchar |  |  | SI | Colloids |
| ANA_CompComments | varchar |  |  | SI | Anaesthetic Complications Comments |
| ANA_Consultant_DR | varchar |  | FK | SI | Des Ref Consultant |
| ANA_Crystalloids | varchar |  |  | SI | Crystalloids |
| ANA_Cuff_IntubTube | varchar |  |  | SI | Is there a cuff in Intub Tube |
| ANA_CustomDate1 | date |  |  | SI | Custom Date for custom logic of linked Operation S... |
| ANA_CustomDate2 | date |  |  | SI | Custom Date for custom logic of linked Operation E... |
| ANA_CustomDuration | double |  |  | SI | Custom field for linked Operation Duration  |
| ANA_CustomNumeric1 | double |  |  | SI | Custom Numeric Property 1 |
| ANA_CustomNumeric2 | double |  |  | SI | Custom Numeric Property 2 |
| ANA_CustomNumeric3 | double |  |  | SI | Custom Numeric Property 3 |
| ANA_CustomNumeric4 | double |  |  | SI | Custom Numeric Property 4 |
| ANA_CustomNumeric5 | double |  |  | SI | Custom Numeric Property 5 |
| ANA_CustomText1 | varchar |  |  | SI | Custom Text Property 1 |
| ANA_CustomText2 | varchar |  |  | SI | Custom Text Property 2 |
| ANA_CustomText3 | varchar |  |  | SI | Custom Text Property 3 |
| ANA_CustomText4 | varchar |  |  | SI | Custom Text Property 4 |
| ANA_CustomText5 | varchar |  |  | SI | Custom Text Property 5 |
| ANA_CustomTime1 | time |  |  | SI | Custom Time for special logic of linked Operation ... |
| ANA_CustomTime2 | time |  |  | SI | Custom Time for special logic of linked Operation ... |
| ANA_DEOAirwayMgtAnalgesia_DR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management awa... |
| ANA_DEOAirwayMgtCanInsSite_DR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| ANA_DEOAirwayMgtCanInserted | date |  |  | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| ANA_DEOAirwayMgtCanSize_DR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| ANA_DEOAirwayMgtComments | varchar |  |  | SI | DSU /Endoscopy/Opthalmology airways Management com... |
| ANA_DEOAirwayMgtO2FlowRate | double |  |  | SI | DSU /Endoscopy/Opthalmology airways Management O2 ... |
| ANA_DEOAirwayMgtPosSupine | bit |  |  | SI | DSU /Endoscopy/Opthalmology airways Management pat... |
| ANA_DEOAirwayMgtVentMode_DR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management ven... |
| ANA_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| ANA_Date | date |  |  | SI | Date of Anaest. |
| ANA_ETTType_DR | bigint |  | FK | SI | ETT(Endotracheal Tube) Type |
| ANA_EndCleaningDate | date |  |  | SI | End Cleaning OTRoom after Operation Date |
| ANA_EndCleaningTime | time |  |  | SI | End Cleaning OTRoom after Operation Time |
| ANA_ExtubDone | varchar |  |  | SI | Extubation Done |
| ANA_ExtubTime | time |  |  | SI | Extubation Time |
| ANA_FinishDate | date |  |  | SI | Ana. Finish Date |
| ANA_GenBlock2Antisepsis_DR | bigint |  | FK | SI | Second block information - antisepsis |
| ANA_GenBlock2PerfomedTime | time |  |  | SI | Second block information - block performed at time |
| ANA_GenBlock2PerformedBy_DR | varchar |  | FK | SI | Second block information field names are consisten... |
| ANA_GenBlock2Position_DR | bigint |  | FK | SI | Second general block information - operation posit... |
| ANA_GenBlockAntisepsis_DR | bigint |  | FK | SI | general block information - antisepsis |
| ANA_GenBlockPerfomedTime | time |  |  | SI | general block information - block performed at tim... |
| ANA_GenBlockPerformedBy_DR | varchar |  | FK | SI | general block information - block performed by |
| ANA_GenBlockPosition_DR | bigint |  | FK | SI | general block information - operation position |
| ANA_IVCannulaSize_DR | bigint |  | FK | SI | IV Cannula Size |
| ANA_IVInsertionDate | date |  |  | SI | IV Insertion Date |
| ANA_IVInsertionTime | time |  |  | SI | IV Insertion Time |
| ANA_IntSize_DR | bigint |  | FK | SI | Des Ref to Intub Size |
| ANA_IntubGrade_DR | bigint |  | FK | SI | Intubation Grade Des Ref to ORCIG |
| ANA_IntubRoute_DR | bigint |  | FK | SI | Intubation Route Des Ref to ORCIR |
| ANA_LMAType_DR | bigint |  | FK | SI | LMA(Laryngeal Mask Airway) Type |
| ANA_ManuallyUpdated | varchar |  |  | SI | Updated from ORAnaesthesia.Edit flag to control ac... |
| ANA_Method | bigint |  |  | SI | Method of Anaest. |
| ANA_MonitoringTechComments | varchar |  |  | SI | monitoring technique comments |
| ANA_Neurax2Approach | varchar |  |  | SI | Neuraxial Anaesthesia 2 - Approach  |
| ANA_Neurax2EpiduralCatheterToSkin | double |  |  | SI | Neuraxial Anaesthesia 2 - Epidural Catheter To Ski... |
| ANA_Neurax2EpiduralLevel_DR | bigint |  | FK | SI | Neuraxial Anaesthesia 2 - Epidural Level |
| ANA_Neurax2EpiduralNeedle_DR | bigint |  | FK | SI | Neuraxial Anaesthesia 2 - Epidural Needle |
| ANA_Neurax2EpiduralTip | double |  |  | SI | Neuraxial Anaesthesia 2 - Epidural Tip To |
| ANA_Neurax2PerfomedTime | time |  |  | SI | Neuraxial Anaesthesia 2 - Performed at time |
| ANA_Neurax2PerformedBy_DR | varchar |  | FK | SI | Second Neuraxial Block - Field names have '2' for ... |
| ANA_Neurax2Position_DR | bigint |  | FK | SI | Neuraxial Anaesthesia 2 - Position |
| ANA_Neurax2SkinPrepComment | varchar |  |  | SI | Neuraxial Anaesthesia 2 - Skin Prep Comment  |
| ANA_NeuraxApproach | varchar |  |  | SI | Neuraxial Anaesthesia - Approach  |
| ANA_NeuraxEpiduralCatheterToSkin | double |  |  | SI | Neuraxial Anaesthesia Epidural Catheter To Skin |
| ANA_NeuraxEpiduralComments | varchar |  |  | SI | Neuraxial Anaesthesia Comments |
| ANA_NeuraxEpiduralDrugsUsed | varchar |  |  | SI | Neuraxial Anaesthesia Epidural Initial Bolus/Drugs... |
| ANA_NeuraxEpiduralLevel_DR | bigint |  | FK | SI | Neuraxial Anaesthesia Epidural Level |
| ANA_NeuraxEpiduralNeedle_DR | bigint |  | FK | SI | Neuraxial Anaesthesia Epidural Needle |
| ANA_NeuraxEpiduralTip | double |  |  | SI | Neuraxial Anaesthesia Epidural Tip To |
| ANA_NeuraxPerfomedTime | time |  |  | SI | Neurax block information - block performed at time |
| ANA_NeuraxPerformedBy_DR | varchar |  | FK | SI | Neurax block information - block performed by |
| ANA_NeuraxPosition_DR | bigint |  | FK | SI | Neurax general block information - operation posit... |
| ANA_NeuraxSkinPrepComment | varchar |  |  | SI | Neurax block information - Skin Prep Comment  |
| ANA_NeuraxSkinPrep_DR | bigint |  | FK | SI | Neuraxial Anaesthesia Skin Preparation |
| ANA_NeuraxSpinalLevel_DR | bigint |  | FK | SI | Neuraxial Anaesthesia Spinal Level |
| ANA_NeuraxSpinalNeedleType_DR | bigint |  | FK | SI | Neuraxial Anaesthesia Spinal Needle Type |
| ANA_NeuraxSpinalNeedle_DR | bigint |  | FK | SI | Neuraxial Anaesthesia Spinal Needle |
| ANA_NeuraxUSGuidance | varchar |  |  | SI | Neuraxial Anaesthesia U/S Guidance |
| ANA_NeuraxUSTechnique_DR | bigint |  | FK | SI | Neuraxial Anaesthesia U/S Technique |
| ANA_No | varchar |  |  | SI | Anaesthesia No |
| ANA_Notes | varchar |  |  | SI | Notes |
| ANA_ORAnaNurse_DR | varchar |  | FK | SI | OR Anast. Nurse Des Ref to CTCP |
| ANA_OTRoomPrepDate | date |  |  | SI | OT Room Preparation Date |
| ANA_OTRoomPrepTime | time |  |  | SI | OT Room Preparation Time |
| ANA_ObsOnAdm_DR | varchar |  | FK | SI | Observations on admission |
| ANA_Orbital05MarcainWithHylase | double |  |  | SI | Orbital Blocks 0.5% Marcaine plain with Hylase |
| ANA_Orbital075RopiWidthHylase | double |  |  | SI | Orbital Blocks 0.75% Ropivocaine with Hylase |
| ANA_Orbital1RopiWidthHylase | double |  |  | SI | Orbital Blocks 1% Ropivocaine with Hylase |
| ANA_Orbital2LignoWithHylase | double |  |  | SI | Orbital Blocks 2% Lignocaine plain with Hylase |
| ANA_OrbitalComments | varchar |  |  | SI | Orbital Blocks Comments |
| ANA_OrbitalEyeDrops_DR | bigint |  | FK | SI | Orbital Blocks Eye Drops |
| ANA_OrbitalNeedleType_DR | bigint |  | FK | SI | Orbital Blocks Needle Type |
| ANA_OutcomeOfSurgery_DR | bigint |  | FK | SI | Des Ref OutcomeOfSurgery |
| ANA_PACUAnaDischarge_DR | varchar |  | FK | SI | PACU Anaest who allowed Discharge DR to CTCP |
| ANA_PACUAnaNurse_DR | varchar |  | FK | SI | PACU AnaestNurse Des Ref to CTCP |
| ANA_PACU_FinishDate | date |  |  | SI | PACU FinishDate |
| ANA_PACU_FinishTime | time |  |  | SI | PACU Finish Time |
| ANA_PACU_ReadyLeaveDate | date |  |  | SI | PACU_ReadyLeaveDate |
| ANA_PACU_ReadyLeaveTime | time |  |  | SI | PACU_ReadyLeaveTime |
| ANA_PACU_StartDate | date |  |  | SI | PACU StartDate |
| ANA_PACU_StartTime | time |  |  | SI | PACU Start Time |
| ANA_PACU_Time | time |  |  | SI | Time in PACU |
| ANA_PatAnaInducDate | date |  |  | SI | Patient Ready after Anaesthesia Induction Date |
| ANA_PatAnaInducTime | time |  |  | SI | Patient Ready after Anaesthesia Induction Time |
| ANA_PatAwakeDate | date |  |  | SI | Patient Awake in OTRoom Date |
| ANA_PatAwakeTime | time |  |  | SI | Patient Awake in OTRoom Time |
| ANA_PatCallDate | date |  |  | SI | Patient Call To OT Room Date |
| ANA_PatCallTime | time |  |  | SI | Patient Call To OT Room Time |
| ANA_PatReviewDate | date |  |  | SI | Medical/nursing Review of Patient Date |
| ANA_PatReviewTime | time |  |  | SI | Medical/nursing Review of Patient Time |
| ANA_Plasma | varchar |  |  | SI | Plasma |
| ANA_PlasmaCode | varchar |  |  | SI | PlasmaCode |
| ANA_Platelets | varchar |  |  | SI | Platelets |
| ANA_PlateletsCode | varchar |  |  | SI | PlateletsCode |
| ANA_PostOpBed | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| ANA_PostOpBedDate | date |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| ANA_PostOpBedTime | time |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| ANA_PostOpBedTimeOut | time |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| ANA_PostOperInstructions | varchar |  |  | SI | PostOperInstructions |
| ANA_PreAnaAssessAirwayDent | varchar |  |  | SI | Pre-anaesthetic assessment airway/dentition |
| ANA_PreAnaAssessAnaesthetist_DR | varchar |  | FK | SI | Pre-anaesthetic assessment anaesthetist |
| ANA_PreAnaAssessCardiovasResp | varchar |  |  | SI | Pre-anaesthetic assessment cardiovascular / respir... |
| ANA_PreAnaAssessDate | date |  |  | SI | Pre-anaesthetic assessment date |
| ANA_PreAnaAssessHistory | varchar |  |  | SI | Pre-anaesthetic assessment history |
| ANA_PreAnaAssessInfAnaRisk | varchar |  |  | SI | Pre-anaesthetic assessment informed of anaesthetic... |
| ANA_PreAnaAssessMalampatiScore | bigint |  |  | SI | Pre-anaesthetic assessment malampati score |
| ANA_PreAnaAssessOper_DR | bigint |  | FK | SI | Pre-anaesthetic assessment operation |
| ANA_PreAnaAssessOther | varchar |  |  | SI | Pre-anaesthetic assessment other |
| ANA_PreAnaAssessPlan | varchar |  |  | SI | Pre-anaesthetic assessment plan |
| ANA_PreAnaAssessSurgeon_DR | varchar |  | FK | SI | Pre-anaesthetic assessment surgeon |
| ANA_PreOpBed | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| ANA_PreOpBedDate | date |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| ANA_PreOpBedTime | time |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| ANA_PreOpBedTimeOut | time |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| ANA_PreOpRoomInDate | date |  |  | SI | PreOp/Anaesthetic Room In Date |
| ANA_PreOpRoomInTime | time |  |  | SI | PreOp/Anaesthetic Room In Time |
| ANA_PreOpRoom_DR | bigint |  | FK | SI | PreOp/Anaesthetic Room Des Ref |
| ANA_PrepRoomEndDate | date |  |  | SI | Room Preparation End Date |
| ANA_PrepRoomEndTime | time |  |  | SI | Room Preparation End Time |
| ANA_PrevAnaest_DR | varchar |  | FK | SI | Des Ref PrevAnaest |
| ANA_PrevMethod_DR | bigint |  | FK | SI | Des Ref PrevMethod |
| ANA_PrevRecOp_DR | bigint |  | FK | SI | Des Ref PrevRecOp |
| ANA_PrevRecSPPP_DR | bigint |  | FK | SI | Des Ref PrevRecSPPP |
| ANA_RBOperatingRoom_DR | bigint |  | FK | SI | DR RBOperatingRoom |
| ANA_ReasTotTimeChange | bigint |  |  | SI | Reason for Duration Change |
| ANA_Reason_Suspend_DR | bigint |  | FK | SI | DEs Ref Reason for Suspend |
| ANA_RecReviewed | varchar |  |  | SI | Anaesthetic Record Reviewed |
| ANA_RecovOper_DR | bigint |  | FK | SI | Des Ref RecovOper |
| ANA_RecovSPPP_DR | bigint |  | FK | SI | Des Ref RecovSPPP |
| ANA_RecoveryRoom_DR | bigint |  | FK | SI | Recovery Room Des Ref |
| ANA_RedCells | varchar |  |  | SI | Red Cells |
| ANA_RedCellsCode | varchar |  |  | SI | RedCellsCode |
| ANA_RegBlock2AnaTypeComment | varchar |  |  | SI | Second block information - Anaesthesia Type Commen... |
| ANA_RegBlock2Comments | varchar |  |  | SI | Second block information - nerve location techniqu... |
| ANA_RegBlock2Parasthesia_DR | bigint |  | FK | SI | Second block information - nerve location techniqu... |
| ANA_RegBlock2Side_DR | bigint |  | FK | SI | Second block information - Block Side |
| ANA_RegBlock2SkinPrepComment | varchar |  |  | SI | Second block information - Skin Prep Comment  |
| ANA_RegBlock2SurfLandmark_DR | bigint |  | FK | SI | Second block information - nerve location techniqu... |
| ANA_RegBlock2Technique | varchar |  |  | SI | Block 2 information - Technique |
| ANA_RegBlockAnaTypeComment | varchar |  |  | SI | Regional block information - Anaesthesia Type Comm... |
| ANA_RegBlockComments | varchar |  |  | SI | regional block information - nerve location techni... |
| ANA_RegBlockParasthesia_DR | bigint |  | FK | SI | regional block information - nerve location techni... |
| ANA_RegBlockSide_DR | bigint |  | FK | SI | Regional block information - Block Side |
| ANA_RegBlockSkinPrepComment | varchar |  |  | SI | Regional block information - Skin Prep Comment  |
| ANA_RegBlockStimCurrent | varchar |  |  | SI | regional block information - nerve location techni... |
| ANA_RegBlockSurfLandmark_DR | bigint |  | FK | SI | regional block information - nerve location techni... |
| ANA_RegBlockTechnique | varchar |  |  | SI | Regional block information - Technique |
| ANA_RegBlockUltraSoundGuided | varchar |  |  | SI | regional block information - nerve location techni... |
| ANA_RegDrugsAdm | varchar |  |  | SI | Regional Drugs Administered |
| ANA_RowId | varchar |  |  | NO | - |
| ANA_SourceType | varchar |  |  | SI | Source Type |
| ANA_StartCleaningDate | date |  |  | SI | Start Cleaning OTRoom after Operation Date |
| ANA_StartCleaningTime | time |  |  | SI | Start Cleaning OTRoom after Operation Time |
| ANA_Status | varchar |  |  | SI | Status |
| ANA_Supervisor_DR | varchar |  | FK | SI | Supervisor Des Ref to CTCP |
| ANA_SurgFinishTime | time |  |  | SI | Surgery Finish Time |
| ANA_SurgStartTime | time |  |  | SI | Surgery Start Time |
| ANA_Surgery_Duration | time |  |  | SI | Surgery Duration |
| ANA_TextArea1 | varchar |  |  | SI | Text Area 1 |
| ANA_TextArea2 | varchar |  |  | SI | Text Area 2 |
| ANA_TextArea3 | varchar |  |  | SI | Text Area 3 |
| ANA_TextArea4 | varchar |  |  | SI | Text Area 4 |
| ANA_TheaterRecoveryFinishDate | date |  |  | SI | Recovery In Theater Finish Date |
| ANA_TheaterRecoveryFinishTime | time |  |  | SI | Recovery In Theater Finish Time |
| ANA_TheaterRecoveryReadyDate | date |  |  | SI | Recovery In Theater Ready Date |
| ANA_TheaterRecoveryReadyTime | time |  |  | SI | Recovery In Theater Ready Time |
| ANA_TheaterRecoveryStartDate | date |  |  | SI | Recovery In Theater Start Date |
| ANA_TheaterRecoveryStartTime | time |  |  | SI | Recovery In Theater Start Time |
| ANA_TheatreInDate | date |  |  | SI | Theatre In Date |
| ANA_TheatreInTime | time |  |  | SI | Theatre In Time |
| ANA_TheatreOutDate | date |  |  | SI | Theatre Out Date |
| ANA_TheatreOutTime | time |  |  | SI | Theatre Out Time |
| ANA_TotalOTRoomTime | double |  |  | SI | Total Time of OT Room in Minutes |
| ANA_Total_Input | double |  |  | SI | Total Input |
| ANA_Total_Output | double |  |  | SI | Total Output |
| ANA_TransLoc_DR | bigint |  | FK | SI | Transfer to Loc Des Ref to CTLOC |
| ANA_UpdateDate | date |  |  | SI | Last Update Date |
| ANA_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital |
| ANA_UpdateTime | time |  |  | SI | Last Update Time |
| ANA_UpdateUser_DR | bigint |  | FK | SI | Last Update User |
| Q01 | - |  |  | SI | Consider psychological, social, and occupational f... |
| Q02 | - |  |  | SI | Do not include impairment in functioning due to ph... |
| Q03 | - |  |  | SI | Rating scale |
| Q04 | - |  |  | SI | Superior functioning in a wide range of activities... |
| Q05 | - |  |  | SI | Absent or minimal symptoms (e.g., mild anxiety bef... |
| Q05B | - |  |  | SI | Socially effective, generally satisfied with life,... |
| Q06 | - |  |  | SI | If symptoms are present, they are transient and ex... |
| Q06B | - |  |  | SI | No more than slight impairment in social, occupati... |
| Q07 | - |  |  | SI | Some mild symptoms (e.g. depressed mood and mild i... |
| Q07B | - |  |  | SI | OR some difficulty in social, occupational, or sch... |
| Q07C | - |  |  | SI | (e.g., occasional truancy, or theft within the hou... |
| Q08 | - |  |  | SI | Moderate symptoms (e.g., flat affect and circumsta... |
| Q08B | - |  |  | SI | OR moderate difficulty in social, occupational, or... |
| Q09 | - |  |  | SI | Serious symptoms (e.g.. suicidal ideation, severe ... |
| Q09B | - |  |  | SI | OR any serious impairment in social, occupational,... |
| Q10 | - |  |  | SI | Some impairment in reality testing or communicatio... |
| Q10B | - |  |  | SI | OR major impairment in several areas, such as work... |
| Q10C | - |  |  | SI | (e.g., depressed man avoids friends, neglects fami... |
| Q11 | - |  |  | SI | Behaviour is considerably influenced by delusions ... |
| Q11B | - |  |  | SI | OR serious impairment in communication or judgment... |
| Q11C | - |  |  | SI | OR inability to function in almost all areas (e.g.... |
| Q12 | - |  |  | SI | Some danger of hurting self or others (e.g., suici... |
| Q12B | - |  |  | SI | OR occasionally fails to maintain minimal personal... |
| Q12C | - |  |  | SI | OR gross impairment in communication (e.g., largel... |
| Q13 | - |  |  | SI | Persistent danger of severely hurting self or othe... |
| Q13B | - |  |  | SI | OR persistent inability to maintain minimal person... |
| Q13C | - |  |  | SI | OR serious suicidal act with clear expectation of ... |
| Q14 | - |  |  | SI | Inadequate information |
| Q30 | - |  |  | SI | A higher number is associated with a higher degree... |
| Q31 | - |  |  | SI | The Global Assessment of Functioning (GAF) is a nu... |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
| Q34 | - |  |  | SI | 0 |
| Q35 | - |  |  | SI | 10 - 1 |
| Q36 | - |  |  | SI | 20 - 11 |
| Q37 | - |  |  | SI | 30 - 21 |
| Q38 | - |  |  | SI | 40 - 31 |
| Q39 | - |  |  | SI | 50 - 41 |
| Q40 | - |  |  | SI | 60 - 51 |
| Q41 | - |  |  | SI | 70 - 61 |
| Q42 | - |  |  | SI | Score |
| Q43 | - |  |  | SI | 80 - 71 |
| Q44 | - |  |  | SI | 90 - 81 |
| Q45 | - |  |  | SI | 100 - 91 |
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