# SQLUser.PAC_Art

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ART_RowId | bigint | PK |  | NO | - |
| ART_Code | varchar |  |  | NO | Code |
| ART_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ART_CreatedDate | date |  |  | SI | Created Date |
| ART_CreatedTime | time |  |  | SI | Created Time |
| ART_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ART_DateFrom | date |  |  | SI | Date From |
| ART_DateTo | date |  |  | SI | Date To |
| ART_Desc | varchar |  |  | NO | Description |
| ART_Owner | varchar |  |  | SI | Owner |
| ART_UpdatedDate | date |  |  | SI | Updated Date |
| ART_UpdatedTime | time |  |  | SI | Updated Time |
| ART_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ13DR | - |  |  | SI | Child Reference: Threshold test details	 |
| Q01 | - |  |  | SI | Ventricular Tachycardia (VT) episodes 	 |
| Q02 | - |  |  | SI | Ventricular Fibrillation (VF) episodes 	 |
| Q03 | - |  |  | SI | Cycle length VT	 |
| Q04 | - |  |  | SI | Cycle length VF	 |
| Q05 | - |  |  | SI | Appropriate therapy 	 |
| Q06 | - |  |  | SI | Non sustained events	 |
| Q07 | - |  |  | SI | Premature Ventricular Tachycardia (PVC) count	 |
| Q08 | - |  |  | SI | Type of Premature Ventricular Tachycardia (PVC)	 |
| Q09 | - |  |  | SI | Battery status	 |
| Q10 | - |  |  | SI | Charge time	 |
| Q11 | - |  |  | SI | Last capacitor reform	 |
| Q12 | - |  |  | SI | Threshold test performed |
| Q14 | - |  |  | SI | Comments / Issues	 |
| Q15 | - |  |  | SI | ECG rhythm	 |
| Q16 | - |  |  | SI | Program changes and reasons	 |
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