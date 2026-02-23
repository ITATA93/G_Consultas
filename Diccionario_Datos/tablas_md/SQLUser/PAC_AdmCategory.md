# SQLUser.PAC_AdmCategory

**Schema:** SQLUser
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADMCAT_RowId | bigint | PK |  | NO | - |
| ADMCAT_Code | varchar |  |  | NO | Code |
| ADMCAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADMCAT_CreatedDate | date |  |  | SI | Created Date |
| ADMCAT_CreatedTime | time |  |  | SI | Created Time |
| ADMCAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADMCAT_DateFrom | date |  |  | SI | Date From |
| ADMCAT_DateTo | date |  |  | SI | Date To |
| ADMCAT_Desc | varchar |  |  | NO | Description |
| ADMCAT_Owner | varchar |  |  | SI | Owner |
| ADMCAT_Subregion_DR | bigint |  | FK | SI | Subregion  |
| ADMCAT_UpdatedDate | date |  |  | SI | Updated Date |
| ADMCAT_UpdatedTime | time |  |  | SI | Updated Time |
| ADMCAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | I feel tense or 'wound up' (A)	 |
| Q02 | - |  |  | SI | I feel as if I am slowed down (D)	 |
| Q03 | - |  |  | SI | I still enjoy the things I used to enjoy (D)	 |
| Q04 | - |  |  | SI | I get a sort of frightening feeling like 'butterfl... |
| Q05 | - |  |  | SI | I get a sort of frightened feeling as if something... |
| Q06 | - |  |  | SI | I have lost interest in my appearance (D)	 |
| Q07 | - |  |  | SI | I can laugh and see the funny side of things (D)	 |
| Q08 | - |  |  | SI | I feel restless as if I have to be on the move (A)... |
| Q09 | - |  |  | SI | Worrying thoughts go through my mind (A)	 |
| Q10 | - |  |  | SI | I look forward with enjoyment to things (D)	 |
| Q11 | - |  |  | SI | I feel cheerful (D)	 |
| Q12 | - |  |  | SI | I get sudden feelings of panic (A)	 |
| Q13 | - |  |  | SI | I can sit at ease and feel relaxed (A)	 |
| Q14 | - |  |  | SI | I can enjoy a good book or radio or TV programme (... |
| Q15 | - |  |  | SI |  Additional comments	 |
| Q16 | - |  |  | SI | Total score (Depression)	 |
| Q17 | - |  |  | SI | Total score (Anxiety)	 |
| Q18 | - |  |  | SI | 0 - 7: Normal |
| Q19 | - |  |  | SI | 8 - 10: Borderline abnormal |
| Q20 | - |  |  | SI | 11 - 21: Abnormal	 |
| Q21 | - |  |  | SI | Collects the required data to accurately calculate... |
| Q22 | - |  |  | SI | Questions suffixed with (A) relate to anxiety scor... |
| Q23 | - |  |  | SI | Score |
| Q24 | - |  |  | SI | Classification |
| Q25 | - |  |  | SI | 0 - 7: |
| Q26 | - |  |  | SI | Normal |
| Q27 | - |  |  | SI | 8 - 10: |
| Q28 | - |  |  | SI | Borderline abnormal |
| Q29 | - |  |  | SI | 11 - 21: |
| Q30 | - |  |  | SI | Abnormal |
| Q31 | - |  |  | SI | Hospital Anxiety and Depression Scale collects the... |
| Q32 | - |  |  | SI | Total score (Depression) |
| Q33 | - |  |  | SI | Total score (Anxiety) |
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