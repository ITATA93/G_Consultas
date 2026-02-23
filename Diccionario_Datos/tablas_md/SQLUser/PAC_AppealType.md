# SQLUser.PAC_AppealType

**Schema:** SQLUser
**Columnas:** 128
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPTYPE_ParRef | bigint | PK |  | NO | PAC_Appeal Parent Reference |
| APPTYPE_Childsub | double |  |  | NO | Childsub |
| APPTYPE_Code | varchar |  |  | SI | Code |
| APPTYPE_CreatedDate | date |  |  | SI | Created Date |
| APPTYPE_CreatedTime | time |  |  | SI | Created Time |
| APPTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPTYPE_DateFrom | date |  |  | SI | DateFrom |
| APPTYPE_DateTo | date |  |  | SI | DateTo |
| APPTYPE_Desc | varchar |  |  | SI | Description |
| APPTYPE_RowId | varchar |  |  | NO | - |
| APPTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| APPTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| APPTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | This form is designed to enable us to record and m... |
| Q02 | - |  |  | SI | (i.e. over the last 10 days or so). All informatio... |
| Q03 | - |  |  | SI | 1. For questions where a number of different respo... |
| Q04 | - |  |  | SI | 2. Some questions will require you to write in an ... |
| Q05 | - |  |  | SI | 3. Some questions require you to put a cross on a ... |
| Q06 | - |  |  | SI | Do you currently suffer from abdominal (tummy) pai... |
| Q07 | - |  |  | SI | How severe is your abdominal (tummy) pain? |
| Q08 | - |  |  | SI | 0%: no pain - 25%: not very severe - 50%: quite se... |
| Q09 | - |  |  | SI | Please enter the number of days that you get the p... |
| Q10 | - |  |  | SI | For example, if you enter 4 it means that you get ... |
| Q11 | - |  |  | SI | Do you currently suffer from abdominal distension ... |
| Q12 | - |  |  | SI | (*women, please ignore distension related to your ... |
| Q13 | - |  |  | SI | How severe is your abdominal distension / tightnes... |
| Q14 | - |  |  | SI | 0%: no distension - 25%: not very severe - 50%: qu... |
| Q15 | - |  |  | SI | How satisfied are you with your bowel habit? |
| Q16 | - |  |  | SI | 0%: very happy - 33%: quite happy - 66%: unhappy -... |
| Q17 | - |  |  | SI | How much is your Irritable Bowel Syndrome affectin... |
| Q18 | - |  |  | SI | 0%: not at all - 33%: not much - 66%: quite a lot-... |
| Q19 | - |  |  | SI | Irritable Bowel Syndrome Severity Score |
| Q20 | - |  |  | SI | Bowel habit |
| Q21 | - |  |  | SI | a) What is the most number of times you open your ... |
| Q22 | - |  |  | SI | Per day / week / month |
| Q23 | - |  |  | SI | Are your motions ever normal? |
| Q24 | - |  |  | SI | Are your motions ever hard? |
| Q25 | - |  |  | SI | Are your motions ever very thin (like string)? |
| Q26 | - |  |  | SI | Are your motions ever in small pieces (like rabbit... |
| Q27 | - |  |  | SI | Are your motions ever mushy (like porridge)? |
| Q28 | - |  |  | SI | Are your motions ever watery? |
| Q29 | - |  |  | SI | Do you ever pass mucus (or slime or jelly) with yo... |
| Q30 | - |  |  | SI | Do you ever pass blood with your motions? |
| Q31 | - |  |  | SI | Do you ever have to hurry / rush to the toilet to ... |
| Q32 | - |  |  | SI | Do you ever strain to open your bowels? |
| Q33 | - |  |  | SI | Do you ever feel you haven't emptied your bowel co... |
| Q34 | - |  |  | SI | Site of pain: Please mark with a cross (X) on the ... |
| Q35 | - |  |  | SI | Site of pain |
| Q36 | - |  |  | SI | Do you ever notice your stools are more frequent o... |
| Q37 | - |  |  | SI | Do you ever notice whether the pain is frequently ... |
| Q38 | - |  |  | SI | In the last year on approximately how many weeks w... |
| Q39 | - |  |  | SI | (enter 52 if you have given up completely work bec... |
| Q40 | - |  |  | SI | In the last year on approximately how many weeks w... |
| Q41 | - |  |  | SI | Irritable Bowel Syndrome Severity Score |
| Q42 | - |  |  | SI | Classification |
| Q43 | - |  |  | SI | <75 |
| Q44 | - |  |  | SI | Disease in remission |
| Q45 | - |  |  | SI | 75 to 175 |
| Q46 | - |  |  | SI | Mild disease |
| Q47 | - |  |  | SI | 176 to 300 |
| Q48 | - |  |  | SI | Moderate disease |
| Q49 | - |  |  | SI | >300 |
| Q50 | - |  |  | SI | Severe disease |
| Q51 | - |  |  | SI | 0 - 74: No disease |
| Q52 | - |  |  | SI | 75 - 175: Mild disease |
| Q53 | - |  |  | SI | 176 - 300: Moderate disease |
| Q54 | - |  |  | SI | 301 - 500: Severe disease |
| Q55 | - |  |  | SI | The Irritable Bowel Syndrome Severity Score (Franc... |
| Q56 | - |  |  | SI | The system, incorporating pain, distension, bowel ... |
| Q57 | - |  |  | SI | Date |
| Q58 | - |  |  | SI | Time |
| Q59 | - |  |  | SI | Note: For some people the answer to question a and... |
| Q60 | - |  |  | SI | b) What is the least number of times you open your... |
| Q61 | - |  |  | SI | Per day / week / month |
| Q62 | - |  |  | SI | Irritable Bowel Syndrome Severity Score |
| Q63 | - |  |  | SI | Do you ever have to hurry / rush to the toilet to ... |
| Q64 | - |  |  | SI | Irritable Bowel Syndrome Severity Score Interpreta... |
| Q65 | - |  |  | SI | Male torso |
| Q66 | - |  |  | SI | The Irritable Bowel Syndrome Severity Score is a s... |
| Q67 | - |  |  | SI | The severity score was evaluated in adult patients... |
| Q68 | - |  |  | SI | References |
| Q69 | - |  |  | SI | 1. Francis CY, Morris J, Whorwell PJ. The irritabl... |
| Q70 | - |  |  | SI | 2. Tibble JA, Sigthorsson G, Foster R, Forgacs I, ... |
| Q71 | - |  |  | SI | Francis CY, Morris J, Whorwell PJ. The irritable b... |
| Q72 | - |  |  | SI | % |
| Q73 | - |  |  | SI | % |
| Q74 | - |  |  | SI | % |
| Q75 | - |  |  | SI | % |
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