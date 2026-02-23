# SQLUser.PAC_ProviderPrefReason

**Schema:** SQLUser
**Columnas:** 116
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROVREA_RowId | bigint | PK |  | NO | - |
| PROVREA_Code | varchar |  |  | NO | Code |
| PROVREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROVREA_CreatedDate | date |  |  | SI | Created Date |
| PROVREA_CreatedTime | time |  |  | SI | Created Time |
| PROVREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROVREA_DateFrom | date |  |  | SI | Date From |
| PROVREA_DateTo | date |  |  | SI | Date To |
| PROVREA_Desc | varchar |  |  | NO | Description |
| PROVREA_Owner | varchar |  |  | SI | Owner |
| PROVREA_UpdatedDate | date |  |  | SI | Updated Date |
| PROVREA_UpdatedTime | time |  |  | SI | Updated Time |
| PROVREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Procedure |
| Q02 | - |  |  | SI | Conscious & orientated |
| Q03 | - |  |  | SI | Comments |
| Q04 | - |  |  | SI | Maintaining the airway & having protective reflexe... |
| Q05 | - |  |  | SI | Comments |
| Q06 | - |  |  | SI | Stable cardiovascular function |
| Q07 | - |  |  | SI | Comments |
| Q08 | - |  |  | SI | Stable respiratory function |
| Q09 | - |  |  | SI | Comments |
| Q10 | - |  |  | SI | Body Temp >35.9°C |
| Q11 | - |  |  | SI | Comments |
| Q12 | - |  |  | SI | NEWS Score |
| Q13 | - |  |  | SI | Comments |
| Q14 | - |  |  | SI | Surgical site satisfactory |
| Q15 | - |  |  | SI | Comments |
| Q16 | - |  |  | SI | Is patient nauseous &/or vomiting |
| Q17 | - |  |  | SI | Comments |
| Q18 | - |  |  | SI | Is pain score 0 or 1 |
| Q19 | - |  |  | SI | Comments |
| Q20 | - |  |  | SI | Oxygenation |
| Q21 | - |  |  | SI | Comments |
| Q22 | - |  |  | SI | IV access / fluid replacement |
| Q23 | - |  |  | SI | Comments |
| Q24 | - |  |  | SI | Drugs given in recovery |
| Q25 | - |  |  | SI | Comments |
| Q26 | - |  |  | SI | PCA/IV site checked |
| Q27 | - |  |  | SI | Comments |
| Q28 | - |  |  | SI | Epidural site checked |
| Q29 | - |  |  | SI | Comments |
| Q30 | - |  |  | SI | Surgical site / wound checked |
| Q31 | - |  |  | SI | Comments |
| Q32 | - |  |  | SI | Dressing & drains |
| Q33 | - |  |  | SI | Comments |
| Q34 | - |  |  | SI | Skin condition assessed |
| Q35 | - |  |  | SI | Comments |
| Q36 | - |  |  | SI | Pressure areas intact |
| Q37 | - |  |  | SI | Comments |
| Q38 | - |  |  | SI | Patient passed urine |
| Q39 | - |  |  | SI | Comments |
| Q40 | - |  |  | SI | Fluid balanced chart commenced? |
| Q41 | - |  |  | SI | Comments |
| Q42 | - |  |  | SI | Pressure areas checked on handover to ward |
| Q43 | - |  |  | SI | Comments |
| Q44 | - |  |  | SI | Patient property checked |
| Q45 | - |  |  | SI | Comments |
| Q46 | - |  |  | SI | X-rays / Scans |
| Q47 | - |  |  | SI | Comments |
| Q48 | - |  |  | SI | Recovery staff name |
| Q49 | - |  |  | SI | Ward staff |
| Q50 | - |  |  | SI | Temperature ( ℃) |
| Q50ObsDR | - |  |  | SI | Temperature ( ℃) DR |
| Q51 | - |  |  | SI | Blood glucose (mmol/l) |
| Q51ObsDR | - |  |  | SI | Blood glucose (mmol/l) DR |
| Q52 | - |  |  | SI | Comments |
| Q53 | - |  |  | SI | Is the patient nauseous? |
| Q54 | - |  |  | SI | Is the patient vomiting? |
| Q55 | - |  |  | SI | Comments |
| Q56 | - |  |  | SI | Pain Score (0-10) |
| Q56ObsDR | - |  |  | SI | Pain Score (0-10) DR |
| Q57 | - |  |  | SI | Is the patient diabetic? |
| Q58 | - |  |  | SI | Comments |
| Q59 | - |  |  | SI | Date |
| Q60 | - |  |  | SI | Time |
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