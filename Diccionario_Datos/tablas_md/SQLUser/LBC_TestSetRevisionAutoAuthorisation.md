# SQLUser.LBC_TestSetRevisionAutoAuthorisation

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSRAA_ParRef | bigint | PK |  | NO | Parent Reference LBCTestSetRevisionDR |
| LBCTSRAA_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTSRAA_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRAA_AuthorisationMode | varchar |  |  | SI | Auto Authorisation Mode
 - Disabled (default valu... |
| LBCTSRAA_AuthorisingUser_DR | bigint |  | FK | SI | User assigned to Auto Auth |
| LBCTSRAA_AutoFailureQueue_DR | bigint |  | FK | SI | Failure queue to which the test set will be added ... |
| LBCTSRAA_BloodProductGroup_DR | bigint |  | FK | SI | Blood Product Group |
| LBCTSRAA_CareProv_DR | varchar |  | FK | SI | Requesting Care Provider |
| LBCTSRAA_ClinicalConditions | varchar |  |  | SI | Clinical Condition(s) - may be multiple |
| LBCTSRAA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRAA_Container_DR | bigint |  | FK | SI | Container |
| LBCTSRAA_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRAA_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRAA_EnableDeltaRangeChecksTestItems | varchar |  |  | SI | Enable Delta Range Checks for selected Test Items |
| LBCTSRAA_EnableQCChecks | varchar |  |  | SI | Enable Worksheet QC Checks
Instrument QC checks a... |
| LBCTSRAA_EnableRangeChecksTestItems | varchar |  |  | SI | Enable Auto/Normal Range Checks for selected Test ... |
| LBCTSRAA_EnableSignifResCheck | varchar |  |  | SI |  Enable Significant Result Check |
| LBCTSRAA_ExclInstrumentFlagTypes | varchar |  |  | SI | Exclude Instrument Flag Type |
| LBCTSRAA_ExcludeClinRevFlagged | varchar |  |  | SI |  Exclude Clinical Review Flagged |
| LBCTSRAA_ExcludeInvalidSpecimen | varchar |  |  | SI |  Exclude expired specimen validity flagged test se... |
| LBCTSRAA_ExcludePatientFlags | varchar |  |  | SI | Exclude Patient Flag |
| LBCTSRAA_IgnoreErrorInstrumentFlags | varchar |  |  | SI | Ignore Error Instrument Flags |
| LBCTSRAA_IgnoreRangeFailureIfDeltaCheckPasses | varchar |  |  | SI | Ignore any range failure if delta checks are appli... |
| LBCTSRAA_IgnoreWarningInstrumentFlags | varchar |  |  | SI | Ignore Warning Instrument Flags |
| LBCTSRAA_InstrumentGroup_DR | bigint |  | FK | SI | Instrument Group |
| LBCTSRAA_Instrument_DR | bigint |  | FK | SI | Instrument Code |
| LBCTSRAA_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRAA_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRAA_OnSpecialInterestQueue_DR | bigint |  | FK | SI | On Special Interest Queue |
| LBCTSRAA_PatientLocation_DR | bigint |  | FK | SI | Requesting Location |
| LBCTSRAA_PrevTestSetLookbackPeriod | numeric |  |  | SI | Lookback period for previous test set |
| LBCTSRAA_PrevTestSetNotFinal | varchar |  |  | SI | Check if a previous test set in the lookback perio... |
| LBCTSRAA_PrevTestSetOnFailQueue | varchar |  |  | SI |  Check if a previous test set in the lookback peri... |
| LBCTSRAA_Priority_DR | bigint |  | FK | SI | Priority |
| LBCTSRAA_ReferringRoctor_DR | bigint |  | FK | SI | Requesting Referral Doctor |
| LBCTSRAA_RowID | varchar |  |  | NO | - |
| LBCTSRAA_Sequence | double |  |  | SI | Priority  Sequence |
| LBCTSRAA_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTSRAA_Species_DR | bigint |  | FK | SI | Species |
| LBCTSRAA_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRAA_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRAA_SubjectType_DR | bigint |  | FK | SI | SubjectType |
| Q01 | - |  |  | SI | Nombre Cuidador |
| Q02 | - |  |  | SI | Diagnóstico |
| Q03 | - |  |  | SI | Fecha Ingreso |
| Q04 | - |  |  | SI | Alimentación e Hidratación |
| Q05 | - |  |  | SI | Nombre de Profesional |
| Q06 | - |  |  | SI | Eliminación |
| Q07 | - |  |  | SI | Movilización |
| Q08 | - |  |  | SI | Aseo y Cuidados de la Piel |
| Q09 | - |  |  | SI | Cuidados del Entorno |
| Q10 | - |  |  | SI | Cuidados del Cuidador |
| Q11 | - |  |  | SI | Otras Indicaciones |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*