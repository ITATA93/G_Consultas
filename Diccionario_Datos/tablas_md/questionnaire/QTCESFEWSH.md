# questionnaire.QTCESFEWSH

> Extended Social, Family, Education, Work and Stress History

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Extended Social, Family, Education, Work and Stress History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Current relationship status |
| Q02 | varchar |  |  | SI | Relationship status notes |
| Q03 | varchar |  |  | SI | Family support |
| Q04 | varchar |  |  | SI | Include details on local and distant family member... |
| Q05 | varchar |  |  | SI | Living accommodation |
| Q06 | varchar |  |  | SI | Living accommodation access |
| Q07 | varchar |  |  | SI | Is going up or down steps a problem for you? |
| Q08 | varchar |  |  | SI | Living accommodation notes |
| Q09 | varchar |  |  | SI | Education |
| Q10 | varchar |  |  | SI | Education level notes |
| Q11 | varchar |  |  | SI | Occupation (now or previously) |
| Q12 | varchar |  |  | SI | Employers name |
| Q13 | varchar |  |  | SI | Occupation status |
| Q15 | varchar |  |  | SI | When did this begin? |
| Q16 | varchar |  |  | SI | Physical demands at work |
| Q17 | varchar |  |  | SI | Notes on occupation including any work limitations |
| Q18 | varchar |  |  | SI | Stress |
| Q19 | varchar |  |  | SI | Stress areas |
| Q20 | varchar |  |  | SI | Describe any unusually high stress issues |
| Q21 | varchar |  |  | SI | Military service history |
| Q22 | varchar |  |  | SI | Military service details (War, length of service e... |
| Q23 | varchar |  |  | SI | Personal combat stress or family or social stress ... |
| Q24 | varchar |  |  | SI | Describe combat, family or social stress as a resu... |
| Q25 | date |  |  | SI | Date |
| Q26 | time |  |  | SI | Time |
| Q27 | varchar |  |  | SI | Physical environment and modification |
| Q28 | varchar |  |  | SI | Assistive devices / technology |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*