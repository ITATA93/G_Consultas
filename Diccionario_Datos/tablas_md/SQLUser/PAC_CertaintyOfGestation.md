# SQLUser.PAC_CertaintyOfGestation

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| GEST_RowId | bigint | PK |  | NO | - |
| ChildQ21DR | - |  |  | SI | Child Reference: Assessment |
| GEST_Code | varchar |  |  | NO | Code |
| GEST_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| GEST_CreatedDate | date |  |  | SI | Created Date |
| GEST_CreatedTime | time |  |  | SI | Created Time |
| GEST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| GEST_DateFrom | date |  |  | SI | Date From |
| GEST_DateTo | date |  |  | SI | Date To |
| GEST_Desc | varchar |  |  | NO | Description |
| GEST_NationalCode | varchar |  |  | SI | National Code |
| GEST_Owner | varchar |  |  | SI | Owner |
| GEST_UpdatedDate | date |  |  | SI | Updated Date |
| GEST_UpdatedTime | time |  |  | SI | Updated Time |
| GEST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Activity |
| Q04 | - |  |  | SI | Insertion date / time |
| Q05 | - |  |  | SI | Insertion time |
| Q06 | - |  |  | SI | Total days of insertion |
| Q07 | - |  |  | SI | Catheter type |
| Q08 | - |  |  | SI | Laterality |
| Q09 | - |  |  | SI | Site |
| Q10 | - |  |  | SI | Size |
| Q11 | - |  |  | SI | Reason for insertion |
| Q12 | - |  |  | SI | Patient identified |
| Q13 | - |  |  | SI | Insertion unit |
| Q14 | - |  |  | SI | Performing provider |
| Q15 | - |  |  | SI | Assisting in insertion |
| Q16 | - |  |  | SI | Procedure preparation |
| Q17 | - |  |  | SI | Number of attempts |
| Q18 | - |  |  | SI | Procedure result |
| Q19 | - |  |  | SI | Comment |
| Q20 | - |  |  | SI | Intraosseous Line Assessment |
| Q23 | - |  |  | SI | Site condition |
| Q24 | - |  |  | SI | Extravasation score |
| Q25 | - |  |  | SI | Infiltration score |
| Q26 | - |  |  | SI | Phlebitis score |
| Q27 | - |  |  | SI | Equipment used |
| Q28 | - |  |  | SI | Discontinuation details |
| Q29 | - |  |  | SI | Discontinue date / time |
| Q30 | - |  |  | SI | Discontinue time |
| Q31 | - |  |  | SI | Care provider discontinued the line |
| Q32 | - |  |  | SI | Discontinue reason |
| Q33 | - |  |  | SI | Unexpected events |
| Q34 | - |  |  | SI | Removal result |
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