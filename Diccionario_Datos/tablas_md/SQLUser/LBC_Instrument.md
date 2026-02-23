# SQLUser.LBC_Instrument

**Schema:** SQLUser
**Columnas:** 160
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCIN_RowID | bigint | PK |  | NO | - |
| ChildQ24DR | - |  |  | SI | Child Reference: CTG |
| LBCIN_BloodPackDINLabel_DR | bigint |  | FK | SI | The report to use to produce the barcode-label of ... |
| LBCIN_Code | varchar |  |  | NO | Instrument Code |
| LBCIN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCIN_ControlledByInstrument_DR | bigint |  | FK | SI | Instrument is controlled by another instrument
On... |
| LBCIN_CreatedDate | date |  |  | SI | Created Date |
| LBCIN_CreatedTime | time |  |  | SI | Created Time |
| LBCIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCIN_DateCommissioning | date |  |  | SI | Date of commissioning |
| LBCIN_DateDecommissioning | date |  |  | SI | Date of de-commissioning |
| LBCIN_DateFrom | date |  |  | SI | Date From |
| LBCIN_DateReceiptEquipment | date |  |  | SI | Date of receipt of equipment |
| LBCIN_DateTo | date |  |  | SI | Date To |
| LBCIN_Department_DR | bigint |  | FK | NO | Department |
| LBCIN_Desc | varchar |  |  | NO | Instrument Description
HTMLTextBox |
| LBCIN_DeviceIndicator | varchar |  |  | SI | Unique device indicator |
| LBCIN_DisplayStatusMsgOnSpecRec | varchar |  |  | SI | Display status message at specimen receive |
| LBCIN_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBCIN_InstrumentID | varchar |  |  | SI | The instrument ID the analyser is known by the mid... |
| LBCIN_InstrumentInterfaceNamespace | varchar |  |  | SI | Namespace of the instrument interface production |
| LBCIN_InstrumentType | varchar |  |  | SI | Type of the instrument
Standard type: LabInstrume... |
| LBCIN_InterfaceType | varchar |  |  | SI | Type of the instrument interface
Standard type: L... |
| LBCIN_LabAssetNumber | varchar |  |  | SI | Unique laboratory asset number |
| LBCIN_LabSite_DR | bigint |  | FK | NO | Lab Site (Location)
For POCT instruments that is ... |
| LBCIN_ManufacturerName | varchar |  |  | SI | Manufacturer Name |
| LBCIN_Model | varchar |  |  | SI | Model |
| LBCIN_Owner | varchar |  |  | SI | Owner |
| LBCIN_POCTCareProvider_DR | varchar |  | FK | SI | POCT Ordering Care Provider |
| LBCIN_POCTLocation_DR | bigint |  | FK | SI | POCT Location, the physical location of the POCT i... |
| LBCIN_POCTSpeciality_DR | bigint |  | FK | SI | POCT Speciality, the execute location of the POCT ... |
| LBCIN_QCBracketDuration | integer |  |  | SI | QC Bracket Duration |
| LBCIN_QCBracketDurationUnit | varchar |  |  | SI | QC Bracket Duration unit |
| LBCIN_QCBracketNumEpisodes | integer |  |  | SI | QC Bracket Number Of Samples |
| LBCIN_QCBracketing | varchar |  |  | SI | Instrument QC Bracketing
Standard type: LabInstru... |
| LBCIN_QCMode | varchar |  |  | SI | Instrument QC Mode
Standard type: LabInstrumentQC... |
| LBCIN_QCRunStartTime | time |  |  | SI | Start time of the daily run
Only used for Instrum... |
| LBCIN_SerialNumber | varchar |  |  | SI | Serial Number |
| LBCIN_StatusMessage | varchar |  |  | SI | User Defined Status Message |
| LBCIN_TransmitsInstrumentIDs | varchar |  |  | SI | The middleware instrument transmits instrument IDs... |
| LBCIN_UpdatedDate | date |  |  | SI | Updated Date |
| LBCIN_UpdatedTime | time |  |  | SI | Updated Time |
| LBCIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCIN_UseSpecimenID | varchar |  |  | SI | Instrument uses Specimen IDs
Yes: reconcile is do... |
| Q01 | - |  |  | SI | Referred by |
| Q02 | - |  |  | SI | Referred by other |
| Q02ObsDR | - |  |  | SI | Referred by other DR |
| Q03 | - |  |  | SI | Reason for referral |
| Q03ObsDR | - |  |  | SI | Reason for referral DR |
| Q04 | - |  |  | SI | Temperature |
| Q04ObsDR | - |  |  | SI | Temperature DR |
| Q05 | - |  |  | SI | Pulse |
| Q05ObsDR | - |  |  | SI | Pulse DR |
| Q06 | - |  |  | SI | Systolic blood pressure |
| Q06ObsDR | - |  |  | SI | Systolic blood pressure DR |
| Q07 | - |  |  | SI | Diastolic blood pressure |
| Q07ObsDR | - |  |  | SI | Diastolic blood pressure DR |
| Q08 | - |  |  | SI | Visual disturbance |
| Q08ObsDR | - |  |  | SI | Visual disturbance DR |
| Q09 | - |  |  | SI | Headaches |
| Q09ObsDR | - |  |  | SI | Headaches DR |
| Q10 | - |  |  | SI | Epigastric pain |
| Q10ObsDR | - |  |  | SI | Epigastric pain DR |
| Q11 | - |  |  | SI | How are you feeling |
| Q11ObsDR | - |  |  | SI | How are you feeling DR |
| Q12 | - |  |  | SI | Urinalysis |
| Q12ObsDR | - |  |  | SI | Urinalysis DR |
| Q13 | - |  |  | SI | Oedema |
| Q13ObsDR | - |  |  | SI | Oedema DR |
| Q14 | - |  |  | SI | Blood pressure profile performed |
| Q14ObsDR | - |  |  | SI | Blood pressure profile performed DR |
| Q15 | - |  |  | SI | Fundal height |
| Q15ObsDR | - |  |  | SI | Fundal height DR |
| Q16 | - |  |  | SI | Lie |
| Q16ObsDR | - |  |  | SI | Lie DR |
| Q17 | - |  |  | SI | Presentation |
| Q17ObsDR | - |  |  | SI | Presentation DR |
| Q18 | - |  |  | SI | Fetal Position |
| Q18ObsDR | - |  |  | SI | Fetal Position DR |
| Q19 | - |  |  | SI | Presentation / 5ths palpable |
| Q19ObsDR | - |  |  | SI | Presentation / 5ths palpable DR |
| Q20 | - |  |  | SI | Membranes |
| Q20ObsDR | - |  |  | SI | Membranes DR |
| Q21 | - |  |  | SI | Fetal heart |
| Q21ObsDR | - |  |  | SI | Fetal heart DR |
| Q23 | - |  |  | SI | CTG required |
| Q23ObsDR | - |  |  | SI | CTG required DR |
| Q25 | - |  |  | SI | Number of contractions in 10mins |
| Q27 | - |  |  | SI | Fetal tone score |
| Q28 | - |  |  | SI | Fetal movement score |
| Q29 | - |  |  | SI | Amniotic fluid score |
| Q30 | - |  |  | SI | Fetal breathing score |
| Q31 | - |  |  | SI | Biophysical score |
| Q32 | - |  |  | SI | Vacuum Extraction Indication |
| Q32ObsDR | - |  |  | SI | Vacuum Extraction Indication DR |
| Q33 | - |  |  | SI | Consent obtained |
| Q33ObsDR | - |  |  | SI | Consent obtained DR |
| Q34 | - |  |  | SI | Cervical position |
| Q34ObsDR | - |  |  | SI | Cervical position DR |
| Q35 | - |  |  | SI | Cervical consistency |
| Q35ObsDR | - |  |  | SI | Cervical consistency DR |
| Q36 | - |  |  | SI | Cervical effacement / length |
| Q36ObsDR | - |  |  | SI | Cervical effacement / length DR |
| Q37 | - |  |  | SI | Cervical dilation |
| Q38 | - |  |  | SI | Presenting part |
| Q38ObsDR | - |  |  | SI | Presenting part DR |
| Q39 | - |  |  | SI | Relation to ischial spines |
| Q39ObsDR | - |  |  | SI | Relation to ischial spines DR |
| Q40 | - |  |  | SI | Fetal position |
| Q40ObsDR | - |  |  | SI | Fetal position DR |
| Q41 | - |  |  | SI | Caput |
| Q41ObsDR | - |  |  | SI | Caput DR |
| Q42 | - |  |  | SI | Moulding |
| Q42ObsDR | - |  |  | SI | Moulding DR |
| Q43 | - |  |  | SI | Comments |
| Q44 | - |  |  | SI | Follow-up |
| Q44ObsDR | - |  |  | SI | Follow-up DR |
| Q45 | - |  |  | SI | Midwife countersigning |
| Q46 | - |  |  | SI | Fetal movements felt by mother |
| Q46ObsDR | - |  |  | SI | Fetal movements felt by mother DR |
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