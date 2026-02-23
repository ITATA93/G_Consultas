# SQLUser.CT_Dictionary

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DICT_RowId | bigint | PK |  | NO | - |
| DICT_Code | varchar |  |  | NO | Code |
| DICT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DICT_CreatedDate | date |  |  | SI | Created Date |
| DICT_CreatedTime | time |  |  | SI | Created Time |
| DICT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DICT_DateFrom | date |  |  | SI | DateFrom |
| DICT_DateTo | date |  |  | SI | DateTo |
| DICT_Desc | varchar |  |  | NO | Description |
| DICT_Owner | varchar |  |  | SI | Owner |
| DICT_UpdatedDate | date |  |  | SI | Updated Date |
| DICT_UpdatedTime | time |  |  | SI | Updated Time |
| DICT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of examination |
| Q02 | - |  |  | SI | Time of examination |
| Q03 | - |  |  | SI | Occupation |
| Q04 | - |  |  | SI | Handedness |
| Q05 | - |  |  | SI | Ask: What is the |
| Q06 | - |  |  | SI | Ask: Which |
| Q07 | - |  |  | SI | Tell: I'm going to give you three words and I'd li... |
| Q08 | - |  |  | SI | After the subject repeats, say: Try to remember th... |
| Q09 | - |  |  | SI | Score only the first trial (repeat 3 times if nece... |
| Q10 | - |  |  | SI | Number of trials |
| Q11 | - |  |  | SI | Ask the subject: Could you take 7 away from 100? I... |
| Q12 | - |  |  | SI | If subject makes a mistake, do not stop them. Let ... |
| Q13 | - |  |  | SI | Stop after five subtractions: (93,85,79,72,65) |
| Q14 | - |  |  | SI | Ask: Which 3 words did I ask you to repeat and rem... |
| Q15 | - |  |  | SI | Words remembered |
| Q16 | - |  |  | SI | Letters |
| Q17 | - |  |  | SI | Say: I'm going to give you a letter of the alphabe... |
| Q18 | - |  |  | SI | you could give me words like cat, cry, clock and s... |
| Q19 | - |  |  | SI | Words generated |
| Q20 | - |  |  | SI | Letters comment |
| Q21 | - |  |  | SI | Animals |
| Q22 | - |  |  | SI | Say: Now can you name as many animals as possible.... |
| Q23 | - |  |  | SI | Animals generated |
| Q24 | - |  |  | SI | Animals comment |
| Q25 | - |  |  | SI | Tell: I'm going to give you a name and address and... |
| Q26 | - |  |  | SI | Harry Barnes |
| Q27 | - |  |  | SI | 73 Orchard Close |
| Q28 | - |  |  | SI | Kingsbridge |
| Q29 | - |  |  | SI | Devon |
| Q30 | - |  |  | SI | (use country appropriate address) |
| Q31 | - |  |  | SI | Score only the third trial |
| Q32 | - |  |  | SI | Name of the |
| Q33 | - |  |  | SI | Place a pencil and a piece of paper in front of th... |
| Q34 | - |  |  | SI | Do not continue further |
| Q35 | - |  |  | SI | Trial is |
| Q36 | - |  |  | SI | Ask the subject to |
| Q37 | - |  |  | SI | Continue with the following three commands below: ... |
| Q38 | - |  |  | SI | Ask the subject to write two (or more) complete se... |
| Q39 | - |  |  | SI | Number of complete sentences |
| Q40 | - |  |  | SI | Sentences written by subject |
| Q41 | - |  |  | SI | Ask the subject to repeat: Catepillar, Eccentricit... |
| Q42 | - |  |  | SI | Ask the subject to repeat |
| Q43 | - |  |  | SI | Ask the subject to name the following pictures |
| Q44 | - |  |  | SI | Using the pictures above |
| Q45 | - |  |  | SI | Ask the subject to point to |
| Q46 | - |  |  | SI | Ask the subject to read the following words: Sew, ... |
| Q47 | - |  |  | SI | Infinity diagram |
| Q48 | - |  |  | SI | Ask the subject to copy the diagram |
| Q49 | - |  |  | SI | Copy output |
| Q50 | - |  |  | SI | Wire cube |
| Q51 | - |  |  | SI | Ask the subject to copy the drawing |
| Q52 | - |  |  | SI | Copy output |
| Q53 | - |  |  | SI | Clock |
| Q54 | - |  |  | SI | Ask the subject to draw a clock face with numbers ... |
| Q55 | - |  |  | SI | Drawing output |
| Q56 | - |  |  | SI | Ask the subject to count the dots without pointing... |
| Q57 | - |  |  | SI | Dots counted |
| Q58 | - |  |  | SI | Ask the subject to identify the letters |
| Q59 | - |  |  | SI | Letters identified |
| Q60 | - |  |  | SI | Ask: Now tell me what you remember about that last... |
| Q61 | - |  |  | SI | What he/she remember? |
| Q62 | - |  |  | SI | This test should be done if the subject failed to ... |
| Q63 | - |  |  | SI |  the right hand side |
| Q64 | - |  |  | SI | recalling |
| Q65 | - |  |  | SI | Recognized items |
| Q66 | - |  |  | SI | Dots |
| Q67 | - |  |  | SI | Letters |
| Q68 | - |  |  | SI | ACE III is a brief battery that provides evaluatio... |
| Q69 | - |  |  | SI | Total ACE III Score |
| Q70 | - |  |  | SI | >=88: Normal |
| Q71 | - |  |  | SI | 83 - 87: Inconclusive |
| Q72 | - |  |  | SI | <83: Abnormal |
| Q73 | - |  |  | SI | Attention Score (/18) |
| Q74 | - |  |  | SI | Memory Score (/26) |
| Q75 | - |  |  | SI | Fluency Score (/14) |
| Q76 | - |  |  | SI | Language Score (/26) |
| Q77 | - |  |  | SI | Visuospatial Score (/16) |
| Q78 | - |  |  | SI | Total ACE III Score (/100) |
| Q79 | - |  |  | SI | Language Score (/16) |
| Q80 | - |  |  | SI | Total ACEIII Score (/100) |
| Q81 | - |  |  | SI | Age at leaving full-time education |
| Q82 | - |  |  | SI | If incorrect, score 0 (do not check any boxes belo... |
| Q83 | - |  |  | SI | Continue with the following three commands below: ... |
| Q84 | - |  |  | SI | Give 1 point if there are two (or more) complete s... |
| Q85 | - |  |  | SI | What he/she remember? |
| Q86 | - |  |  | SI | ≥ 88 |
| Q87 | - |  |  | SI | Normal |
| Q88 | - |  |  | SI | 83 - 87 |
| Q89 | - |  |  | SI | Inconclusive |
| Q90 | - |  |  | SI | < 83 |
| Q91 | - |  |  | SI | Abnormal |
| Q92 | - |  |  | SI | Classification |
| Q93 | - |  |  | SI | Score |
| Q94 | - |  |  | SI | Recall status |
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