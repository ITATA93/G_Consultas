# questionnaire.QGXXXMUST

> Malnutrition Universal Screening Tool (MUST)

**Schema:** questionnaire
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Malnutrition Universal Screening Tool (MUST)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Height (cm) |
| Q01ObsDR | varchar |  | FK | SI | Height (cm) DR |
| Q02 | varchar |  |  | SI | Current weight (kg) |
| Q02ObsDR | varchar |  | FK | SI | Current weight (kg) DR |
| Q03 | numeric |  |  | SI | Unplanned weight loss in past 3-6 months (kg) |
| Q04 | varchar |  |  | SI | BMI (kg/m2) |
| Q05 | varchar |  |  | SI | BMI score |
| Q06 | varchar |  |  | SI | Unplanned weight loss (%) in past 3-6 months |
| Q07 | varchar |  |  | SI | Acute disease effect (ADE) |
| Q08 | varchar |  |  | SI | Weight loss in % |
| Q09 | varchar |  |  | SI | ADE - Yes, if patient is acutely ill and if there ... |
| Q10 | varchar |  |  | SI | Acutely ill: Such patients include those who are c... |
| Q11 | varchar |  |  | SI | 0: Low risk |
| Q12 | varchar |  |  | SI | 1: Medium risk |
| Q13 | varchar |  |  | SI | 2: High risk |
| Q14 | varchar |  |  | SI | MUST is a five-step screening tool to identify adu... |
| Q16 | varchar |  |  | SI | Estimating BMI category from Mid Upper Arm Circumf... |
| Q17 | varchar |  |  | SI | The subject's left arm should be bent at the elbow... |
| Q18 | varchar |  |  | SI | Ask the subject to let arm hang loose and measure ... |
| Q19 | varchar |  |  | SI | If MUAC is <23.5, BMI is likely to be <20 kg/m2 |
| Q20 | varchar |  |  | SI |  If MUAC is >32.0 cm, BMI is likely to be >30 kg/m... |
| Q21 | varchar |  |  | SI | The use of MUAC provides a general indication of B... |
| Q22 | varchar |  |  | SI | Estimating height from Ulna length	 |
| Q23 | varchar |  |  | SI | https://www.bapen.org.uk/pdfs/must/must_explan.pdf |
| Q24 | varchar |  |  | SI |  Measure the distance between the bony protrusion ... |
| Q25 | varchar |  |  | SI | 0 |
| Q26 | varchar |  |  | SI | Low risk |
| Q27 | varchar |  |  | SI | 1 |
| Q28 | varchar |  |  | SI | Medium risk |
| Q29 | varchar |  |  | SI | 2 - 6 |
| Q30 | varchar |  |  | SI | High risk |
| Q31 | varchar |  |  | SI | Score |
| Q32 | varchar |  |  | SI | Classification |
| Q33 | date |  |  | SI | Date |
| Q34 | time |  |  | SI | Time |
| Q35 | varchar |  |  | SI | Score |
| Q36 | varchar |  |  | SI | Score interpretation |
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