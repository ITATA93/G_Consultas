# SQLUser.PAC_DelLocLogicResult

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Registro de eventos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DELLOG_RowId | bigint | PK |  | NO | - |
| DELLOG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DELLOG_CreatedDate | date |  |  | SI | Created Date |
| DELLOG_CreatedTime | time |  |  | SI | Created Time |
| DELLOG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DELLOG_DateFrom | date |  |  | SI | Date From |
| DELLOG_DateTo | date |  |  | SI | Date To |
| DELLOG_DeliveryLoc_DR | bigint |  | FK | SI | Des Ref DeliveryLoc |
| DELLOG_EpisLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DELLOG_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| DELLOG_Owner | varchar |  |  | SI | Owner |
| DELLOG_RecLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DELLOG_UpdatedDate | date |  |  | SI | Updated Date |
| DELLOG_UpdatedTime | time |  |  | SI | Updated Time |
| DELLOG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Pain scale |
| Q03ObsDR | - |  |  | SI | Pain scale DR |
| Q04 | - |  |  | SI | How does the patient feel? |
| Q05 | - |  |  | SI | Does the patient have nausea / vomiting? |
| Q06 | - |  |  | SI | Does the patient have nausea / vomiting? |
| Q07 | - |  |  | SI | Does the patient indicate any numbness in the leg? |
| Q08 | - |  |  | SI | Additional subjective information |
| Q09 | - |  |  | SI | Vital Signs |
| Q10 | - |  |  | SI | Temperature |
| Q10ObsDR | - |  |  | SI | Temperature DR |
| Q11 | - |  |  | SI | RR |
| Q11ObsDR | - |  |  | SI | RR DR |
| Q12 | - |  |  | SI | Pulse |
| Q12ObsDR | - |  |  | SI | Pulse DR |
| Q13 | - |  |  | SI | Systolic BP |
| Q13ObsDR | - |  |  | SI | Systolic BP DR |
| Q14 | - |  |  | SI | Diastolic BP |
| Q14ObsDR | - |  |  | SI | Diastolic BP DR |
| Q15 | - |  |  | SI | Wound Details |
| Q16 | - |  |  | SI | Bleeding |
| Q17 | - |  |  | SI | Signs of infection |
| Q18 | - |  |  | SI | Swelling |
| Q19 | - |  |  | SI | Signs of DVT |
| Q20 | - |  |  | SI | Vacuum drain |
| Q21 | - |  |  | SI | Vacuum drain (ml) |
| Q22 | - |  |  | SI | ml |
| Q23 | - |  |  | SI | Additional wound information |
| Q24 | - |  |  | SI | Knee Range of Motion (ROM) |
| Q26 | - |  |  | SI | Neurovascular Status |
| Q27 | - |  |  | SI | Neurovascular status |
| Q28 | - |  |  | SI | Neurovascular details |
| Q29 | - |  |  | SI | Ambulation |
| Q30 | - |  |  | SI | Ambulation |
| Q31 | - |  |  | SI | Ambulation details |
| Q32 | - |  |  | SI | Post-op progress |
| Q33 | - |  |  | SI | Recovery as expected |
| Q34 | - |  |  | SI | Additional assessment information |
| Q35 | - |  |  | SI | Plan |
| Q36 | - |  |  | SI | Self physical therapy training program explained a... |
| Q37 | - |  |  | SI | Continue intravenous antibiotics |
| Q38 | - |  |  | SI | Additional discharge information |
| Q39 | - |  |  | SI | °C |
| Q40 | - |  |  | SI | br/min |
| Q41 | - |  |  | SI | bt/min |
| Q42 | - |  |  | SI | mmHg |
| Q43 | - |  |  | SI | mmHg |
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