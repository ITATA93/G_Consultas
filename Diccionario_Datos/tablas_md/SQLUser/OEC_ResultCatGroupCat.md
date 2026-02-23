# SQLUser.OEC_ResultCatGroupCat

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CAT_ParRef | bigint | PK |  | NO | OEC_ResultCatGroup Parent Reference |
| CAT_Childsub | double |  |  | NO | Childsub |
| CAT_Code | varchar |  |  | NO | Code |
| CAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CAT_CreatedDate | date |  |  | SI | Created Date |
| CAT_CreatedTime | time |  |  | SI | Created Time |
| CAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CAT_DateFrom | date |  |  | SI | Date From |
| CAT_DateTo | date |  |  | SI | Date To |
| CAT_Desc | varchar |  |  | NO | Description |
| CAT_RowId | varchar |  |  | NO | - |
| CAT_UpdatedDate | date |  |  | SI | Updated Date |
| CAT_UpdatedTime | time |  |  | SI | Updated Time |
| CAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q04 | - |  |  | SI | The Richmond Agitation Sedation Scale is a ten-cla... |
| Q05 | - |  |  | SI | 1. Observe Patient: Patient is alert, restless or ... |
| Q05S | - |  |  | SI | Score 0 to +4 |
| Q07 | - |  |  | SI | Verbal Stimulation |
| Q08 | - |  |  | SI | 2. If not alert, state patient’s name and ask to o... |
| Q08A | - |  |  | SI | • Patient awakens with sustained eye opening and e... |
| Q08AS | - |  |  | SI | Score -1 |
| Q08B | - |  |  | SI | • Patient awakens with eye opening and eye contact... |
| Q08BS | - |  |  | SI | Score -2 |
| Q08C | - |  |  | SI | • Patient has any movement in response to voice bu... |
| Q08CS | - |  |  | SI | Score -3 |
| Q09 | - |  |  | SI | 3. When no response to verbal stimulation, physica... |
| Q09A | - |  |  | SI | • Patient has any movement to physical stimulation |
| Q09AS | - |  |  | SI | Score -4 |
| Q09B | - |  |  | SI | • Patient has no response to any stimulation |
| Q09BS | - |  |  | SI | Score -5 |
| Q10 | - |  |  | SI | Physical Stimulation |
| Q13 | - |  |  | SI | Assess Anxiety / Agitation / Quality of Sedation |
| Q19 | - |  |  | SI | Date |
| Q20 | - |  |  | SI | Time |
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