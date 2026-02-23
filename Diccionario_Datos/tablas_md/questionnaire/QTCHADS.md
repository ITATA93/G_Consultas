# questionnaire.QTCHADS

> Hospital Anxiety and Depression Scale

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hospital Anxiety and Depression Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | I feel tense or 'wound up' (A)	 |
| Q02 | varchar |  |  | SI | I feel as if I am slowed down (D)	 |
| Q03 | varchar |  |  | SI | I still enjoy the things I used to enjoy (D)	 |
| Q04 | varchar |  |  | SI | I get a sort of frightening feeling like 'butterfl... |
| Q05 | varchar |  |  | SI | I get a sort of frightened feeling as if something... |
| Q06 | varchar |  |  | SI | I have lost interest in my appearance (D)	 |
| Q07 | varchar |  |  | SI | I can laugh and see the funny side of things (D)	 |
| Q08 | varchar |  |  | SI | I feel restless as if I have to be on the move (A)... |
| Q09 | varchar |  |  | SI | Worrying thoughts go through my mind (A)	 |
| Q10 | varchar |  |  | SI | I look forward with enjoyment to things (D)	 |
| Q11 | varchar |  |  | SI | I feel cheerful (D)	 |
| Q12 | varchar |  |  | SI | I get sudden feelings of panic (A)	 |
| Q13 | varchar |  |  | SI | I can sit at ease and feel relaxed (A)	 |
| Q14 | varchar |  |  | SI | I can enjoy a good book or radio or TV programme (... |
| Q15 | varchar |  |  | SI |  Additional comments	 |
| Q16 | varchar |  |  | SI | Total score (Depression)	 |
| Q17 | varchar |  |  | SI | Total score (Anxiety)	 |
| Q18 | varchar |  |  | SI | 0 - 7: Normal |
| Q19 | varchar |  |  | SI | 8 - 10: Borderline abnormal |
| Q20 | varchar |  |  | SI | 11 - 21: Abnormal	 |
| Q21 | varchar |  |  | SI | Collects the required data to accurately calculate... |
| Q22 | varchar |  |  | SI | Questions suffixed with (A) relate to anxiety scor... |
| Q23 | varchar |  |  | SI | Score |
| Q24 | varchar |  |  | SI | Classification |
| Q25 | varchar |  |  | SI | 0 - 7: |
| Q26 | varchar |  |  | SI | Normal |
| Q27 | varchar |  |  | SI | 8 - 10: |
| Q28 | varchar |  |  | SI | Borderline abnormal |
| Q29 | varchar |  |  | SI | 11 - 21: |
| Q30 | varchar |  |  | SI | Abnormal |
| Q31 | varchar |  |  | SI | Hospital Anxiety and Depression Scale collects the... |
| Q32 | varchar |  |  | SI | Total score (Depression) |
| Q33 | varchar |  |  | SI | Total score (Anxiety) |
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