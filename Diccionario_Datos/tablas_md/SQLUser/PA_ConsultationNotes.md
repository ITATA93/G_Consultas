# SQLUser.PA_ConsultationNotes

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NOTES_ParRef | bigint | PK |  | NO | PA_Consultation Parent Reference |
| NOTES_Childsub | double |  |  | NO | Childsub |
| NOTES_ConsCategory_DR | bigint |  | FK | SI | Des Ref ConsCategory |
| NOTES_CreateDate | date |  |  | SI | Create Date |
| NOTES_CreateTime | time |  |  | SI | Create Time |
| NOTES_CreateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| NOTES_Notes | varchar |  |  | SI | Notes |
| NOTES_RowId | varchar |  |  | NO | - |
| NOTES_Status | varchar |  |  | SI | Status |
| NOTES_Type | varchar |  |  | SI | Type |
| NOTES_UpdateDate | date |  |  | SI | Update Date |
| NOTES_UpdateTime | time |  |  | SI | Update Time |
| NOTES_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | 1 Point Risk Factors |
| Q04 | - |  |  | SI | 2 Point Risk Factors |
| Q05 | - |  |  | SI | 3 Point risk factors |
| Q06 | - |  |  | SI | 4 Point Risk Factors |
| Q07 | - |  |  | SI | Contraindications for elastic stocking |
| Q08 | - |  |  | SI | Contradindication for VTE phrophylaxis |
| Q09 | - |  |  | SI | Venous Thrombolism Risk Assesment based on NICE gu... |
| Q10 | - |  |  | SI | 0 |
| Q11 | - |  |  | SI | Lowest VTE Risk < 10% |
| Q12 | - |  |  | SI | 1 - 2 |
| Q13 | - |  |  | SI | Low VTE Risk 10 - 20% |
| Q14 | - |  |  | SI | 3 - 4 |
| Q15 | - |  |  | SI | Moderate VTE Risk 20 - 40% |
| Q16 | - |  |  | SI | ≥ 5 |
| Q17 | - |  |  | SI | High VTE Risk 40% - 80% |
| Q18 | - |  |  | SI | Score |
| Q19 | - |  |  | SI | Classification |
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