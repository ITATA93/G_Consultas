# SQLUser.OR_AnaesTemplate

**Schema:** SQLUser
**Columnas:** 180
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Pabellón Quirúrgico**. Gestión de cirugías.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ANATASADR | bigint |  | FK | SI | Des Ref to ORC ASA |
| ANATAirwayEquipments | varchar |  |  | SI | List of Anaesthetic Airway Equipments |
| ANATAirwayMgtAirwayDR | bigint |  | FK | SI | Airway management technique |
| ANATAirwayMgtComments | varchar |  |  | SI | Airway management comments |
| ANATAirwayMgtDrugsDiscarded | varchar |  |  | SI | Airway management drugs discarded |
| ANATAirwayMgtETTSizeDR | bigint |  | FK | SI | Airway management ETT size |
| ANATAirwayMgtLMASizeDR | bigint |  | FK | SI | Airway management LMA size |
| ANATAirwayMgtLaryngoViewDR | bigint |  | FK | SI | Airway management Laryngoscopic View |
| ANATAirwayMgtMaskVentilation | varchar |  |  | SI | Airway management mask ventilation |
| ANATAirwayMgtPEEP | integer |  |  | SI | Airway management PEEP |
| ANATAirwayMgtThroatPkInserted | bit |  |  | SI | Airway management throat pack inserted |
| ANATAirwayMgtThroatPkRemoved | bit |  |  | SI | Airway management throat pack removed |
| ANATAirwayMgtVentPressure | double |  |  | SI | Airway management ventilation pressure |
| ANATAirwayMgtVentRate | integer |  |  | SI | Airway management ventilation rate |
| ANATAnaestMethods | varchar |  |  | SI | List of Anaesthetic Methods |
| ANATAnalgetics | varchar |  |  | SI | List of Analgesics |
| ANATAncillaryEquips | varchar |  |  | SI | List of Ancillary Care Equipments |
| ANATAnestDuration | double |  |  | SI | Duration of Anesthesia |
| ANATBagMaskVentDR | bigint |  | FK | SI | Bag-Mask Ventilation |
| ANATBldtTypeDR | bigint |  | FK | SI | Des Ref BldtType |
| ANATBolusDrugsUsed | varchar |  |  | SI | Initial Bolus/Drugs Used |
| ANATBypassLocDR | bigint |  | FK | SI | Bypass Location |
| ANATBypassRec | varchar |  |  | SI | Bypass Recovery |
| ANATCOMPDR | bigint |  | FK | SI | Des Ref to ORANCOMP |
| ANATCircTypes | varchar |  |  | SI | List of Airway Circuits |
| ANATCompComments | varchar |  |  | SI | Anaesthetic Complications Comments |
| ANATComplicationCards | varchar |  |  | SI | List of Complication Cards |
| ANATComplicationOthers | varchar |  |  | SI | List of Complication Others |
| ANATComplicationResps | varchar |  |  | SI | List of Complication Respiratories |
| ANATCuffIntubTube | varchar |  |  | SI | Is there a cuff in Intub Tube |
| ANATDEOAirwayMgtAnalgesiaDR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management awa... |
| ANATDEOAirwayMgtCanInsSiteDR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| ANATDEOAirwayMgtCanInserted | date |  |  | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| ANATDEOAirwayMgtCanSizeDR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management can... |
| ANATDEOAirwayMgtComments | varchar |  |  | SI | DSU /Endoscopy/Opthalmology airways Management com... |
| ANATDEOAirwayMgtO2FlowRate | double |  |  | SI | DSU /Endoscopy/Opthalmology airways Management O2 ... |
| ANATDEOAirwayMgtPosSupine | bit |  |  | SI | DSU /Endoscopy/Opthalmology airways Management pat... |
| ANATDEOAirwayMgtVentModeDR | bigint |  | FK | SI | DSU /Endoscopy/Opthalmology airways Management ven... |
| ANATDSReportFlag | varchar |  |  | SI | DSReportFlag |
| ANATDate | date |  |  | SI | Last Update Date |
| ANATDesc | varchar |  |  | NO | Description |
| ANATETTTypeDR | bigint |  | FK | SI | ETT(Endotracheal Tube) Type |
| ANATExtubDone | varchar |  |  | SI | Extubation Done |
| ANATGenBlock2PositionDR | bigint |  | FK | SI | Second general block information - operation posit... |
| ANATGenBlockAntisepsisDR | bigint |  | FK | SI | general block information - antisepsis |
| ANATGenBlockPositionDR | bigint |  | FK | SI | general block information - operation position |
| ANATIVCannulaSizeDR | bigint |  | FK | SI | IV Cannula Size |
| ANATIVInsertSites | varchar |  |  | SI | List of Cannula Insertion Sites |
| ANATIndTypes | varchar |  |  | SI | List of Induction Techniques |
| ANATIntubGradeDR | bigint |  | FK | SI | Intubation Grade Des Ref to ORCIG |
| ANATIntubRouteDR | bigint |  | FK | SI | Intubation Route Des Ref to ORCIR |
| ANATLMATypeDR | bigint |  | FK | SI | LMA(Laryngeal Mask Airway) Type |
| ANATLineTypes | varchar |  |  | SI | List of Pre Anaesthetic Lines |
| ANATMethodDR | bigint |  | FK | SI | Method of Anaest. |
| ANATMethodTypes | varchar |  |  | SI | List of Anaesthesia Method Types |
| ANATMnTypes | varchar |  |  | SI | List of Monitoring and Technique Maintenances |
| ANATMonOtherTechniques | varchar |  |  | SI | List of Other Techniques |
| ANATMonitorDevices | varchar |  |  | SI | List of Monitoring Devices |
| ANATMonitoringTechComments | varchar |  |  | SI | monitoring technique comments |
| ANATNeurax2Approach | varchar |  |  | SI | Nueraxial Anaesthesia 2 - Approach  |
| ANATNeurax2EpiduralLevelDR | bigint |  | FK | SI | Nueraxial Anaesthesia 2 - Epidural Level |
| ANATNeurax2EpiduralNeedleDR | bigint |  | FK | SI | Nueraxial Anaesthesia 2 - Epidural Needle |
| ANATNeurax2PositionDR | bigint |  | FK | SI | Neuraxial Anaesthesia 2 - Position |
| ANATNeurax2SkinPrepComment | varchar |  |  | SI | Nueraxial Anaesthesia 2 - Skin Prep Comment  |
| ANATNeuraxApproach | varchar |  |  | SI | Nueraxial Anaesthesia - Approach  |
| ANATNeuraxEpiduralCatheterToSkin | double |  |  | SI | Nueraxial Anaesthesia Epidural Catheter To Skin |
| ANATNeuraxEpiduralComments | varchar |  |  | SI | Nueraxial Anaesthesia Comments |
| ANATNeuraxEpiduralDrugsUsed | varchar |  |  | SI | Nueraxial Anaesthesia Epidural Initial Bolus/Drugs... |
| ANATNeuraxEpiduralLevelDR | bigint |  | FK | SI | Nueraxial Anaesthesia Epidural Level |
| ANATNeuraxEpiduralNeedleDR | bigint |  | FK | SI | Nueraxial Anaesthesia Epidural Needle |
| ANATNeuraxEpiduralTip | double |  |  | SI | Nueraxial Anaesthesia Epidural Tip To |
| ANATNeuraxPositionDR | bigint |  | FK | SI | Neurax general block information - operation posit... |
| ANATNeuraxSkinPrepComment | varchar |  |  | SI | Neurax block information - Skin Prep Comment  |
| ANATNeuraxSkinPrepDR | bigint |  | FK | SI | Nueraxial Anaesthesia Skin Preparation |
| ANATNeuraxSpinalLevelDR | bigint |  | FK | SI | Nueraxial Anaesthesia Spinal Level |
| ANATNeuraxSpinalNeedleDR | bigint |  | FK | SI | Nueraxial Anaesthesia Spinal Needle |
| ANATNeuraxSpinalNeedleTypeDR | bigint |  | FK | SI | Nueraxial Anaesthesia Spinal Needle Type |
| ANATNeuraxUSGuidance | varchar |  |  | SI | Nueraxial Anaesthesia U/S Guidance |
| ANATNeuraxUSTechniqueDR | bigint |  | FK | SI | Nueraxial Anaesthesia U/S Technique |
| ANATNotes | varchar |  |  | SI | Notes |
| ANATO2DelModeEndo | varchar |  |  | SI | List of Anaesthetic Oxygen Delivery Mode Endo |
| ANATOrbital05MarcainWithHylase | double |  |  | SI | Orbital Blocks 0.5% Marcaine plain with Hylase |
| ANATOrbital075RopiWidthHylase | double |  |  | SI | Orbital Blocks 0.75% Ropivocaine with Hylase |
| ANATOrbital1RopiWidthHylase | double |  |  | SI | Orbital Blocks 1% Ropivocaine with Hylase |
| ANATOrbital2LignoWithHylase | double |  |  | SI | Orbital Blocks 2% Lignocaine plain with Hylase |
| ANATOrbitalAgents | varchar |  |  | SI | List of Orbital Agents |
| ANATOrbitalBlocks | varchar |  |  | SI | List of Orbital Blocks |
| ANATOrbitalComments | varchar |  |  | SI | Orbital Blocks Comments |
| ANATOrbitalEyeDropsDR | bigint |  | FK | SI | Orbital Blocks Eye Drops |
| ANATOrbitalNeedleTypeDR | bigint |  | FK | SI | Orbital Blocks Needle Type |
| ANATOutcomeOfSurgeryDR | bigint |  | FK | SI | Des Ref OutcomeOfSurgery |
| ANATPatPositions | varchar |  |  | SI | List of Pat Positions |
| ANATPostOperInstructions | varchar |  |  | SI | PostOperInstructions |
| ANATPreAnaAssessHistory | varchar |  |  | SI | Pre Assessment History - Notes |
| ANATPreAnaAssessPlan | varchar |  |  | SI | Pre-anaesthetic assessment plan |
| ANATPrevMethodDR | bigint |  | FK | SI | Des Ref PrevMethod |
| ANATPrevRecOpDR | bigint |  | FK | SI | Des Ref PrevRecOp |
| ANATPrevRecSPPPDR | bigint |  | FK | SI | Des Ref PrevRecSPPP |
| ANATRBOperatingRoomDR | bigint |  | FK | SI | DR RBOperatingRoom |
| ANATRecovOperDR | bigint |  | FK | SI | Des Ref RecovOper |
| ANATRecovSPPPDR | bigint |  | FK | SI | Des Ref RecovSPPP |
| ANATRegBlock2AnaTypeComment | varchar |  |  | SI | Second block information - Anaesthesia Type Commen... |
| ANATRegBlock2Comments | varchar |  |  | SI | Second block information - nerve location techniqu... |
| ANATRegBlock2ParasthesiaDR | bigint |  | FK | SI | Second block information - nerve location techniqu... |
| ANATRegBlock2SideDR | bigint |  | FK | SI | Second block information - Block Side |
| ANATRegBlock2SkinPrepComment | varchar |  |  | SI | Second block information - Skin Prep Comment  |
| ANATRegBlock2SurfLandmarkDR | bigint |  | FK | SI | Second block information - nerve location techniqu... |
| ANATRegBlock2Technique | varchar |  |  | SI | Block 2 information - Technique |
| ANATRegBlockAnaTypeComment | varchar |  |  | SI | Regional block information - Anaesthesia Type Comm... |
| ANATRegBlockComments | varchar |  |  | SI | regional block information - nerve location techni... |
| ANATRegBlockParasthesiaDR | bigint |  | FK | SI | regional block information - nerve location techni... |
| ANATRegBlockSideDR | bigint |  | FK | SI | Regional block information - Block Side |
| ANATRegBlockSkinPrepComment | varchar |  |  | SI | Regional block information - Skin Prep Comment  |
| ANATRegBlockStimCurrent | varchar |  |  | SI | regional block information - nerve location techni... |
| ANATRegBlockSurfLandmarkDR | bigint |  | FK | SI | regional block information - nerve location techni... |
| ANATRegBlockTechnique | varchar |  |  | SI | Regional block information - Technique |
| ANATRegBlockUltraSoundGuided | varchar |  |  | SI | regional block information - nerve location techni... |
| ANATRegDrugsAdm | varchar |  |  | SI | Regional Drugs Administered |
| ANATRegPositions | varchar |  |  | SI | List of Operation Positions |
| ANATSavedRef | varchar |  |  | NO | Saved Reference ID |
| ANATSavedType | varchar |  |  | NO | Saved Type (SITE, User.SSGroup, User.SSUser) |
| ANATSourceType | varchar |  |  | SI | Source Type |
| ANATTextArea3 | varchar |  |  | SI | Text Area 3 |
| ANATTime | time |  |  | SI | Last Update Time |
| ANATTransLocDR | bigint |  | FK | SI | Transfer to Loc Des Ref to CTLOC |
| ANATUpdateUserDR | bigint |  | FK | SI | Last Update User |
| ANATVentTypes | varchar |  |  | SI | List of Ventilation Modes |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Maternal position |
| Q04 | - |  |  | SI | Number of attempts to collect sample |
| Q05 | - |  |  | SI | Sample collected by |
| Q06 | - |  |  | SI | Fetal blood sample obtained |
| Q07 | - |  |  | SI | Fetal scalp lactate result (mmol/L) |
| Q07ObsDR | - |  |  | SI | Fetal scalp lactate result (mmol/L) DR |
| Q08 | - |  |  | SI | Result verified |
| Q09 | - |  |  | SI | Verified by |
| Q10 | - |  |  | SI | Comments |
| Q11 | - |  |  | SI | Management plan |
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