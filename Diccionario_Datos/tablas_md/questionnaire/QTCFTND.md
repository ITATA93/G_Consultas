# questionnaire.QTCFTND

> Fagerstroem Test for Nicotine Dependence (FTND)

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fagerstroem Test for Nicotine Dependence (FTND)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | How soon after you wake up do you smoke your first... |
| Q02 | varchar |  |  | SI | Do you find it difficult to refrain from smoking i... |
| Q03 | varchar |  |  | SI | Which cigarette would you hate to give up most? |
| Q04 | varchar |  |  | SI | How many cigarettes per day do you smoke? |
| Q05 | varchar |  |  | SI | Do you smoke more frequently during the first hour... |
| Q06 | varchar |  |  | SI | Do you smoke if you are so ill that you are in bed... |
| Q07 | varchar |  |  | SI | Score |
| Q08 | varchar |  |  | SI | Classification |
| Q09 | varchar |  |  | SI | 0 ‐ 2 |
| Q10 | varchar |  |  | SI | Low dependence |
| Q11 | varchar |  |  | SI | 3 - 4 |
| Q12 | varchar |  |  | SI | Low to mod dependence |
| Q13 | varchar |  |  | SI | 5 |
| Q14 | varchar |  |  | SI | Moderate dependence |
| Q15 | varchar |  |  | SI | 6 - 7 |
| Q16 | varchar |  |  | SI | High dependence |
| Q17 | varchar |  |  | SI | 8 + |
| Q18 | varchar |  |  | SI | Very high dependence |
| Q19 | varchar |  |  | SI | 0 ‐ 2: Low dependence |
| Q20 | varchar |  |  | SI | 3 ‐ 4: Low to mod dependence |
| Q21 | varchar |  |  | SI | 5: Moderate dependence |
| Q22 | varchar |  |  | SI | 6 - 7: High dependence |
| Q23 | varchar |  |  | SI | 8 +: Very high dependence |
| Q24 | date |  |  | SI | Date |
| Q25 | time |  |  | SI | Time |
| Q26 | varchar |  |  | SI | The Fagerstroem Test for Nicotine Dependence (FTND... |
| Q27 | varchar |  |  | SI | The test was designed to provide an ordinal measur... |
| Q28 | varchar |  |  | SI | It contains six items that evaluate the quantity o... |
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