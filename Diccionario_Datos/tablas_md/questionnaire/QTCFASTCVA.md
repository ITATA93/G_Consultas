# questionnaire.QTCFASTCVA

> CVA / Stroke Screen using FAST

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CVA / Stroke Screen using FAST

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q02 | varchar |  |  | SI | Blood glucose concentration |
| Q02ObsDR | varchar |  | FK | SI | Blood glucose concentration DR |
| Q03 | varchar |  |  | SI | If hypoglycaemic, treat and reassess |
| Q04 | varchar |  |  | SI | Other sudden symptoms |
| Q05 | varchar |  |  | SI | Use the below guide when carrying out a FAST scree... |
| Q06 | varchar |  |  | SI | Facial Movements |
| Q07 | varchar |  |  | SI | Ask patient to smile or show teeth |
| Q08 | varchar |  |  | SI | Look for NEW lack of symmetry |
| Q09 | varchar |  |  | SI | Arm Movements |
| Q10 | varchar |  |  | SI | Lift the patient's arms together (90 degrees if si... |
| Q11 | varchar |  |  | SI | Look for one arm drifting down or falling rapidly. |
| Q12 | varchar |  |  | SI | Speech |
| Q13 | varchar |  |  | SI | If the patient attempts a conversation: |
| Q14 | varchar |  |  | SI | Look for NEW disturbance of speech |
| Q15 | varchar |  |  | SI | Check with companion |
| Q16 | varchar |  |  | SI | Look for slurred speech |
| Q17 | varchar |  |  | SI | Look for word-finding difficulties. This can be co... |
| Q18 | varchar |  |  | SI | If there is a severe visual disturbance, place an ... |
| Q19 | varchar |  |  | SI | Action to be taken if stroke onset within a certai... |
| Q20 | varchar |  |  | SI | Emergency Department: If suspected stroke and symp... |
| Q21 | varchar |  |  | SI | Label for own instructions 1 |
| Q22 | varchar |  |  | SI | Label for own instructions 2 |
| Q23 | date |  |  | SI | Date |
| Q24 | time |  |  | SI | Time |
| Q25 | varchar |  |  | SI | mmol/L |
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