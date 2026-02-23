# SQLUser.DTC_Protein

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Dieta**. Parámetros de alimentación y nutrición.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROT_RowId | bigint | PK |  | NO | - |
| PROT_Code | varchar |  |  | NO | Code |
| PROT_CreatedDate | date |  |  | SI | Created Date |
| PROT_CreatedTime | time |  |  | SI | Created Time |
| PROT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROT_Desc | varchar |  |  | NO | Description |
| PROT_UpdatedDate | date |  |  | SI | Updated Date |
| PROT_UpdatedTime | time |  |  | SI | Updated Time |
| PROT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Site |
| Q02 | - |  |  | SI | Onset |
| Q03 | - |  |  | SI | Character |
| Q04 | - |  |  | SI | Radiation |
| Q05 | - |  |  | SI | Associated symptoms |
| Q06 | - |  |  | SI | Duration |
| Q07 | - |  |  | SI | Exacerbating factors |
| Q08 | - |  |  | SI | Severity |
| Q09 | - |  |  | SI | Comments |
| Q10 | - |  |  | SI | Relieving factors |
| Q11 | - |  |  | SI | Onset |
| Q12 | - |  |  | SI | Has it been getting worse ? |
| Q13 | - |  |  | SI | Severity |
| Q14 | - |  |  | SI | Orthopnea |
| Q15 | - |  |  | SI | Paroxysmal Nocturnal Dyspnoea (PND) |
| Q16 | - |  |  | SI | Palpitations ? |
| Q17 | - |  |  | SI | Palpitations precipitating factor |
| Q18 | - |  |  | SI | Presyncope / Syncope? |
| Q19 | - |  |  | SI | Oedema ? |
| Q19ObsDR | - |  |  | SI | Oedema ? DR |
| Q23 | - |  |  | SI | Symptoms of previous cardiac events |
| Q24 | - |  |  | SI | Syncope type |
| Q24ObsDR | - |  |  | SI | Syncope type DR |
| Q25 | - |  |  | SI | Fatigue |
| Q26 | - |  |  | SI | Previous cardiac events ? |
| Q27 | - |  |  | SI | Other associated symptom |
| Q28 | - |  |  | SI | Other exacerbating factor |
| Q29 | - |  |  | SI | Other relieving factor |
| Q30 | - |  |  | SI | Relieving factors |
| Q31 | - |  |  | SI | Other relieving factor |
| Q32 | - |  |  | SI | Date |
| Q33 | - |  |  | SI | Time |
| Q40 | - |  |  | SI | Chest pain |
| Q41 | - |  |  | SI | Shortness of breath |
| Q42 | - |  |  | SI | Risk factors |
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