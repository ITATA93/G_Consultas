# SQLUser.PAC_BabyFeedingType

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BABYFEED_RowId | bigint | PK |  | NO | - |
| BABYFEED_Code | varchar |  |  | NO | Code |
| BABYFEED_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BABYFEED_CreatedDate | date |  |  | SI | Created Date |
| BABYFEED_CreatedTime | time |  |  | SI | Created Time |
| BABYFEED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BABYFEED_DateFrom | date |  |  | SI | Date From |
| BABYFEED_DateTo | date |  |  | SI | Date To |
| BABYFEED_Desc | varchar |  |  | NO | Description |
| BABYFEED_Owner | varchar |  |  | SI | Owner |
| BABYFEED_UpdatedDate | date |  |  | SI | Updated Date |
| BABYFEED_UpdatedTime | time |  |  | SI | Updated Time |
| BABYFEED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Variance |
| Q04 | - |  |  | SI | Observations stable and within acceptable limits |
| Q05 | - |  |  | SI | Variance |
| Q06 | - |  |  | SI | 12 lead electrocardiogram performed post procedure... |
| Q07 | - |  |  | SI | Variance |
| Q08 | - |  |  | SI | Cardiac rhythmn monitored and all arrhythmias repo... |
| Q09 | - |  |  | SI | Variance |
| Q10 | - |  |  | SI | Neurovascular observations within normal parameter... |
| Q11 | - |  |  | SI | Variance |
| Q12 | - |  |  | SI | Medications administered as prescribed |
| Q13 | - |  |  | SI | Variance |
| Q14 | - |  |  | SI | Insertion site checked and free of haematoma and o... |
| Q15 | - |  |  | SI | Variance |
| Q16 | - |  |  | SI | Intravascular fluid therapy administered as prescr... |
| Q17 | - |  |  | SI | Variance |
| Q18 | - |  |  | SI | Patient has voided post procedure |
| Q19 | - |  |  | SI | Variance |
| Q20 | - |  |  | SI | Patient tolerated oral diet as appropriate |
| Q21 | - |  |  | SI | Variance |
| Q22 | - |  |  | SI | Post-procedure positioning as per guidelines |
| Q23 | - |  |  | SI | Variance |
| Q24 | - |  |  | SI | Dummy1 |
| Q25 | - |  |  | SI | Variance |
| Q26 | - |  |  | SI | Explained sheath removal to patient (if sheath pre... |
| Q27 | - |  |  | SI | Variance |
| Q28 | - |  |  | SI | Completed cardiac education |
| Q29 | - |  |  | SI | Variance |
| Q30 | - |  |  | SI | Post-Procedure Positioning |
| Q31 | - |  |  | SI | Femoral approach: lay flat for first hour then rai... |
| Q32 | - |  |  | SI | Radial approach: patient can sit upon return |
| Q33 | - |  |  | SI | Variance |
| Q34 | - |  |  | SI | Variance |
| Q35 | - |  |  | SI | Variance |
| Q36 | - |  |  | SI | Variance |
| Q37 | - |  |  | SI | Variance |
| Q38 | - |  |  | SI | Variance |
| Q39 | - |  |  | SI | Variance |
| Q40 | - |  |  | SI | Variance |
| Q41 | - |  |  | SI | Variance |
| Q42 | - |  |  | SI | Variance |
| Q43 | - |  |  | SI | Variance |
| Q44 | - |  |  | SI | Variance |
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