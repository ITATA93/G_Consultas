# questionnaire.QTCFPRA

> Falls Prevention Checklist (Risk Areas)

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Falls Prevention Checklist (Risk Areas)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Intervention planning checklist |
| Q10 | varchar |  |  | SI | Glasses / Hearing aids within patients' reach |
| Q11 | varchar |  |  | SI | Comments |
| Q12 | varchar |  |  | SI | 2- Pharmacological therapy |
| Q13 | varchar |  |  | SI | Information given on certain medications' effect o... |
| Q14 | varchar |  |  | SI | Medical team aware of falls risk related to medica... |
| Q15 | varchar |  |  | SI | Comments |
| Q16 | varchar |  |  | SI | 3 - Mobility issues |
| Q17 | varchar |  |  | SI | Mobilisation plan in place to minimise falls risk |
| Q18 | varchar |  |  | SI | Mobility aids given - training given |
| Q19 | varchar |  |  | SI | Patient alerted not to mobilise alone |
| Q2 | varchar |  |  | SI | Objective: draw attention to specific falls risk a... |
| Q20 | varchar |  |  | SI | Patient instructed to use call bell |
| Q21 | varchar |  |  | SI | Patient trained on safe mobility techniques |
| Q22 | varchar |  |  | SI | Continence aids / Plan in place |
| Q23 | varchar |  |  | SI | Bed rails / Call bell within reach at night |
| Q24 | varchar |  |  | SI | Relatives / Caregiver presence or assistance encou... |
| Q25 | varchar |  |  | SI | Medical team aware of falls risk related to medica... |
| Q26 | varchar |  |  | SI | Comments |
| Q27 | varchar |  |  | SI | 4 - Post-operative risk  |
| Q28 | varchar |  |  | SI | Patient / Relative / Caregiver instructed on calli... |
| Q29 | varchar |  |  | SI | Comments |
| Q3 | varchar |  |  | SI | Interventions: |
| Q30 | varchar |  |  | SI | Notes |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
| Q4 | varchar |  |  | SI | 1- Cognitive / Sensory status |
| Q5 | varchar |  |  | SI | Falls prevention measures taken |
| Q6 | varchar |  |  | SI | Falls prevention measures taken - other  |
| Q7 | varchar |  |  | SI | Patient within sight of the nursing station |
| Q8 | varchar |  |  | SI | Bed at lowest height |
| Q9 | varchar |  |  | SI | Relatives / Caregiver presence or assistance encou... |
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