# questionnaire.QGXXXCROUP

> Westley croup severity score

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Westley croup severity score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Level of consciousness |
| Q02 | varchar |  |  | SI | Cyanosis |
| Q03 | varchar |  |  | SI | Stridor |
| Q04 | varchar |  |  | SI | Air entry |
| Q05 | varchar |  |  | SI | Retractions |
| Q06 | varchar |  |  | SI | 0 to 2: Mild , Occasional barky cough, no stridor ... |
| Q06a | varchar |  |  | SI | Home treatment: Symptomatic care including antipyr... |
| Q06b | varchar |  |  | SI | Outpatient treatment: Single dose of oral dexameth... |
| Q07 | varchar |  |  | SI | 3 to 7: Moderate , Frequent barky cough, stridor a... |
| Q07a | varchar |  |  | SI | Single dose of oral dexamethasone 0.6 mg/kg (maxim... |
| Q07b | varchar |  |  | SI | Nebulized epinephrine |
| Q07c | varchar |  |  | SI | Hospitalization is generally not needed, but may b... |
| Q08 | varchar |  |  | SI | 8 to 11: Severe , Frequent barky cough, stridor at... |
| Q08a | varchar |  |  | SI | Single dose of oral / IM / IV dexamethasone 0.6 mg... |
| Q08b | varchar |  |  | SI | Repeated doses of nebulized epinephrine** may be n... |
| Q08c | varchar |  |  | SI | Inpatient admission is generally required unless m... |
| Q09 | varchar |  |  | SI | 12 to 17: Impending respiratory failure , Depresse... |
| Q09a | varchar |  |  | SI | Single dose of IM/IV dexamethasone 0.6 mg/kg (maxi... |
| Q09b | varchar |  |  | SI | Repeated doses of nebulized epinephrine** may be n... |
| Q09c | varchar |  |  | SI | Intensive care unit admission is generally require... |
| Q09d | varchar |  |  | SI | Consultation with anesthesiologist or ENT surgeon ... |
| Q10 | varchar |  |  | SI | Management |
| Q23 | varchar |  |  | SI | Westley croup severity score (Acute laryngotracheo... |
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