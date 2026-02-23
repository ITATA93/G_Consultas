# SQLUser.PA_AdmPriority

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Admisión de Pacientes**. Registra episodios de atención hospitalaria.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRI_ParRef | bigint | PK |  | NO | PA_Adm Parent Reference |
| PRI_Childsub | double |  |  | NO | Childsub |
| PRI_Date | date |  |  | SI | Date |
| PRI_Priority_DR | bigint |  | FK | SI | Des Ref Priority |
| PRI_ProposedPriority_DR | bigint |  | FK | SI | Proposed Priority |
| PRI_RowId | varchar |  |  | NO | - |
| PRI_Time | time |  |  | SI | Time |
| PRI_TriageCatChReaComments | varchar |  |  | SI | TriageCategoryChangeReasonComment |
| PRI_TriageCatChangeReason_DR | bigint |  | FK | SI | Des Ref PACTriageCatChangeReason |
| PRI_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Roll to weak side |
| Q02 | - |  |  | SI | Roll to strong side |
| Q03 | - |  |  | SI | Balance in sitting position on the edge of the bed... |
| Q04 | - |  |  | SI | Sit up from lying down |
| Q05 | - |  |  | SI | Score |
| Q06 | - |  |  | SI | Classification |
| Q07 | - |  |  | SI | 0 - 100 |
| Q08 | - |  |  | SI | A higher score indicates better performance |
| Q09 | - |  |  | SI | 0 - 100: A higher score indicates better performan... |
| Q10 | - |  |  | SI | The Trunk Control Test (TCT) measures four simple ... |
| Q11 | - |  |  | SI | If the test is done at 6 weeks after stroke a scor... |
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