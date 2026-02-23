# SQLUser.PAC_UsualAccomodation

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| USACC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Respiratory rate (per min) |
| Q02 | - |  |  | SI | Cyanosis |
| Q03 | - |  |  | SI | Retractions |
| Q04 | - |  |  | SI | Grunting |
| Q05 | - |  |  | SI | Air entry (crying) |
| Q06 | - |  |  | SI | Air entry represents the quality of inspiratory br... |
| Q07 | - |  |  | SI | Score |
| Q08 | - |  |  | SI | Classification |
| Q09 | - |  |  | SI | < 4 |
| Q10 | - |  |  | SI | No respiratory distress |
| Q11 | - |  |  | SI | &lt |
| Q12 | - |  |  | SI | Respiratory distress |
| Q13 | - |  |  | SI | &gt |
| Q14 | - |  |  | SI | Impending respiratory failure |
| Q15 | - |  |  | SI | < 4: No respiratory distress |
| Q16 | - |  |  | SI | 4 - 7: Respiratory distress |
| Q17 | - |  |  | SI | > 7: Impending respiratory failure |
| Q18 | - |  |  | SI | This Downes Respiratory Distress Score allows clin... |
| Q19 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | Time |
| Q21 | - |  |  | SI | Downes JJ, Vidyasagar D, Morrow GM, Boggs TR. Resp... |
| Q22 | - |  |  | SI | Clin Pediatr 1970 |
| Q23 | - |  |  | SI | Wood DW, Downes JJ, Lecks HI. (1972) A clinical sc... |
| Q24 | - |  |  | SI | Donahoe M. (2011) Acute respiratory distress syndr... |
| Q25 | - |  |  | SI | Shashidhar A, Suman Rao PN, Joe J. (2016) Downes S... |
| Q26 | - |  |  | SI | Greenough A, Roberton NRC. Acute respiratory disea... |
| Q27 | - |  |  | SI | Mathai SS, Raju U, Kanitkar M. (2007) Management o... |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |
| USACC_Code | varchar |  |  | NO | Code |
| USACC_CreatedDate | date |  |  | SI | Created Date |
| USACC_CreatedTime | time |  |  | SI | Created Time |
| USACC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| USACC_DateFrom | date |  |  | SI | Date From |
| USACC_DateTo | date |  |  | SI | Date To |
| USACC_Desc | varchar |  |  | NO | Description |
| USACC_NationalCode | varchar |  |  | SI | NationalCode |
| USACC_UpdatedDate | date |  |  | SI | Updated Date |
| USACC_UpdatedTime | time |  |  | SI | Updated Time |
| USACC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*