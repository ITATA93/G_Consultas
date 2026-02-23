# SQLUser.PAC_ContServiceRec

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CONTSERVREC_RowId | bigint | PK |  | NO | - |
| CONTSERVREC_Code | varchar |  |  | NO | Code |
| CONTSERVREC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CONTSERVREC_CreatedDate | date |  |  | SI | Created Date |
| CONTSERVREC_CreatedTime | time |  |  | SI | Created Time |
| CONTSERVREC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CONTSERVREC_DateFrom | date |  |  | SI | Date From |
| CONTSERVREC_DateTo | date |  |  | SI | Date To |
| CONTSERVREC_Desc | varchar |  |  | NO | Description |
| CONTSERVREC_Owner | varchar |  |  | SI | Owner |
| CONTSERVREC_UpdatedDate | date |  |  | SI | Updated Date |
| CONTSERVREC_UpdatedTime | time |  |  | SI | Updated Time |
| CONTSERVREC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ21DR | - |  |  | SI | Child Reference: Assessment |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Activity |
| Q04 | - |  |  | SI | Peripheral intravenous present |
| Q05 | - |  |  | SI | Insertion date and time |
| Q06 | - |  |  | SI | Insertion time |
| Q07 | - |  |  | SI | Total days of insertion |
| Q08 | - |  |  | SI | Catheter type |
| Q09 | - |  |  | SI | Laterality |
| Q10 | - |  |  | SI | Site |
| Q11 | - |  |  | SI | Reason for insertion |
| Q12 | - |  |  | SI | Patient identified |
| Q13 | - |  |  | SI | Insertion unit |
| Q14 | - |  |  | SI | Performing provider |
| Q15 | - |  |  | SI | Assisting in insertion |
| Q16 | - |  |  | SI | Procedure preparation |
| Q17 | - |  |  | SI | Number of attempts |
| Q18 | - |  |  | SI | Procedure result |
| Q19 | - |  |  | SI | Referred to intravenous nurse |
| Q20 | - |  |  | SI | Comment |
| Q23 | - |  |  | SI | Site condition |
| Q24 | - |  |  | SI | Extravasation score |
| Q25 | - |  |  | SI | Infiltration score |
| Q26 | - |  |  | SI | Phlebitis score |
| Q27 | - |  |  | SI | Equipment used |
| Q28 | - |  |  | SI | Discontinue date and time |
| Q29 | - |  |  | SI | Discontinue time |
| Q30 | - |  |  | SI | Care provider discontinued the line |
| Q31 | - |  |  | SI | Discontinue reason |
| Q32 | - |  |  | SI | Unexpected events |
| Q33 | - |  |  | SI | Removal result |
| Q34 | - |  |  | SI | Size |
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