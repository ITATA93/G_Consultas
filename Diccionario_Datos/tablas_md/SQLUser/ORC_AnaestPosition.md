# SQLUser.ORC_AnaestPosition

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORCAPS_RowId | bigint | PK |  | NO | - |
| ORCAPS_Code | varchar |  |  | NO | Code |
| ORCAPS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORCAPS_CreatedDate | date |  |  | SI | Created Date |
| ORCAPS_CreatedTime | time |  |  | SI | Created Time |
| ORCAPS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORCAPS_DateFrom | date |  |  | SI | Date From |
| ORCAPS_DateTo | date |  |  | SI | Date To |
| ORCAPS_Desc | varchar |  |  | NO | Description |
| ORCAPS_Owner | varchar |  |  | SI | Owner |
| ORCAPS_UpdatedDate | date |  |  | SI | Updated Date |
| ORCAPS_UpdatedTime | time |  |  | SI | Updated Time |
| ORCAPS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Current problem |
| Q02 | - |  |  | SI | When problem began? |
| Q03 | - |  |  | SI | First episode related to a specific incident? |
| Q04 | - |  |  | SI | If yes, specify |
| Q05 | - |  |  | SI | Since incident is it |
| Q06 | - |  |  | SI | Why or how? |
| Q07 | - |  |  | SI | If pain is present rate pain on 0-10 scale |
| Q08 | - |  |  | SI | Describe the nature of the pain |
| Q09 | - |  |  | SI | Describe previous treatment / exercises |
| Q10 | - |  |  | SI | Activities that cause or aggravate your symptoms |
| Q11 | - |  |  | SI | Comments on activities (timings, describe etc) |
| Q12 | - |  |  | SI | What relieves your symptoms? |
| Q13 | - |  |  | SI | Social activities (exclude physical activities) af... |
| Q14 | - |  |  | SI | Diet /Fluid intake |
| Q15 | - |  |  | SI | Physical activity |
| Q16 | - |  |  | SI | Work |
| Q17 | - |  |  | SI | Other |
| Q18 | - |  |  | SI | Rate the severity of this problem from 0-10 |
| Q18A | - |  |  | SI | (0 being no problem and 10 being worst) |
| Q19 | - |  |  | SI | Treatment Goals / Concerns |
| Q20 | - |  |  | SI | Since onset of symptoms |
| Q21 | - |  |  | SI | Since onset comments |
| Q22 | - |  |  | SI | Date of last physical exam |
| Q23 | - |  |  | SI | Last physical exam comments |
| Q24 | - |  |  | SI | General health |
| Q25 | - |  |  | SI | Occupation |
| Q26 | - |  |  | SI | Hours per week |
| Q27 | - |  |  | SI | On disability or leave |
| Q28 | - |  |  | SI | Activity Restrictions? |
| Q29 | - |  |  | SI | Activity / Exercise |
| Q30 | - |  |  | SI | Activity / Exercise Comments |
| Q31 | - |  |  | SI | Current level of stress |
| Q32 | - |  |  | SI | Current psych therapy? |
| Q33 | - |  |  | SI | Number of childbirth vaginal deliveries |
| Q34 | - |  |  | SI | Number of Episiotomy |
| Q35 | - |  |  | SI | Number of C-Section |
| Q36 | - |  |  | SI | Number of difficult childbirth |
| Q37 | - |  |  | SI | Prolapse or organ falling out |
| Q38 | - |  |  | SI | Vaginal dryness |
| Q39 | - |  |  | SI | Painful periods |
| Q40 | - |  |  | SI | Menopause |
| Q41 | - |  |  | SI | If menopause, when? |
| Q42 | - |  |  | SI | Painful vaginal penetration |
| Q43 | - |  |  | SI | Pelvic / genital pain |
| Q44 | - |  |  | SI | Other |
| Q46 | - |  |  | SI | General Health |
| Q47 | - |  |  | SI | Mental Health |
| Q48 | - |  |  | SI | Obstetric and Gynecology History |
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