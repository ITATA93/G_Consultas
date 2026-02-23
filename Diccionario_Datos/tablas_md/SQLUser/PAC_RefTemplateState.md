# SQLUser.PAC_RefTemplateState

**Schema:** SQLUser
**Columnas:** 95
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFTMS_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Prescription type	 |
| Q02 | - |  |  | SI | Peritoneal dialysis type |
| Q03 | - |  |  | SI | Target weight (empty)	 |
| Q04 | - |  |  | SI | Number of exchanges	 |
| Q05 | - |  |  | SI | Total volume (ml) |
| Q06 | - |  |  | SI | Type of peritoneal dialysis solutions	 |
| Q07 | - |  |  | SI | APD target weight (empty)	 |
| Q08 | - |  |  | SI | Target (Nocturnal Intermittent Peritoneal Dialysis... |
| Q09 | - |  |  | SI | If on TIDAL, specify %	 |
| Q10 | - |  |  | SI | Duration of night therapy	 |
| Q11 | - |  |  | SI | Volume / Solution of last fill	 |
| Q12 | - |  |  | SI | Total volume	 |
| Q13 | - |  |  | SI | Additional day fill (specify)	 |
| Q14 | - |  |  | SI | Target empty weight (kg) |
| Q15 | - |  |  | SI | Comments |
| Q16 | - |  |  | SI | Date of prescription |
| Q17 | - |  |  | SI | Prescription type |
| Q18 | - |  |  | SI | Days off dialysis |
| Q19 | - |  |  | SI | Comments |
| Q20 | - |  |  | SI | APD modality |
| Q21 | - |  |  | SI | Fill volume (ml) |
| Q22 | - |  |  | SI | Comments |
| Q23 | - |  |  | SI | Number of cycles |
| Q24 | - |  |  | SI | Comments |
| Q25 | - |  |  | SI | Therapy time (hr) |
| Q26 | - |  |  | SI | Comments |
| Q27 | - |  |  | SI | Last fill |
| Q28 | - |  |  | SI | Last fill concentration |
| Q29 | - |  |  | SI | Last fill volume (ml) |
| Q30 | - |  |  | SI | Comments |
| Q31 | - |  |  | SI | Last fill dwell time (hr) |
| Q32 | - |  |  | SI | Comments |
| Q33 | - |  |  | SI | Daytime cycle |
| Q34 | - |  |  | SI | Daytime cycle concentration |
| Q35 | - |  |  | SI | Daytime cycle volume (ml) |
| Q36 | - |  |  | SI | Comments |
| Q37 | - |  |  | SI | Daytime cycle dwell time (hr) |
| Q38 | - |  |  | SI | Comments |
| Q39 | - |  |  | SI | Additional details |
| Q40 | - |  |  | SI | Comments |
| Q41 | - |  |  | SI | Date |
| Q42 | - |  |  | SI | Time |
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
| RFTMS_Code | varchar |  |  | NO | Code |
| RFTMS_Colour | varchar |  |  | SI | Colour |
| RFTMS_CreatedDate | date |  |  | SI | Created Date |
| RFTMS_CreatedTime | time |  |  | SI | Created Time |
| RFTMS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFTMS_DateFrom | date |  |  | SI | Date From	 |
| RFTMS_DateTo | date |  |  | SI | Date To |
| RFTMS_Desc | varchar |  |  | NO | Description |
| RFTMS_Rank | double |  |  | SI | Rank |
| RFTMS_UpdatedDate | date |  |  | SI | Updated Date |
| RFTMS_UpdatedTime | time |  |  | SI | Updated Time |
| RFTMS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*