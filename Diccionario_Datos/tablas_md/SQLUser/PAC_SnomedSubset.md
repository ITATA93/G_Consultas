# SQLUser.PAC_SnomedSubset

**Schema:** SQLUser
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNOSS_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Turning over left side |
| Q04 | - |  |  | SI | Turning over right side |
| Q05 | - |  |  | SI | Lying to sitting |
| Q06 | - |  |  | SI | Sitting balance (assessor to time patient for 10 s... |
| Q07 | - |  |  | SI | Sitting from standing (takes less than 15 secs) |
| Q08 | - |  |  | SI | Standing (assessor to time patient for 10 secs) |
| Q09 | - |  |  | SI | Transfers (assessor to place chair on unaffected s... |
| Q10 | - |  |  | SI | Walking indoors (walk 10 meters in usual way) |
| Q11 | - |  |  | SI | Stairs (climb up and down in usual way) |
| Q12 | - |  |  | SI | Score |
| Q13 | - |  |  | SI | Comments |
| Q14 | - |  |  | SI | Score |
| Q15 | - |  |  | SI | Classification |
| Q16 | - |  |  | SI | 0: |
| Q17 | - |  |  | SI | 1: |
| Q18 | - |  |  | SI | 2: |
| Q19 | - |  |  | SI | 3: |
| Q20 | - |  |  | SI | 4: |
| Q21 | - |  |  | SI | 5: |
| Q22 | - |  |  | SI | Unable to perform |
| Q23 | - |  |  | SI | Assistance of two people |
| Q24 | - |  |  | SI | Assistance of one person |
| Q25 | - |  |  | SI | Requires supervision or verbal instruction |
| Q26 | - |  |  | SI | Requires an aid or appliance |
| Q27 | - |  |  | SI | Independent |
| Q28 | - |  |  | SI | The Physiotherapy & Occupational Therapy Assessmen... |
| Q29 | - |  |  | SI | Range = 0 - 45. The higher the patient score the g... |
| Q30 | - |  |  | SI | Range = 0 - 45. The higher the patient score the g... |
| Q31 | - |  |  | SI | Turning Over - Patient turning from back onto side |
| Q32 | - |  |  | SI | Lying to sitting - Patient moving from lying to si... |
| Q33 | - |  |  | SI | Sitting balance - Patient sitting on edge of bed |
| Q34 | - |  |  | SI | Sitting from Standing - Patient stands from chair |
| Q35 | - |  |  | SI | Standing - Patient remains standing |
| Q36 | - |  |  | SI | Transfers - Patient moves from bed to chair and ba... |
| Q37 | - |  |  | SI | Walking - Patient walks for 10 meters |
| Q38 | - |  |  | SI | Stairs - Patient climbs up and down 1 flight of st... |
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
| SNOSS_ContextID | varchar |  |  | SI | ContextID |
| SNOSS_CreatedDate | date |  |  | SI | Created Date |
| SNOSS_CreatedTime | time |  |  | SI | Created Time |
| SNOSS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNOSS_Language_DR | bigint |  | FK | SI | Des Ref Language |
| SNOSS_RealmID | varchar |  |  | SI | RealmID |
| SNOSS_SubsetID | varchar |  |  | SI | SubsetID |
| SNOSS_SubsetName | varchar |  |  | SI | SubsetName |
| SNOSS_SubsetOriginalID | varchar |  |  | SI | SubsetOriginalID |
| SNOSS_SubsetType | varchar |  |  | SI | SubsetType |
| SNOSS_SubsetVersion | varchar |  |  | SI | SubsetVersion |
| SNOSS_UpdatedDate | date |  |  | SI | Updated Date |
| SNOSS_UpdatedTime | time |  |  | SI | Updated Time |
| SNOSS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*