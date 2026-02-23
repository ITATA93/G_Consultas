# SQLUser.CT_WorkShif

**Schema:** SQLUser
**Columnas:** 136
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTWS_RowId | bigint | PK |  | NO | - |
| CTWS_Code | varchar |  |  | NO | Shift Code |
| CTWS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTWS_CreatedDate | date |  |  | SI | Created Date |
| CTWS_CreatedTime | time |  |  | SI | Created Time |
| CTWS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTWS_DateFrom | date |  |  | SI | DateFrom |
| CTWS_DateTo | date |  |  | SI | DateTo |
| CTWS_Desc | varchar |  |  | NO | Shift Description |
| CTWS_EndTime | time |  |  | NO | Shift End Time |
| CTWS_Owner | varchar |  |  | SI | Owner |
| CTWS_StartTime | time |  |  | NO | Shift Start Time |
| CTWS_UpdatedDate | date |  |  | SI | Updated Date |
| CTWS_UpdatedTime | time |  |  | SI | Updated Time |
| CTWS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Burn type |
| Q04 | - |  |  | SI | Other burn type |
| Q05 | - |  |  | SI | Thermal burns |
| Q06 | - |  |  | SI | Other thermal burns |
| Q07 | - |  |  | SI | 0 - 1 year |
| Q08 | - |  |  | SI | 9.5 |
| Q09 | - |  |  | SI | 2.75 |
| Q10 | - |  |  | SI | 2.5 |
| Q11 | - |  |  | SI | 1 - 4 years |
| Q12 | - |  |  | SI | 8.5 |
| Q13 | - |  |  | SI | 3.25 |
| Q14 | - |  |  | SI | 2.5 |
| Q15 | - |  |  | SI | 5 - 9 years |
| Q16 | - |  |  | SI | 6.5 |
| Q17 | - |  |  | SI | 4 |
| Q18 | - |  |  | SI | 2.75 |
| Q19 | - |  |  | SI | 10 - 14 years |
| Q20 | - |  |  | SI | 5.5 |
| Q21 | - |  |  | SI | 4.5 |
| Q22 | - |  |  | SI | 3 |
| Q23 | - |  |  | SI | 15 - 18 years |
| Q24 | - |  |  | SI | 4.5 |
| Q25 | - |  |  | SI | 4.5 |
| Q26 | - |  |  | SI | 3.25 |
| Q27 | - |  |  | SI | Adults |
| Q28 | - |  |  | SI | 3.5 |
| Q29 | - |  |  | SI | 4.75 |
| Q30 | - |  |  | SI | 3.5 |
| Q31 | - |  |  | SI | Area % for all ages |
| Q32 | - |  |  | SI | Neck = 1 |
| Q33 | - |  |  | SI | Anterior Trunk = 13 |
| Q34 | - |  |  | SI | One anterior upper arm = 2 |
| Q35 | - |  |  | SI | One anterior lower arm = 1.5 |
| Q36 | - |  |  | SI | One anterior hand = 1.5 |
| Q37 | - |  |  | SI | One posterior upper arm = 2 |
| Q38 | - |  |  | SI | One posterior lower arm = 1.5 |
| Q39 | - |  |  | SI | One posterior hand = 1.5 |
| Q40 | - |  |  | SI | Buttock = 2.5 |
| Q41 | - |  |  | SI | Genitalia = 1 |
| Q42 | - |  |  | SI | Adult body map |
| Q43 | - |  |  | SI | Pediatric body map |
| Q44 | - |  |  | SI | Legend for Annotation |
| Q45 | - |  |  | SI | Dummy 1 = Superficial Burn |
| Q46 | - |  |  | SI | Dummy 2 = Deep Burn |
| Q47 | - |  |  | SI | Please confirm that you have completed the Lund an... |
| Q48 | - |  |  | SI | Injury to Area % |
| Q49 | - |  |  | SI | Head (A) |
| Q50 | - |  |  | SI | Neck |
| Q51 | - |  |  | SI | Anterior Trunk |
| Q52 | - |  |  | SI | Posterior Trunk |
| Q53 | - |  |  | SI | Right Arm |
| Q54 | - |  |  | SI | Left Arm |
| Q55 | - |  |  | SI | Buttocks |
| Q56 | - |  |  | SI | Genitalia |
| Q57 | - |  |  | SI | Right Upper Leg (B) |
| Q58 | - |  |  | SI | Right Lower Leg (C) |
| Q59 | - |  |  | SI | Left Upper Leg (B) |
| Q60 | - |  |  | SI | Left Lower Leg (C) |
| Q61 | - |  |  | SI | Total Burn Surface Area |
| Q62 | - |  |  | SI | Notes |
| Q63 | - |  |  | SI | A = 1/2 of head |
| Q64 | - |  |  | SI | B = 1/2 of one thigh |
| Q65 | - |  |  | SI | C = 1/2 of one lower leg |
| Q66 | - |  |  | SI | Area % by age |
| Q67 | - |  |  | SI | Posterior Trunk = 13 |
| Q68 | - |  |  | SI | Adult schema |
| Q69 | - |  |  | SI | Child schema |
| Q70 | - |  |  | SI | Head (A) |
| Q71 | - |  |  | SI | Neck |
| Q72 | - |  |  | SI | Anterior Trunk |
| Q73 | - |  |  | SI | Posterior Trunk |
| Q74 | - |  |  | SI | Right Arm |
| Q75 | - |  |  | SI | Left Arm |
| Q76 | - |  |  | SI | Buttocks |
| Q77 | - |  |  | SI | Genitalia |
| Q78 | - |  |  | SI | Right Upper Leg (B) |
| Q79 | - |  |  | SI | Right Lower Leg (C) |
| Q80 | - |  |  | SI | Left Upper Leg (B) |
| Q81 | - |  |  | SI | Left Lower Leg (C) |
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