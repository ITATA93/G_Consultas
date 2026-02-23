# questionnaire.QTCCARG

> Cancer And Aging Research Group (CARG) Chemotherapy Toxicity Tool

**Schema:** questionnaire
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cancer And Aging Research Group (CARG) Chemotherapy Toxicity Tool

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Age ≥72 years old |
| Q04 | varchar |  |  | SI | Cancer type (gastrointestinal or genitourinary) |
| Q05 | varchar |  |  | SI | Chemotherapy dosing (standard dosing) |
| Q06 | varchar |  |  | SI | More than one chemotherapy drug (polychemotherapy) |
| Q07 | varchar |  |  | SI | Haemoglobin (&lt;11 g/dL in males; &lt;10 g/dL in ... |
| Q08 | varchar |  |  | SI | Creatinine clearance (&lt;34 mL/min) |
| Q09 | varchar |  |  | SI | Hearing (fair, poor, or deaf) |
| Q10 | varchar |  |  | SI | Number of falls in the past 6 months (one or more) |
| Q11 | varchar |  |  | SI | Take medications with some help or unable |
| Q12 | varchar |  |  | SI | Walking one block, somewhat limited or limited a l... |
| Q13 | varchar |  |  | SI | Decreased social activity because of physical or e... |
| Q14 | varchar |  |  | SI | The CARG Chemotherapy Toxicity Tool was published ... |
| Q15 | varchar |  |  | SI | And estimates the proportion of patients that deve... |
| Q16 | varchar |  |  | SI | 1. Hurria A, Togawa K, Mohile SG, et al. Predictin... |
| Q17 | varchar |  |  | SI | 2. National Cancer Institute Common Terminology Cr... |
| Q18 | varchar |  |  | SI | https://ctep.cancer.gov/protocoldevelopment/electr... |
| Q19 | varchar |  |  | SI | Cancer and Aging Research Group (CARG) Chemotherap... |
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