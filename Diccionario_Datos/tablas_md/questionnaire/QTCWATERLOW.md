# questionnaire.QTCWATERLOW

> Waterlow Pressure Ulcer Prevention with MST

**Schema:** questionnaire
**Columnas:** 114
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Waterlow Pressure Ulcer Prevention with MST

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Build / Weight for Height |
| Q02 | varchar |  |  | SI | Skin Type Visual Risk Areas |
| Q03 | varchar |  |  | SI | Continence |
| Q04 | varchar |  |  | SI | Age |
| Q05 | varchar |  |  | SI | Mobility |
| Q07 | varchar |  |  | SI | Tissue malnutrition |
| Q08 | varchar |  |  | SI | Neurological deficit |
| Q09 | varchar |  |  | SI | Major Surgery or Trauma |
| Q10 | varchar |  |  | SI | Medication |
| Q11 | varchar |  |  | SI | 10+ At risk |
| Q12 | varchar |  |  | SI | 15+ High risk |
| Q13 | varchar |  |  | SI | 20+ Very high risk |
| Q14 | varchar |  |  | SI | The Waterlow score gives an estimated risk for the... |
| Q15 | varchar |  |  | SI | Sex |
| Q16 | varchar |  |  | SI | Neurological deficit (score) |
| Q17 | date |  |  | SI | Date |
| Q18 | varchar |  |  | SI | Malnutrition Screening Tool (MST) |
| Q18a | varchar |  |  | SI | Medication (score) |
| Q19 | varchar |  |  | SI | Has patient lost weight recently? |
| Q20 | varchar |  |  | SI | Weight loss score |
| Q21 | varchar |  |  | SI | Patient eating poorly or lack of appetite |
| Q22 | varchar |  |  | SI | Nutrition score (calculated) |
| Q22b | varchar |  |  | SI | Nutrition score (calculated) |
| Q23 | varchar |  |  | SI | If Nutrition score >2 refer for nutrition assessme... |
| Q24 | varchar |  |  | SI | Total score |
| Q24b | varchar |  |  | SI | Total score |
| Q24c | varchar |  |  | SI | Total score |
| Q28 | varchar |  |  | SI | Special risks |
| Q29 | varchar |  |  | SI | < 10 No risk |
| Q2a | varchar |  |  | SI | Skin Type Visual Risk Areas |
| Q30 | varchar |  |  | SI | Medication - Cytotoxics, long term/high dose stero... |
| Q31 | varchar |  |  | SI | Neurological deficit - Diabetes, MS, CVA, Motor/Se... |
| Q33 | varchar |  |  | SI | The Waterlow Scale should be used in conjunction w... |
| Q34 | varchar |  |  | SI | As a result of the assessment, patients will be ei... |
| Q35 | varchar |  |  | SI | More than one option can be selected against the f... |
| Q36 | varchar |  |  | SI | This questionnaire incorporates the Australian Mal... |
| Q37 | varchar |  |  | SI | Please, note that the MST Nutrition Score will not... |
| Q38 | varchar |  |  | SI | Guidance |
| Q39 | varchar |  |  | SI | Waterlow score |
| Q40 | varchar |  |  | SI | MST score |
| Q43 | varchar |  |  | SI | <=2 Nutrition assessment/intervention not required |
| Q44 | varchar |  |  | SI | >2 Refer for nutrition assessment/intervention |
| Q45 | varchar |  |  | SI | The neurological deficit score can vary between 4 ... |
| Q46 | varchar |  |  | SI | The Medication section is at the care provider's d... |
| Q47 | varchar |  |  | SI | Nutrition is an extremely important contributory f... |
| Q48 | varchar |  |  | SI | Guidelines |
| Q49 | date |  |  | SI | Date |
| Q50 | time |  |  | SI | Time |
| Q51 | varchar |  |  | SI | Score |
| Q52 | varchar |  |  | SI | Classification |
| Q53 | varchar |  |  | SI | Score |
| Q54 | varchar |  |  | SI | < 10 |
| Q55 | varchar |  |  | SI | No risk |
| Q56 | varchar |  |  | SI | 10+ |
| Q57 | varchar |  |  | SI | At risk |
| Q58 | varchar |  |  | SI | 15+ |
| Q59 | varchar |  |  | SI | High risk |
| Q5a | varchar |  |  | SI | Mobility |
| Q60 | varchar |  |  | SI | 20+ |
| Q61 | varchar |  |  | SI | Very high risk |
| Q62 | varchar |  |  | SI | < 10: No risk |
| Q63 | varchar |  |  | SI | 10+: At risk |
| Q64 | varchar |  |  | SI | 15+: High risk |
| Q65 | varchar |  |  | SI | 20+: Very high risk |
| Q66 | varchar |  |  | SI | ≤ 2 |
| Q67 | varchar |  |  | SI | Nutrition assessment/intervention not required |
| Q68 | varchar |  |  | SI | > 2 |
| Q69 | varchar |  |  | SI | Refer for nutrition assessment / intervention |
| Q70 | varchar |  |  | SI | ≤ 2: Nutrition assessment / intervention not requi... |
| Q71 | varchar |  |  | SI | > 2: Refer for nutrition assessment / intervention |
| Q72 | varchar |  |  | SI | Waterlow score |
| Q73 | varchar |  |  | SI | MST score |
| Q9a | varchar |  |  | SI | Major Surgery or Trauma |
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