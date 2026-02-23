# SQLUser.PAC_DependentChildren

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registros hijos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEPCHL_RowId | bigint | PK |  | NO | - |
| DEPCHL_Code | varchar |  |  | NO | Code |
| DEPCHL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEPCHL_CreatedDate | date |  |  | SI | Created Date |
| DEPCHL_CreatedTime | time |  |  | SI | Created Time |
| DEPCHL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEPCHL_DateFrom | date |  |  | SI | Date From |
| DEPCHL_DateTo | date |  |  | SI | DateTo |
| DEPCHL_Desc | varchar |  |  | NO | Description |
| DEPCHL_Owner | varchar |  |  | SI | Owner |
| DEPCHL_UpdatedDate | date |  |  | SI | Updated Date |
| DEPCHL_UpdatedTime | time |  |  | SI | Updated Time |
| DEPCHL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Latch |
| Q02 | - |  |  | SI | Audible swallowing	 |
| Q03 | - |  |  | SI | Type of nipple	 |
| Q04 | - |  |  | SI | Comfort (breast and nipple)	 |
| Q05 | - |  |  | SI | Hold (positioning) |
| Q06 | - |  |  | SI | A LATCH score < 7 can predict non-exclusive breast... |
| Q07 | - |  |  | SI | A LATCH score >=7 can predict exclusive breastfeed... |
| Q08 | - |  |  | SI | LATCH is a breastfeeding charting system that prov... |
| Q09 | - |  |  | SI | L'' is for how well the infant latches onto the br... |
| Q10 | - |  |  | SI | H'' is for the amount of help the mother needs to ... |
| Q11 | - |  |  | SI | Document feeding time of newborn. |
| Q12 | - |  |  | SI | Observe a minimum of one breastfeeding session per... |
| Q13 | - |  |  | SI | Score the feed in the appropriate space and docume... |
| Q14 | - |  |  | SI | Document whether the feed was observed or reported... |
| Q15 | - |  |  | SI | If score is less than 7, the next feeding is to be... |
| Q16 | - |  |  | SI | If two subsequent scores less than 7 are obtained,... |
| Q17 | - |  |  | SI | Additional comments |
| Q18 | - |  |  | SI | Latch score |
| Q19 | - |  |  | SI | 0 - 6 |
| Q20 | - |  |  | SI | 7 - 10 |
| Q21 | - |  |  | SI | It can predict non-exclusive breastfeeding at disc... |
| Q22 | - |  |  | SI | It can predict exclusive breastfeeding at discharg... |
| Q23 | - |  |  | SI | Score |
| Q24 | - |  |  | SI | Classification |
| Q25 | - |  |  | SI | 0 - 6: It can predict non-exclusive breastfeeding ... |
| Q26 | - |  |  | SI | 7 - 10: It can predict exclusive breastfeeding at ... |
| Q27 | - |  |  | SI | Date |
| Q28 | - |  |  | SI | Time |
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

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*