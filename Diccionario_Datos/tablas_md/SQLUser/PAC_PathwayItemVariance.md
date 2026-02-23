# SQLUser.PAC_PathwayItemVariance

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPIV_ParRef | varchar | PK |  | NO | Parent Reference |
| PACPIV_AccessProfile_DR | bigint |  | FK | SI | Access Profile |
| PACPIV_CanChange | varchar |  |  | SI | Can Change |
| PACPIV_Childsub | double |  |  | NO | Childsub |
| PACPIV_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| PACPIV_CreatedDate | date |  |  | SI | Created Date |
| PACPIV_CreatedTime | time |  |  | SI | Created Time |
| PACPIV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPIV_ReasonRequired | varchar |  |  | SI | Reason Required |
| PACPIV_RowId | varchar |  |  | NO | - |
| PACPIV_UpdatedDate | date |  |  | SI | Updated Date |
| PACPIV_UpdatedTime | time |  |  | SI | Updated Time |
| PACPIV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | I. The pain you have had on the average, including... |
| Q02 | - |  |  | SI | II. How often have you had back, buttock, or leg p... |
| Q03 | - |  |  | SI | III. The pain in your back or buttocks? |
| Q04 | - |  |  | SI | IV. The pain in your legs or feet? |
| Q05 | - |  |  | SI | V. Numbness or tingling in your legs or feet? |
| Q06 | - |  |  | SI | VI. Weakness in your legs or feet? |
| Q07 | - |  |  | SI | VII. Problems with your balance? |
| Q08 | - |  |  | SI | VIII. How far have you been able to walk? |
| Q09 | - |  |  | SI | IX. Have you taken walks outdoors or around the sh... |
| Q10 | - |  |  | SI | X. Have you been shopping for groceries or other i... |
| Q11 | - |  |  | SI | XI. Have you walked around the different rooms in ... |
| Q12 | - |  |  | SI | XII. Have you walked from your bedroom to the bath... |
| Q13 | - |  |  | SI | XIII. The overall result of your back operation? |
| Q14 | - |  |  | SI | XIV. Relief of pain after your operation? |
| Q15 | - |  |  | SI | XV. The ability to walk after your operation? |
| Q16 | - |  |  | SI | XVI. Your ability to do housework, yardwork, or jo... |
| Q17 | - |  |  | SI | XVII. Your strength in your thighs, legs, and feet... |
| Q18 | - |  |  | SI | XVIII. Your balance, or steadiness, on your feet? |
| Q19 | - |  |  | SI | The Zurich Claudication Questionnaire quantifies s... |
| Q20 | - |  |  | SI | There are 12 questions for all patients, and a fur... |
| Q21 | - |  |  | SI | The The Zurich Claudication Questionnaire consists... |
| Q22 | - |  |  | SI | 1. Symptom severity scale  (questions I-VII) [furt... |
| Q23 | - |  |  | SI | 2. Physical function scale (questions VIII-XII): P... |
| Q24 | - |  |  | SI | 3. Patient's satisfaction with treatment scale (qu... |
| Q25 | - |  |  | SI | The score increases with worsening disability. |
| Q26 | - |  |  | SI | 0 = No Disability & 79 = Worsening Disability |
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