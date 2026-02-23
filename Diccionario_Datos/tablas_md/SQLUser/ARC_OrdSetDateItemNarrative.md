# SQLUser.ARC_OrdSetDateItemNarrative

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITMN_ParRef | varchar | PK |  | NO | ARC_OrdSetDateItem Parent Reference |
| ITMN_Active | bit |  |  | SI | Active - Only active narratives will display in th... |
| ITMN_Childsub | double |  |  | NO | Childsub |
| ITMN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITMN_CreatedDate | date |  |  | SI | Created Date |
| ITMN_CreatedTime | time |  |  | SI | Created Time |
| ITMN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ITMN_DisplaySource | bit |  |  | SI | Display Source - will display Source at the end of... |
| ITMN_RecommendationLevel_DR | bigint |  | FK | SI | Des Ref to Recommendation Level - will display at ... |
| ITMN_RowId | varchar |  |  | NO | - |
| ITMN_Source_DR | bigint |  | FK | SI | Des Ref to Source of the Narrative information |
| ITMN_Stream_DR | bigint |  | FK | SI | Narrative Stream  |
| ITMN_Type | varchar |  |  | SI | Narrative Type - Uses the standard type "Narrative... |
| ITMN_UpdatedDate | date |  |  | SI | Updated Date |
| ITMN_UpdatedTime | time |  |  | SI | Updated Time |
| ITMN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Peso |
| Q01ObsDR | - |  |  | SI | Peso DR |
| Q02 | - |  |  | SI | Estatura |
| Q02ObsDR | - |  |  | SI | Estatura DR |
| Q03 | - |  |  | SI | Peso Ideal (Hombres) |
| Q04 | - |  |  | SI | Peso Ideal (Mujeres) |
| Q05 | - |  |  | SI | Peso Ajustado (Hombres) |
| Q06 | - |  |  | SI | Peso Ajustado (Mujeres) |
| Q07 | - |  |  | SI | Peso Magro (Hombres) |
| Q08 | - |  |  | SI | Peso Magro (Mujeres) |
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