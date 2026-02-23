# SQLUser.NRC_ProblemSuggestion

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NRCPPS_RowId | bigint | PK |  | NO | - |
| NRCPPS_Code | varchar |  |  | NO | Code |
| NRCPPS_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| NRCPPS_CreatedDate | date |  |  | SI | Created Date |
| NRCPPS_CreatedTime | time |  |  | SI | Created Time |
| NRCPPS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NRCPPS_DateFrom | date |  |  | SI | Date From |
| NRCPPS_DateTo | date |  |  | SI | Date To |
| NRCPPS_Desc | varchar |  |  | NO | Description |
| NRCPPS_NRCProblem | varchar |  |  | SI | NRC Problem |
| NRCPPS_Owner | varchar |  |  | SI | Code Table Owner |
| NRCPPS_UpdatedDate | date |  |  | SI | Updated Date |
| NRCPPS_UpdatedTime | time |  |  | SI | Updated Time |
| NRCPPS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| NRCPPS_VisualRule_DR | bigint |  | FK | SI | Condition (Visual Rule) |
| Q01 | - |  |  | SI | Consultant who decided to give Methotrexate |
| Q02 | - |  |  | SI | Methotrexate given |
| Q02ObsDR | - |  |  | SI | Methotrexate given DR |
| Q03 | - |  |  | SI | Methotrexate cycle - Follow - up |
| Q04 | - |  |  | SI | Days post Methotrexate |
| Q05 | - |  |  | SI | Pain since Methotrexate |
| Q05ObsDR | - |  |  | SI | Pain since Methotrexate DR |
| Q06 | - |  |  | SI | Bleeding since Methotrexate |
| Q06ObsDR | - |  |  | SI | Bleeding since Methotrexate DR |
| Q07 | - |  |  | SI | Second dose of Methotrexate required |
| Q07ObsDR | - |  |  | SI | Second dose of Methotrexate required DR |
| Q08 | - |  |  | SI | Consultant who decided 2nd dose Methotrexate |
| Q09 | - |  |  | SI | HCG done |
| Q09ObsDR | - |  |  | SI | HCG done DR |
| Q10 | - |  |  | SI | HCG level within protocol |
| Q10ObsDR | - |  |  | SI | HCG level within protocol DR |
| Q11 | - |  |  | SI | US findings within protocol |
| Q11ObsDR | - |  |  | SI | US findings within protocol DR |
| Q12 | - |  |  | SI | Medical history within protocol |
| Q12ObsDR | - |  |  | SI | Medical history within protocol DR |
| Q13 | - |  |  | SI | Follow - up |
| Q13ObsDR | - |  |  | SI | Follow - up DR |
| Q14 | - |  |  | SI | Surgery required |
| Q14ObsDR | - |  |  | SI | Surgery required DR |
| Q15 | - |  |  | SI | Hospital consent form signed |
| Q15ObsDR | - |  |  | SI | Hospital consent form signed DR |
| Q16 | - |  |  | SI | Patient information consent signed |
| Q16ObsDR | - |  |  | SI | Patient information consent signed DR |
| Q17 | - |  |  | SI | Group and save date |
| Q18 | - |  |  | SI | Group and save done |
| Q18ObsDR | - |  |  | SI | Group and save done DR |
| Q19 | - |  |  | SI | Anti D required |
| Q19ObsDR | - |  |  | SI | Anti D required DR |
| Q20 | - |  |  | SI | Consultant who decided conservative management |
| Q21 | - |  |  | SI | Registrar reviewing patient |
| Q22 | - |  |  | SI | Comments |
| Q23 | - |  |  | SI | Consultant who decided surgery |
| Q24 | - |  |  | SI | Follow - up location |
| Q25 | - |  |  | SI | Methotrexate dose |
| Q25ObsDR | - |  |  | SI | Methotrexate dose DR |
| Q26 | - |  |  | SI | Methotrexate administration time |
| Q27 | - |  |  | SI | Methotrexate cycle |
| Q28 | - |  |  | SI | Anti D given |
| Q29 | - |  |  | SI | Anti D dose |
| Q29ObsDR | - |  |  | SI | Anti D dose DR |
| Q30 | - |  |  | SI | Anti D batch number |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
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