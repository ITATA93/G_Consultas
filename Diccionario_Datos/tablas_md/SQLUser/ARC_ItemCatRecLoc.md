# SQLUser.ARC_ItemCatRecLoc

**Schema:** SQLUser
**Columnas:** 122
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RL_ParRef | bigint | PK |  | NO | ARC_ItemCat Parent Reference |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | In general, would you say your health is |
| Q04 | - |  |  | SI | Compared to one year ago, how would you rate your ... |
| Q05 | - |  |  | SI | The following items are about activities you might... |
| Q06 | - |  |  | SI | Vigorous activities, such as running, lifting heav... |
| Q07 | - |  |  | SI | Moderate activities, such as moving a table, pushi... |
| Q08 | - |  |  | SI | Lifting or carrying groceries |
| Q09 | - |  |  | SI | Climbing several flights of stairs |
| Q10 | - |  |  | SI | Climbing one flight of stairs |
| Q11 | - |  |  | SI | Bending, kneeling, or stooping |
| Q12 | - |  |  | SI | Walking more than a mile |
| Q13 | - |  |  | SI | Walking several blocks |
| Q14 | - |  |  | SI | Walking one block |
| Q15 | - |  |  | SI | Bathing or dressing yourself |
| Q16 | - |  |  | SI | During the past 4 weeks, have you had any of the f... |
| Q17 | - |  |  | SI | Cut down the amount of time you spent on work or o... |
| Q18 | - |  |  | SI | Accomplished less than you would like |
| Q19 | - |  |  | SI | Were limited in the kind of work or other activiti... |
| Q20 | - |  |  | SI | Had difficulty performing the work or other activi... |
| Q21 | - |  |  | SI | During the past 4 weeks, have you had any of the f... |
| Q22 | - |  |  | SI | Cut down the amount of time you spent on work or o... |
| Q23 | - |  |  | SI | Accomplished less than you would like |
| Q24 | - |  |  | SI | Didn't do work or other activities as carefully as... |
| Q25 | - |  |  | SI | During the past 4 weeks, to what extent has your p... |
| Q26 | - |  |  | SI | How much bodily pain have you had during the past ... |
| Q27 | - |  |  | SI | During the past 4 weeks, how much did pain interfe... |
| Q28 | - |  |  | SI | These questions are about how you feel and how thi... |
| Q29 | - |  |  | SI | How much of the time during the past 4 weeks: |
| Q30 | - |  |  | SI | Did you feel full of pep? |
| Q31 | - |  |  | SI | Have you been a very nervous person? |
| Q32 | - |  |  | SI | Have you felt so down in the dumps that nothing co... |
| Q33 | - |  |  | SI | Have you felt calm and peaceful? |
| Q34 | - |  |  | SI | Did you have a lot of energy? |
| Q35 | - |  |  | SI | Have you felt downhearted and blue? |
| Q36 | - |  |  | SI | Did you feel worn out? |
| Q37 | - |  |  | SI | Have you been a happy person? |
| Q38 | - |  |  | SI | Did you feel tired? |
| Q39 | - |  |  | SI | During the past 4 weeks, how much of the time has ... |
| Q40 | - |  |  | SI | How TRUE or FALSE is each of the following stateme... |
| Q41 | - |  |  | SI | I seem to get sick a little easier than other peop... |
| Q42 | - |  |  | SI | I am as healthy as anybody I know |
| Q43 | - |  |  | SI | I expect my health to get worse |
| Q44 | - |  |  | SI | My health is excellent |
| Q45 | - |  |  | SI | Notes |
| Q46 | - |  |  | SI | Total score |
| Q47 | - |  |  | SI | Physical functioning |
| Q48 | - |  |  | SI | Role limitations due to physical health |
| Q49 | - |  |  | SI | Role limitations due to emotional problems |
| Q50 | - |  |  | SI | Energy / Fatigue |
| Q51 | - |  |  | SI | Emotional well-being |
| Q52 | - |  |  | SI | Social functioning |
| Q53 | - |  |  | SI | Pain |
| Q54 | - |  |  | SI | General health |
| Q55 | - |  |  | SI | Lower scores indicate more disability while higher... |
| Q56 | - |  |  | SI | Physical functioning, Bodily pain, Role limitation... |
| Q57 | - |  |  | SI | Emotional well-being, Social functioning, Energy F... |
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
| RL_CTHospitalDR | bigint |  | FK | SI | CT Hospital dr |
| RL_Childsub | double |  |  | NO | Childsub |
| RL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RL_CreatedDate | date |  |  | SI | Created Date |
| RL_CreatedTime | time |  |  | SI | Created Time |
| RL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RL_DateFrom | date |  |  | SI | Date From |
| RL_DateTo | date |  |  | SI | Date To |
| RL_DaysOfTheWeek | varchar |  |  | SI | DaysOfTheWeek |
| RL_DefaultFlag | varchar |  |  | SI | Default Flag |
| RL_DispenseType | varchar |  |  | SI | Dispense Type |
| RL_Function | varchar |  |  | NO | Function |
| RL_OrdLoc_DR | bigint |  | FK | SI | OrderLocation_DR |
| RL_OrderPriority_DR | bigint |  | FK | SI | Des Ref OrderPriority |
| RL_Owner | varchar |  |  | SI | Owner - DEPRECATED - Code Table Overrides |
| RL_PRNFlag | varchar |  |  | SI | PRN Flag |
| RL_RecLoc_DR | bigint |  | FK | SI | Receive Location DR |
| RL_Resource_DR | bigint |  | FK | SI | Resource |
| RL_RowId | varchar |  |  | NO | - |
| RL_TimeFrom | time |  |  | SI | Time From |
| RL_TimeTo | time |  |  | SI | TimeTo |
| RL_UpdatedDate | date |  |  | SI | Updated Date |
| RL_UpdatedTime | time |  |  | SI | Updated Time |
| RL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*