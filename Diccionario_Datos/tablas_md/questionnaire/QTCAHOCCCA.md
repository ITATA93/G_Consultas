# questionnaire.QTCAHOCCCA

> Cognition Assessment

**Schema:** questionnaire
**Columnas:** 130
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cognition Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Cognitive and perception |
| Q02 | varchar |  |  | SI | Orientation |
| Q03 | varchar |  |  | SI | Orientation for place |
| Q04 | varchar |  |  | SI | Orientation for time |
| Q05 | varchar |  |  | SI | Awareness |
| Q06 | varchar |  |  | SI | Reason for hospitalization |
| Q07 | varchar |  |  | SI | Awareness of cognitive disabilities |
| Q08 | varchar |  |  | SI | Visual Perception |
| Q09 | varchar |  |  | SI | Objects identification |
| Q10 | varchar |  |  | SI | Figure-ground |
| Q11 | varchar |  |  | SI | Object constancy |
| Q12 | varchar |  |  | SI | Spatial Perception |
| Q13 | varchar |  |  | SI | Directions on client's body |
| Q14 | varchar |  |  | SI | Spatial relations |
| Q15 | varchar |  |  | SI | Spatial relations on picture |
| Q16 | varchar |  |  | SI | Praxis |
| Q17 | varchar |  |  | SI | Motor imitation |
| Q18 | varchar |  |  | SI | Utilization of objects |
| Q19 | varchar |  |  | SI | Symbolic actions |
| Q20 | varchar |  |  | SI | Memory |
| Q21 | varchar |  |  | SI | Visuomotor Construction |
| Q22 | varchar |  |  | SI | Copying geometric forms |
| Q23 | varchar |  |  | SI | Two-dimensional model |
| Q24 | varchar |  |  | SI | Pegboard construction |
| Q25 | varchar |  |  | SI | Colored block-design |
| Q26 | varchar |  |  | SI | Plain block-design |
| Q27 | varchar |  |  | SI | Puzzle |
| Q28 | varchar |  |  | SI | Clock drawing |
| Q29 | varchar |  |  | SI | Thinking Operations |
| Q30 | varchar |  |  | SI | Categorization |
| Q31 | varchar |  |  | SI | Object classification unstructured |
| Q32 | varchar |  |  | SI | Pictorial sequence A |
| Q33 | varchar |  |  | SI | Pictorial sequence B |
| Q34 | varchar |  |  | SI | Geometric sequences A |
| Q35 | varchar |  |  | SI | Geometric sequences B |
| Q36 | varchar |  |  | SI | Object classification structured |
| Q37 | varchar |  |  | SI | Verbal mathematical questions |
| Q38 | varchar |  |  | SI | Activity Daily Living |
| Q39 | varchar |  |  | SI | Bed mobility |
| Q40 | varchar |  |  | SI | Transfer |
| Q41 | varchar |  |  | SI | Locomotion |
| Q42 | varchar |  |  | SI | Toileting |
| Q43 | varchar |  |  | SI | Eating |
| Q44 | varchar |  |  | SI | Hygiene / Grooming |
| Q45 | varchar |  |  | SI | Bathing |
| Q46 | varchar |  |  | SI | Dressing |
| Q47 | varchar |  |  | SI | Fall Risk Assessment |
| Q48 | varchar |  |  | SI | Fall risk |
| Q49 | varchar |  |  | SI | High risk by |
| Q50 | varchar |  |  | SI | Fracture risk |
| Q51 | varchar |  |  | SI | Pain Assessment |
| Q52 | varchar |  |  | SI | Does patient have pain? |
| Q53 | varchar |  |  | SI | Location |
| Q54 | varchar |  |  | SI | Assessment tool |
| Q55 | varchar |  |  | SI | Pain assessment score |
| Q56 | varchar |  |  | SI | Characteristic of pain |
| Q57 | varchar |  |  | SI | Other characteristic |
| Q58 | varchar |  |  | SI | Frequency |
| Q59 | varchar |  |  | SI | Duration |
| Q60 | varchar |  |  | SI | Pain re-assessment score |
| Q61 | varchar |  |  | SI | Goals and Planning |
| Q62 | varchar |  |  | SI | Goal no 1 |
| Q63 | varchar |  |  | SI | Type |
| Q64 | varchar |  |  | SI | Performance |
| Q65 | varchar |  |  | SI | Satisfaction |
| Q66 | varchar |  |  | SI | Goal no 2 |
| Q67 | varchar |  |  | SI | Type |
| Q68 | varchar |  |  | SI | Performance |
| Q69 | varchar |  |  | SI | Satisfaction |
| Q70 | varchar |  |  | SI | Goal no 3 |
| Q71 | varchar |  |  | SI | Type |
| Q72 | varchar |  |  | SI | Performance |
| Q73 | varchar |  |  | SI | Satisfaction |
| Q74 | varchar |  |  | SI | Goal no 4 |
| Q75 | varchar |  |  | SI | Type |
| Q76 | varchar |  |  | SI | Performance |
| Q77 | varchar |  |  | SI | Satisfaction |
| Q78 | varchar |  |  | SI | Intervention plan |
| Q79 | date |  |  | SI | Re-assessment date |
| Q80 | varchar |  |  | SI | Instruction |
| Q81 | bit |  |  | SI | Patient and/or family was given and understood abo... |
| Q82 | bit |  |  | SI | Need reviewed |
| Q83 | varchar |  |  | SI | Goal |
| Q84 | varchar |  |  | SI | Type |
| Q85 | varchar |  |  | SI | Type |
| Q86 | varchar |  |  | SI | Type |
| Q87 | varchar |  |  | SI | Type |
| Q88 | date |  |  | SI | Date |
| Q89 | time |  |  | SI | Time |
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