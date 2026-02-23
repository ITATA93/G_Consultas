# questionnaire.QTCPOTA

> Physiotherapy & Occupational Therapy Assessment

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physiotherapy & Occupational Therapy Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time  |
| Q03 | varchar |  |  | SI | Turning over left side |
| Q04 | varchar |  |  | SI | Turning over right side |
| Q05 | varchar |  |  | SI | Lying to sitting  |
| Q06 | varchar |  |  | SI | Sitting balance (assessor to time patient for 10 s... |
| Q07 | varchar |  |  | SI | Sitting from standing (takes less than 15 secs) |
| Q08 | varchar |  |  | SI | Standing (assessor to time patient for 10 secs) |
| Q09 | varchar |  |  | SI | Transfers (assessor to place chair on unaffected s... |
| Q10 | varchar |  |  | SI | Walking indoors (walk 10 meters in usual way) |
| Q11 | varchar |  |  | SI | Stairs (climb up and down in usual way) |
| Q12 | varchar |  |  | SI | Score |
| Q13 | varchar |  |  | SI | Comments |
| Q14 | varchar |  |  | SI | Score |
| Q15 | varchar |  |  | SI | Classification |
| Q16 | varchar |  |  | SI | 0: |
| Q17 | varchar |  |  | SI | 1: |
| Q18 | varchar |  |  | SI | 2: |
| Q19 | varchar |  |  | SI | 3: |
| Q20 | varchar |  |  | SI | 4: |
| Q21 | varchar |  |  | SI | 5: |
| Q22 | varchar |  |  | SI | Unable to perform |
| Q23 | varchar |  |  | SI | Assistance of two people |
| Q24 | varchar |  |  | SI | Assistance of one person |
| Q25 | varchar |  |  | SI | Requires supervision or verbal instruction |
| Q26 | varchar |  |  | SI | Requires an aid or appliance |
| Q27 | varchar |  |  | SI | Independent |
| Q28 | varchar |  |  | SI | The Physiotherapy & Occupational Therapy Assessmen... |
| Q29 | varchar |  |  | SI | Range = 0 - 45. The higher the patient score the g... |
| Q30 | varchar |  |  | SI | Range = 0 - 45. The higher the patient score the g... |
| Q31 | varchar |  |  | SI | Turning Over - Patient turning from back onto side |
| Q32 | varchar |  |  | SI | Lying to sitting - Patient moving from lying to si... |
| Q33 | varchar |  |  | SI | Sitting balance - Patient sitting on edge of bed |
| Q34 | varchar |  |  | SI | Sitting from Standing - Patient stands from chair |
| Q35 | varchar |  |  | SI | Standing - Patient remains standing |
| Q36 | varchar |  |  | SI | Transfers - Patient moves from bed to chair and ba... |
| Q37 | varchar |  |  | SI | Walking - Patient walks for 10 meters |
| Q38 | varchar |  |  | SI | Stairs - Patient climbs up and down 1 flight of st... |
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