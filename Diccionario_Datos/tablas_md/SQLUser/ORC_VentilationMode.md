# SQLUser.ORC_VentilationMode

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VENMOD_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Current relationship status |
| Q02 | - |  |  | SI | Relationship status notes |
| Q03 | - |  |  | SI | Family support |
| Q04 | - |  |  | SI | Include details on local and distant family member... |
| Q05 | - |  |  | SI | Living accommodation |
| Q06 | - |  |  | SI | Living accommodation access |
| Q07 | - |  |  | SI | Is going up or down steps a problem for you? |
| Q08 | - |  |  | SI | Living accommodation notes |
| Q09 | - |  |  | SI | Education |
| Q10 | - |  |  | SI | Education level notes |
| Q11 | - |  |  | SI | Occupation (now or previously) |
| Q12 | - |  |  | SI | Employers name |
| Q13 | - |  |  | SI | Occupation status |
| Q15 | - |  |  | SI | When did this begin? |
| Q16 | - |  |  | SI | Physical demands at work |
| Q17 | - |  |  | SI | Notes on occupation including any work limitations |
| Q18 | - |  |  | SI | Stress |
| Q19 | - |  |  | SI | Stress areas |
| Q20 | - |  |  | SI | Describe any unusually high stress issues |
| Q21 | - |  |  | SI | Military service history |
| Q22 | - |  |  | SI | Military service details (War, length of service e... |
| Q23 | - |  |  | SI | Personal combat stress or family or social stress ... |
| Q24 | - |  |  | SI | Describe combat, family or social stress as a resu... |
| Q25 | - |  |  | SI | Date |
| Q26 | - |  |  | SI | Time |
| Q27 | - |  |  | SI | Physical environment and modification |
| Q28 | - |  |  | SI | Assistive devices / technology |
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
| VENMOD_Code | varchar |  |  | NO | Code |
| VENMOD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VENMOD_CreatedDate | date |  |  | SI | Created Date |
| VENMOD_CreatedTime | time |  |  | SI | Created Time |
| VENMOD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VENMOD_DateFrom | date |  |  | SI | Date From |
| VENMOD_DateTo | date |  |  | SI | Date To |
| VENMOD_Desc | varchar |  |  | NO | Description |
| VENMOD_Owner | varchar |  |  | SI | Owner |
| VENMOD_UpdatedDate | date |  |  | SI | Updated Date |
| VENMOD_UpdatedTime | time |  |  | SI | Updated Time |
| VENMOD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*