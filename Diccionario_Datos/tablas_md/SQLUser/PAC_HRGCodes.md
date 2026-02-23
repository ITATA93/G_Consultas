# SQLUser.PAC_HRGCodes

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HRG_RowId | bigint | PK |  | NO | - |
| HRG_Code | varchar |  |  | NO | Code |
| HRG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HRG_CreatedDate | date |  |  | SI | Created Date |
| HRG_CreatedTime | time |  |  | SI | Created Time |
| HRG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HRG_DateFrom | date |  |  | SI | Date From |
| HRG_DateTo | date |  |  | SI | Date To |
| HRG_DepartmwentGroup | bigint |  |  | SI | Department Group |
| HRG_Desc | varchar |  |  | NO | Description |
| HRG_EpisodeType | varchar |  |  | SI | Episode Type |
| HRG_LocationDR | bigint |  | FK | SI | CT_Loc des ref |
| HRG_Owner | varchar |  |  | SI | Owner |
| HRG_UpdatedDate | date |  |  | SI | Updated Date |
| HRG_UpdatedTime | time |  |  | SI | Updated Time |
| HRG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Instructions: Score one point for each correct res... |
| Q05 | - |  |  | SI | “What is the year? Season? Date? Day? Month?” |
| Q06 | - |  |  | SI | “Where are we now? State? County? Town / city? Hos... |
| Q07 | - |  |  | SI | The examiner names three unrelated objects clearly... |
| Q07B | - |  |  | SI | The patient’s response is used for scoring. The ex... |
| Q08 | - |  |  | SI | “I would like you to count backward from 100 by se... |
| Q08B | - |  |  | SI | Alternative: “Spell WORLD backwards.” (D-L-R-O-W) |
| Q09 | - |  |  | SI | “Earlier I told you the names of three things. Can... |
| Q10 | - |  |  | SI | Show the patient two simple objects, such as a wri... |
| Q100 | - |  |  | SI | Moderate |
| Q101 | - |  |  | SI | 0-10 |
| Q102 | - |  |  | SI | Severe |
| Q103 | - |  |  | SI | 26-30 |
| Q104 | - |  |  | SI | 21-25 |
| Q105 | - |  |  | SI | 11-20 |
| Q11 | - |  |  | SI | “Repeat the phrase: ‘No ifs, ands, or buts.’” |
| Q12 | - |  |  | SI | “Take the paper in your right hand, fold it in hal... |
| Q13 | - |  |  | SI | “Please read this and do what it says.” (Written i... |
| Q14 | - |  |  | SI | “Make up and write a sentence about anything.” (Th... |
| Q15 | - |  |  | SI | “Please copy this picture.” (The examiner gives th... |
| Q15B | - |  |  | SI | All 10 angles must be present and two must interse... |
| Q31 | - |  |  | SI | Interpretation of the MMSE Methods |
| Q32 | - |  |  | SI | Method |
| Q33 | - |  |  | SI | Score |
| Q34 | - |  |  | SI | Interpretation |
| Q35 | - |  |  | SI | Single Cutoff |
| Q36 | - |  |  | SI | <24 |
| Q37 | - |  |  | SI | Abnormal |
| Q38 | - |  |  | SI | Range |
| Q39 | - |  |  | SI | <21 |
| Q40 | - |  |  | SI | Increased odds of dementia |
| Q41 | - |  |  | SI | >25 |
| Q42 | - |  |  | SI | Decreased odds of dementia |
| Q43 | - |  |  | SI | Education |
| Q44 | - |  |  | SI | 21 |
| Q45 | - |  |  | SI | Abnormal for 8th grade education |
| Q46 | - |  |  | SI | <23 |
| Q47 | - |  |  | SI | Abnormal for high school education |
| Q48 | - |  |  | SI | Abnormal for college education |
| Q48A | - |  |  | SI | <24 |
| Q49 | - |  |  | SI | Severity |
| Q50 | - |  |  | SI | 24-30 |
| Q51 | - |  |  | SI | No cognitive impairment |
| Q52 | - |  |  | SI | 18-23 |
| Q53 | - |  |  | SI | Mild cognitive impairment |
| Q54 | - |  |  | SI | 0-17 |
| Q55 | - |  |  | SI | Severe cognitive impairment |
| Q56 | - |  |  | SI | Interpretation of MMSE Scores |
| Q57 | - |  |  | SI | Score |
| Q58 | - |  |  | SI | Degree of Impairment |
| Q59 | - |  |  | SI | Formal Psychometric Assessment |
| Q60 | - |  |  | SI | Day-to-Day Functioning |
| Q61 | - |  |  | SI | 25-30 |
| Q62 | - |  |  | SI | Questionably significant |
| Q63 | - |  |  | SI | If clinical signs of cognitive impairment are pres... |
| Q64 | - |  |  | SI | May have clinically significant but mild deficits.... |
| Q65 | - |  |  | SI | 20-25 |
| Q66 | - |  |  | SI | Mild |
| Q67 | - |  |  | SI | Formal assessment may be helpful to better determi... |
| Q68 | - |  |  | SI | Significant effect. May require some supervision, ... |
| Q69 | - |  |  | SI | 10-20 |
| Q70 | - |  |  | SI | Moderate |
| Q71 | - |  |  | SI | Formal assessment may be helpful if there are spec... |
| Q72 | - |  |  | SI | Clear impairment. May require 24-hour supervision. |
| Q73 | - |  |  | SI | 0-10 |
| Q74 | - |  |  | SI | Severe |
| Q75 | - |  |  | SI | Patient not likely to be testable |
| Q76 | - |  |  | SI | Marked impairment. Likely to require 24-hour super... |
| Q77 | - |  |  | SI | 0-10: Severe |
| Q78 | - |  |  | SI | 10-20: Moderate |
| Q79 | - |  |  | SI | 20-25: Mild |
| Q80 | - |  |  | SI | 25-30: Questionably significant |
| Q81 | - |  |  | SI | The Mini-Mental State Examination (MMSE) questionn... |
| Q82 | - |  |  | SI | “What is the year? Season? Date? Day? Month?” |
| Q83 | - |  |  | SI | “Where are we now? State? County? Town / city? Hos... |
| Q84 | - |  |  | SI | The examiner names three unrelated objects clearly... |
| Q85 | - |  |  | SI | “I would like you to count backward from 100 by se... |
| Q86 | - |  |  | SI | “Earlier I told you the names of three things. Can... |
| Q87 | - |  |  | SI | Show the patient two simple objects, such as a wri... |
| Q88 | - |  |  | SI | “Repeat the phrase: ‘No ifs, ands, or buts.’” |
| Q89 | - |  |  | SI | “Take the paper in your right hand, fold it in hal... |
| Q90 | - |  |  | SI | “Please read this and do what it says.” (Written i... |
| Q91 | - |  |  | SI | “Make up and write a sentence about anything.” (Th... |
| Q92 | - |  |  | SI | “Please copy this picture.” (The examiner gives th... |
| Q93 | - |  |  | SI | Score |
| Q94 | - |  |  | SI | Degree of Impairment |
| Q95 | - |  |  | SI | 25-30 |
| Q96 | - |  |  | SI | Questionably significant |
| Q97 | - |  |  | SI | 20-25 |
| Q98 | - |  |  | SI | Mild |
| Q99 | - |  |  | SI | 10-20 |
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