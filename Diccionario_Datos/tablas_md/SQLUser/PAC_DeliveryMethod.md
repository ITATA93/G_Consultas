# SQLUser.PAC_DeliveryMethod

**Schema:** SQLUser
**Columnas:** 117
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DLMTH_RowId | bigint | PK |  | NO | - |
| DLMTH_Code | varchar |  |  | NO | Delivery Mode Code |
| DLMTH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DLMTH_CreatedDate | date |  |  | SI | Created Date |
| DLMTH_CreatedTime | time |  |  | SI | Created Time |
| DLMTH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DLMTH_DateFrom | date |  |  | SI | DateFrom |
| DLMTH_DateTo | date |  |  | SI | Date To |
| DLMTH_Desc | varchar |  |  | NO | Delivery Mode Description |
| DLMTH_NationalCode | varchar |  |  | SI | NationalCode |
| DLMTH_Owner | varchar |  |  | SI | Owner |
| DLMTH_RcFlag | varchar |  |  | SI | Archived Flag |
| DLMTH_UpdatedDate | date |  |  | SI | Updated Date |
| DLMTH_UpdatedTime | time |  |  | SI | Updated Time |
| DLMTH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Knee examination - laterality |
| Q04 | - |  |  | SI | Left hip |
| Q05 | - |  |  | SI | Right hip |
| Q06 | - |  |  | SI | Hip examination details |
| Q07 | - |  |  | SI | Knee swelling |
| Q08 | - |  |  | SI | Muscle atrophy |
| Q09 | - |  |  | SI | Deformity	 |
| Q10 | - |  |  | SI | Q-Angle |
| Q11 | - |  |  | SI | degrees |
| Q12 | - |  |  | SI | Knee tenderness |
| Q14 | - |  |  | SI | Pain elicited at extension of |
| Q15 | - |  |  | SI | degrees |
| Q16 | - |  |  | SI | Pain elicited at flexion of |
| Q17 | - |  |  | SI | degrees |
| Q18 | - |  |  | SI | Physical finding details |
| Q19 | - |  |  | SI | Wound healing well |
| Q20 | - |  |  | SI | Instability |
| Q21 | - |  |  | SI | Patella examination |
| Q22 | - |  |  | SI | Date |
| Q23 | - |  |  | SI | Time |
| Q24 | - |  |  | SI | Knee examination - laterality |
| Q25 | - |  |  | SI | Left hip examination |
| Q26 | - |  |  | SI | Right hip examination |
| Q27 | - |  |  | SI | Additional hip examination details |
| Q28 | - |  |  | SI | Knee Swelling |
| Q29 | - |  |  | SI | Left knee swelling |
| Q30 | - |  |  | SI | Right knee swelling |
| Q31 | - |  |  | SI | Muscle Atrophy |
| Q32 | - |  |  | SI | Left knee muscle atrophy |
| Q33 | - |  |  | SI | Right knee muscle atrophy |
| Q34 | - |  |  | SI | Deformity |
| Q35 | - |  |  | SI | Left knee deformity |
| Q36 | - |  |  | SI | Left knee Q-Angle |
| Q37 | - |  |  | SI | degrees |
| Q38 | - |  |  | SI | Right knee deformity |
| Q39 | - |  |  | SI | Right knee Q-Angle |
| Q40 | - |  |  | SI | Knee Tenderness |
| Q41 | - |  |  | SI | Left knee tenderness |
| Q42 | - |  |  | SI | Right knee tenderness |
| Q43 | - |  |  | SI | Knee Range of Motion (ROM) |
| Q44 | - |  |  | SI | Knee Range Of Motion (ROM) |
| Q44ObsDR | - |  |  | SI | Knee Range Of Motion (ROM) DR |
| Q45 | - |  |  | SI | Left knee pain elicited at extension of |
| Q46 | - |  |  | SI | degrees |
| Q47 | - |  |  | SI | Left knee pain elicited at flexion of |
| Q48 | - |  |  | SI | degrees |
| Q49 | - |  |  | SI | Right knee pain elicited at extension of |
| Q50 | - |  |  | SI | degrees |
| Q51 | - |  |  | SI | Right knee pain elicited at flexion of |
| Q52 | - |  |  | SI | degrees |
| Q53 | - |  |  | SI | Physical Finding |
| Q54 | - |  |  | SI | Physical finding details |
| Q55 | - |  |  | SI | Wound healing well |
| Q56 | - |  |  | SI | Instability |
| Q57 | - |  |  | SI | Left knee instability |
| Q58 | - |  |  | SI | Right knee instability |
| Q59 | - |  |  | SI | Patella Examination |
| Q60 | - |  |  | SI | Left knee patella examination |
| Q61 | - |  |  | SI | Right knee patella examination |
| Q62 | - |  |  | SI | Degrees |
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