# SQLUser.PAC_PlaceOfInjury

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLINJ_RowId | bigint | PK |  | NO | - |
| PLINJ_Code | varchar |  |  | NO | Code |
| PLINJ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PLINJ_CreatedDate | date |  |  | SI | Created Date |
| PLINJ_CreatedTime | time |  |  | SI | Created Time |
| PLINJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PLINJ_DateFrom | date |  |  | SI | Date From |
| PLINJ_DateTo | date |  |  | SI | Date To |
| PLINJ_Desc | varchar |  |  | NO | Description |
| PLINJ_NationalCode | varchar |  |  | SI | National Code |
| PLINJ_Owner | varchar |  |  | SI | Owner |
| PLINJ_Subregion_DR | bigint |  | FK | SI | Subregion  |
| PLINJ_UpdatedDate | date |  |  | SI | Updated Date |
| PLINJ_UpdatedTime | time |  |  | SI | Updated Time |
| PLINJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Side |
| Q02 | - |  |  | SI | Symptoms |
| Q03 | - |  |  | SI | Others |
| Q04 | - |  |  | SI | Reason for surgery |
| Q05 | - |  |  | SI | Others |
| Q06 | - |  |  | SI | Risk factors |
| Q07 | - |  |  | SI | Others |
| Q08 | - |  |  | SI | Contralateral ear |
| Q09 | - |  |  | SI | Others |
| Q10 | - |  |  | SI | Otomycosis |
| Q11 | - |  |  | SI | Discharge |
| Q12 | - |  |  | SI | Perforation |
| Q13 | - |  |  | SI | Tympanic Membrane (TM) atelectasis |
| Q14 | - |  |  | SI | Site of atelectasis |
| Q15 | - |  |  | SI | Tympanic Membrane (TM) drawing |
| Q16 | - |  |  | SI | Tuning fork |
| Q17 | - |  |  | SI | Rinne test, right |
| Q18 | - |  |  | SI | Rinne test, left |
| Q19 | - |  |  | SI | Weber test |
| Q20 | - |  |  | SI | Other findings |
| Q21 | - |  |  | SI | Assessment interval |
| Q22 | - |  |  | SI | Complications |
| Q23 | - |  |  | SI | Others |
| Q24 | - |  |  | SI | Discharge |
| Q25 | - |  |  | SI | Otoscopic Appearance |
| Q26 | - |  |  | SI | Tympanic Membrane (TM)  integrity |
| Q27 | - |  |  | SI | Tympanic Membrane (TM) surface |
| Q28 | - |  |  | SI | Tympanic Membrane (TM) morphology |
| Q29 | - |  |  | SI | External canal |
| Q30 | - |  |  | SI | Cholesteatoma |
| Q31 | - |  |  | SI | Ossicular prosthesis |
| Q32 | - |  |  | SI | Note |
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