# SQLUser.PA_ORAnaestSnapshot

**Schema:** SQLUser
**Columnas:** 205
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAAS_RowId | bigint | PK |  | NO | - |
| PAAS_ASA_DR | bigint |  | FK | SI | Des Ref to ORC ASA |
| PAAS_AdminAnaOutOTRoomDate | date |  |  | SI | Administration of Anaesthesia Outside OT Room Date |
| PAAS_AdminAnaOutOTRoomTime | time |  |  | SI | Administration of Anaesthesia Outside OT Room Time |
| PAAS_AirwayMgtAirway_DR | bigint |  | FK | SI | Airway management technique |
| PAAS_AirwayMgtComments | varchar |  |  | SI | Airway management comments |
| PAAS_AirwayMgtDrugsDiscarded | varchar |  |  | SI | Airway management drugs discarded |
| PAAS_AirwayMgtETTSize_DR | bigint |  | FK | SI | Airway management ETT size |
| PAAS_AirwayMgtLMASize_DR | bigint |  | FK | SI | Airway management LMA size |
| PAAS_AirwayMgtLaryngoView_DR | bigint |  | FK | SI | Airway management Laryngoscopic View |
| PAAS_AirwayMgtMaskVentilation | varchar |  |  | SI | Airway management mask ventilation |
| PAAS_AirwayMgtPEEP | integer |  |  | SI | Airway management PEEP |
| PAAS_AirwayMgtThroatPkInserted | bit |  |  | SI | Airway management throat pack inserted |
| PAAS_AirwayMgtThroatPkRemoved | bit |  |  | SI | Airway management throat pack removed |
| PAAS_AirwayMgtVentPressure | double |  |  | SI | Airway management ventilation pressure |
| PAAS_AirwayMgtVentRate | integer |  |  | SI | Airway management ventilation rate |
| PAAS_AmtBloodLoss | double |  |  | SI | Amount of Blood Loss |
| PAAS_AmtBloodTranfused | double |  |  | SI | Amount of Blood Tranfused |
| PAAS_AmtFluidInfused | double |  |  | SI | Amount of Fluid Infused |
| PAAS_AmtUrineOutput | double |  |  | SI | Amount of Urine Output |
| PAAS_AnaFinishTime | time |  |  | SI | Anaest. Finish Time |
| PAAS_AnaStartTime | time |  |  | SI | Anaest. Start Time |
| PAAS_AnaestMethods | varchar |  |  | SI | List of Anaesthetic Methods |
| PAAS_Anaesthesia_DR | varchar |  | FK | SI | Anaesthetist Des Ref to ORAnaesthesia Record |
| PAAS_Anaesthetist_DR | varchar |  | FK | SI | Anaesthetist Des Ref to CTCP |
| PAAS_Anest_Duration | double |  |  | SI | Duration of Anesthesia |
| PAAS_AreaInDate | date |  |  | SI | Area In Date |
| PAAS_AreaInTime | time |  |  | SI | Area In Time |
| PAAS_AreaOutDate | date |  |  | SI | Area Out Date |
| PAAS_AreaOutTime | time |  |  | SI | Area Out Time |
| PAAS_BagMaskVent_DR | bigint |  | FK | SI | Bag-Mask Ventilation |
| PAAS_BldtType_DR | bigint |  | FK | SI | Des Ref BldtType |
| PAAS_BolusDrugsUsed | varchar |  |  | SI | Initial Bolus/Drugs Used |
| PAAS_BypassLoc_DR | bigint |  | FK | SI | Bypass Location |
| PAAS_BypassRec | varchar |  |  | SI | Bypass Recovery |
| PAAS_COMP_DR | bigint |  | FK | SI | Des Ref to ORANCOMP |
| PAAS_Colloids | varchar |  |  | SI | Colloids |
| PAAS_CompComments | varchar |  |  | SI | Anaesthetic Complications Comments |
| PAAS_Consultant_DR | varchar |  | FK | SI | Des Ref Consultant |
| PAAS_Crystalloids | varchar |  |  | SI | Crystalloids |
| PAAS_Cuff_IntubTube | varchar |  |  | SI | Is there a cuff in Intub Tube |
| PAAS_CustomDate1 | date |  |  | SI | Custom Date for custom logic of linked Operation S... |
| PAAS_CustomDate2 | date |  |  | SI | Custom Date for custom logic of linked Operation E... |
| PAAS_CustomDuration | double |  |  | SI | Custom field for linked Operation Duration  |
| PAAS_CustomNumeric1 | double |  |  | SI | Custom Numeric Property 1 |
| PAAS_CustomNumeric2 | double |  |  | SI | Custom Numeric Property 2 |
| PAAS_CustomNumeric3 | double |  |  | SI | Custom Numeric Property 3 |
| PAAS_CustomNumeric4 | double |  |  | SI | Custom Numeric Property 4 |
| PAAS_CustomNumeric5 | double |  |  | SI | Custom Numeric Property 5 |
| PAAS_CustomTime1 | time |  |  | SI | Custom Time for special logic of linked Operation ... |
| PAAS_CustomTime2 | time |  |  | SI | Custom Time for special logic of linked Operation ... |
| PAAS_DEOAirwayMgtAnalgesia_DR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management awa... |
| PAAS_DEOAirwayMgtCanInsSite_DR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| PAAS_DEOAirwayMgtCanInserted | date |  |  | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| PAAS_DEOAirwayMgtCanSize_DR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| PAAS_DEOAirwayMgtComments | varchar |  |  | SI | DSU /Endoscopy/Opthalmology airways Management com... |
| PAAS_DEOAirwayMgtO2FlowRate | double |  |  | SI | DSU /Endoscopy/Opthalmology airways Management O2 ... |
| PAAS_DEOAirwayMgtPosSupine | bit |  |  | SI | DSU /Endoscopy/Opthalmology airways Management pat... |
| PAAS_DEOAirwayMgtVentMode_DR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management ven... |
| PAAS_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| PAAS_Date | date |  |  | SI | Date of Anaest. |
| PAAS_ETTType_DR | bigint |  | FK | SI | ETT(Endotracheal Tube) Type |
| PAAS_EndCleaningDate | date |  |  | SI | End Cleaning OTRoom after Operation Date |
| PAAS_EndCleaningTime | time |  |  | SI | End Cleaning OTRoom after Operation Time |
| PAAS_ExtubDone | varchar |  |  | SI | Extubation Done |
| PAAS_ExtubTime | time |  |  | SI | Extubation Time |
| PAAS_FinishDate | date |  |  | SI | Ana. Finish Date |
| PAAS_GenBlockAntisepsis_DR | bigint |  | FK | SI | general block information - antisepsis |
| PAAS_GenBlockPerfomedTime | time |  |  | SI | general block information - block performed at tim... |
| PAAS_GenBlockPerformedBy_DR | varchar |  | FK | SI | general block information - block performed by |
| PAAS_GenBlockPosition_DR | bigint |  | FK | SI | general block information - operation position |
| PAAS_IVCannulaSize_DR | bigint |  | FK | SI | IV Cannula Size |
| PAAS_IVInsertionDate | date |  |  | SI | IV Insertion Date |
| PAAS_IVInsertionTime | time |  |  | SI | IV Insertion Time |
| PAAS_IntSize_DR | bigint |  | FK | SI | Des Ref to Intub Size |
| PAAS_IntubGrade_DR | bigint |  | FK | SI | Intubation Grade Des Ref to ORCIG |
| PAAS_IntubRoute_DR | bigint |  | FK | SI | Intubation Route Des Ref to ORCIR |
| PAAS_LMAType_DR | bigint |  | FK | SI | LMA(Laryngeal Mask Airway) Type |
| PAAS_ManuallyUpdated | varchar |  |  | SI | Updated from ORAnaesthesia.Edit flag to control ac... |
| PAAS_Method | bigint |  |  | SI | Method of Anaest. |
| PAAS_MonitoringTechComments | varchar |  |  | SI | monitoring technique comments |
| PAAS_NeuraxEpiduralCatheterToSkin | double |  |  | SI | Nueraxial Anaesthesia Epidural Catheter To Skin |
| PAAS_NeuraxEpiduralComments | varchar |  |  | SI | Nueraxial Anaesthesia Comments |
| PAAS_NeuraxEpiduralDrugsUsed | varchar |  |  | SI | Nueraxial Anaesthesia Epidural Initial Bolus/Drugs... |
| PAAS_NeuraxEpiduralLevel_DR | bigint |  | FK | SI | Nueraxial Anaesthesia Epidural Level |
| PAAS_NeuraxEpiduralNeedle_DR | bigint |  | FK | SI | Nueraxial Anaesthesia Epidural Needle |
| PAAS_NeuraxEpiduralTip | double |  |  | SI | Nueraxial Anaesthesia Epidural Tip To |
| PAAS_NeuraxSkinPrep_DR | bigint |  | FK | SI | Nueraxial Anaesthesia Skin Preparation |
| PAAS_NeuraxSpinalLevel_DR | bigint |  | FK | SI | Nueraxial Anaesthesia Spinal Level |
| PAAS_NeuraxSpinalNeedleType_DR | bigint |  | FK | SI | Nueraxial Anaesthesia Spinal Needle Type |
| PAAS_NeuraxSpinalNeedle_DR | bigint |  | FK | SI | Nueraxial Anaesthesia Spinal Needle |
| PAAS_NeuraxUSGuidance | varchar |  |  | SI | Nueraxial Anaesthesia U/S Guidance |
| PAAS_NeuraxUSTechnique_DR | bigint |  | FK | SI | Nueraxial Anaesthesia U/S Technique |
| PAAS_No | varchar |  |  | SI | Anaesthesia No |
| PAAS_Notes | varchar |  |  | SI | Notes |
| PAAS_ORAnaNurse_DR | varchar |  | FK | SI | OR Anast. Nurse Des Ref to CTCP |
| PAAS_OTRoomPrepDate | date |  |  | SI | OT Room Preparation Date |
| PAAS_OTRoomPrepTime | time |  |  | SI | OT Room Preparation Time |
| PAAS_ObsOnAdm_DR | varchar |  | FK | SI | Observations on admission |
| PAAS_Orbital05MarcainWithHylase | double |  |  | SI | Orbital Blocks 0.5% Marcaine plain with Hylase |
| PAAS_Orbital075RopiWidthHylase | double |  |  | SI | Orbital Blocks 0.75% Ropivocaine with Hylase |
| PAAS_Orbital1RopiWidthHylase | double |  |  | SI | Orbital Blocks 1% Ropivocaine with Hylase |
| PAAS_Orbital2LignoWithHylase | double |  |  | SI | Orbital Blocks 2% Lignocaine plain with Hylase |
| PAAS_OrbitalComments | varchar |  |  | SI | Orbital Blocks Comments |
| PAAS_OrbitalEyeDrops_DR | bigint |  | FK | SI | Orbital Blocks Eye Drops |
| PAAS_OrbitalNeedleType_DR | bigint |  | FK | SI | Orbital Blocks Needle Type |
| PAAS_OutcomeOfSurgery_DR | bigint |  | FK | SI | Des Ref OutcomeOfSurgery |
| PAAS_PACUAnaDischarge_DR | varchar |  | FK | SI | PACU Anaest who allowed Discharge DR to CTCP |
| PAAS_PACUAnaNurse_DR | varchar |  | FK | SI | PACU AnaestNurse Des Ref to CTCP |
| PAAS_PACU_FinishDate | date |  |  | SI | PACU FinishDate |
| PAAS_PACU_FinishTime | time |  |  | SI | PACU Finish Time |
| PAAS_PACU_ReadyLeaveDate | date |  |  | SI | PACU_ReadyLeaveDate |
| PAAS_PACU_ReadyLeaveTime | time |  |  | SI | PACU_ReadyLeaveTime |
| PAAS_PACU_StartDate | date |  |  | SI | PACU StartDate |
| PAAS_PACU_StartTime | time |  |  | SI | PACU Start Time |
| PAAS_PACU_Time | time |  |  | SI | Time in PACU |
| PAAS_PatAnaInducDate | date |  |  | SI | Patient Ready after Anaesthesia Induction Date |
| PAAS_PatAnaInducTime | time |  |  | SI | Patient Ready after Anaesthesia Induction Time |
| PAAS_PatAwakeDate | date |  |  | SI | Patient Awake in OTRoom Date |
| PAAS_PatAwakeTime | time |  |  | SI | Patient Awake in OTRoom Time |
| PAAS_PatCallDate | date |  |  | SI | Patient Call To OT Room Date |
| PAAS_PatCallTime | time |  |  | SI | Patient Call To OT Room Time |
| PAAS_PatReviewDate | date |  |  | SI | Medical/nursing Review of Patient Date |
| PAAS_PatReviewTime | time |  |  | SI | Medical/nursing Review of Patient Time |
| PAAS_Plasma | varchar |  |  | SI | Plasma |
| PAAS_PlasmaCode | varchar |  |  | SI | PlasmaCode |
| PAAS_Platelets | varchar |  |  | SI | Platelets |
| PAAS_PlateletsCode | varchar |  |  | SI | PlateletsCode |
| PAAS_PostOpBed | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| PAAS_PostOpBedDate | date |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| PAAS_PostOpBedTime | time |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| PAAS_PostOpBedTimeOut | time |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| PAAS_PostOperInstructions | varchar |  |  | SI | PostOperInstructions |
| PAAS_PreAnaAssessAirwayDent | varchar |  |  | SI | Pre-anaesthetic assessment airway/dentition |
| PAAS_PreAnaAssessAnaesthetist_DR | varchar |  | FK | SI | Pre-anaesthetic assessment anaesthetist |
| PAAS_PreAnaAssessCardiovasResp | varchar |  |  | SI | Pre-anaesthetic assessment cardiovascular / respir... |
| PAAS_PreAnaAssessDate | date |  |  | SI | Pre-anaesthetic assessment date |
| PAAS_PreAnaAssessHistory | varchar |  |  | SI | Pre-anaesthetic assessment history |
| PAAS_PreAnaAssessInfAnaRisk | varchar |  |  | SI | Pre-anaesthetic assessment informed of anaesthetic... |
| PAAS_PreAnaAssessMalampatiScore | bigint |  |  | SI | Pre-anaesthetic assessment malampati score |
| PAAS_PreAnaAssessOper_DR | bigint |  | FK | SI | Pre-anaesthetic assessment operation |
| PAAS_PreAnaAssessOther | varchar |  |  | SI | Pre-anaesthetic assessment other |
| PAAS_PreAnaAssessPlan | varchar |  |  | SI | Pre-anaesthetic assessment plan |
| PAAS_PreAnaAssessSurgeon_DR | varchar |  | FK | SI | Pre-anaesthetic assessment surgeon |
| PAAS_PreOpBed | varchar |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| PAAS_PreOpBedDate | date |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| PAAS_PreOpBedTime | time |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| PAAS_PreOpBedTimeOut | time |  |  | SI | [DEPRECATED]Deprecated in TrakCare T2017+ as of TC... |
| PAAS_PreOpRoomInDate | date |  |  | SI | PreOp/Anaesthetic Room In Date |
| PAAS_PreOpRoomInTime | time |  |  | SI | PreOp/Anaesthetic Room In Time |
| PAAS_PreOpRoom_DR | bigint |  | FK | SI | PreOp/Anaesthetic Room Des Ref |
| PAAS_PrepRoomEndDate | date |  |  | SI | Room Preparation End Date |
| PAAS_PrepRoomEndTime | time |  |  | SI | Room Preparation End Time |
| PAAS_PrevAnaest_DR | varchar |  | FK | SI | Des Ref PrevAnaest |
| PAAS_PrevMethod_DR | bigint |  | FK | SI | Des Ref PrevMethod |
| PAAS_PrevRecOp_DR | bigint |  | FK | SI | Des Ref PrevRecOp |
| PAAS_PrevRecSPPP_DR | bigint |  | FK | SI | Des Ref PrevRecSPPP |
| PAAS_RBOperatingRoom_DR | bigint |  | FK | SI | DR RBOperatingRoom |
| PAAS_ReasTotTimeChange | bigint |  |  | SI | Reason for Duration Change |
| PAAS_Reason_Suspend_DR | bigint |  | FK | SI | DEs Ref Reason for Suspend |
| PAAS_RecReviewed | varchar |  |  | SI | Anaesthetic Record Reviewed |
| PAAS_RecovOper_DR | bigint |  | FK | SI | Des Ref RecovOper |
| PAAS_RecovSPPP_DR | bigint |  | FK | SI | Des Ref RecovSPPP |
| PAAS_RecoveryRoom_DR | bigint |  | FK | SI | Recovery Room Des Ref |
| PAAS_RedCells | varchar |  |  | SI | Red Cells |
| PAAS_RedCellsCode | varchar |  |  | SI | RedCellsCode |
| PAAS_RegBlockComments | varchar |  |  | SI | regional block information - nerve location techni... |
| PAAS_RegBlockParasthesia_DR | bigint |  | FK | SI | regional block information - nerve location techni... |
| PAAS_RegBlockStimCurrent | varchar |  |  | SI | regional block information - nerve location techni... |
| PAAS_RegBlockSurfLandmark_DR | bigint |  | FK | SI | regional block information - nerve location techni... |
| PAAS_RegBlockUltraSoundGuided | varchar |  |  | SI | regional block information - nerve location techni... |
| PAAS_RegDrugsAdm | varchar |  |  | SI | Regional Drugs Administered |
| PAAS_SnapshotDate | date |  |  | SI | Create Date |
| PAAS_SnapshotTime | time |  |  | SI | Create Time |
| PAAS_SnapshotUser_DR | bigint |  | FK | SI | Des Ref SSUSR |
| PAAS_SourceType | varchar |  |  | SI | Source Type |
| PAAS_StartCleaningDate | date |  |  | SI | Start Cleaning OTRoom after Operation Date |
| PAAS_StartCleaningTime | time |  |  | SI | Start Cleaning OTRoom after Operation Time |
| PAAS_Status | varchar |  |  | SI | Status |
| PAAS_Supervisor_DR | varchar |  | FK | SI | Supervisor Des Ref to CTCP |
| PAAS_SurgFinishTime | time |  |  | SI | Surgery Finish Time |
| PAAS_SurgStartTime | time |  |  | SI | Surgery Start Time |
| PAAS_Surgery_Duration | time |  |  | SI | Surgery Duration |
| PAAS_TextArea1 | varchar |  |  | SI | Text Area 1 |
| PAAS_TextArea2 | varchar |  |  | SI | Text Area 2 |
| PAAS_TextArea3 | varchar |  |  | SI | Text Area 3 |
| PAAS_TextArea4 | varchar |  |  | SI | Text Area 4 |
| PAAS_TheaterRecoveryFinishDate | date |  |  | SI | Recovery In Theater Finish Date |
| PAAS_TheaterRecoveryFinishTime | time |  |  | SI | Recovery In Theater Finish Time |
| PAAS_TheaterRecoveryReadyDate | date |  |  | SI | Recovery In Theater Ready Date |
| PAAS_TheaterRecoveryReadyTime | time |  |  | SI | Recovery In Theater Ready Time |
| PAAS_TheaterRecoveryStartDate | date |  |  | SI | Recovery In Theater Start Date |
| PAAS_TheaterRecoveryStartTime | time |  |  | SI | Recovery In Theater Start Time |
| PAAS_TheatreInDate | date |  |  | SI | Theatre In Date |
| PAAS_TheatreInTime | time |  |  | SI | Theatre In Time |
| PAAS_TheatreOutDate | date |  |  | SI | Theatre Out Date |
| PAAS_TheatreOutTime | time |  |  | SI | Theatre Out Time |
| PAAS_TotalOTRoomTime | double |  |  | SI | Total Time of OT Room in Minutes |
| PAAS_Total_Input | double |  |  | SI | Total Input |
| PAAS_Total_Output | double |  |  | SI | Total Output |
| PAAS_TransLoc_DR | bigint |  | FK | SI | Transfer to Loc Des Ref to CTLOC |
| PAAS_UpdateDate | date |  |  | SI | Last Update Date |
| PAAS_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital |
| PAAS_UpdateTime | time |  |  | SI | Last Update Time |
| PAAS_UpdateUser_DR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*