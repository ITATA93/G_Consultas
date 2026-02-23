# SQLUser.MR_ClinDiagnosis

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLNDIAG_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| CLNDIAG_Childsub | double |  |  | NO | Childsub |
| CLNDIAG_Comment | varchar |  |  | SI | Comment |
| CLNDIAG_CreateDate | date |  |  | SI | CreateDate |
| CLNDIAG_CreateTime | time |  |  | SI | CreateTime |
| CLNDIAG_Deleted | varchar |  |  | SI | Deleted |
| CLNDIAG_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| CLNDIAG_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| CLNDIAG_IdentifiedByMe | varchar |  |  | SI | IdentifiedByMe |
| CLNDIAG_Laterality | varchar |  |  | SI | Laterality |
| CLNDIAG_MainEpisDiagnos | varchar |  |  | SI | MainEpisDiagnos |
| CLNDIAG_MasterVersion_DR | varchar |  | FK | SI | Des Ref MRClinDiagnosis |
| CLNDIAG_OnsetCalcDateAge | integer |  |  | SI | Calculated date "at the age of" |
| CLNDIAG_OnsetCalcDateAgeUnit | varchar |  |  | SI | Calculated date units "at the age of [num] [unit]  |
| CLNDIAG_OnsetCalcDateAgo | varchar |  |  | SI | Calculated date ago or from "[num] [unit] ago on/f... |
| CLNDIAG_OnsetCalcDateAgoNum | integer |  |  | SI | Calculated date number of units "[num] [unit] ago ... |
| CLNDIAG_OnsetCalcDateAgoUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| CLNDIAG_OnsetCalcDateBase | date |  |  | SI | date calculated date is based on |
| CLNDIAG_OnsetDate | date |  |  | SI | OnsetDate |
| CLNDIAG_OnsetTime | time |  |  | SI | OnsetTime |
| CLNDIAG_ReasonForChange | varchar |  |  | SI | ReasonForChange |
| CLNDIAG_RefinedSiteSCTIDs | varchar |  |  | SI | RefinedSiteSCTIDs |
| CLNDIAG_RowId | varchar |  |  | NO | - |
| CLNDIAG_SeveritySnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| CLNDIAG_Severity_DR | bigint |  | FK | SI | Des Ref MRCSeverity |
| CLNDIAG_SiteSnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| CLNDIAG_SiteText | varchar |  |  | SI | SiteText |
| CLNDIAG_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| CLNDIAG_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| CLNDIAG_Status | varchar |  |  | SI | Status |
| CLNDIAG_UpdateDate | date |  |  | SI | UpdateDate |
| CLNDIAG_UpdateTime | time |  |  | SI | UpdateTime |
| CLNDIAG_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| CLNDIAG_VersionReason | varchar |  |  | SI | VersionReason |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Percepcion de su salud |
| Q03 | - |  |  | SI | Solicita ayuda espiritual |
| Q04 | - |  |  | SI | Religion |
| Q05 | - |  |  | SI | Dificultad en la toma de decisiones |
| Q06 | - |  |  | SI | Conflictos entre creencias y cuidados de salud |
| Q07 | - |  |  | SI | Preocupacion por el sentido de la vida, muerte y v... |
| Q08 | - |  |  | SI | Valores importantes en su vida |
| Q09 | - |  |  | SI | Diagnostico 1 |
| Q10 | - |  |  | SI | Diagnostico 2 |
| Q11 | - |  |  | SI | Conclusion |
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