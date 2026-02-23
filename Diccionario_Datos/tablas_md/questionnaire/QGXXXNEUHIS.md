# questionnaire.QGXXXNEUHIS

> Neurological History

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Weakness |
| Q01N | varchar |  |  | SI | Note |
| Q01Y | varchar |  |  | SI | If yes |
| Q03 | varchar |  |  | SI | Numbness or paresthesia |
| Q03N | varchar |  |  | SI | Note |
| Q03Y | varchar |  |  | SI | If yes |
| Q05 | varchar |  |  | SI | Impaired speech |
| Q05N | varchar |  |  | SI | Note |
| Q07 | varchar |  |  | SI | Nausea or Vomiting |
| Q07N | varchar |  |  | SI | Note |
| Q09 | varchar |  |  | SI | Headaches |
| Q09N | varchar |  |  | SI | Note |
| Q09Y | varchar |  |  | SI | If yes |
| Q11 | varchar |  |  | SI | Head injury |
| Q11N | varchar |  |  | SI | Note |
| Q11Y | varchar |  |  | SI | If yes |
| Q13 | varchar |  |  | SI | Fever |
| Q13N | varchar |  |  | SI | Note |
| Q15 | varchar |  |  | SI | Confusion |
| Q15N | varchar |  |  | SI | Note |
| Q17 | varchar |  |  | SI | Abnormal behaviour |
| Q17N | varchar |  |  | SI | Note |
| Q19 | varchar |  |  | SI | Delusions or hallucinations |
| Q19N | varchar |  |  | SI | Note |
| Q21 | varchar |  |  | SI | Altered mood |
| Q21N | varchar |  |  | SI | Note |
| Q23 | varchar |  |  | SI | Syncope or loss of consciousness |
| Q23N | varchar |  |  | SI | Note |
| Q25 | varchar |  |  | SI | Seizure |
| Q25N | varchar |  |  | SI | Note |
| Q27 | varchar |  |  | SI | Gait abnormality |
| Q27N | varchar |  |  | SI | Note |
| Q29 | varchar |  |  | SI | Impaired memory |
| Q29N | varchar |  |  | SI | Note |
| Q31 | varchar |  |  | SI | Recent falls |
| Q31N | varchar |  |  | SI | Note |
| Q33 | varchar |  |  | SI | Excessive bleeding / bruising |
| Q33N | varchar |  |  | SI | Note |
| Q35 | varchar |  |  | SI | Taking aspirin or platelet inhibitor |
| Q35N | varchar |  |  | SI | Note |
| Q37 | varchar |  |  | SI | Taking anticoagulant |
| Q37N | varchar |  |  | SI | Note |
| Q43 | varchar |  |  | SI | Dizziness |
| Q43N | varchar |  |  | SI | Note |
| Q45 | date |  |  | SI | Date |
| Q46 | time |  |  | SI | Time |
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