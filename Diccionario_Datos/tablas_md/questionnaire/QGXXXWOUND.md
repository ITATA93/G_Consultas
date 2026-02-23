# questionnaire.QGXXXWOUND

> Wound Management

**Schema:** questionnaire
**Columnas:** 106
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Wound Management

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| CQ03 | varchar |  |  | SI | - |
| CQ04 | varchar |  |  | SI | - |
| CQ47 | varchar |  |  | SI | - |
| CQ49 | varchar |  |  | SI | - |
| CQ52 | varchar |  |  | SI | - |
| CQ53 | varchar |  |  | SI | - |
| CQ54 | varchar |  |  | SI | - |
| Q01 | varchar |  |  | SI | Wound Assessment |
| Q02 | varchar |  |  | SI | Location on body map |
| Q03 | varchar |  |  | SI | Wound site |
| Q04 | varchar |  |  | SI | Type of wound |
| Q155 | varchar |  |  | SI | Evaluation |
| Q156 | varchar |  |  | SI | Treatment |
| Q157 | varchar |  |  | SI | Pain Assessment |
| Q17 | date |  |  | SI | Expected date to heal |
| Q18 | date |  |  | SI | Achieved healing date |
| Q20 | date |  |  | SI | Established aetiology within 14 days |
| Q21 | date |  |  | SI | Established aetiology within 14 days date achieved |
| Q22 | date |  |  | SI | Established aetiology within 14 days review date |
| Q23 | date |  |  | SI | Control underlying factors within 14 days |
| Q24 | date |  |  | SI | Control underlying factors within 14 days date ach... |
| Q25 | date |  |  | SI | Control underlying factors within 14 days review d... |
| Q26 | date |  |  | SI | Control pain within 7 days |
| Q27 | date |  |  | SI | Control pain within 7 days date achieved |
| Q28 | date |  |  | SI | Control pain within 7 days review date |
| Q29 | date |  |  | SI | Absence of necrotic tissue within 14 days |
| Q30 | date |  |  | SI | Absence of necrotic tissue within 14 days date ach... |
| Q31 | date |  |  | SI | Absence of necrotic tissue within 14 days review d... |
| Q32 | date |  |  | SI | Absence of clinical infections within 14 days |
| Q33 | date |  |  | SI | Absence of clinical infections within 14 date achi... |
| Q34 | date |  |  | SI | Absence of clinical infections within 14 review da... |
| Q35 | date |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q36 | date |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q37 | date |  |  | SI | Healthy surrounding tissue and reduction of oedema... |
| Q38 | date |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q39 | date |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q40 | date |  |  | SI | Decreased wound surface area by 25% within 42 days... |
| Q41 | date |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q42 | date |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q43 | date |  |  | SI | Decreased wound surface area by 50% within 60 days... |
| Q44 | date |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q45 | date |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q46 | date |  |  | SI | Demonstration of adherence to treatment / preventi... |
| Q47 | varchar |  |  | SI | Care plan |
| Q48 | bigint |  |  | SI | Wound image |
| Q48TxtOnly | bigint |  |  | SI | Wound image Plain Text Only |
| Q49 | varchar |  |  | SI | Acquired location |
| Q50 | varchar |  |  | SI | Comments |
| Q51 | varchar |  |  | SI | Site Detail |
| Q52 | varchar |  |  | SI | Laterality |
| Q53 | varchar |  |  | SI | Orientation |
| Q54 | varchar |  |  | SI | Type of wound |
| Q55 | varchar |  |  | SI | Please specify |
| Q56 | varchar |  |  | SI | Stage of pressure injury |
| Q57 | varchar |  |  | SI | Packing in situ? |
| Q58 | numeric |  |  | SI | Number of packs in situ |
| Q59 | varchar |  |  | SI | Details of packing |
| Q60 | varchar |  |  | SI | Location on body map (Front / Side) |
| Q61 | varchar |  |  | SI | Location on body map (Feet) |
| Q64 | varchar |  |  | SI | Swab taken? |
| Q65 | date |  |  | SI | Date |
| Q66 | time |  |  | SI | Time |
| Q67 | varchar |  |  | SI | Include patient in hospital - acquired injuries pr... |
| Q68 | varchar |  |  | SI | Female body map |
| Q69 | varchar |  |  | SI | Wound site |
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