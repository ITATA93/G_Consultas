# SQLUser.PAC_OperTimeRange

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OPERTR_RowId | bigint | PK |  | NO | - |
| ChildQ24DR | - |  |  | SI | Child Reference: Goals |
| OPERTR_Code | varchar |  |  | NO | Code |
| OPERTR_CreatedDate | date |  |  | SI | Created Date |
| OPERTR_CreatedTime | time |  |  | SI | Created Time |
| OPERTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OPERTR_Desc | varchar |  |  | NO | Description |
| OPERTR_UpdatedDate | date |  |  | SI | Updated Date |
| OPERTR_UpdatedTime | time |  |  | SI | Updated Time |
| OPERTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Type of Assessment |
| Q02 | - |  |  | SI | Does patient have any red flags? |
| Q03 | - |  |  | SI | Level of Procedure |
| Q04 | - |  |  | SI | Type of Procedure |
| Q05 | - |  |  | SI | Special Precautions / Indications |
| Q06 | - |  |  | SI | Recommended Spinal Support |
| Q07 | - |  |  | SI | Prior Level of Function |
| Q08 | - |  |  | SI | Home / Office Setup |
| Q09 | - |  |  | SI | Has the patient attended regular physiotherapy ses... |
| Q10 | - |  |  | SI | Kind Of Physiotherapy Treatment |
| Q11 | - |  |  | SI | Indicate the Areas on Diagram (Surgery Site, Pain,... |
| Q11A | - |  |  | SI | Indicate the Areas on Diagram (Surgery Site, Pain,... |
| Q12 | - |  |  | SI | Pain Score |
| Q12ObsDR | - |  |  | SI | Pain Score DR |
| Q13 | - |  |  | SI | Type of Pain |
| Q13ObsDR | - |  |  | SI | Type of Pain DR |
| Q14 | - |  |  | SI | Do any other affected areas (other than Surgical) ... |
| Q14A | - |  |  | SI | Area |
| Q15 | - |  |  | SI | Drain placed on surgery site? |
| Q16 | - |  |  | SI | Complain of Intraoperative Position? |
| Q17 | - |  |  | SI | Area |
| Q19 | - |  |  | SI | Sensory Testing |
| Q20 | - |  |  | SI | Type of Sensory Test |
| Q21 | - |  |  | SI | Comparison left to right in %= ? |
| Q22 | - |  |  | SI | Mark Affected Dermatomes |
| Q22A | - |  |  | SI | Mark Affected Dermatomes |
| Q23 | - |  |  | SI | Any Anal Sensation |
| Q23ObsDR | - |  |  | SI | Any Anal Sensation DR |
| Q25 | - |  |  | SI | Plan of Intervention |
| Q26 | - |  |  | SI | Referral to |
| Q27 | - |  |  | SI | Checklist |
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