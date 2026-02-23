# questionnaire.QTCLATCH

> Latch score

**Schema:** questionnaire
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Latch score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Latch |
| Q02 | varchar |  |  | SI | Audible swallowing	 |
| Q03 | varchar |  |  | SI | Type of nipple	 |
| Q04 | varchar |  |  | SI | Comfort (breast and nipple)	 |
| Q05 | varchar |  |  | SI | Hold (positioning) |
| Q06 | varchar |  |  | SI | A LATCH score < 7 can predict non-exclusive breast... |
| Q07 | varchar |  |  | SI | A LATCH score >=7 can predict exclusive breastfeed... |
| Q08 | varchar |  |  | SI | LATCH is a breastfeeding charting system that prov... |
| Q09 | varchar |  |  | SI | ''L'' is for how well the infant latches onto the ... |
| Q10 | varchar |  |  | SI | ''H'' is for the amount of help the mother needs t... |
| Q11 | varchar |  |  | SI | Document feeding time of newborn. |
| Q12 | varchar |  |  | SI | Observe a minimum of one breastfeeding session per... |
| Q13 | varchar |  |  | SI | Score the feed in the appropriate space and docume... |
| Q14 | varchar |  |  | SI | Document whether the feed was observed or reported... |
| Q15 | varchar |  |  | SI | If score is less than 7, the next feeding is to be... |
| Q16 | varchar |  |  | SI | If two subsequent scores less than 7 are obtained,... |
| Q17 | varchar |  |  | SI | Additional comments |
| Q18 | varchar |  |  | SI | Latch score |
| Q19 | varchar |  |  | SI | 0 - 6  |
| Q20 | varchar |  |  | SI | 7 - 10 |
| Q21 | varchar |  |  | SI | It can predict non-exclusive breastfeeding at disc... |
| Q22 | varchar |  |  | SI | It can predict exclusive breastfeeding at discharg... |
| Q23 | varchar |  |  | SI | Score |
| Q24 | varchar |  |  | SI | Classification |
| Q25 | varchar |  |  | SI | 0 - 6: It can predict non-exclusive breastfeeding ... |
| Q26 | varchar |  |  | SI | 7 - 10: It can predict exclusive breastfeeding at ... |
| Q27 | date |  |  | SI | Date |
| Q28 | time |  |  | SI | Time |
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