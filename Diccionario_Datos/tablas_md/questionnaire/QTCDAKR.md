# questionnaire.QTCDAKR

> Dermatology Actinic Keratosis Review

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dermatology Actinic Keratosis Review

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Previous skin cancer |
| Q04 | varchar |  |  | SI | Type of skin cancer |
| Q05 | varchar |  |  | SI | Please specify |
| Q06 | varchar |  |  | SI | Family history of melanoma |
| Q07 | varchar |  |  | SI | Please ensure this is documented in the patient's ... |
| Q08 | varchar |  |  | SI | Additional risk factors |
| Q09 | varchar |  |  | SI | Other risks |
| Q10 | varchar |  |  | SI | Fitzpatrick skin type |
| Q10ObsDR | varchar |  | FK | SI | Fitzpatrick skin type DR |
| Q11 | varchar |  |  | SI | Full skin surveillance examination |
| Q12 | varchar |  |  | SI | Patient-directed examination |
| Q13 | varchar |  |  | SI | Scalp |
| Q14 | varchar |  |  | SI | Scalp notes |
| Q15 | varchar |  |  | SI | Face |
| Q16 | varchar |  |  | SI | Face notes |
| Q17 | varchar |  |  | SI | Trunk |
| Q18 | varchar |  |  | SI | Trunk notes |
| Q19 | varchar |  |  | SI | Arms / Hands |
| Q20 | varchar |  |  | SI | Arms / Hands notes |
| Q21 | varchar |  |  | SI | Legs / Feet |
| Q22 | varchar |  |  | SI | Legs / Feet notes |
| Q23 | varchar |  |  | SI | Lymph Node Basins Examined |
| Q24 | varchar |  |  | SI | Cervical nodes |
| Q25 | varchar |  |  | SI | Findings |
| Q26 | varchar |  |  | SI | Axillary |
| Q27 | varchar |  |  | SI | Findings |
| Q28 | varchar |  |  | SI | Inguinal |
| Q29 | varchar |  |  | SI | Findings |
| Q30 | varchar |  |  | SI | Abdominal palpation |
| Q31 | varchar |  |  | SI | Findings |
| Q32 | varchar |  |  | SI | Other findings / Issues |
| Q33 | varchar |  |  | SI | Education given about sun protection / Sunscreen u... |
| Q34 | varchar |  |  | SI | Education details |
| Q35 | varchar |  |  | SI | Breslow thickness (mm) |
| Q36 | varchar |  |  | SI | Type of skin cancer |
| Q37 | varchar |  |  | SI | Previous skin cancer |
| Q38 | varchar |  |  | SI | Family history of melanoma |
| Q39 | varchar |  |  | SI | Prevention |
| Q40 | varchar |  |  | SI | Other prevention |
| Q41 | varchar |  |  | SI | Fitzpatrick skin type |
| Q41ObsDR | varchar |  | FK | SI | Fitzpatrick skin type DR |
| Q42 | varchar |  |  | SI | Type of examination |
| Q43 | varchar |  |  | SI | Solar keratoses notes |
| Q44 | varchar |  |  | SI | Findings |
| Q45 | varchar |  |  | SI | Findings |
| Q46 | varchar |  |  | SI | Findings |
| Q47 | varchar |  |  | SI | Findings |
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