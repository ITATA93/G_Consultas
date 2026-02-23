# questionnaire.QGXXXCAPA

> Pre Anaesthetic

**Schema:** questionnaire
**Columnas:** 99
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pre Anaesthetic

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Red blood cells |
| Q01ObsDR | varchar |  | FK | SI | Red blood cells DR |
| Q02 | varchar |  |  | SI | Haemoglobin |
| Q02ObsDR | varchar |  | FK | SI | Haemoglobin DR |
| Q03 | varchar |  |  | SI | Hematocrit |
| Q03ObsDR | varchar |  | FK | SI | Hematocrit DR |
| Q04 | varchar |  |  | SI | Platelets |
| Q04ObsDR | varchar |  | FK | SI | Platelets DR |
| Q05 | varchar |  |  | SI | Potassium (K+) |
| Q05ObsDR | varchar |  | FK | SI | Potassium (K+) DR |
| Q06 | varchar |  |  | SI | Sodium (Na+) |
| Q06ObsDR | varchar |  | FK | SI | Sodium (Na+) DR |
| Q07 | varchar |  |  | SI | Glycemia |
| Q07ObsDR | varchar |  | FK | SI | Glycemia DR |
| Q08 | varchar |  |  | SI | Activated partial thromboplastin time (aPTT) contr... |
| Q08ObsDR | varchar |  | FK | SI | Activated partial thromboplastin time (aPTT) contr... |
| Q09 | varchar |  |  | SI | Urea |
| Q09ObsDR | varchar |  | FK | SI | Urea DR |
| Q10 | varchar |  |  | SI | Prothrombin time (PT) control / patient |
| Q10ObsDR | varchar |  | FK | SI | Prothrombin time (PT) control / patient DR |
| Q11 | varchar |  |  | SI | Creatinine |
| Q11ObsDR | varchar |  | FK | SI | Creatinine DR |
| Q12 | varchar |  |  | SI | aPTT |
| Q12ObsDR | varchar |  | FK | SI | aPTT DR |
| Q13 | varchar |  |  | SI | Prothrombin time / International normalized ratio ... |
| Q13ObsDR | varchar |  | FK | SI | Prothrombin time / International normalized ratio ... |
| Q14 | varchar |  |  | SI | Electrocardiogram |
| Q15 | varchar |  |  | SI | Thorax X Ray |
| Q16 | varchar |  |  | SI | Observation |
| Q17 | varchar |  |  | SI | Mallampati |
| Q18 | varchar |  |  | SI | American Society of Anaesthesiologists (ASA) physi... |
| Q19 | varchar |  |  | SI | Mouth opening |
| Q20 | varchar |  |  | SI | Thyromental distance |
| Q21 | varchar |  |  | SI | Cervical mobility |
| Q22 | varchar |  |  | SI | Mandibular protrusion |
| Q23 | varchar |  |  | SI | Airway |
| Q24 | varchar |  |  | SI | Additional tests |
| Q25 | varchar |  |  | SI | Comments |
| Q26 | varchar |  |  | SI | Red blood cells comment |
| Q27 | varchar |  |  | SI | Haemoglobin comment |
| Q28 | varchar |  |  | SI | Hematocrit |
| Q29 | varchar |  |  | SI | Platelets comment |
| Q30 | varchar |  |  | SI | aPTT control / patient comment |
| Q31 | varchar |  |  | SI | PT control / patient comment |
| Q32 | varchar |  |  | SI | aPTT comment |
| Q33 | varchar |  |  | SI | K+ comment |
| Q34 | varchar |  |  | SI | Na+ comment |
| Q35 | varchar |  |  | SI | Glycemia comment |
| Q36 | varchar |  |  | SI | Urea comment |
| Q37 | varchar |  |  | SI | Creatinine comment |
| Q38 | varchar |  |  | SI | PT/INR comment |
| Q39 | date |  |  | SI | Date |
| Q40 | time |  |  | SI | Time |
| Q41 | varchar |  |  | SI | and comments |
| Q42 | varchar |  |  | SI | Patient fully consented |
| Q43 | varchar |  |  | SI | Comments |
| Q44 | varchar |  |  | SI | Mallampati |
| Q45 | varchar |  |  | SI | Intubation grade |
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