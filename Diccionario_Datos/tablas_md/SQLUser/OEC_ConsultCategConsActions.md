# SQLUser.OEC_ConsultCategConsActions

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONSACT_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| CONSACT_Childsub | double |  |  | NO | Childsub |
| CONSACT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONSACT_ConsActions_DR | bigint |  | FK | SI | Des Ref ConsActions |
| CONSACT_CreatedDate | date |  |  | SI | Created Date |
| CONSACT_CreatedTime | time |  |  | SI | Created Time |
| CONSACT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONSACT_Filter | varchar |  |  | SI | Filter |
| CONSACT_RowId | varchar |  |  | NO | - |
| CONSACT_SOAPType | varchar |  |  | SI | SOAPType |
| CONSACT_UpdatedDate | date |  |  | SI | Updated Date |
| CONSACT_UpdatedTime | time |  |  | SI | Updated Time |
| CONSACT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Duration of surgery is more than 60 minutes |
| Q02 | - |  |  | SI | Female |
| Q03 | - |  |  | SI | History of motion sickness |
| Q04 | - |  |  | SI | History of postoperative nausea and vomiting |
| Q05 | - |  |  | SI | Non-smoker |
| Q06 | - |  |  | SI | The nausea and vomiting score assesses a patients ... |
| Q07 | - |  |  | SI | 0: Risk of 17% |
| Q08 | - |  |  | SI | 1: Risk of 18% |
| Q09 | - |  |  | SI | 2: Risk of 42% |
| Q10 | - |  |  | SI | 3: Risk of 54% |
| Q11 | - |  |  | SI | 4: Risk of 74% |
| Q12 | - |  |  | SI | 5: Risk of 87% |
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