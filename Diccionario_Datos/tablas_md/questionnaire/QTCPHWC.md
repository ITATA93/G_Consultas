# questionnaire.QTCPHWC

> Pulmonary Hypertension Workup Checklist

**Schema:** questionnaire
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pulmonary Hypertension Workup Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Referred to appropriate specialist |
| Q04 | varchar |  |  | SI | Comment |
| Q05 | varchar |  |  | SI | Right heart catheterisation |
| Q06 | date |  |  | SI | Date completed |
| Q07 | varchar |  |  | SI | Comments |
| Q08 | varchar |  |  | SI | Computerised tomography (CT) pulmonary angiogram |
| Q09 | date |  |  | SI | Date completed |
| Q10 | varchar |  |  | SI | Comments |
| Q11 | varchar |  |  | SI | Echocardiogram |
| Q12 | date |  |  | SI | Date completed |
| Q13 | varchar |  |  | SI | Comments |
| Q14 | varchar |  |  | SI | High resolution CT chest |
| Q15 | date |  |  | SI | Date completed |
| Q16 | varchar |  |  | SI | Comments |
| Q17 | varchar |  |  | SI | Ventilation / Perfusion (VQ) scan completed |
| Q18 | date |  |  | SI | Date completed |
| Q19 | varchar |  |  | SI | Comments |
| Q20 | varchar |  |  | SI | Pulmonary function tests |
| Q21 | date |  |  | SI | Date completed |
| Q22 | varchar |  |  | SI | Comment |
| Q23 | varchar |  |  | SI | Arterial blood gas |
| Q24 | varchar |  |  | SI | Comments |
| Q25 | varchar |  |  | SI | Autoimmune screen |
| Q26 | varchar |  |  | SI | Comments |
| Q27 | varchar |  |  | SI | N-terminal prohormone of brain natriuretic peptide... |
| Q28 | varchar |  |  | SI | Comments |
| Q29 | varchar |  |  | SI | Liver function tests |
| Q30 | varchar |  |  | SI | Comments |
| Q31 | varchar |  |  | SI | Sleep study |
| Q32 | date |  |  | SI | Date completed |
| Q33 | varchar |  |  | SI | Comment |
| Q34 | varchar |  |  | SI | 6 minute walk test |
| Q35 | date |  |  | SI | Date completed |
| Q36 | varchar |  |  | SI | Comments |
| Q37 | varchar |  |  | SI | Other tests |
| Q38 | varchar |  |  | SI | Details of other tests |
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