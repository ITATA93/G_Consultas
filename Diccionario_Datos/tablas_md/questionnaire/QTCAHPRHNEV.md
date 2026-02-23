# questionnaire.QTCAHPRHNEV

> Neurological Evaluation

**Schema:** questionnaire
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neurological Evaluation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Previous Physical Therapy Services |
| Q02 | varchar |  |  | SI | Previous Functional Status |
| Q03 | varchar |  |  | SI | Occupation |
| Q04 | varchar |  |  | SI | Place of Residence |
| Q05 | varchar |  |  | SI | Lives with |
| Q06 | varchar |  |  | SI | Floors |
| Q07 | varchar |  |  | SI | Stairs |
| Q08 | varchar |  |  | SI | Marital Status |
| Q09 | numeric |  |  | SI | No. of children |
| Q10 | varchar |  |  | SI | Hand Dominance |
| Q11 | varchar |  |  | SI | Precautions |
| Q12 | varchar |  |  | SI | Patient Goals / Concerns |
| Q13 | varchar |  |  | SI | Orientation |
| Q14 | varchar |  |  | SI | Speech |
| Q15 | varchar |  |  | SI | Hearing |
| Q16 | varchar |  |  | SI | Best Gaze |
| Q17 | varchar |  |  | SI | Visual Field (Right) |
| Q18 | varchar |  |  | SI | Visual Field (Left) |
| Q19 | varchar |  |  | SI | Involuntary Movements |
| Q20 | varchar |  |  | SI | Tremor |
| Q21 | varchar |  |  | SI | Other Involuntary Movements |
| Q37 | varchar |  |  | SI | Deformities |
| Q38 | varchar |  |  | SI | Comments |
| Q39 | varchar |  |  | SI | Contractures |
| Q40 | varchar |  |  | SI | Comments |
| Q42 | varchar |  |  | SI | Functional Ambulation Score |
| Q43 | varchar |  |  | SI | Score |
| Q44 | varchar |  |  | SI | Category  |
| Q45 | varchar |  |  | SI | 0 |
| Q46 | varchar |  |  | SI | Nonfunctional Ambulation |
| Q47 | varchar |  |  | SI | Patient cannot ambulate, ambulates in parallel bar... |
| Q48 | varchar |  |  | SI | 1 |
| Q49 | varchar |  |  | SI | Ambulator-Dependence for Physical Assisstance Leve... |
| Q50 | varchar |  |  | SI | Patient requires manual contacts of no more than o... |
| Q51 | varchar |  |  | SI |  Manual contacts are continuous and necessary to s... |
| Q52 | varchar |  |  | SI | 2 |
| Q53 | varchar |  |  | SI | Ambulator-Dependent for Physical Assisstance Level... |
| Q54 | varchar |  |  | SI | Patient requires manual contact of no more than on... |
| Q55 | varchar |  |  | SI | 3 |
| Q56 | varchar |  |  | SI | Ambulator-Dependent for Supervision |
| Q57 | varchar |  |  | SI | Patient can physically ambulate on level surfaces ... |
| Q58 | varchar |  |  | SI |  or the need for verbal cuing to complete the task |
| Q59 | varchar |  |  | SI | 4 |
| Q60 | varchar |  |  | SI | Ambulator-Independent Level Surfaces only |
| Q61 | varchar |  |  | SI | Patient can ambulate independently on level surfac... |
| Q62 | varchar |  |  | SI | 5 |
| Q63 | varchar |  |  | SI | Ambulator-Independent |
| Q64 | varchar |  |  | SI | Patient can ambulate independently on non level an... |
| Q65 | varchar |  |  | SI | Pattern |
| Q66 | varchar |  |  | SI | Stairs |
| Q67 | varchar |  |  | SI | Problems List |
| Q68 | varchar |  |  | SI | Rehabilitation Potential |
| Q69 | varchar |  |  | SI | Family / Patient involved in and verbalized unders... |
| Q70 | varchar |  |  | SI | Treatment Plan |
| Q71 | varchar |  |  | SI | Short Term Goals Period |
| Q72 | varchar |  |  | SI | Short Term Goals |
| Q73 | varchar |  |  | SI | Long Term Goals Period |
| Q74 | varchar |  |  | SI | Long Term Goals |
| Q75 | varchar |  |  | SI | Treatment |
| Q76 | date |  |  | SI | Re evaluation Date |
| Q77 | varchar |  |  | SI | Treatment Options |
| Q78 | varchar |  |  | SI | Assistive Device |
| Q79 | varchar |  |  | SI | Other |
| Q80 | varchar |  |  | SI | Social History |
| Q81 | varchar |  |  | SI | Mental Status |
| Q82 | varchar |  |  | SI | Behaviour / Cognitive |
| Q83 | varchar |  |  | SI | Vision |
| Q84 | varchar |  |  | SI | Visual Field |
| Q85 | varchar |  |  | SI | Involuntary Movements |
| Q86 | varchar |  |  | SI | Rolling |
| Q87 | varchar |  |  | SI | Bridging |
| Q88 | varchar |  |  | SI | Lying to Sitting |
| Q89 | varchar |  |  | SI | Shifting Hip |
| Q90 | varchar |  |  | SI | Sitting to Standing |
| Q91 | varchar |  |  | SI | Transfer Bed to Wheelchair |
| Q92 | varchar |  |  | SI | Functional Mobility |
| Q93 | varchar |  |  | SI | Comments |
| Q94 | varchar |  |  | SI | Comments |
| Q95 | varchar |  |  | SI | Comments |
| Q96 | date |  |  | SI | Date |
| Q97 | time |  |  | SI | Time |
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