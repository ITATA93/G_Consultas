# web_Msg.LBC_TestSetRevisionAutoAuthorisation

**Schema:** web_Msg
**Columnas:** 57
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRAA_AnatomicalSiteQualifier_DR | varchar |  | FK | SI | Anatomical Site Qualifier |
| LBCTSRAA_AnatomicalSiteQualifiers | varchar |  |  | SI | Anatomical Site Qualifiers |
| LBCTSRAA_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRAA_AnatomicalSites | varchar |  |  | SI | Anatomical Sites |
| LBCTSRAA_AuthorisationMode | varchar |  |  | SI | Auto Authorisation Mode
 - Disabled (default valu... |
| LBCTSRAA_AuthorisingUser_DR | bigint |  | FK | SI | User assigned to Auto Auth |
| LBCTSRAA_AutoFailureQueue_DR | bigint |  | FK | SI | Failure queue to which the test set will be added ... |
| LBCTSRAA_BloodProductGroup_DR | bigint |  | FK | SI | Blood Product Group |
| LBCTSRAA_CareProv_DR | varchar |  | FK | SI | Requesting Care Provider |
| LBCTSRAA_ClinicalConditions | varchar |  |  | SI | Clinical Condition(s) - may be multiple |
| LBCTSRAA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRAA_Container_DR | bigint |  | FK | SI | Container |
| LBCTSRAA_Containers | varchar |  |  | SI | Containers |
| LBCTSRAA_Date | date |  |  | SI | Date of collection |
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
| LBCTSRAA_Lesions | varchar |  |  | SI | Lesions |
| LBCTSRAA_OnSpecialInterestQueue_DR | bigint |  | FK | SI | On Special Interest Queue |
| LBCTSRAA_OnSpecialInterestQueues | varchar |  |  | SI | On Special Interest Queue |
| LBCTSRAA_ParRef | bigint |  |  | SI | Parent Reference LBCTestSetRevisionDR |
| LBCTSRAA_PatientLocation_DR | bigint |  | FK | SI | Requesting Location |
| LBCTSRAA_PrevTestSetLookbackPeriod | numeric |  |  | SI | Lookback period for previous test set |
| LBCTSRAA_PrevTestSetNotFinal | varchar |  |  | SI | Check if a previous test set in the lookback perio... |
| LBCTSRAA_PrevTestSetOnFailQueue | varchar |  |  | SI |  Check if a previous test set in the lookback peri... |
| LBCTSRAA_Priority_DR | bigint |  | FK | SI | Priority |
| LBCTSRAA_ReferringRoctor_DR | bigint |  | FK | SI | Requesting Referral Doctor |
| LBCTSRAA_RowID | varchar |  |  | SI | - |
| LBCTSRAA_Sequence | double |  |  | SI | Priority  Sequence |
| LBCTSRAA_SpeciesBreed_DR | varchar |  | FK | SI | Breed |
| LBCTSRAA_Species_DR | bigint |  | FK | SI | Species |
| LBCTSRAA_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRAA_SpecimenGroups | varchar |  |  | SI | Specimen Groups |
| LBCTSRAA_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRAA_Specimens | varchar |  |  | SI | Specimens |
| LBCTSRAA_SubjectType_DR | bigint |  | FK | SI | SubjectType |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TestSetSpecimenValidityStatus | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*