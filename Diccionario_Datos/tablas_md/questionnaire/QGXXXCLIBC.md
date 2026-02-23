# questionnaire.QGXXXCLIBC

> Central Line Insertion Bundle Checklist

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Central Line Insertion Bundle Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Type of catheter |
| Q01ObsDR | varchar |  | FK | SI | Type of catheter DR |
| Q02 | varchar |  |  | SI | Localisation of catheter |
| Q02ObsDR | varchar |  | FK | SI | Localisation of catheter DR |
| Q03 | varchar |  |  | SI | Characteristics of catheter |
| Q03ObsDR | varchar |  | FK | SI | Characteristics of catheter DR |
| Q04 | varchar |  |  | SI | Insertion reason |
| Q05 | varchar |  |  | SI | Explained procedure to patient and verified consen... |
| Q06 | varchar |  |  | SI | Prepared materials / documents / medications? |
| Q07 | varchar |  |  | SI | Marked / Assessed site? |
| Q08 | varchar |  |  | SI | Assembled equipment, verified supplies? |
| Q09 | varchar |  |  | SI | Positioned patient correctly? |
| Q10 | varchar |  |  | SI | All persons in the room had clean hands? |
| Q11 | varchar |  |  | SI | Skin disinfected correctly? |
| Q12 | varchar |  |  | SI | Patient was covered from head to toe with a steril... |
| Q13 | varchar |  |  | SI | Used ultrasound guidance if appropriate? |
| Q14 | varchar |  |  | SI | Wore a cap, mask, sterile gown and gloves? |
| Q15 | varchar |  |  | SI | Care provider and patient in the room wore masks? |
| Q16 | varchar |  |  | SI | Maintained sterile field? |
| Q17 | varchar |  |  | SI | Was sterile technique maintained when applying dre... |
| Q18 | varchar |  |  | SI | Was dressing dated? |
| Q19 | varchar |  |  | SI | Catheter position confirmed? |
| Q20 | varchar |  |  | SI | Daily review of line necessity? |
| Q21 | varchar |  |  | SI | Note |
| Q22 | varchar |  |  | SI | Name of Procedure CP |
| Q23 | varchar |  |  | SI | Name of Assisting CP |
| Q24 | varchar |  |  | SI | Name of other CP |
| Q25 | numeric |  |  | SI | Number of insertion attempts |
| Q26 | date |  |  | SI | Assessment date |
| Q27 | time |  |  | SI | Assessment time |
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