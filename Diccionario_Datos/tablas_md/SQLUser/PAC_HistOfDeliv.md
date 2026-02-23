# SQLUser.PAC_HistOfDeliv

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HISTD_RowId | bigint | PK |  | NO | - |
| HISTD_Code | varchar |  |  | NO | Code |
| HISTD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HISTD_CreatedDate | date |  |  | SI | Created Date |
| HISTD_CreatedTime | time |  |  | SI | Created Time |
| HISTD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HISTD_DateFrom | date |  |  | SI | Date From |
| HISTD_DateTo | date |  |  | SI | Date To |
| HISTD_Desc | varchar |  |  | NO | Description |
| HISTD_Owner | varchar |  |  | SI | Owner |
| HISTD_UpdatedDate | date |  |  | SI | Updated Date |
| HISTD_UpdatedTime | time |  |  | SI | Updated Time |
| HISTD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Pinch grip |
| Q04 | - |  |  | SI | Elbow flexion from 90° |
| Q05 | - |  |  | SI | Shoulder abduction |
| Q06 | - |  |  | SI | Right Arm Score |
| Q07 | - |  |  | SI | Pinch grip |
| Q08 | - |  |  | SI | Elbow flexion from 90° |
| Q09 | - |  |  | SI | Shoulder abduction |
| Q10 | - |  |  | SI | Left Arm Score |
| Q11 | - |  |  | SI | Ankle dorsiflection |
| Q12 | - |  |  | SI | Knee extension |
| Q13 | - |  |  | SI | Hip flexion |
| Q14 | - |  |  | SI | Right Leg Score |
| Q15 | - |  |  | SI | Ankle dorsiflection |
| Q16 | - |  |  | SI | Knee extension |
| Q17 | - |  |  | SI | Hip flexion |
| Q18 | - |  |  | SI | Left Leg Score |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Classification |
| Q21 | - |  |  | SI | 0 - 100 |
| Q22 | - |  |  | SI | Lower scores indicate greater impairment |
| Q23 | - |  |  | SI | 0 - 100: Lower scores indicate greater impairment |
| Q24 | - |  |  | SI | The Motricity Index (MI) is an ordinal method of m... |
| Q25 | - |  |  | SI | Right Arm score Calculated |
| Q26 | - |  |  | SI | Left Arm Score Calculated |
| Q27 | - |  |  | SI | Right Leg Score Calculated |
| Q28 | - |  |  | SI | Left Leg Score Calculated |
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