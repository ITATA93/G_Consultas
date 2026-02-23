# SQLUser.PAC_AllergyReason

**Schema:** SQLUser
**Columnas:** 146
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALRGREA_RowId | bigint | PK |  | NO | - |
| ALRGREA_Code | varchar |  |  | NO | Code |
| ALRGREA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALRGREA_CreatedDate | date |  |  | SI | Created Date |
| ALRGREA_CreatedTime | time |  |  | SI | Created Time |
| ALRGREA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALRGREA_Desc | varchar |  |  | NO | Description |
| ALRGREA_Owner | varchar |  |  | SI | Owner |
| ALRGREA_UpdatedDate | date |  |  | SI | Updated Date |
| ALRGREA_UpdatedTime | time |  |  | SI | Updated Time |
| ALRGREA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | These questions should be answered thinking of you... |
| Q04 | - |  |  | SI | Do you feel grinding, hear clicking or any other t... |
| Q05 | - |  |  | SI | Difficulties spreading legs wide apart |
| Q06 | - |  |  | SI | Difficulties to stride out when walking |
| Q07 | - |  |  | SI | The following questions concern the amount of join... |
| Q08 | - |  |  | SI | last week |
| Q09 | - |  |  | SI | in your hip. Stiffness is a sensation of restricti... |
| Q10 | - |  |  | SI | How severe is your hip joint stiffness after first... |
| Q11 | - |  |  | SI | How severe is your hip stiffness after sitting, ly... |
| Q12 | - |  |  | SI | later in the day? |
| Q13 | - |  |  | SI | How often is your hip painful? |
| Q14 | - |  |  | SI | What amount of hip pain have you experienced the |
| Q15 | - |  |  | SI | last week |
| Q16 | - |  |  | SI | during the following activities? |
| Q17 | - |  |  | SI | Straightening your hip fully |
| Q18 | - |  |  | SI | Bending your hip fully |
| Q19 | - |  |  | SI | Walking on a flat surface |
| Q20 | - |  |  | SI | Going up or downstairs |
| Q21 | - |  |  | SI | At night while in bed |
| Q22 | - |  |  | SI | Sitting or lying |
| Q23 | - |  |  | SI | Standing upright |
| Q24 | - |  |  | SI | Walking on a hard surface (asphalt, concrete, etc.... |
| Q25 | - |  |  | SI | Walking on an uneven surface |
| Q26 | - |  |  | SI | The following questions concern your physical func... |
| Q27 | - |  |  | SI | For each of the following activities please indica... |
| Q28 | - |  |  | SI | last week |
| Q29 | - |  |  | SI | due to your hip. |
| Q30 | - |  |  | SI | Descending stairs |
| Q31 | - |  |  | SI | Ascending stairs |
| Q32 | - |  |  | SI | Rising from sitting |
| Q33 | - |  |  | SI | Standing |
| Q34 | - |  |  | SI | For each of the following activities please indica... |
| Q35 | - |  |  | SI | Bending to the floor / pick up an object |
| Q36 | - |  |  | SI | Walking on a flat surface |
| Q37 | - |  |  | SI | Getting in/out of car |
| Q38 | - |  |  | SI | Going shopping |
| Q39 | - |  |  | SI | Putting on socks / stockings |
| Q40 | - |  |  | SI | Rising from bed |
| Q41 | - |  |  | SI | Taking off socks / stockings |
| Q42 | - |  |  | SI | Lying in bed (turning over, maintaining hip positi... |
| Q43 | - |  |  | SI | Getting in/out of bath |
| Q44 | - |  |  | SI | Sitting |
| Q45 | - |  |  | SI | Getting on/off toilet |
| Q46 | - |  |  | SI | Heavy domestic duties (moving heavy boxes, scrubbi... |
| Q47 | - |  |  | SI | Light domestic duties (cooking, dusting, etc) |
| Q48 | - |  |  | SI | The following questions concern your physical func... |
| Q49 | - |  |  | SI | last week |
| Q50 | - |  |  | SI | due to your hip. |
| Q51 | - |  |  | SI | Squatting |
| Q52 | - |  |  | SI | Running |
| Q53 | - |  |  | SI | Twisting / pivoting on loaded leg |
| Q54 | - |  |  | SI | Walking on uneven surface |
| Q55 | - |  |  | SI | How often are you aware of your hip problem? |
| Q56 | - |  |  | SI | How much are you troubled with lack of confidence ... |
| Q57 | - |  |  | SI | In general, how much difficulty do you have with y... |
| Q58 | - |  |  | SI | >50% of questions without a valid answer - no sub ... |
| Q59 | - |  |  | SI | Pain Score |
| Q60 | - |  |  | SI | Symptoms Score |
| Q61 | - |  |  | SI | Activities of Daily Living Score |
| Q62 | - |  |  | SI | Sports and Recreational Activities Score |
| Q63 | - |  |  | SI | Quality of Life Score |
| Q64 | - |  |  | SI | 100 indicates no problems and 0 indicates extreme ... |
| Q65 | - |  |  | SI | 100 indicates no problems and 0 indicates extreme ... |
| Q66 | - |  |  | SI | 100 indicates no problems and 0 indicates extreme ... |
| Q67 | - |  |  | SI | 100 indicates no problems and 0 indicates extreme ... |
| Q68 | - |  |  | SI | Each item is scored from 0 to 4, with 0 representi... |
| Q69 | - |  |  | SI | A normalized score (100 indicating no symptoms and... |
| Q70 | - |  |  | SI | Score |
| Q71 | - |  |  | SI | Classification |
| Q72 | - |  |  | SI | 100 |
| Q73 | - |  |  | SI | No problems |
| Q74 | - |  |  | SI | 0 |
| Q75 | - |  |  | SI | Extreme problems |
| Q76 | - |  |  | SI | HOOS is developed as an instrument to assess the p... |
| Q77 | - |  |  | SI | Have you modified your life style to avoid potenti... |
| Q78 | - |  |  | SI | last week. |
| Q79 | - |  |  | SI | 100 indicates no problems |
| Q80 | - |  |  | SI | and |
| Q81 | - |  |  | SI | 0 indicates extreme problems. |
| Q82 | - |  |  | SI | last week |
| Q83 | - |  |  | SI | due to your hip. |
| Q84 | - |  |  | SI | These questions should be answered thinking of you... |
| Q85 | - |  |  | SI | The following questions concern the amount of join... |
| Q86 | - |  |  | SI | Stiffness is a sensation of restriction or slownes... |
| Q87 | - |  |  | SI | What amount of hip pain have you experienced the l... |
| Q88 | - |  |  | SI | The following questions concern your physical func... |
| Q89 | - |  |  | SI | For each of the following activities please indica... |
| Q90 | - |  |  | SI | For each of the following activities please indica... |
| Q91 | - |  |  | SI | The following questions concern your physical func... |
| Q92 | - |  |  | SI | The questions should be answered thinking of what ... |
| Q93 | - |  |  | SI | Each item is scored from 0 to 4, with 0 representi... |
| Q94 | - |  |  | SI | A normalized score (100 indicating no symptoms and... |
| Q95 | - |  |  | SI | 100 indicates no problems and 0 indicates extreme ... |
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