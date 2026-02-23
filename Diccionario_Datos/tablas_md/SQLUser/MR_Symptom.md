# SQLUser.MR_Symptom

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SYM_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| Q01 | - |  |  | SI | Wound location |
| Q01N | - |  |  | SI | Note |
| Q02 | - |  |  | SI | Wound description |
| Q02N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Wound contamination / Foreign body |
| Q03N | - |  |  | SI | Note |
| Q04 | - |  |  | SI | Depth / Tissues involved |
| Q04N | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Distal sensation intact |
| Q05N | - |  |  | SI | Note |
| Q07 | - |  |  | SI | Distal movement intact |
| Q07N | - |  |  | SI | Note |
| Q09 | - |  |  | SI | Distal tendon function |
| Q09N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Other |
| Q16 | - |  |  | SI | NOTE: You will need to fill a seperate form for ea... |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
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
| SYM_Childsub | double |  |  | NO | Childsub |
| SYM_Comment | varchar |  |  | SI | Comment |
| SYM_CreateDate | date |  |  | SI | CreateDate |
| SYM_CreateTime | time |  |  | SI | CreateTime |
| SYM_Deleted | varchar |  |  | SI | Deleted |
| SYM_ICDCode_DR | bigint |  | FK | SI | Des Ref to MRCID |
| SYM_ICPCCode_DR | bigint |  | FK | SI | Des Ref to MRCICPC2 |
| SYM_Laterality | varchar |  |  | SI | Laterality |
| SYM_MasterVersion_DR | varchar |  | FK | SI | Des Ref MRSymptom |
| SYM_NoSymptomOf | bit |  |  | SI | NoSymptomOf |
| SYM_OnsetDate | date |  |  | SI | OnsetDate |
| SYM_OnsetTime | time |  |  | SI | OnsetTime |
| SYM_ROSSystem_DR | varchar |  | FK | SI | Des Ref MRCROSSystem
only used when symptom part ... |
| SYM_RefinedSiteSCTIDs | varchar |  |  | SI | RefinedSiteSCTIDs |
| SYM_ReviewOfSystems_DR | varchar |  | FK | SI | Des Ref MRReviewOfSystems
only used when symptom ... |
| SYM_RowId | varchar |  |  | NO | - |
| SYM_SeveritySnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| SYM_Severity_DR | bigint |  | FK | SI | Des Ref MRCSeverity |
| SYM_SiteSnomed_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| SYM_SiteText | varchar |  |  | SI | SiteText |
| SYM_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| SYM_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| SYM_UpdateDate | date |  |  | SI | UpdateDate |
| SYM_UpdateTime | time |  |  | SI | UpdateTime |
| SYM_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*