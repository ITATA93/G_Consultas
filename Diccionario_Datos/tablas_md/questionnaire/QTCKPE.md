# questionnaire.QTCKPE

> Knee - Physical Examination

**Schema:** questionnaire
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Knee - Physical Examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Knee examination - laterality |
| Q04 | varchar |  |  | SI | Left hip |
| Q05 | varchar |  |  | SI | Right hip |
| Q06 | varchar |  |  | SI | Hip examination details |
| Q07 | varchar |  |  | SI | Knee swelling |
| Q08 | varchar |  |  | SI | Muscle atrophy |
| Q09 | varchar |  |  | SI | Deformity	 |
| Q10 | numeric |  |  | SI | Q-Angle |
| Q11 | varchar |  |  | SI | degrees |
| Q12 | varchar |  |  | SI | Knee tenderness |
| Q14 | numeric |  |  | SI | Pain elicited at extension of |
| Q15 | varchar |  |  | SI | degrees |
| Q16 | numeric |  |  | SI | Pain elicited at flexion of |
| Q17 | varchar |  |  | SI | degrees |
| Q18 | varchar |  |  | SI | Physical finding details |
| Q19 | varchar |  |  | SI | Wound healing well |
| Q20 | varchar |  |  | SI | Instability |
| Q21 | varchar |  |  | SI | Patella examination |
| Q22 | date |  |  | SI | Date |
| Q23 | time |  |  | SI | Time |
| Q24 | varchar |  |  | SI | Knee examination - laterality |
| Q25 | varchar |  |  | SI | Left hip examination |
| Q26 | varchar |  |  | SI | Right hip examination |
| Q27 | varchar |  |  | SI | Additional hip examination details |
| Q28 | varchar |  |  | SI | Knee Swelling |
| Q29 | varchar |  |  | SI | Left knee swelling |
| Q30 | varchar |  |  | SI | Right knee swelling |
| Q31 | varchar |  |  | SI | Muscle Atrophy |
| Q32 | varchar |  |  | SI | Left knee muscle atrophy |
| Q33 | varchar |  |  | SI | Right knee muscle atrophy |
| Q34 | varchar |  |  | SI | Deformity |
| Q35 | varchar |  |  | SI | Left knee deformity |
| Q36 | numeric |  |  | SI | Left knee Q-Angle  |
| Q37 | varchar |  |  | SI | degrees |
| Q38 | varchar |  |  | SI | Right knee deformity |
| Q39 | numeric |  |  | SI | Right knee Q-Angle |
| Q40 | varchar |  |  | SI | Knee Tenderness |
| Q41 | varchar |  |  | SI | Left knee tenderness |
| Q42 | varchar |  |  | SI | Right knee tenderness |
| Q43 | varchar |  |  | SI | Knee Range of Motion (ROM) |
| Q44 | varchar |  |  | SI | Knee Range Of Motion (ROM) |
| Q44ObsDR | varchar |  | FK | SI | Knee Range Of Motion (ROM) DR |
| Q45 | numeric |  |  | SI | Left knee pain elicited at extension of |
| Q46 | varchar |  |  | SI | degrees |
| Q47 | numeric |  |  | SI | Left knee pain elicited at flexion of |
| Q48 | varchar |  |  | SI | degrees |
| Q49 | numeric |  |  | SI | Right knee pain elicited at extension of |
| Q50 | varchar |  |  | SI | degrees |
| Q51 | numeric |  |  | SI | Right knee pain elicited at flexion of |
| Q52 | varchar |  |  | SI | degrees |
| Q53 | varchar |  |  | SI | Physical Finding |
| Q54 | varchar |  |  | SI | Physical finding details |
| Q55 | varchar |  |  | SI | Wound healing well |
| Q56 | varchar |  |  | SI | Instability |
| Q57 | varchar |  |  | SI | Left knee instability |
| Q58 | varchar |  |  | SI | Right knee instability |
| Q59 | varchar |  |  | SI | Patella Examination |
| Q60 | varchar |  |  | SI | Left knee patella examination |
| Q61 | varchar |  |  | SI | Right knee patella examination |
| Q62 | varchar |  |  | SI | Degrees |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*