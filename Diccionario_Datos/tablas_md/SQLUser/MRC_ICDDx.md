# SQLUser.MRC_ICDDx

**Schema:** SQLUser
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MRCID_RowId | bigint | PK |  | NO | - |
| MRCID_2ndCodeInPair | varchar |  |  | SI | 2nd Code in Pair |
| MRCID_AdditionalCodeREqDR | bigint |  | FK | SI | Des Ref Additional Code Requirement |
| MRCID_Age2CheckType | varchar |  |  | SI | Age2CheckType |
| MRCID_Age2From | varchar |  |  | SI | Age2From |
| MRCID_Age2To | varchar |  |  | SI | Age2To |
| MRCID_AgeCheckType | varchar |  |  | SI | AgeCheckType |
| MRCID_AgeCheckType1DR | bigint |  | FK | SI | Des Ref Age Check Type1 |
| MRCID_AgeCheckType2_DR | bigint |  | FK | SI | Des Ref Age Check Type2 |
| MRCID_AgeFrom | varchar |  |  | SI | Age From |
| MRCID_AgeTo | varchar |  |  | SI | Age To |
| MRCID_AllowToDuplicate | varchar |  |  | SI | AllowToDuplicate |
| MRCID_AlternateDesc | varchar |  |  | SI | Alternate Desc |
| MRCID_AreaCodeRestraintDR | bigint |  | FK | SI | Area Code Restraint DR |
| MRCID_BillFlag1 | varchar |  |  | SI | Bill Flag 1 |
| MRCID_BillFlag2 | varchar |  |  | SI | Bill Flag 2 |
| MRCID_BillFlag3 | varchar |  |  | SI | Bill Flag 3 |
| MRCID_Billsub1_DR | varchar |  | FK | SI | Des Ref Billsub1 |
| MRCID_Billsub2_DR | varchar |  | FK | SI | Des Ref Billsub2 |
| MRCID_BodyArea_DR | bigint |  | FK | SI | Des Ref BodyArea |
| MRCID_BodySysProbStat_DR | bigint |  | FK | SI | Des Ref BodySysProbStat |
| MRCID_Cancer | varchar |  |  | SI | Cancer |
| MRCID_CodChapterBlockCateg_DR | varchar |  | FK | SI | Des Ref MRCICDCodChapterBlockCateg |
| MRCID_CodChapterBlock_DR | varchar |  | FK | SI | Des Ref MRCICDCodChapterBlock |
| MRCID_CodChapter_DR | bigint |  | FK | SI | Des Ref MRCICDCodChapter |
| MRCID_Code | varchar |  |  | SI | ICD Diagnosis Code |
| MRCID_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MRCID_CodeTranslated | varchar |  |  | SI | - |
| MRCID_CodingPracticesDR | bigint |  | FK | SI | Des Ref Coding Practices |
| MRCID_CreatedDate | date |  |  | SI | Created Date |
| MRCID_CreatedTime | time |  |  | SI | Created Time |
| MRCID_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MRCID_DaggerNAsteriskEditDR | bigint |  | FK | SI | Des Ref Dagger N Asterisk Edit |
| MRCID_DateActiveFrom | date |  |  | NO | Date Active From |
| MRCID_DateActiveTo | date |  |  | SI | Date Active To |
| MRCID_Desc | varchar |  |  | SI | Description |
| MRCID_DescTranslated | varchar |  |  | SI | - |
| MRCID_DiagGroup1_DR | bigint |  | FK | SI | Des Ref DiagGroup1 |
| MRCID_DiagGroup2 | varchar |  |  | SI | Diagnostic Group 2 |
| MRCID_EpisodeType | varchar |  |  | SI | EpisodeType |
| MRCID_ExtCauseDateMandatory | varchar |  |  | SI | External Cause Date Mandatory |
| MRCID_ExternalCause | varchar |  |  | SI | External Cause |
| MRCID_GenerateGES | varchar |  |  | SI | GenerateGES |
| MRCID_ICD9CM_Code | varchar |  |  | SI | ICD9CM Code |
| MRCID_ICD9_Map | varchar |  |  | SI | ICD9 Mapping |
| MRCID_InjuryPoisoningCode | varchar |  |  | SI | Injury/Poisoning Code |
| MRCID_InsDesc | varchar |  |  | SI | Description for Ins Co |
| MRCID_LongDescription | varchar |  |  | SI | Long Description |
| MRCID_MaxWaitPeriod | double |  |  | SI | Max Waiting Period |
| MRCID_MetastaticSite | varchar |  |  | SI | MetastaticSite |
| MRCID_MorphologyCode | varchar |  |  | SI | MorphologyCode |
| MRCID_Owner | varchar |  |  | SI | Owner |
| MRCID_PayorGroup_DR | bigint |  | FK | SI | Des Ref PayorGroup |
| MRCID_SeriousDis | varchar |  |  | SI | SeriousDisease |
| MRCID_SexCheckType | varchar |  |  | SI | SexCheckType |
| MRCID_SexCheckTypeDR | bigint |  | FK | SI | Des Ref to Sex Check Type |
| MRCID_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| MRCID_ShortDesc | varchar |  |  | SI | Short Description |
| MRCID_UnacceptablePDx | varchar |  |  | SI | Unacceptable PDx |
| MRCID_UpdatedDate | date |  |  | SI | Updated Date |
| MRCID_UpdatedTime | time |  |  | SI | Updated Time |
| MRCID_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| MRCID_Valid | varchar |  |  | SI | Valid |
| MRCID_ValidMCodeExt | varchar |  |  | SI | Valid M Code Extention |
| Q01 | - |  |  | SI | Resultado Indice Barthel |
| Q01ObsDR | - |  |  | SI | Resultado Indice Barthel DR |
| Q02 | - |  |  | SI | Previsión |
| Q03 | - |  |  | SI | Prais |
| Q04 | - |  |  | SI | Chile Solidario |
| Q05 | - |  |  | SI | PASIS |
| Q06 | - |  |  | SI | Ficha Protección Social Menor a 8.500 pts. |
| Q07 | - |  |  | SI | ¿Corresponde estipendio? |
| Q08 | - |  |  | SI | Asigna Estipendio |
| Q09 | - |  |  | SI | Número de Pacientes a cargo del cuidador |
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