# questionnaire.QTCSFPSA

> Patient Smoking Agreement

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Smoking Agreement

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | The patient / guardian acknowledges that: |
| Q04 | varchar |  |  | SI | 1. The hospital has a smoke free policy in place |
| Q05 | varchar |  |  | SI | 2. Smoking is banned on hospital property includin... |
| Q06 | varchar |  |  | SI | 3. Nicotine Replacement Therapy (NRT) is available |
| Q07 | varchar |  |  | SI | 4. Smoking while receiving care is bad for my heal... |
| Q08 | varchar |  |  | SI | 5. Should I leave hospital property to smoke, I ag... |
| Q09 | varchar |  |  | SI | 6. I need to inform staff caring for me should I g... |
| Q10 | varchar |  |  | SI | 7. This Agreement remains valid for the duration o... |
| Q11 | varchar |  |  | SI | Patient declined to sign form |
| Q12 | varchar |  |  | SI | Patient unable to sign form |
| Q13 | varchar |  |  | SI | Person responsible for signing agreement |
| Q14 | longvarbinary |  |  | SI | Patient signature |
| Q14UDt | date |  |  | SI | Patient signature Last Updated Date |
| Q14UTm | time |  |  | SI | Patient signature Last Updated Time |
| Q15 | longvarbinary |  |  | SI | Guardian signature |
| Q15UDt | date |  |  | SI | Guardian signature Last Updated Date |
| Q15UTm | time |  |  | SI | Guardian signature Last Updated Time |
| Q16 | longvarbinary |  |  | SI | Signature of witness |
| Q16UDt | date |  |  | SI | Signature of witness Last Updated Date |
| Q16UTm | time |  |  | SI | Signature of witness Last Updated Time |
| Q17 | varchar |  |  | SI | Witness name |
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