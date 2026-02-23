# questionnaire.QTCCFC

> Considerations For Care

**Schema:** questionnaire
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Considerations For Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Registered nurse to complete |
| Q10 | varchar |  |  | SI | Metabolic exercise test score indicative of reduce... |
| Q11 | varchar |  |  | SI | Polypharmacy |
| Q12 | varchar |  |  | SI | Multiple comorbidities |
| Q13 | varchar |  |  | SI | Appears frail upon visual assessment |
| Q14 | varchar |  |  | SI | If yes to any, please complete clinical frailty sc... |
| Q15 | numeric |  |  | SI | Clinical frailty score |
| Q16 | varchar |  |  | SI | Scores < 5 - provide advice on how to improve modi... |
| Q17 | varchar |  |  | SI | Score ≥ 5 - refer to anaesthetist for further revi... |
| Q18 | varchar |  |  | SI | Has the patient made any legal decisions regarding... |
| Q19 | varchar |  |  | SI | If yes please detail |
| Q2 | varchar |  |  | SI | Is the patient safe to be nursed in a single room?... |
| Q20 | varchar |  |  | SI | Additional risk assessments completed (please deta... |
| Q21 | date |  |  | SI | Date |
| Q22 | time |  |  | SI | Time |
| Q3 | varchar |  |  | SI | If no, please detail |
| Q4 | varchar |  |  | SI | Does the patient meet any of the following conside... |
| Q5 | varchar |  |  | SI | Age > 65 yrs |
| Q6 | varchar |  |  | SI | High risk of falls |
| Q7 | varchar |  |  | SI | Poor nutritional assessment |
| Q8 | varchar |  |  | SI | Poor skin integrity / high risk of pressure ulcers |
| Q9 | varchar |  |  | SI | Displaying signs of declining / reduced cognitive ... |
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