# questionnaire.QGXXXCINSER

> Cannula insertion details

**Schema:** questionnaire
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cannula insertion details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Insertion site |
| Q01ObsDR | varchar |  | FK | SI | Insertion site DR |
| Q02 | varchar |  |  | SI | Cannula type |
| Q02ObsDR | varchar |  | FK | SI | Cannula type DR |
| Q03 | varchar |  |  | SI | Cannula gauge |
| Q03ObsDR | varchar |  | FK | SI | Cannula gauge DR |
| Q04 | varchar |  |  | SI | Insertion attempts |
| Q04ObsDR | varchar |  | FK | SI | Insertion attempts DR |
| Q05 | varchar |  |  | SI | Dressing |
| Q05ObsDR | varchar |  | FK | SI | Dressing DR |
| Q06 | varchar |  |  | SI | Site preparation |
| Q06ObsDR | varchar |  | FK | SI | Site preparation DR |
| Q07 | varchar |  |  | SI | Infection control |
| Q08 | varchar |  |  | SI | Person who placed IV |
| Q09 | date |  |  | SI | Insertion date |
| Q10 | time |  |  | SI | Insertion time |
| Q11 | varchar |  |  | SI | Removal reason |
| Q11ObsDR | varchar |  | FK | SI | Removal reason DR |
| Q12 | date |  |  | SI | Removal date |
| Q13 | time |  |  | SI | Removal time |
| Q14 | varchar |  |  | SI | Safety precautions |
| Q15 | varchar |  |  | SI | Line type |
| Q16 | varchar |  |  | SI | Catheter type |
| Q17 | varchar |  |  | SI | Catheter gauge |
| Q18 | varchar |  |  | SI | Patient information leaflets given	 |
| Q19 | varchar |  |  | SI | Indication of IV access	 |
| Q20 | varchar |  |  | SI | Mark site with an X on image below	 |
| Q21 | varchar |  |  | SI | Bodymap |
| Q22 | varchar |  |  | SI | Number of attempts	 |
| Q23 | varchar |  |  | SI | Aseptic Non Touch Technique (ANTT) adhered to	 |
| Q24 | varchar |  |  | SI | Reason for deviation	 |
| Q25 | varchar |  |  | SI | Inserted by ambulance crew	 |
| Q26 | varchar |  |  | SI | Inserted during clinical emergency / resuscitation... |
| Q27 | numeric |  |  | SI | Visual Infusion Phlebitis (VIP) score on removal	 |
| Q28 | varchar |  |  | SI | Notes |
| Q29 | varchar |  |  | SI | Observation |
| Q30 | varchar |  |  | SI | No sign of Phlebitis.  Observe PIVC & ensure docum... |
| Q31 | varchar |  |  | SI | Possible first sign of Phlebitis.  Remove PIVC, re... |
| Q32 | varchar |  |  | SI | Early Phlebitis: Remove PIVC , resite is necessary... |
| Q33 | varchar |  |  | SI | Medium Phlebitis: Remove PIVC, resite is necessary... |
| Q34 | varchar |  |  | SI | Advance Phlebitis:  Remove PIVC, resite if neneces... |
| Q35 | varchar |  |  | SI | Advance Thrombophlebitis:  Remove PIVC, initiate T... |
| Q36 | varchar |  |  | SI | Please consider Referral to IV team	 |
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