# SQLUser.ARC_ItemEpisodicBillingLimit

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LIM_ParRef | varchar | PK |  | NO | ARC_EpisodicBilling Parent Reference |
| LIM_ApplyLimitEachOrderItem | varchar |  |  | SI | Apply Limit to each Order Item |
| LIM_Childsub | double |  |  | NO | Childsub |
| LIM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LIM_CreatedDate | date |  |  | SI | Created Date |
| LIM_CreatedTime | time |  |  | SI | Created Time |
| LIM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LIM_DateFrom | date |  |  | SI | Date From |
| LIM_DateTo | date |  |  | SI | Date To |
| LIM_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| LIM_EpisodeType | varchar |  |  | SI | Episode Type |
| LIM_LimitAmount | double |  |  | SI | Limit Amount |
| LIM_Rank | double |  |  | SI | Rank |
| LIM_RowId | varchar |  |  | NO | - |
| LIM_UpdatedDate | date |  |  | SI | Updated Date |
| LIM_UpdatedTime | time |  |  | SI | Updated Time |
| LIM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age on onset |
| Q04 | - |  |  | SI | History of depression / mood disorder / anxiety / ... |
| Q05 | - |  |  | SI | History of migraines / severe headaches / personal... |
| Q06 | - |  |  | SI | Considering future in military / aviation / other ... |
| Q07 | - |  |  | SI | Family history of acne / family members had isotre... |
| Q08 | - |  |  | SI | History notes |
| Q09 | - |  |  | SI | Cheeks / Forehead |
| Q10 | - |  |  | SI | Involvement of |
| Q11 | - |  |  | SI | Other examination findings |
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