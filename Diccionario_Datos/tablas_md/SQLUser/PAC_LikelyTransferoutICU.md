# SQLUser.PAC_LikelyTransferoutICU

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LTICU_RowId | bigint | PK |  | NO | - |
| LTICU_Code | varchar |  |  | NO | Code |
| LTICU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LTICU_CreatedDate | date |  |  | SI | Created Date |
| LTICU_CreatedTime | time |  |  | SI | Created Time |
| LTICU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LTICU_Desc | varchar |  |  | NO | Description |
| LTICU_IconName | varchar |  |  | SI | Icon Name |
| LTICU_IconPrior | double |  |  | SI | Icon Priority |
| LTICU_Owner | varchar |  |  | SI | Owner |
| LTICU_UpdatedDate | date |  |  | SI | Updated Date |
| LTICU_UpdatedTime | time |  |  | SI | Updated Time |
| LTICU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01A | - |  |  | SI | Please select the number (0-10) that best describe... |
| Q03A | - |  |  | SI | Please indicate if any of the following has been a... |
| Q04 | - |  |  | SI | Practical Problems |
| Q10 | - |  |  | SI | Child care |
| Q11 | - |  |  | SI | Food |
| Q12 | - |  |  | SI | Family Problems |
| Q13 | - |  |  | SI | Housing |
| Q14 | - |  |  | SI | Insurance / Financial |
| Q15 | - |  |  | SI | Transportation |
| Q16 | - |  |  | SI | Work / School |
| Q17 | - |  |  | SI | Emotional Problems |
| Q18 | - |  |  | SI | Treatment decisions |
| Q19 | - |  |  | SI | Family Problems |
| Q20 | - |  |  | SI | Dealing with children |
| Q21 | - |  |  | SI | Dealing with partner |
| Q22 | - |  |  | SI | Ability to have children |
| Q23 | - |  |  | SI | Family health issues |
| Q24 | - |  |  | SI | Spiritual / Religious Concerns |
| Q25 | - |  |  | SI | Emotional Problems |
| Q26 | - |  |  | SI | Physical Problems |
| Q27 | - |  |  | SI | Depression |
| Q28 | - |  |  | SI | Fears |
| Q29 | - |  |  | SI | Nervousness |
| Q30 | - |  |  | SI | Sadness |
| Q31 | - |  |  | SI | Worry |
| Q32 | - |  |  | SI | Loss of interest in usual activities |
| Q33 | - |  |  | SI | Spiritual / Religious concerns |
| Q34 | - |  |  | SI | Spiritual / Religious concerns |
| Q35 | - |  |  | SI | Physical Problems |
| Q36 | - |  |  | SI | Appearance |
| Q37 | - |  |  | SI | Bathing / Dressing |
| Q38 | - |  |  | SI | Breathing |
| Q39 | - |  |  | SI | Changes in urination |
| Q40 | - |  |  | SI | Constipation |
| Q41 | - |  |  | SI | Diarrhoea |
| Q42 | - |  |  | SI | Eating |
| Q43 | - |  |  | SI | Fatigue |
| Q44 | - |  |  | SI | Feeling swollen |
| Q45 | - |  |  | SI | Fevers |
| Q46 | - |  |  | SI | Getting around |
| Q47 | - |  |  | SI | Indigestion |
| Q48 | - |  |  | SI | Memory / Concentration |
| Q49 | - |  |  | SI | Other Problems |
| Q50 | - |  |  | SI | Other problems |
| Q51 | - |  |  | SI | Mouth sores |
| Q52 | - |  |  | SI | Nausea |
| Q53 | - |  |  | SI | Nose dry / Congested |
| Q54 | - |  |  | SI | Pain |
| Q55 | - |  |  | SI | Sexual |
| Q56 | - |  |  | SI | Skin dry / Itchy |
| Q57 | - |  |  | SI | Sleep |
| Q58 | - |  |  | SI | Substance use |
| Q59 | - |  |  | SI | Tingling in hands / Feet |
| Q60 | - |  |  | SI | NCCN Distress Thermometer |
| Q61 | - |  |  | SI | Date |
| Q62 | - |  |  | SI | Time |
| Q63 | - |  |  | SI | Score |
| Q64 | - |  |  | SI | Classification |
| Q65 | - |  |  | SI | Higher scores represents higher distress |
| Q66 | - |  |  | SI | 0 - 10 |
| Q67 | - |  |  | SI | The NCCN Distress Thermometere and Problem List is... |
| Q68 | - |  |  | SI | It measures distress based on the past week and do... |
| Q69 | - |  |  | SI | Patient distress |
| Q69ObsDR | - |  |  | SI | Patient distress DR |
| Q70 | - |  |  | SI | Total Score |
| Q71 | - |  |  | SI | 0 - 10: Higher scores represents higher distress |
| Q72 | - |  |  | SI | Dealing with children |
| Q73 | - |  |  | SI | Patient distress |
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