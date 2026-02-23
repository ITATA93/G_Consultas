# questionnaire.QTCNCCNDTPL

> NCCN Distress Thermometer and Problem List

**Schema:** questionnaire
**Columnas:** 109
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* NCCN Distress Thermometer and Problem List

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01A | varchar |  |  | SI | Please select the number (0-10) that best describe... |
| Q03A | varchar |  |  | SI | Please indicate if any of the following has been a... |
| Q04 | varchar |  |  | SI | Practical Problems |
| Q10 | varchar |  |  | SI | Child care |
| Q11 | varchar |  |  | SI | Food |
| Q12 | varchar |  |  | SI | Family Problems |
| Q13 | varchar |  |  | SI | Housing |
| Q14 | varchar |  |  | SI | Insurance / Financial |
| Q15 | varchar |  |  | SI | Transportation |
| Q16 | varchar |  |  | SI | Work / School |
| Q17 | varchar |  |  | SI | Emotional Problems |
| Q18 | varchar |  |  | SI | Treatment decisions |
| Q19 | varchar |  |  | SI | Family Problems |
| Q20 | varchar |  |  | SI | Dealing with children |
| Q21 | varchar |  |  | SI | Dealing with partner |
| Q22 | varchar |  |  | SI | Ability to have children |
| Q23 | varchar |  |  | SI | Family health issues |
| Q24 | varchar |  |  | SI | Spiritual / Religious Concerns |
| Q25 | varchar |  |  | SI | Emotional Problems |
| Q26 | varchar |  |  | SI | Physical Problems |
| Q27 | varchar |  |  | SI | Depression |
| Q28 | varchar |  |  | SI | Fears |
| Q29 | varchar |  |  | SI | Nervousness |
| Q30 | varchar |  |  | SI | Sadness |
| Q31 | varchar |  |  | SI | Worry |
| Q32 | varchar |  |  | SI | Loss of interest in usual activities |
| Q33 | varchar |  |  | SI | Spiritual / Religious concerns |
| Q34 | varchar |  |  | SI | Spiritual / Religious concerns |
| Q35 | varchar |  |  | SI | Physical Problems |
| Q36 | varchar |  |  | SI | Appearance |
| Q37 | varchar |  |  | SI | Bathing / Dressing |
| Q38 | varchar |  |  | SI | Breathing |
| Q39 | varchar |  |  | SI | Changes in urination |
| Q40 | varchar |  |  | SI | Constipation |
| Q41 | varchar |  |  | SI | Diarrhoea |
| Q42 | varchar |  |  | SI | Eating |
| Q43 | varchar |  |  | SI | Fatigue |
| Q44 | varchar |  |  | SI | Feeling swollen |
| Q45 | varchar |  |  | SI | Fevers |
| Q46 | varchar |  |  | SI | Getting around |
| Q47 | varchar |  |  | SI | Indigestion |
| Q48 | varchar |  |  | SI | Memory / Concentration |
| Q49 | varchar |  |  | SI | Other Problems |
| Q50 | varchar |  |  | SI | Other problems |
| Q51 | varchar |  |  | SI | Mouth sores |
| Q52 | varchar |  |  | SI | Nausea |
| Q53 | varchar |  |  | SI | Nose dry / Congested |
| Q54 | varchar |  |  | SI | Pain |
| Q55 | varchar |  |  | SI | Sexual |
| Q56 | varchar |  |  | SI | Skin dry / Itchy |
| Q57 | varchar |  |  | SI | Sleep |
| Q58 | varchar |  |  | SI | Substance use |
| Q59 | varchar |  |  | SI | Tingling in hands / Feet |
| Q60 | varchar |  |  | SI | NCCN Distress Thermometer |
| Q61 | date |  |  | SI | Date |
| Q62 | time |  |  | SI | Time |
| Q63 | varchar |  |  | SI | Score |
| Q64 | varchar |  |  | SI | Classification |
| Q65 | varchar |  |  | SI | Higher scores represents higher distress |
| Q66 | varchar |  |  | SI | 0 - 10 |
| Q67 | varchar |  |  | SI | The NCCN Distress Thermometere and Problem List is... |
| Q68 | varchar |  |  | SI | It measures distress based on the past week and do... |
| Q69 | varchar |  |  | SI | Patient distress |
| Q69ObsDR | varchar |  | FK | SI | Patient distress DR |
| Q70 | varchar |  |  | SI | Total Score |
| Q71 | varchar |  |  | SI | 0 - 10: Higher scores represents higher distress |
| Q72 | varchar |  |  | SI | Dealing with children |
| Q73 | varchar |  |  | SI | Patient distress |
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