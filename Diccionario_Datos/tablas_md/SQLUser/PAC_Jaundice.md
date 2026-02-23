# SQLUser.PAC_Jaundice

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| JAUN_RowId | bigint | PK |  | NO | - |
| JAUN_Code | varchar |  |  | NO | Code |
| JAUN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| JAUN_CreatedDate | date |  |  | SI | Created Date |
| JAUN_CreatedTime | time |  |  | SI | Created Time |
| JAUN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| JAUN_Desc | varchar |  |  | NO | Description |
| JAUN_Owner | varchar |  |  | SI | Owner |
| JAUN_UpdatedDate | date |  |  | SI | Updated Date |
| JAUN_UpdatedTime | time |  |  | SI | Updated Time |
| JAUN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Fingers - Right |
| Q04 | - |  |  | SI | Fingers - Left |
| Q05 | - |  |  | SI | Hand - Right |
| Q06 | - |  |  | SI | Hand - Left |
| Q07 | - |  |  | SI | Forearm - Right |
| Q08 | - |  |  | SI | Forearm - Left |
| Q09 | - |  |  | SI | Upper arm - Right |
| Q10 | - |  |  | SI | Upper arm - Left |
| Q11 | - |  |  | SI | Face |
| Q12 | - |  |  | SI | Anterior chest |
| Q13 | - |  |  | SI | Abdomen |
| Q14 | - |  |  | SI | Thigh - Right |
| Q15 | - |  |  | SI | Thigh - Left |
| Q16 | - |  |  | SI | Leg - Right |
| Q17 | - |  |  | SI | Leg - Left |
| Q18 | - |  |  | SI | Feet - Right |
| Q19 | - |  |  | SI | Feet - Left |
| Q20 | - |  |  | SI | Notes |
| Q21 | - |  |  | SI | Score |
| Q22 | - |  |  | SI | Modified Rodnan Skin Score score range 0 to 51. Hi... |
| Q23 | - |  |  | SI | Right |
| Q24 | - |  |  | SI | Left |
| Q25 | - |  |  | SI | Fingers |
| Q26 | - |  |  | SI | Hand |
| Q27 | - |  |  | SI | Forearm |
| Q28 | - |  |  | SI | Upper arm |
| Q29 | - |  |  | SI | Thigh |
| Q30 | - |  |  | SI | Leg |
| Q31 | - |  |  | SI | Feet |
| Q34 | - |  |  | SI | Right |
| Q35 | - |  |  | SI | Right |
| Q36 | - |  |  | SI | Right |
| Q37 | - |  |  | SI | Right |
| Q38 | - |  |  | SI | Right |
| Q39 | - |  |  | SI | Left |
| Q40 | - |  |  | SI | Face |
| Q41 | - |  |  | SI | Anterior chest |
| Q42 | - |  |  | SI | Abdomen |
| Q43 | - |  |  | SI | Right |
| Q44 | - |  |  | SI | Right |
| Q45 | - |  |  | SI | Left |
| Q46 | - |  |  | SI | Left |
| Q47 | - |  |  | SI | Left |
| Q48 | - |  |  | SI | Left |
| Q49 | - |  |  | SI | Left |
| Q50 | - |  |  | SI | Left |
| Q51 | - |  |  | SI | Left |
| Q52 | - |  |  | SI | Right |
| Q53 | - |  |  | SI | Annotated image |
| Q54 | - |  |  | SI | (Khanna D, Furst DE, Clements PJ, et al. Standardi... |
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