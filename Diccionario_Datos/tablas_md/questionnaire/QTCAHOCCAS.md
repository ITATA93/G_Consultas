# questionnaire.QTCAHOCCAS

> Adult Occupational Therapy Assessment

**Schema:** questionnaire
**Columnas:** 131
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Adult Occupational Therapy Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Hand Function |
| Q02 | varchar |  |  | SI | Hand Function Evaluation |
| Q03 | varchar |  |  | SI | Side |
| Q04 | varchar |  |  | SI | Reach Forward |
| Q05 | varchar |  |  | SI | Carry Out |
| Q06 | varchar |  |  | SI | Release |
| Q07 | varchar |  |  | SI | Spherical |
| Q08 | varchar |  |  | SI | Cylindrical |
| Q09 | varchar |  |  | SI | Hook |
| Q10 | varchar |  |  | SI | Lateral Pinch |
| Q11 | varchar |  |  | SI | Tripod pinch |
| Q12 | varchar |  |  | SI | Pad Pinch |
| Q13 | varchar |  |  | SI | Tip Pinch |
| Q14 | varchar |  |  | SI | Eye-Hand Coordination |
| Q15 | varchar |  |  | SI | In-Hand Manipulation |
| Q16 | varchar |  |  | SI | Hand Dexterity |
| Q17 | varchar |  |  | SI | Finger to Palm |
| Q18 | varchar |  |  | SI | Activities of Daily Living (ADL) |
| Q19 | varchar |  |  | SI | ADL Evaluation |
| Q20 | varchar |  |  | SI | Bed Mobility |
| Q21 | varchar |  |  | SI | Transfer |
| Q22 | varchar |  |  | SI | Locomotion |
| Q23 | varchar |  |  | SI | Toileting |
| Q24 | varchar |  |  | SI | Eating |
| Q25 | varchar |  |  | SI | Dressing |
| Q26 | varchar |  |  | SI | Bathing |
| Q27 | varchar |  |  | SI | Hygiene / Grooming |
| Q28 | varchar |  |  | SI | Swallowing |
| Q29 | varchar |  |  | SI | Swallowing Evaluation |
| Q30 | varchar |  |  | SI | Feeding by |
| Q31 | varchar |  |  | SI | Tracheostomy |
| Q32 | varchar |  |  | SI | Drooling |
| Q33 | varchar |  |  | SI | Lip Control |
| Q34 | varchar |  |  | SI | Tongue Movement |
| Q35 | varchar |  |  | SI | Jaw Control |
| Q36 | varchar |  |  | SI | Cough Reflex |
| Q37 | varchar |  |  | SI | Gag Reflex |
| Q38 | varchar |  |  | SI | Swallow Reflex |
| Q39 | varchar |  |  | SI | Bite Reflex |
| Q40 | varchar |  |  | SI | Swallowing Test |
| Q41 | varchar |  |  | SI | Cognitive and Perception |
| Q42 | varchar |  |  | SI | Cognitive and Perception Evaluation |
| Q43 | varchar |  |  | SI | Neglect |
| Q44 | varchar |  |  | SI | Memory (Short) |
| Q45 | varchar |  |  | SI | Memory (Long) |
| Q46 | varchar |  |  | SI | Orientation to Time |
| Q47 | varchar |  |  | SI | Orientation to Place |
| Q48 | varchar |  |  | SI | Object Identification |
| Q49 | varchar |  |  | SI | Spatial Relations |
| Q50 | varchar |  |  | SI | Utilization of Objects |
| Q51 | varchar |  |  | SI | Calculation |
| Q52 | varchar |  |  | SI | Copy Two-Dimensional |
| Q53 | varchar |  |  | SI | Attention Span |
| Q54 | varchar |  |  | SI | Fall Risk Assessment |
| Q55 | varchar |  |  | SI | Fall Risk |
| Q56 | varchar |  |  | SI | High Risk by |
| Q57 | varchar |  |  | SI | Fracture Risk |
| Q58 | varchar |  |  | SI | Pain Assessment |
| Q59 | varchar |  |  | SI | Does Patient have Pain? |
| Q60 | varchar |  |  | SI | Location |
| Q61 | varchar |  |  | SI | Assessment Tool |
| Q62 | varchar |  |  | SI | Pain Assessment Score |
| Q63 | varchar |  |  | SI | Characteristic of Pain |
| Q64 | varchar |  |  | SI | Other Characteristic |
| Q65 | varchar |  |  | SI | Frequency |
| Q66 | varchar |  |  | SI | Duration |
| Q67 | varchar |  |  | SI | Pain Re-Assessment Score |
| Q68 | varchar |  |  | SI | Goals and Planning |
| Q69 | varchar |  |  | SI | Goal No 1 |
| Q70 | varchar |  |  | SI | Type |
| Q71 | varchar |  |  | SI | Performance |
| Q72 | varchar |  |  | SI | Satisfaction |
| Q73 | varchar |  |  | SI | Goal No 2 |
| Q74 | varchar |  |  | SI | Type |
| Q75 | varchar |  |  | SI | Performance |
| Q76 | varchar |  |  | SI | Satisfaction |
| Q77 | varchar |  |  | SI | Goal No 3 |
| Q78 | varchar |  |  | SI | Type |
| Q79 | varchar |  |  | SI | Performance |
| Q80 | varchar |  |  | SI | Satisfaction |
| Q81 | varchar |  |  | SI | Goal No 4 |
| Q82 | varchar |  |  | SI | Type |
| Q83 | varchar |  |  | SI | Performance |
| Q84 | varchar |  |  | SI | Satisfaction |
| Q85 | varchar |  |  | SI | Intervention Plan |
| Q86 | date |  |  | SI | Re-Assessment Date |
| Q87 | varchar |  |  | SI | Instruction |
| Q88 | bit |  |  | SI | Patient and/or Family was given and understood abo... |
| Q89 | bit |  |  | SI | Need Reviewed |
| Q90 | varchar |  |  | SI | Goal |
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