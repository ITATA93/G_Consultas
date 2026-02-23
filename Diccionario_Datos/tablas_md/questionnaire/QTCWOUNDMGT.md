# questionnaire.QTCWOUNDMGT

> Wound Assessment and Care

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Assessment and Care

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | date |  |  | SI | Date wound identified |
| Q04 | varchar |  |  | SI | Incident report number |
| Q05 | numeric |  |  | SI | Wound number |
| Q06 | varchar |  |  | SI | Please complete a separate form for each wound ide... |
| Q07 | date |  |  | SI | Expected date to heal |
| Q08 | date |  |  | SI | Achieved healing date |
| Q09 | varchar |  |  | SI | Wound location |
| Q10 | varchar |  |  | SI | Other location |
| Q11 | varchar |  |  | SI | Foot detail |
| Q12 | varchar |  |  | SI | Laterality |
| Q13 | varchar |  |  | SI | Orientation |
| Q14 | varchar |  |  | SI | Type of wound |
| Q15 | varchar |  |  | SI | Burn level |
| Q16 | varchar |  |  | SI | Burn type |
| Q17 | varchar |  |  | SI | Other wound type |
| Q18 | varchar |  |  | SI | Bodymap |
| Q19 | varchar |  |  | SI | Head |
| Q20 | varchar |  |  | SI | Feet |
| Q21 | varchar |  |  | SI | Acquired location |
| Q22 | varchar |  |  | SI | Consent for photography obtained? |
| Q23 | varchar |  |  | SI | Wound normally managed by |
| Q24 | varchar |  |  | SI | Type of healing |
| Q25 | varchar |  |  | SI | Wound closure material used |
| Q26 | varchar |  |  | SI | Overall goal |
| Q28 | varchar |  |  | SI | Treatment plan |
| Q29 | varchar |  |  | SI | Dressing frequency |
| Q30 | varchar |  |  | SI | Change earlier if leaking |
| Q31 | varchar |  |  | SI | Analgesia required / recommended prior to wound tr... |
| Q32 | varchar |  |  | SI | Refer to medication chart |
| Q33 | varchar |  |  | SI | Cleansing / Care of surrounding region |
| Q34 | varchar |  |  | SI | Cleaning - wound bed |
| Q35 | varchar |  |  | SI | Primary dressing |
| Q36 | varchar |  |  | SI | Secondary dressing |
| Q37 | varchar |  |  | SI | Additional dressing detail |
| Q38 | varchar |  |  | SI | Short term goal |
| Q39 | date |  |  | SI | Established aetiology within 14 days |
| Q40 | date |  |  | SI | Established aetiology within 14 days |
| Q41 | date |  |  | SI | Established aetiology within 14 days |
| Q42 | date |  |  | SI | Control underlying factors within 14 days |
| Q43 | date |  |  | SI | Control underlying factors within 14 days |
| Q44 | date |  |  | SI | Control underlying factors within 14 days |
| Q45 | date |  |  | SI | Control pain within 7 days |
| Q46 | date |  |  | SI | Control pain within 7 days |
| Q47 | date |  |  | SI | Control pain within 7 days |
| Q48 | date |  |  | SI | Absence of necrotic tissue within 14 days |
| Q49 | date |  |  | SI | Absence of necrotic tissue within 14 days |
| Q50 | date |  |  | SI | Absence of necrotic tissue within 14 days |
| Q51 | date |  |  | SI | Absence of clinical infections within 14 days |
| Q52 | date |  |  | SI | Absence of clinical infections within 14 days |
| Q53 | date |  |  | SI | Absence of clinical infections within 14 days |
| Q54 | date |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q55 | date |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q56 | date |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q57 | date |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q58 | date |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q59 | date |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q60 | date |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q61 | date |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q62 | date |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q63 | date |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q64 | date |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q65 | date |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q66 | varchar |  |  | SI | Expected date |
| Q67 | varchar |  |  | SI | Review date |
| Q68 | varchar |  |  | SI | Achieved date |
| Q76 | varchar |  |  | SI | Laterality |
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