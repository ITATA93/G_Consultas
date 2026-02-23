# SQLUser.PAC_AccomSetting

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACCOMS_RowId | bigint | PK |  | NO | - |
| ACCOMS_Code | varchar |  |  | NO | Code |
| ACCOMS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACCOMS_CreatedDate | date |  |  | SI | Created Date |
| ACCOMS_CreatedTime | time |  |  | SI | Created Time |
| ACCOMS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACCOMS_DateFrom | date |  |  | SI | DateFrom |
| ACCOMS_DateTo | date |  |  | SI | DateTo |
| ACCOMS_Desc | varchar |  |  | NO | Description |
| ACCOMS_Owner | varchar |  |  | SI | Owner |
| ACCOMS_UpdatedDate | date |  |  | SI | Updated Date |
| ACCOMS_UpdatedTime | time |  |  | SI | Updated Time |
| ACCOMS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Heart beating quickly or strongly |
| Q04 | - |  |  | SI | Feeling tense or nervous |
| Q05 | - |  |  | SI | Difficulty in sleeping |
| Q06 | - |  |  | SI | Excitable |
| Q07 | - |  |  | SI | Attacks of anxiety, panic |
| Q08 | - |  |  | SI | Difficulty in concentrating |
| Q09 | - |  |  | SI | Feeling tired or lacking in energy |
| Q10 | - |  |  | SI | Loss of interest in most things |
| Q11 | - |  |  | SI | Feeling unhappy or depressed |
| Q12 | - |  |  | SI | Crying spells |
| Q13 | - |  |  | SI | Irritability |
| Q14 | - |  |  | SI | Feeling dizzy or faint |
| Q15 | - |  |  | SI | Pressure or tightness in head |
| Q16 | - |  |  | SI | Parts of body feel numb |
| Q17 | - |  |  | SI | Headaches |
| Q18 | - |  |  | SI | Muscle and joint pains |
| Q19 | - |  |  | SI | Loss of feeling in hands or feet |
| Q20 | - |  |  | SI | Breathing difficulties |
| Q21 | - |  |  | SI | Hot flushes |
| Q22 | - |  |  | SI | Sweating at night |
| Q23 | - |  |  | SI | Loss of interest in sex |
| Q24 | - |  |  | SI | Please indicate the extent to which you are bother... |
| Q25 | - |  |  | SI | Score |
| Q26 | - |  |  | SI | Classification |
| Q27 | - |  |  | SI | 0 - 63 |
| Q28 | - |  |  | SI | 69 |
| Q29 | - |  |  | SI | Higher scores represents worse symptoms |
| Q30 | - |  |  | SI | 0 - 63: Higher scores represents worse symptoms |
| Q31 | - |  |  | SI | The Greene Climacteric Scale provides a brief meas... |
| Q32 | - |  |  | SI | physical or somatic symptoms and vasomotor symptom... |
| Q33 | - |  |  | SI | The scale consist of 21 questions with four point ... |
| Q34 | - |  |  | SI | Parts of body feel numb |
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