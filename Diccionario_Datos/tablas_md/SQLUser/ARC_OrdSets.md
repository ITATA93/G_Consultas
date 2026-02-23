# SQLUser.ARC_OrdSets

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCOS_RowId1 | varchar | PK |  | NO | - |
| ARCOS_ActiveFlag | varchar |  |  | SI | Archived Flag |
| ARCOS_AdditionICDList | varchar |  |  | SI | Additional Diagnosis List |
| ARCOS_AdmCategory_DR | bigint |  | FK | SI | Des Ref PACAdmCategory |
| ARCOS_AnaestMethod_DR | bigint |  | FK | SI | Expected Anaesthetic Method, Des Ref ORCAnaestMeth... |
| ARCOS_ApprovalRequired | varchar |  |  | SI | Requires Payor Approval |
| ARCOS_BedType_DR | bigint |  | FK | SI | Des Ref PACBedType - Bed Type |
| ARCOS_BillGroup_DR | bigint |  | FK | SI | Des Ref BillGroup |
| ARCOS_BillSub_DR | varchar |  | FK | SI | Des Ref BillSub |
| ARCOS_Code | varchar |  |  | NO | Order Set Code |
| ARCOS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ARCOS_CodeTranslated | varchar |  |  | SI | - |
| ARCOS_CreatedDate | date |  |  | SI | Created Date |
| ARCOS_CreatedTime | time |  |  | SI | Created Time |
| ARCOS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCOS_CurVerFlg | varchar |  |  | SI | Current |
| ARCOS_CurVers_DR | varchar |  | FK | SI | Current Version |
| ARCOS_DRGCode_DR | bigint |  | FK | SI | Provisional DRG, Des Ref MRCDRGCodes |
| ARCOS_DRGEpisode | varchar |  |  | SI | DRG Episode |
| ARCOS_Days | double |  |  | SI | Days |
| ARCOS_DefPriority_DR | bigint |  | FK | SI | Des Ref DefPriority |
| ARCOS_Desc | varchar |  |  | NO | Description |
| ARCOS_DescTranslated | varchar |  |  | SI | - |
| ARCOS_Details | longvarchar |  |  | SI | Details |
| ARCOS_DispOSListDuringOE | varchar |  |  | SI | Display Order Set List during order entry |
| ARCOS_DurationDR | bigint |  | FK | SI | Duration DR |
| ARCOS_EffDate | date |  |  | SI | Effective Date |
| ARCOS_EffDateFrom | date |  |  | NO | Effective Date From |
| ARCOS_EffDateTime | varchar |  |  | SI | Effective Date / Time |
| ARCOS_EffDateTo | date |  |  | SI | Effective Date To |
| ARCOS_EffTime | time |  |  | SI | Effective Time |
| ARCOS_EpisodeSubType_DR | bigint |  | FK | SI | Des Ref PACEpisodeSubType - Episode Sub Type |
| ARCOS_EpisodeType | varchar |  |  | SI | Episode Type |
| ARCOS_ExpAdmDate | varchar |  |  | SI | Expected Admission Date |
| ARCOS_ExpAnaestTime | double |  |  | SI | Expected Anaesthetic Time |
| ARCOS_ExpLOS | double |  |  | SI | Expected Length of Stay |
| ARCOS_ExternalServiceID | varchar |  |  | SI | ExternalServiceID |
| ARCOS_FrequencyDR | bigint |  | FK | SI | FrequencyDR |
| ARCOS_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| ARCOS_ICD_DR | bigint |  | FK | SI | Des Ref MRCICDDx - Primary Diagnosis |
| ARCOS_ItemType_DR | bigint |  | FK | SI | (needed? lsk) Des Ref to ARCIC |
| ARCOS_LabTrakTestSet | varchar |  |  | SI | LabTrak TestSet Code |
| ARCOS_Minutes | double |  |  | SI | Minutes |
| ARCOS_OperCateg_DR | bigint |  | FK | SI | Des Ref ORCOperationCategory |
| ARCOS_OrdCat_DR | bigint |  | FK | SI | Des Ref to OrdCat |
| ARCOS_OrdSubCat_DR | bigint |  | FK | SI | Des Ref to OrdSubCat |
| ARCOS_OrderQty | double |  |  | SI | Order Quantity |
| ARCOS_Owner | varchar |  |  | SI | Owner |
| ARCOS_PackagePrice | double |  |  | SI | Package Price |
| ARCOS_RespUnit_DR | bigint |  | FK | SI | Des Ref RespUnit |
| ARCOS_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| ARCOS_RowId | varchar |  |  | NO | ARCOS Row ID |
| ARCOS_SameDay | varchar |  |  | SI | Same Day |
| ARCOS_ServiceGroup_DR | bigint |  | FK | SI | Des Ref Service Group |
| ARCOS_Subscript | numeric |  |  | SI | Subscript |
| ARCOS_Type_Calc | varchar |  |  | SI | ARCOS_Type_Calc |
| ARCOS_UpdatedDate | date |  |  | SI | Updated Date |
| ARCOS_UpdatedTime | time |  |  | SI | Updated Time |
| ARCOS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ARCOS_Version | double |  |  | SI | Version |
| Q01 | - |  |  | SI | a) Epicrisis Médica |
| Q02 | - |  |  | SI | b) Epicrisis de Enfermería |
| Q03 | - |  |  | SI | c) Horas de Control |
| Q04 | - |  |  | SI | d) Exámenes |
| Q05 | - |  |  | SI | e) Material Educativo |
| Q06 | - |  |  | SI | f) Pertenencias Personales |
| Q07 | - |  |  | SI | g) Otros |
| Q08 | - |  |  | SI | Comentarios Epicrisis Médica |
| Q09 | - |  |  | SI | Comentarios Epicrisis de Enfermería |
| Q10 | - |  |  | SI | Comentarios Horas de Control |
| Q11 | - |  |  | SI | Comentarios Exámenes |
| Q12 | - |  |  | SI | Comentarios Material Educativo |
| Q13 | - |  |  | SI | Comentarios Pertenencias Personales |
| Q14 | - |  |  | SI | Comentarios Otros |
| Q15 | - |  |  | SI | Nombre de quien recibe los documentos |
| Q16 | - |  |  | SI | Relación con el Paciente |
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