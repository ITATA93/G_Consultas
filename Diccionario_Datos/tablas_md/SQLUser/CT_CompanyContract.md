# SQLUser.CT_CompanyContract

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONT_ParRef | bigint | PK |  | NO | CT_Company Parent Reference |
| CONT_AdditTestItems_DR | varchar |  | FK | SI | Des Ref to ARCOS |
| CONT_Childsub | double |  |  | NO | Childsub |
| CONT_Code | varchar |  |  | SI | Contract Code |
| CONT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONT_CreatedDate | date |  |  | SI | Created Date |
| CONT_CreatedTime | time |  |  | SI | Created Time |
| CONT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONT_DiscAmt | double |  |  | SI | Discount Amt |
| CONT_DiscPerc | double |  |  | SI | Discount % |
| CONT_DiscReason_DR | bigint |  | FK | SI | Des Ref  to DiscReason |
| CONT_EndDate | date |  |  | SI | End Date |
| CONT_INCI_DR | bigint |  | FK | SI | Des Ref INCI |
| CONT_No | double |  |  | SI | No of people |
| CONT_Notes | varchar |  |  | SI | Notes |
| CONT_RowId | varchar |  |  | NO | - |
| CONT_StartDate | date |  |  | SI | Start Date |
| CONT_TestType_DR | varchar |  | FK | SI | Des Ref to ARCOS |
| CONT_UpdatedDate | date |  |  | SI | Updated Date |
| CONT_UpdatedTime | time |  |  | SI | Updated Time |
| CONT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Incapacidad para mantenerse quieto o tranquilo |
| Q02 | - |  |  | SI | Hiperactividad motora o verbal, hiperrreactividad |
| Q03 | - |  |  | SI | Tensión emocional |
| Q04 | - |  |  | SI | Dificultades en la comunicación |
| Q05 | - |  |  | SI | Marca Velocímetro: 1 (Puntaje Screening 0-1) Manej... |
| Q06 | - |  |  | SI | Marca Velocímetro: 2 (Puntaje Screening 2) Manejo ... |
| Q07 | - |  |  | SI | Marca Velocímetro: 3 (Puntaje Screening 3-4) Manej... |
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