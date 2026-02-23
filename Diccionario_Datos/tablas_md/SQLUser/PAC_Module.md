# SQLUser.PAC_Module

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MODUL_RowId | bigint | PK |  | NO | - |
| MODUL_Code | varchar |  |  | NO | Code |
| MODUL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MODUL_CreatedDate | date |  |  | SI | Created Date |
| MODUL_CreatedTime | time |  |  | SI | Created Time |
| MODUL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MODUL_Desc | varchar |  |  | NO | Description |
| MODUL_Owner | varchar |  |  | SI | Owner |
| MODUL_Type | varchar |  |  | SI | - |
| MODUL_UpdatedDate | date |  |  | SI | Updated Date |
| MODUL_UpdatedTime | time |  |  | SI | Updated Time |
| MODUL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Variance |
| Q04 | - |  |  | SI | Alert and&nbsp |
| Q05 | - |  |  | SI | Variance |
| Q06 | - |  |  | SI | Patient received prescribed analgesia and reports ... |
| Q07 | - |  |  | SI | Patient provided education on using Patient&nbsp |
| Q08 | - |  |  | SI | Variance |
| Q09 | - |  |  | SI | Variance |
| Q10 | - |  |  | SI | Observations are within acceptable limits and stab... |
| Q11 | - |  |  | SI | Variance |
| Q12 | - |  |  | SI | Administer oxygen via nasal prongs at 2L/min until... |
| Q13 | - |  |  | SI | Variance |
| Q14 | - |  |  | SI | Patients fluid intake and output recorded on the f... |
| Q15 | - |  |  | SI | Variance |
| Q16 | - |  |  | SI | Drain remained patent and all drainage documented ... |
| Q17 | - |  |  | SI | Variance |
| Q18 | - |  |  | SI | Patient has voided post operatively (can stand wit... |
| Q19 | - |  |  | SI | Variance |
| Q20 | - |  |  | SI | All medication and intravenous (IV) fluid administ... |
| Q21 | - |  |  | SI | Variance |
| Q22 | - |  |  | SI | Post-operative wash attended |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Wound site remained free from haematoma |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | Patient preformed deep breathing and coughing exer... |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | Patient position and movement as per post operativ... |
| Q29 | - |  |  | SI | Variance |
| Q30 | - |  |  | SI | Patient mobilised in/out of bed while maintaining ... |
| Q31 | - |  |  | SI | Variance |
| Q32 | - |  |  | SI | Referrals&nbsp |
| Q33 | - |  |  | SI | Variance |
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