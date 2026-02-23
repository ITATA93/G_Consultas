# SQLUser.PAC_NoFirstSkinContactReason

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NFSC_RowId | bigint | PK |  | NO | - |
| NFSC_Code | varchar |  |  | NO | Code |
| NFSC_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| NFSC_CreatedDate | date |  |  | SI | Created Date |
| NFSC_CreatedTime | time |  |  | SI | Created Time |
| NFSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NFSC_DateFrom | date |  |  | SI | Date From |
| NFSC_DateTo | date |  |  | SI | Date To |
| NFSC_Desc | varchar |  |  | NO | Description |
| NFSC_Owner | varchar |  |  | SI | Code Table Owner |
| NFSC_UpdatedDate | date |  |  | SI | Updated Date |
| NFSC_UpdatedTime | time |  |  | SI | Updated Time |
| NFSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | To be completed prior to oral intake |
| Q02 | - |  |  | SI | Date of admission: |
| Q03 | - |  |  | SI | Date of screen: |
| Q04 | - |  |  | SI | Time of screen |
| Q05 | - |  |  | SI | If the answer is Yes to the questions 2-7, obtain ... |
| Q06 | - |  |  | SI | 1. Patient is alert (can follow commands) |
| Q07 | - |  |  | SI | 2. Does patient exhibit slurred or garbled speech? |
| Q08 | - |  |  | SI | 3. Does patient exhibit trouble speaking or unders... |
| Q09 | - |  |  | SI | 4. Does patient exhibit drooling? |
| Q10 | - |  |  | SI | 5. Does patient have a wet-sounding voice? |
| Q11 | - |  |  | SI | 6. Give patient a teaspoon of water – Do any of th... |
| Q12 | - |  |  | SI | 7. Give patient 60 mL of water (only if teaspoon o... |
| Q13 | - |  |  | SI | Make patient NPO (Nil Per Oral) and obtain order f... |
| Q14 | - |  |  | SI | Comments |
| Q15 | - |  |  | SI | Comment 2 |
| Q16 | - |  |  | SI | Comment 3 |
| Q17 | - |  |  | SI | Comment 4 |
| Q18 | - |  |  | SI | Comment 5 |
| Q19 | - |  |  | SI | Comment 6 |
| Q20 | - |  |  | SI | Comment 7 |
| Q21 | - |  |  | SI | If the answers are all NO to Questions 2-7, consid... |
| Q22 | - |  |  | SI | If only Questions 2, 3, and/or 4 is checked as YES... |
| Q23 | - |  |  | SI | Stop, make patient NPO (Nil Per Oral) and obtain o... |
| Q24 | - |  |  | SI | Stop, make patient NPO (Nil Per Oral) and obtain o... |
| Q25 | - |  |  | SI | Modified Massey Bedside Swallowing Screen is used ... |
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