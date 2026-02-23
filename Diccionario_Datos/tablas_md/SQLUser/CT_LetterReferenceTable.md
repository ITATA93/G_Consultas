# SQLUser.CT_LetterReferenceTable

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LETREFT_RowId | bigint | PK |  | NO | - |
| ChildQ17DR | - |  |  | SI | Child Reference: Other Drugs / Substances |
| LETREFT_APPTAdminCategory_DR | bigint |  | FK | SI | Des Ref AccountClass |
| LETREFT_AppointCareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| LETREFT_AppointSpecialty_DR | bigint |  | FK | SI | Des Ref CTLoc |
| LETREFT_BaseTable | varchar |  |  | SI | BaseTable |
| LETREFT_CareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| LETREFT_Code | varchar |  |  | NO | Code |
| LETREFT_CreatedDate | date |  |  | SI | Created Date |
| LETREFT_CreatedTime | time |  |  | SI | Created Time |
| LETREFT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LETREFT_DateFrom | date |  |  | SI | DateFrom |
| LETREFT_DateTo | date |  |  | SI | DateTo |
| LETREFT_EpisodeSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType |
| LETREFT_EpisodeType | varchar |  |  | SI | Episode Type |
| LETREFT_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| LETREFT_ItemCat_DR | bigint |  | FK | SI | Des Ref ARCItemCat |
| LETREFT_ItmMast_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| LETREFT_LetterTemplate_DR | bigint |  | FK | SI | Des Ref CTLetterTemplate |
| LETREFT_LetterType_DR | bigint |  | FK | SI | Des Ref PACLetterType |
| LETREFT_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| LETREFT_Module_DR | bigint |  | FK | SI | Des Ref CTModules |
| LETREFT_Operation_DR | bigint |  | FK | SI | Des Ref ORCOperation |
| LETREFT_OrderRecLoc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| LETREFT_PACModule_DR | bigint |  | FK | SI | Des Ref PACModule |
| LETREFT_RTTPathway_DR | bigint |  | FK | SI | Des Ref RTTPathway |
| LETREFT_StatePPP_DR | bigint |  | FK | SI | Des Ref PACStatePPP |
| LETREFT_Surgeon_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| LETREFT_UpdatedDate | date |  |  | SI | Updated Date |
| LETREFT_UpdatedTime | time |  |  | SI | Updated Time |
| LETREFT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LETREFT_WLAdminCategory_DR | bigint |  | FK | SI | Des Ref PACAccountClass |
| LETREFT_WLCareProv_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| LETREFT_WLSpecialty_DR | bigint |  | FK | SI | Des Ref CTLoc |
| LETREFT_WLType_DR | bigint |  | FK | SI | Des Ref PACWaitingListType |
| LETREFT_Workflow_DR | bigint |  | FK | SI | Des Ref websys.WorkFlow |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Tell the patient, In this Health Service we ask al... |
| Q04 | - |  |  | SI | Alcohol |
| Q05 | - |  |  | SI | Do you drink daily and if so do you drink >2 drink... |
| Q06 | - |  |  | SI | Do you binge drink |
| Q07 | - |  |  | SI | At risk alcohol consumption - Males and females >2... |
| Q08 | - |  |  | SI | Alcohol last consumed on |
| Q09 | - |  |  | SI | Time alcohol last consumed on |
| Q10 | - |  |  | SI | Smoking / Vaping |
| Q11 | - |  |  | SI | Do you currently use nicotine / tobacco |
| Q12 | - |  |  | SI | Please complete the Fagerstrom Test |
| Q13 | - |  |  | SI | Nicotine Replacement Therapy (NRT) offered accordi... |
| Q14 | - |  |  | SI | Nicotine Replacement Therapy (NRT) initiated accor... |
| Q15 | - |  |  | SI | Patient referred to Alcohol and Other Drugs (AOD) ... |
| Q16 | - |  |  | SI | Other Drugs / Substances |
| Q18 | - |  |  | SI | Patient referred to alcohol and drug service for c... |
| Q19 | - |  |  | SI | Dummy1 |
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