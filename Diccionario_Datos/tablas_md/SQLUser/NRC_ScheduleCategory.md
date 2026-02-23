# SQLUser.NRC_ScheduleCategory

**Schema:** SQLUser
**Columnas:** 104
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Enfermería**. Parámetros de enfermería.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCHED_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Interuterine transfusion |
| Q01ObsDR | - |  |  | SI | Interuterine transfusion DR |
| Q02 | - |  |  | SI | Procedure straightforward |
| Q02ObsDR | - |  |  | SI | Procedure straightforward DR |
| Q03 | - |  |  | SI | Dry tap |
| Q03ObsDR | - |  |  | SI | Dry tap DR |
| Q04 | - |  |  | SI | Blood stained liquor |
| Q04ObsDR | - |  |  | SI | Blood stained liquor DR |
| Q05 | - |  |  | SI | Sample sent to |
| Q06 | - |  |  | SI | Amniocentesis results normal |
| Q06ObsDR | - |  |  | SI | Amniocentesis results normal DR |
| Q07 | - |  |  | SI | Procedure done by |
| Q08 | - |  |  | SI | More than 1 attempt - CVS |
| Q08ObsDR | - |  |  | SI | More than 1 attempt - CVS DR |
| Q09 | - |  |  | SI | More than 1 attempt - amnio |
| Q09ObsDR | - |  |  | SI | More than 1 attempt - amnio DR |
| Q10 | - |  |  | SI | Transabdominal |
| Q10ObsDR | - |  |  | SI | Transabdominal DR |
| Q11 | - |  |  | SI | CVS results normal |
| Q11ObsDR | - |  |  | SI | CVS results normal DR |
| Q12 | - |  |  | SI | Procedure done by |
| Q13 | - |  |  | SI | Sample sent to |
| Q14 | - |  |  | SI | Reason for investigation |
| Q14ObsDR | - |  |  | SI | Reason for investigation DR |
| Q15 | - |  |  | SI | Information booklet (before test) |
| Q15ObsDR | - |  |  | SI | Information booklet (before test) DR |
| Q16 | - |  |  | SI | Information leaflet (after test) |
| Q16ObsDR | - |  |  | SI | Information leaflet (after test) DR |
| Q17 | - |  |  | SI | General practitioner informed |
| Q17ObsDR | - |  |  | SI | General practitioner informed DR |
| Q18 | - |  |  | SI | Comments |
| Q19 | - |  |  | SI | Womans condition after procedure |
| Q19ObsDR | - |  |  | SI | Womans condition after procedure DR |
| Q20 | - |  |  | SI | Fetus number |
| Q20ObsDR | - |  |  | SI | Fetus number DR |
| Q21 | - |  |  | SI | Anti D required |
| Q21ObsDR | - |  |  | SI | Anti D required DR |
| Q22 | - |  |  | SI | Date Anti D given |
| Q23 | - |  |  | SI | Time Anti D given |
| Q24 | - |  |  | SI | Anti D batch number |
| Q25 | - |  |  | SI | Mother informed of result |
| Q25ObsDR | - |  |  | SI | Mother informed of result DR |
| Q26 | - |  |  | SI | Mother informed of baby's sex |
| Q26ObsDR | - |  |  | SI | Mother informed of baby's sex DR |
| Q27 | - |  |  | SI | Community midwife informed |
| Q27ObsDR | - |  |  | SI | Community midwife informed DR |
| Q28 | - |  |  | SI | Procedure straightforward |
| Q28ObsDR | - |  |  | SI | Procedure straightforward DR |
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
| SCHED_Active | varchar |  |  | SI | Active |
| SCHED_Code | varchar |  |  | NO | Code |
| SCHED_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SCHED_CreatedDate | date |  |  | SI | Created Date |
| SCHED_CreatedTime | time |  |  | SI | Created Time |
| SCHED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SCHED_DateFrom | date |  |  | SI | DateFrom |
| SCHED_DateTo | date |  |  | SI | DateTo |
| SCHED_Desc | varchar |  |  | NO | Description |
| SCHED_Owner | varchar |  |  | SI | Owner |
| SCHED_UpdatedDate | date |  |  | SI | Updated Date |
| SCHED_UpdatedTime | time |  |  | SI | Updated Time |
| SCHED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SCHED_WorkShift | varchar |  |  | SI | Work Shift |
| SCHED_WorkShift_DR | bigint |  | FK | SI | Des Ref WorkShift |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*