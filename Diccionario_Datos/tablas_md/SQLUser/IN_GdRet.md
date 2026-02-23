# SQLUser.IN_GdRet

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INGRR_INGR_ParRef | bigint | PK |  | NO | Des Ref to INGR |
| INGRR_ChildSub | double |  |  | NO | INGRR ChildSub (New Key) |
| INGRR_Completed | varchar |  |  | SI | Completed |
| INGRR_Date | date |  |  | NO | Good Return Date |
| INGRR_DateLastUpdated | date |  |  | SI | DateLastUpdated |
| INGRR_No | varchar |  |  | NO | Good Return Reference No |
| INGRR_RowId | varchar |  |  | NO | - |
| INGRR_SSUSR_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| INGRR_Time | time |  |  | NO | Time |
| INGRR_TimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| INGRR_UserLastUpdated_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| Q01 | - |  |  | SI | Date of test |
| Q02 | - |  |  | SI | Time of test |
| Q03 | - |  |  | SI | Standing on a firm surface with eyes open time (se... |
| Q04 | - |  |  | SI | Attempt 1 |
| Q05 | - |  |  | SI | Attempt 2 |
| Q06 | - |  |  | SI | Attempt 3 |
| Q07 | - |  |  | SI | Result |
| Q08 | - |  |  | SI | Standing on a firm surface with eyes closed time (... |
| Q09 | - |  |  | SI | Attempt 1 |
| Q10 | - |  |  | SI | Attempt 2 |
| Q11 | - |  |  | SI | Attempt 3 |
| Q12 | - |  |  | SI | Result |
| Q13 | - |  |  | SI | Standing on a firm surface with visual conflict ti... |
| Q14 | - |  |  | SI | Attempt 1 |
| Q15 | - |  |  | SI | Attempt 2 |
| Q16 | - |  |  | SI | Attempt 3 |
| Q17 | - |  |  | SI | Result |
| Q18 | - |  |  | SI | Standing on an unstable surface with eyes open tim... |
| Q19 | - |  |  | SI | Attempt 1 |
| Q20 | - |  |  | SI | Attempt 2 |
| Q21 | - |  |  | SI | Attempt 3 |
| Q22 | - |  |  | SI | Result |
| Q23 | - |  |  | SI | Standing on an unstable surface with eyes closed t... |
| Q24 | - |  |  | SI | Attempt 1 |
| Q25 | - |  |  | SI | Attempt 2 |
| Q26 | - |  |  | SI | Attempt 3 |
| Q27 | - |  |  | SI | Result |
| Q28 | - |  |  | SI | Standing on an unstable surface with visual confli... |
| Q29 | - |  |  | SI | Attempt 1 |
| Q30 | - |  |  | SI | Attempt 2 |
| Q31 | - |  |  | SI | Attempt 3 |
| Q32 | - |  |  | SI | Result |
| Q33 | - |  |  | SI | Comments |
| Q34 | - |  |  | SI | General Information |
| Q35 | - |  |  | SI | 1. Patients stand with their hands at their sides,... |
| Q36 | - |  |  | SI | 2. Patient performance is timed for 30 seconds. |
| Q37 | - |  |  | SI | 3. The test is terminated when: |
| Q38 | - |  |  | SI | • 30 seconds elapses |
| Q39 | - |  |  | SI | • A subject's arms or feet change position |
| Q40 | - |  |  | SI | 4. If a patient is unable to maintain the position... |
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