# questionnaire.QTCAHPRHRM

> Rivermead Index (Modified)

**Schema:** questionnaire
**Columnas:** 59
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Rivermead Index (Modified)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | 1. Turning over: Turn over from your back to any s... |
| Q02 | varchar |  |  | SI | 2. Lying to sitting: Sit on the side of the bed |
| Q03 | varchar |  |  | SI | 3. Sitting balance: Sit on the edge of the bed wit... |
| Q04 | varchar |  |  | SI | 4. Sitting to standing: Stand up from your chair (... |
| Q05 | varchar |  |  | SI | 5. Standing unsupported: Stand without holding on ... |
| Q06 | varchar |  |  | SI | 6. Transfer: Go from your bed to chair and back ag... |
| Q07 | varchar |  |  | SI | 7. Walking indoors: Walk for 10 meters in your usu... |
| Q08 | varchar |  |  | SI | 8. Stairs: Climb up this flight of steps in your u... |
| Q09 | varchar |  |  | SI | Score 1 (Yes) if the patient can perform the activ... |
| Q10 | varchar |  |  | SI | Score 0 (No) if the patient cannot |
| Q11 | varchar |  |  | SI | In case of STROKE patient, please see in Physical ... |
| Q12 | varchar |  |  | SI | 0 - Unable to perform |
| Q13 | varchar |  |  | SI | 1 - Assistance of 2 people |
| Q14 | varchar |  |  | SI | 2 - Assistance of 1 person |
| Q15 | varchar |  |  | SI | 3 - Requires supervision or verbal instruction |
| Q16 | varchar |  |  | SI | 4 - Requires an aid or an appliance |
| Q17 | varchar |  |  | SI | 5 - Independent |
| Q18 | varchar |  |  | SI | The Modified Rivermead Index evaluates the effecti... |
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