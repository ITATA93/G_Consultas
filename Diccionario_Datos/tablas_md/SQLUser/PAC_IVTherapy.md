# SQLUser.PAC_IVTherapy

**Schema:** SQLUser
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IVT_RowId | bigint | PK |  | NO | - |
| ChildQ31DR | - |  |  | SI | Child Reference: Pain localization |
| IVT_Code | varchar |  |  | NO | Code |
| IVT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IVT_CreatedDate | date |  |  | SI | Created Date |
| IVT_CreatedTime | time |  |  | SI | Created Time |
| IVT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IVT_DateFrom | date |  |  | SI | Date From |
| IVT_DateTo | date |  |  | SI | Date to |
| IVT_Desc | varchar |  |  | NO | Description |
| IVT_Owner | varchar |  |  | SI | Owner |
| IVT_UpdatedDate | date |  |  | SI | Updated Date |
| IVT_UpdatedTime | time |  |  | SI | Updated Time |
| IVT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Sensory (S) |
| Q02 | - |  |  | SI | 1 |
| Q03 | - |  |  | SI | 2 |
| Q04 | - |  |  | SI | 3 |
| Q05 | - |  |  | SI | 4 |
| Q06 | - |  |  | SI | 5 |
| Q07 | - |  |  | SI | 6 |
| Q08 | - |  |  | SI | 7 |
| Q09 | - |  |  | SI | 8 |
| Q10 | - |  |  | SI | 9 |
| Q11 | - |  |  | SI | 10 |
| Q12 | - |  |  | SI | Affective (A) |
| Q13 | - |  |  | SI | 11 |
| Q14 | - |  |  | SI | 12 |
| Q15 | - |  |  | SI | 13 |
| Q16 | - |  |  | SI | 14 |
| Q17 | - |  |  | SI | 15 |
| Q18 | - |  |  | SI | Evaluative (E) |
| Q19 | - |  |  | SI | 16 |
| Q20 | - |  |  | SI | 17 |
| Q21 | - |  |  | SI | 18 |
| Q22 | - |  |  | SI | 19 |
| Q23 | - |  |  | SI | 20 |
| Q24 | - |  |  | SI | (S) Score |
| Q25 | - |  |  | SI | (A) Score |
| Q26 | - |  |  | SI | (E) Score |
| Q27 | - |  |  | SI | (M) Score |
| Q28 | - |  |  | SI | Score ranges from 0 (no pain) to 78 (severe pain) |
| Q29 | - |  |  | SI | Present Pain Intensity (PPI) |
| Q30 | - |  |  | SI | Comments |
| Q32 | - |  |  | SI | Repeat this section as many times as necessary |
| Q33 | - |  |  | SI | Accompanying symptoms |
| Q34 | - |  |  | SI | Comments |
| Q35 | - |  |  | SI | Sleep |
| Q36 | - |  |  | SI | Comments |
| Q37 | - |  |  | SI | Food intake |
| Q38 | - |  |  | SI | Comments |
| Q39 | - |  |  | SI | Activity |
| Q40 | - |  |  | SI | Comments |
| Q41 | - |  |  | SI | What Does Your Pain Feel Like? |
| Q42 | - |  |  | SI | Some of the words describe your present pain. Circ... |
| Q43 | - |  |  | SI | The McGill Pain Questionnaire (MPQ) can be used to... |
| Q44 | - |  |  | SI | Score Interpretation |
| Q45 | - |  |  | SI | Score ranges from 0 (no pain) to 78 (severe pain) |
| Q46 | - |  |  | SI | Score ranges from 0 (no pain) to 78 (severe pain) |
| Q47 | - |  |  | SI | Miscellaneous (M) |
| Q48 | - |  |  | SI | Date |
| Q49 | - |  |  | SI | Time |
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