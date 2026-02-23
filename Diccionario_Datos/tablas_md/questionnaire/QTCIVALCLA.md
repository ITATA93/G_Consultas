# questionnaire.QTCIVALCLA

> Central Line Assessment

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Central Line Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Activity |
| Q04 | varchar |  |  | SI | Central venous catheter present |
| Q05 | date |  |  | SI | Insertion date and time |
| Q06 | time |  |  | SI | Insertion time |
| Q07 | varchar |  |  | SI | Procedure type |
| Q08 | varchar |  |  | SI | Access type |
| Q09 | varchar |  |  | SI | Number of lumens |
| Q10 | varchar |  |  | SI | Laterality |
| Q11 | varchar |  |  | SI | Site |
| Q12 | varchar |  |  | SI | Catheter size |
| Q13 | varchar |  |  | SI | Antibiotic coated line used |
| Q14 | varchar |  |  | SI | Reason for insertion |
| Q15 | varchar |  |  | SI | Patient identified |
| Q16 | varchar |  |  | SI | Insertion unit |
| Q17 | varchar |  |  | SI | Performing provider |
| Q18 | varchar |  |  | SI | Assisting in insertion |
| Q19 | varchar |  |  | SI | Procedure preparation |
| Q20 | varchar |  |  | SI | Maximal sterile barrier precautions compliance |
| Q21 | varchar |  |  | SI | Non - Compliant maximal sterile barrier precaution... |
| Q22 | varchar |  |  | SI | Procedure result |
| Q23 | numeric |  |  | SI | Number of attempts |
| Q24 | varchar |  |  | SI | Catheter position correction required |
| Q26 | varchar |  |  | SI | Radio - graphic confirmation done |
| Q27 | varchar |  |  | SI | Catheter tip confirmation site |
| Q28 | varchar |  |  | SI | Comment |
| Q29 | varchar |  |  | SI | Catheter insertion bundle |
| Q30 | varchar |  |  | SI | Explained procedure to patient and verified consen... |
| Q31 | varchar |  |  | SI | Comment |
| Q32 | varchar |  |  | SI | Catheter insertion bundle |
| Q33 | varchar |  |  | SI | Explained procedure to patient and verified consen... |
| Q34 | varchar |  |  | SI | Prepared materials / documents / medications? |
| Q35 | varchar |  |  | SI | Marked / assessed site? |
| Q36 | varchar |  |  | SI | Assembled equipment, verified supplies? |
| Q37 | varchar |  |  | SI | Positioned patient correctly? |
| Q38 | varchar |  |  | SI | All persons in the room had clean hands? |
| Q39 | varchar |  |  | SI | Skin disinfected correctly? |
| Q40 | varchar |  |  | SI | Patient was covered from head to toe with a steril... |
| Q41 | varchar |  |  | SI | Used ultrasound guidance if appropriate? |
| Q42 | varchar |  |  | SI | Wore a cap, mask, sterile gown and gloves? |
| Q43 | varchar |  |  | SI | Care provider and patient in the room wore masks? |
| Q44 | varchar |  |  | SI | Maintained sterile field? |
| Q45 | varchar |  |  | SI | Was sterile technique maintained when applying dre... |
| Q46 | varchar |  |  | SI | Was dressing dated? |
| Q47 | varchar |  |  | SI | Catheter position confirmed? |
| Q50 | varchar |  |  | SI | Central venous catheter line care bundle |
| Q53 | varchar |  |  | SI | Catheter tunnel / porta cath |
| Q54 | varchar |  |  | SI | Catheter tunnel status |
| Q55 | varchar |  |  | SI | Tunnel exit site / port pocket |
| Q56 | varchar |  |  | SI | Tunnel cath anchor suture removed |
| Q57 | varchar |  |  | SI | Port needle type |
| Q58 | varchar |  |  | SI | Accessing port |
| Q59 | varchar |  |  | SI | Accessing port reason |
| Q61 | date |  |  | SI | Discontinue date and time |
| Q62 | time |  |  | SI | Discontinue time |
| Q63 | varchar |  |  | SI | Care provider discontinued the line |
| Q64 | varchar |  |  | SI | Discontinue reason |
| Q65 | varchar |  |  | SI | Unexpected events |
| Q66 | varchar |  |  | SI | Discontinue result |
| Q67 | numeric |  |  | SI | Direct pressure applied duration |
| Q68 | varchar |  |  | SI | Total days of insertion |
| Q69 | varchar |  |  | SI | Comment |
| Q70 | varchar |  |  | SI | Lumen characteristics |
| Q71 | numeric |  |  | SI | Catheter length (cm) |
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