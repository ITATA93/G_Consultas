# SQLUser.ORC_Dressing

**Schema:** SQLUser
**Columnas:** 137
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRESSING_RowId | bigint | PK |  | NO | - |
| DRESSING_Code | varchar |  |  | NO | Code |
| DRESSING_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRESSING_CreatedDate | date |  |  | SI | Created Date |
| DRESSING_CreatedTime | time |  |  | SI | Created Time |
| DRESSING_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRESSING_DateFrom | date |  |  | SI | Date From |
| DRESSING_DateTo | date |  |  | SI | Date To |
| DRESSING_Desc | varchar |  |  | NO | Description |
| DRESSING_Owner | varchar |  |  | SI | Owner |
| DRESSING_UpdatedDate | date |  |  | SI | Updated Date |
| DRESSING_UpdatedTime | time |  |  | SI | Updated Time |
| DRESSING_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Open a tight or new jar |
| Q02 | - |  |  | SI | Write |
| Q03 | - |  |  | SI | Turn a key |
| Q04 | - |  |  | SI | Prepare a meal |
| Q05 | - |  |  | SI | Push open a heavy door |
| Q06 | - |  |  | SI | Place an object on a shelf above your head |
| Q07 | - |  |  | SI | Do heavy household chores (e.g., wash walls, wash ... |
| Q08 | - |  |  | SI | Garden or do yard work |
| Q09 | - |  |  | SI | Make a bed |
| Q10 | - |  |  | SI | Carry a shopping bag or briefcase |
| Q11 | - |  |  | SI | Carry a heavy object (over 10 lbs) |
| Q12 | - |  |  | SI | Change a lightbulb overhead |
| Q13 | - |  |  | SI | Wash or blow dry your hair |
| Q14 | - |  |  | SI | Wash your back |
| Q15 | - |  |  | SI | Put on a pullover sweater |
| Q16 | - |  |  | SI | Use a knife to cut food |
| Q17 | - |  |  | SI | Recreational activities which require little effor... |
| Q18 | - |  |  | SI | Recreational activities in which you take some for... |
| Q19 | - |  |  | SI | Recreational activities in which you move your arm... |
| Q20 | - |  |  | SI | Manage transportation needs (getting from one plac... |
| Q21 | - |  |  | SI | Sexual activities |
| Q22 | - |  |  | SI | During the past week, to what extent has your arm,... |
| Q23 | - |  |  | SI | During the past week, were you limited in your wor... |
| Q24 | - |  |  | SI | Arm, shoulder or hand pain |
| Q25 | - |  |  | SI | Arm, shoulder or hand pain when you performed any ... |
| Q26 | - |  |  | SI | Tingling (pins and needles) in your arm, shoulder ... |
| Q27 | - |  |  | SI | Weakness in your arm, shoulder or hand |
| Q28 | - |  |  | SI | Stiffness in your arm, shoulder or hand |
| Q29 | - |  |  | SI | During the past week, how much difficulty have you... |
| Q30 | - |  |  | SI | I feel less capable, less confident or less useful... |
| Q31 | - |  |  | SI | Describe your physical ability in the past week |
| Q32 | - |  |  | SI | Using your usual technique for your work? |
| Q33 | - |  |  | SI | Doing your usual work because of arm, shoulder or ... |
| Q34 | - |  |  | SI | Doing your work as well as you would like? |
| Q35 | - |  |  | SI | Spending your usual amount of time doing your work... |
| Q36 | - |  |  | SI | Describe your physical ability in the past week |
| Q37 | - |  |  | SI | Using your usual technique for playing your instru... |
| Q38 | - |  |  | SI | Playing your musical instrument or sport because o... |
| Q39 | - |  |  | SI | Playing your musical instrument or sport as well a... |
| Q40 | - |  |  | SI | Spending your usual amount of time practicing or p... |
| Q41 | - |  |  | SI | Please rate your ability to do the following activ... |
| Q42 | - |  |  | SI | A DASH score may not be calculated if there are gr... |
| Q43 | - |  |  | SI | Check the number that best describes your physical... |
| Q44 | - |  |  | SI | Do you work? |
| Q45 | - |  |  | SI | Please indicate what our job / work is |
| Q46 | - |  |  | SI | You may skip this section |
| Q47 | - |  |  | SI | Please indicate the sport / instrument which is mo... |
| Q48 | - |  |  | SI | You may skip this section |
| Q49 | - |  |  | SI | Do you play one sport or instrument (or both) |
| Q50 | - |  |  | SI | Please answer with respect to that activity which ... |
| Q51 | - |  |  | SI | (e.g., cardplaying, knitting, etc.) |
| Q52 | - |  |  | SI | or impact through your arm, shoulder or hand (e.g.... |
| Q53 | - |  |  | SI | freely (e.g., playing frisbee, badminton, etc.) |
| Q54 | - |  |  | SI | (getting from one place to another) |
| Q55 | - |  |  | SI | The DASH is a disability questionnaire, scaling is... |
| Q56 | - |  |  | SI | DASH Disability / Symptom Score |
| Q57 | - |  |  | SI | Work Module Score |
| Q58 | - |  |  | SI | Sport / Performing Art Module Score |
| Q59 | - |  |  | SI | 0 |
| Q60 | - |  |  | SI | 100 |
| Q61 | - |  |  | SI | No disability |
| Q62 | - |  |  | SI | Maximum disability |
| Q63 | - |  |  | SI | Score |
| Q64 | - |  |  | SI | Classification |
| Q65 | - |  |  | SI | 0: No disability |
| Q66 | - |  |  | SI | 100: Maximum disability |
| Q67 | - |  |  | SI | Work Module Score |
| Q68 | - |  |  | SI | Sport / Performing Art Module Score |
| Q69 | - |  |  | SI | DASH Disability / Symptom Score |
| Q70 | - |  |  | SI | Work Module Score |
| Q71 | - |  |  | SI | Sport / Performing Art Module Score |
| Q72 | - |  |  | SI | DASH Disability / Symptom Score |
| Q73 | - |  |  | SI | DASH Disability / Symptom Score - Display only |
| Q74 | - |  |  | SI | Work Module Score - Display only |
| Q75 | - |  |  | SI | Sport / Performing Art Module Score - Display only |
| Q76 | - |  |  | SI | Date |
| Q77 | - |  |  | SI | Time |
| Q78 | - |  |  | SI | DASH Disability / Symptom Score Caption |
| Q79 | - |  |  | SI | Work Module Score Caption |
| Q80 | - |  |  | SI | Sport / Performing Art Module Score Caption |
| Q81 | - |  |  | SI | Work Module Score |
| Q82 | - |  |  | SI | Sport / Performing Art Module Score |
| Q83 | - |  |  | SI | DASH Disability / Symptom Score |
| Q84 | - |  |  | SI | Please always click Apply then Update to get the s... |
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