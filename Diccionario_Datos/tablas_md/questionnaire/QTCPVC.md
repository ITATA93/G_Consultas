# questionnaire.QTCPVC

> Prescription Verification Checklist

**Schema:** questionnaire
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Prescription Verification Checklist

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Pharmacy review, verification and providing drug i... |
| Q02 | varchar |  |  | SI | Ordering clinician |
| Q03 | date |  |  | SI | Prescription date |
| Q04 | varchar |  |  | SI | Prescription no |
| Q05 | varchar |  |  | SI | Administration Requirements |
| Q06 | varchar |  |  | SI | Patient identification |
| Q07 | varchar |  |  | SI | Note |
| Q08 | varchar |  |  | SI | Prescriber identification |
| Q09 | varchar |  |  | SI | Note |
| Q10 | varchar |  |  | SI | Right patient location |
| Q11 | varchar |  |  | SI | Note |
| Q12 | varchar |  |  | SI | Right prescription date |
| Q13 | varchar |  |  | SI | Note |
| Q14 | varchar |  |  | SI | Pharmaceutical Requirements |
| Q15 | varchar |  |  | SI | Right drug |
| Q16 | varchar |  |  | SI | Note |
| Q17 | varchar |  |  | SI | Right dose |
| Q18 | varchar |  |  | SI | Note |
| Q19 | varchar |  |  | SI | Right route |
| Q20 | varchar |  |  | SI | Note |
| Q21 | varchar |  |  | SI | Right time / frequency |
| Q22 | varchar |  |  | SI | Note |
| Q23 | varchar |  |  | SI | Clinical Requirements |
| Q24 | varchar |  |  | SI | Check therapeutic duplication |
| Q25 | varchar |  |  | SI | Note |
| Q26 | varchar |  |  | SI | Check allergy |
| Q27 | varchar |  |  | SI | Note |
| Q28 | varchar |  |  | SI | Check contraindication |
| Q29 | varchar |  |  | SI | Note |
| Q30 | varchar |  |  | SI | Check drug interaction |
| Q31 | varchar |  |  | SI | Note |
| Q32 | varchar |  |  | SI | Right patient |
| Q33 | varchar |  |  | SI | Note |
| Q34 | varchar |  |  | SI | Right drug |
| Q35 | varchar |  |  | SI | Note |
| Q36 | varchar |  |  | SI | Right dose |
| Q37 | varchar |  |  | SI | Note |
| Q38 | varchar |  |  | SI | Right route |
| Q39 | varchar |  |  | SI | Note |
| Q40 | varchar |  |  | SI | Right time / frequency |
| Q41 | varchar |  |  | SI | Note |
| Q42 | varchar |  |  | SI | Before expired date |
| Q43 | varchar |  |  | SI | Note |
| Q44 | bit |  |  | SI | SBAR (Situation, Background, Assessment, Recommend... |
| Q45 | bigint |  |  | SI | Details |
| Q45TxtOnly | bigint |  |  | SI | Details Plain Text Only |
| Q46 | varchar |  |  | SI | Doctor's instructions |
| Q47 | bit |  |  | SI | Readback |
| Q48 | varchar |  |  | SI | Consultation doctor |
| Q49 | date |  |  | SI | Confirmation date and time |
| Q50 | time |  |  | SI | Confirmation time |
| Q51 | varchar |  |  | SI | Confirmation method |
| Q52 | varchar |  |  | SI | Confirmed pharmacist |
| Q53 | varchar |  |  | SI | Providing drug information |
| Q54 | varchar |  |  | SI | Detail of counselling / drug information |
| Q55 | date |  |  | SI | Date |
| Q56 | time |  |  | SI | Time |
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