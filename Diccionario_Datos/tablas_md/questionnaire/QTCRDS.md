# questionnaire.QTCRDS

> Respiratory Distress Score (Downes' Score)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Respiratory Distress Score (Downes' Score)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Respiratory rate (per min) |
| Q02 | varchar |  |  | SI | Cyanosis |
| Q03 | varchar |  |  | SI | Retractions |
| Q04 | varchar |  |  | SI | Grunting |
| Q05 | varchar |  |  | SI | Air entry (crying) |
| Q06 | varchar |  |  | SI | Air entry represents the quality of inspiratory br... |
| Q07 | varchar |  |  | SI | Score |
| Q08 | varchar |  |  | SI | Classification |
| Q09 | varchar |  |  | SI | < 4 |
| Q10 | varchar |  |  | SI | No respiratory distress |
| Q11 | varchar |  |  | SI | &lt; 6 |
| Q12 | varchar |  |  | SI | Respiratory distress |
| Q13 | varchar |  |  | SI | &gt; 6 |
| Q14 | varchar |  |  | SI | Impending respiratory failure; blood gases are req... |
| Q15 | varchar |  |  | SI | < 4: No respiratory distress |
| Q16 | varchar |  |  | SI | 4 - 7: Respiratory distress |
| Q17 | varchar |  |  | SI | > 7: Impending respiratory failure; blood gases ar... |
| Q18 | varchar |  |  | SI | This Downes Respiratory Distress Score allows clin... |
| Q19 | date |  |  | SI | Date |
| Q20 | time |  |  | SI | Time |
| Q21 | varchar |  |  | SI | Downes JJ, Vidyasagar D, Morrow GM, Boggs TR. Resp... |
| Q22 | varchar |  |  | SI | Clin Pediatr 1970;9:325–331. |
| Q23 | varchar |  |  | SI | Wood DW, Downes JJ, Lecks HI. (1972) A clinical sc... |
| Q24 | varchar |  |  | SI | Donahoe M. (2011) Acute respiratory distress syndr... |
| Q25 | varchar |  |  | SI | Shashidhar A, Suman Rao PN, Joe J. (2016) Downes S... |
| Q26 | varchar |  |  | SI | Greenough A, Roberton NRC. Acute respiratory disea... |
| Q27 | varchar |  |  | SI | Mathai SS, Raju U, Kanitkar M. (2007) Management o... |
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