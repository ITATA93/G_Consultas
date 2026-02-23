# questionnaire.QTCGDA

> General Drain Access

**Schema:** questionnaire
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* General Drain Access

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Insertion Reason |
| Q02 | varchar |  |  | SI | Explained procedure to patient and verified consen... |
| Q03 | varchar |  |  | SI | Prepared materials / documents / medications? |
| Q04 | varchar |  |  | SI | Marked / Assessed site? |
| Q05 | varchar |  |  | SI | Assembled equipment, verified supplies? |
| Q06 | varchar |  |  | SI | Positioned patient correctly? |
| Q07 | varchar |  |  | SI | All persons in the room had clean hands? |
| Q08 | varchar |  |  | SI | Skin disinfected correctly? |
| Q09 | varchar |  |  | SI | Patient was covered from head to toe with a steril... |
| Q10 | varchar |  |  | SI | Used ultrasound guidance if appropriate? |
| Q11 | varchar |  |  | SI | Wore a cap, mask, sterile gown and gloves? |
| Q12 | varchar |  |  | SI | Care provider and patient in the room wore masks? |
| Q13 | varchar |  |  | SI | Maintained sterile field? |
| Q14 | varchar |  |  | SI | Was sterile technique maintained when applying dre... |
| Q15 | varchar |  |  | SI | Was dressing dated? |
| Q16 | varchar |  |  | SI | Catheter position confirmed? |
| Q17 | varchar |  |  | SI | Daily review of line necessity? |
| Q18 | varchar |  |  | SI | Note |
| Q19 | varchar |  |  | SI | Name of Procedure CP |
| Q20 | varchar |  |  | SI | Name of Assisting CP |
| Q21 | varchar |  |  | SI | Name of other CP |
| Q22 | varchar |  |  | SI | Skin preparation |
| Q23 | varchar |  |  | SI | Note |
| Q24 | varchar |  |  | SI | Insertion approach |
| Q25 | varchar |  |  | SI | Checklist |
| Q26 | numeric |  |  | SI | Number of insertion attempts |
| Q27 | varchar |  |  | SI | Information |
| Q28 | date |  |  | SI | Date inserted |
| Q29 | time |  |  | SI | Time inserted |
| Q30 | date |  |  | SI | Date infection found  |
| Q31 | time |  |  | SI | Time infection found |
| Q32 | date |  |  | SI | Date infection healed |
| Q33 | time |  |  | SI | Time infection healed |
| Q34 | date |  |  | SI | Date removed |
| Q35 | time |  |  | SI | Time removed |
| Q37 | varchar |  |  | SI | Characteristics |
| Q37ObsDR | varchar |  | FK | SI | Characteristics DR |
| Q38 | varchar |  |  | SI | Material |
| Q38ObsDR | varchar |  | FK | SI | Material DR |
| Q39 | varchar |  |  | SI | Drain Type |
| Q40 | varchar |  |  | SI | Size |
| Q41 | varchar |  |  | SI | Drain position |
| Q42 | varchar |  |  | SI | Local anaesthetic used |
| Q43 | varchar |  |  | SI | Localisation |
| Q44 | varchar |  |  | SI | Drain labelled with date inserted |
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