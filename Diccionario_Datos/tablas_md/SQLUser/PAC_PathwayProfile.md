# SQLUser.PAC_PathwayProfile

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPAP_ParRef | bigint | PK |  | NO | Parent Reference |
| PACPAP_AccessProfile_DR | bigint |  | FK | SI | Access Profile |
| PACPAP_Childsub | double |  |  | NO | Childsub |
| PACPAP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACPAP_CreatedDate | date |  |  | SI | Created Date |
| PACPAP_CreatedTime | time |  |  | SI | Created Time |
| PACPAP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPAP_RowId | varchar |  |  | NO | - |
| PACPAP_UpdatedDate | date |  |  | SI | Updated Date |
| PACPAP_UpdatedTime | time |  |  | SI | Updated Time |
| PACPAP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | How many times do you typically urinate from wakin... |
| Q02 | - |  |  | SI | How many times do you typically wake up to urinate... |
| Q03 | - |  |  | SI | How often do you have a sudden desire to urinate, ... |
| Q04 | - |  |  | SI | How often do you leak urine because you cannot def... |
| Q05 | - |  |  | SI | Score |
| Q06 | - |  |  | SI | Classification |
| Q07 | - |  |  | SI | 1 - 5 |
| Q08 | - |  |  | SI | Mild Overactive Bladder |
| Q09 | - |  |  | SI | 6 - 11 |
| Q10 | - |  |  | SI | Moderate Overactive Bladder |
| Q11 | - |  |  | SI | ≥ 12 |
| Q12 | - |  |  | SI | Severe Overactive Bladder |
| Q13 | - |  |  | SI | 1 - 5: Mild Overactive Bladder |
| Q14 | - |  |  | SI | 6 - 11: Moderate Overactive Bladder |
| Q15 | - |  |  | SI | >= 12: Severe Overactive Bladder |
| Q16 | - |  |  | SI | The Overactive Bladder Symptom Score (OABSS) is a ... |
| Q17 | - |  |  | SI | Date |
| Q18 | - |  |  | SI | Time |
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