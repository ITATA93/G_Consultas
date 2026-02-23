# questionnaire.QGXXXMFI

> Fetal Investigations

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Fetal Investigations

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Interuterine transfusion |
| Q01ObsDR | varchar |  | FK | SI | Interuterine transfusion DR |
| Q02 | varchar |  |  | SI | Procedure straightforward |
| Q02ObsDR | varchar |  | FK | SI | Procedure straightforward DR |
| Q03 | varchar |  |  | SI | Dry tap |
| Q03ObsDR | varchar |  | FK | SI | Dry tap DR |
| Q04 | varchar |  |  | SI | Blood stained liquor |
| Q04ObsDR | varchar |  | FK | SI | Blood stained liquor DR |
| Q05 | varchar |  |  | SI | Sample sent to |
| Q06 | varchar |  |  | SI | Amniocentesis results normal |
| Q06ObsDR | varchar |  | FK | SI | Amniocentesis results normal DR |
| Q07 | varchar |  |  | SI | Procedure done by |
| Q08 | varchar |  |  | SI | More than 1 attempt - CVS |
| Q08ObsDR | varchar |  | FK | SI | More than 1 attempt - CVS DR |
| Q09 | varchar |  |  | SI | More than 1 attempt - amnio |
| Q09ObsDR | varchar |  | FK | SI | More than 1 attempt - amnio DR |
| Q10 | varchar |  |  | SI | Transabdominal |
| Q10ObsDR | varchar |  | FK | SI | Transabdominal DR |
| Q11 | varchar |  |  | SI | CVS results normal |
| Q11ObsDR | varchar |  | FK | SI | CVS results normal DR |
| Q12 | varchar |  |  | SI | Procedure done by |
| Q13 | varchar |  |  | SI | Sample sent to |
| Q14 | varchar |  |  | SI | Reason for investigation |
| Q14ObsDR | varchar |  | FK | SI | Reason for investigation DR |
| Q15 | varchar |  |  | SI | Information booklet (before test) |
| Q15ObsDR | varchar |  | FK | SI | Information booklet (before test) DR |
| Q16 | varchar |  |  | SI | Information leaflet (after test) |
| Q16ObsDR | varchar |  | FK | SI | Information leaflet (after test) DR |
| Q17 | varchar |  |  | SI | General practitioner informed |
| Q17ObsDR | varchar |  | FK | SI | General practitioner informed DR |
| Q18 | varchar |  |  | SI | Comments |
| Q19 | varchar |  |  | SI | Womans condition after procedure |
| Q19ObsDR | varchar |  | FK | SI | Womans condition after procedure DR |
| Q20 | varchar |  |  | SI | Fetus number |
| Q20ObsDR | varchar |  | FK | SI | Fetus number DR |
| Q21 | varchar |  |  | SI | Anti D required |
| Q21ObsDR | varchar |  | FK | SI | Anti D required DR |
| Q22 | date |  |  | SI | Date Anti D given |
| Q23 | time |  |  | SI | Time Anti D given |
| Q24 | numeric |  |  | SI | Anti D batch number |
| Q25 | varchar |  |  | SI | Mother informed of result |
| Q25ObsDR | varchar |  | FK | SI | Mother informed of result DR |
| Q26 | varchar |  |  | SI | Mother informed of baby's sex |
| Q26ObsDR | varchar |  | FK | SI | Mother informed of baby's sex DR |
| Q27 | varchar |  |  | SI | Community midwife informed |
| Q27ObsDR | varchar |  | FK | SI | Community midwife informed DR |
| Q28 | varchar |  |  | SI | Procedure straightforward |
| Q28ObsDR | varchar |  | FK | SI | Procedure straightforward DR |
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