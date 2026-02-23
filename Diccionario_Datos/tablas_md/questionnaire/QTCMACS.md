# questionnaire.QTCMACS

> Manual Ability Classification System - MACS

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Manual Ability Classification System - MACS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Child's ability to handle objects in important dai... |
| Q02 | varchar |  |  | SI | 1 - Handles objects easily and successfully.  |
| Q03 | varchar |  |  | SI | At most, limitations in the ease of performing man... |
| Q04 | varchar |  |  | SI | 2 - Handles most objects but with somewhat reduced... |
| Q05 | varchar |  |  | SI | Certain activities may be avoided or be achieved w... |
| Q06 | varchar |  |  | SI | 3 - Handles objects with difficulty; needs help to... |
| Q07 | varchar |  |  | SI | The performance is slow and achieved with limited ... |
| Q08 | varchar |  |  | SI | 4 - Handles a limited selection of easily managed ... |
| Q09 | varchar |  |  | SI | Performs parts of activities with effort and with ... |
| Q10 | varchar |  |  | SI | 5 - Does not handle objects and has severely limit... |
| Q11 | varchar |  |  | SI | Requires total assistance. |
| Q12 | varchar |  |  | SI | Distinctions between Levels 1 and 2: |
| Q13 | varchar |  |  | SI | Children in Level 1 may have limitations in handli... |
| Q14 | varchar |  |  | SI | Limitations may also involve performance in new an... |
| Q15 | varchar |  |  | SI | Children in Level 2 perform almost the same activi... |
| Q16 | varchar |  |  | SI | Functional differences between hands can limit eff... |
| Q17 | varchar |  |  | SI | Children in Level 2 commonly try to simplify handl... |
| Q18 | varchar |  |  | SI | Distinctions between Levels 2 and 3: |
| Q19 | varchar |  |  | SI | Children in Level 2 handle most objects, although ... |
| Q20 | varchar |  |  | SI | Children in Level 3 commonly need help to prepare ... |
| Q21 | varchar |  |  | SI | They cannot perform certain activities and their d... |
| Q22 | varchar |  |  | SI | Distinction between Levels 3 and 4: |
| Q23 | varchar |  |  | SI | Children in Level 3 can perform selected activitie... |
| Q24 | varchar |  |  | SI | Children in Level 4 need continuous help during th... |
| Q25 | varchar |  |  | SI | Distinctions between Levels 4 and 5: |
| Q26 | varchar |  |  | SI | Children in Level 4 perform part of an activity, h... |
| Q27 | varchar |  |  | SI | Children in Level 5 might at best participate with... |
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