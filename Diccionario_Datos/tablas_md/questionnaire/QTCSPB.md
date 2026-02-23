# questionnaire.QTCSPB

> SEPSIS prevention bundle Score

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* SEPSIS prevention bundle Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Bundle Compliance Percentage |
| Q04 | varchar |  |  | SI | % |
| Q05 | varchar |  |  | SI | The Quick Sepsis Organ Failure Assessment must be ... |
| Q06 | varchar |  |  | SI | Within 1 hour of recognizing sepsis or septic shoc... |
| Q07 | varchar |  |  | SI | Determination of the lactate level |
| Q08 | varchar |  |  | SI | If initial lactate is> 2 mmol / L new determinatio... |
| Q09 | varchar |  |  | SI | Collection of blood cultures samples before antibi... |
| Q10 | varchar |  |  | SI | Administration of empirical broad spectrum  antimi... |
| Q11 | varchar |  |  | SI | If patient has hypotension or lactates> 4mmol / L,... |
| Q12 | varchar |  |  | SI | If patient has hypotension during or after restora... |
| Q13 | varchar |  |  | SI | After having carried out the above interventions, ... |
| Q14 | varchar |  |  | SI | Periodic monitoring of clinical conditions, Acid-B... |
| Q15 | varchar |  |  | SI | Blood chemistry test: Glucose; Urea; Creatinine; S... |
| Q16 | varchar |  |  | SI | Complete blood count: Hemoglobin; Hematocrit; Red ... |
| Q17 | varchar |  |  | SI | Lymphocytes; Monocytes; Neutrophil granulocytes (%... |
| Q18 | varchar |  |  | SI | Differential Count of Leukocytes: Neutrophil Granu... |
| Q19 | varchar |  |  | SI | Coagulation test: Prothrombin time (PT); activated... |
| Q20 | varchar |  |  | SI | Radiology exams to assess of the source of the inf... |
| Q21 | varchar |  |  | SI | Comments |
| Q22 | varchar |  |  | SI | * The diagnosis of sepsis/septic shock coincides w... |
| Q23 | varchar |  |  | SI | that highlights all the elements of sepsis or sept... |
| Q24 | varchar |  |  | SI | Score |
| Q25 | varchar |  |  | SI | Classifiaction |
| Q26 | varchar |  |  | SI | 0 - 100 |
| Q27 | varchar |  |  | SI | Higher percetage indicates higher compliance |
| Q28 | varchar |  |  | SI | 0 - 100: Higher percetage indicates higher complia... |
| Q29 | varchar |  |  | SI | The SEPSIS prevention bundle is used for decision ... |
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