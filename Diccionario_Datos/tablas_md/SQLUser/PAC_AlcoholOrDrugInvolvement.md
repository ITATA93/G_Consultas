# SQLUser.PAC_AlcoholOrDrugInvolvement

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALCDRGIN_RowId | bigint | PK |  | NO | - |
| ALCDRGIN_Code | varchar |  |  | NO | Code |
| ALCDRGIN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALCDRGIN_CreatedDate | date |  |  | SI | Created Date |
| ALCDRGIN_CreatedTime | time |  |  | SI | Created Time |
| ALCDRGIN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALCDRGIN_DateFrom | date |  |  | SI | Date From |
| ALCDRGIN_DateTo | date |  |  | SI | Date To |
| ALCDRGIN_Desc | varchar |  |  | NO | Description |
| ALCDRGIN_NationalCode | varchar |  |  | SI | National Code |
| ALCDRGIN_Owner | varchar |  |  | SI | Owner |
| ALCDRGIN_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| ALCDRGIN_UpdatedDate | date |  |  | SI | Updated Date |
| ALCDRGIN_UpdatedTime | time |  |  | SI | Updated Time |
| ALCDRGIN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Head control |
| Q04 | - |  |  | SI | Sitting |
| Q05 | - |  |  | SI | Image question sitting |
| Q06 | - |  |  | SI | Voluntary grasp - note side |
| Q07 | - |  |  | SI | Ability to kick in supine |
| Q08 | - |  |  | SI | Image question Ability to kick in supine |
| Q09 | - |  |  | SI | Rolling |
| Q10 | - |  |  | SI | Crawling or bottom shuffling |
| Q11 | - |  |  | SI | Image question crawling or bottom shuffling |
| Q12 | - |  |  | SI | Standing |
| Q13 | - |  |  | SI | Walking |
| Q14 | - |  |  | SI | Score |
| Q15 | - |  |  | SI | Classification |
| Q16 | - |  |  | SI | 1 - 26 |
| Q17 | - |  |  | SI | Higher scores represents better performance |
| Q18 | - |  |  | SI | 1 - 26: Higher scores represents better performanc... |
| Q19 | - |  |  | SI | The Hammersmith Infant Neurological Examination (H... |
| Q20 | - |  |  | SI | Walking |
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