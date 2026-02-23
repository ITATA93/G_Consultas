# questionnaire.QTCVIPS

> Puntaje Flebitis Infusión Visual (VIP)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Puntaje Flebitis Infusión Visual (VIP)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Cannula Insertion Site |
| Q03ObsDR | varchar |  | FK | SI | Cannula Insertion Site DR |
| Q04 | varchar |  |  | SI | VIP score checks |
| Q05 | varchar |  |  | SI | Score |
| Q06 | varchar |  |  | SI | Classification |
| Q07 | varchar |  |  | SI | 0: |
| Q08 | varchar |  |  | SI | No signs of phlebitis - OBSERVE CANNULA |
| Q09 | varchar |  |  | SI | 1: |
| Q10 | varchar |  |  | SI | Possible first signs - OBSERVE CANNULA |
| Q11 | varchar |  |  | SI | 2: |
| Q12 | varchar |  |  | SI | Early stage of phlebitis - RESITE CANNULA |
| Q13 | varchar |  |  | SI | 3: |
| Q14 | varchar |  |  | SI | Mid-stage of phlebitis - RESITE CANNULA | CONSIDER... |
| Q15 | varchar |  |  | SI | 4: |
| Q16 | varchar |  |  | SI | Advanced stage of phlebitis or start of thrombophl... |
| Q17 | varchar |  |  | SI | 5: |
| Q18 | varchar |  |  | SI | Advanced stage of thrombophlebitis – RESITE CANNUL... |
| Q19 | varchar |  |  | SI | The Visual Infusion Phlebitis (VIP) scoring tool a... |
| Q20 | varchar |  |  | SI | 0: No signs of phlebitis - OBSERVE CANNULA |
| Q21 | varchar |  |  | SI | 1: Possible first signs - OBSERVE CANNULA |
| Q22 | varchar |  |  | SI | 2: Early stage of phlebitis - RESITE CANNULA |
| Q23 | varchar |  |  | SI | 3: Mid-stage of phlebitis - RESITE CANNULA | CONSI... |
| Q24 | varchar |  |  | SI | 4: Advanced stage of phlebitis or start of thrombo... |
| Q25 | varchar |  |  | SI | 5:&nbsp;Advanced stage of thrombophlebitis – RESIT... |
| Q26 | varchar |  |  | SI | Gallant P and Schultz AA (2006) Evaluation of a vi... |
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