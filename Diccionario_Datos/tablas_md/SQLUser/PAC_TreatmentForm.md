# SQLUser.PAC_TreatmentForm

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TF_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Clinical indication for completing test	 |
| Q02 | - |  |  | SI | Gait aid |
| Q03 | - |  |  | SI | Patient observations at start of test |
| Q04 | - |  |  | SI | BORG |
| Q05 | - |  |  | SI | Systolic Blood Pressure |
| Q06 | - |  |  | SI | Diastolic Blood Pressure |
| Q07 | - |  |  | SI | Heart Rate |
| Q08 | - |  |  | SI | Respiratory Rate |
| Q09 | - |  |  | SI | SpO2 |
| Q10 | - |  |  | SI | If the patient at 20m has SpO2 > 85% continue walk... |
| Q11 | - |  |  | SI | Patient observations at end of test |
| Q12 | - |  |  | SI | BORG |
| Q13 | - |  |  | SI | Systolic Blood Pressure |
| Q14 | - |  |  | SI | Diastolic Blood Pressure |
| Q15 | - |  |  | SI | Heart Rate |
| Q16 | - |  |  | SI | Respiratory Rate |
| Q17 | - |  |  | SI | SpO2 |
| Q18 | - |  |  | SI | Comments |
| Q18TxtOnly | - |  |  | SI | Comments Plain Text Only |
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
| TF_Code | varchar |  |  | NO | Code |
| TF_CreatedDate | date |  |  | SI | Created Date |
| TF_CreatedTime | time |  |  | SI | Created Time |
| TF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TF_DateFrom | date |  |  | SI | Date From |
| TF_DateTo | date |  |  | SI | DateTo |
| TF_Desc | varchar |  |  | NO | Description |
| TF_UpdatedDate | date |  |  | SI | Updated Date |
| TF_UpdatedTime | time |  |  | SI | Updated Time |
| TF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*