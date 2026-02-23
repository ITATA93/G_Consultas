# SQLUser.CT_Education

**Schema:** SQLUser
**Columnas:** 120
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EDU_RowId | bigint | PK |  | NO | - |
| EDU_Code | varchar |  |  | NO | Code |
| EDU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EDU_CreatedDate | date |  |  | SI | Created Date |
| EDU_CreatedTime | time |  |  | SI | Created Time |
| EDU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EDU_DateFrom | date |  |  | SI | Date From |
| EDU_DateTo | date |  |  | SI | Date To |
| EDU_Desc | varchar |  |  | NO | Description |
| EDU_Owner | varchar |  |  | SI | Owner |
| EDU_UpdatedDate | date |  |  | SI | Updated Date |
| EDU_UpdatedTime | time |  |  | SI | Updated Time |
| EDU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Personal questions concerning alcohol consumption |
| Q02 | - |  |  | SI | Answer these questions to find out how much alcoho... |
| Q03 | - |  |  | SI | Mark the response which is closest to your own sit... |
| Q04 | - |  |  | SI | How often do you have a drink containing alcohol? |
| Q05 | - |  |  | SI | How many drinks do you have on a typical day when ... |
| Q06 | - |  |  | SI | How often do you have six or more drinks on one oc... |
| Q07 | - |  |  | SI | During the last year how often have you found that... |
| Q08 | - |  |  | SI | During the last year how often have you failed to ... |
| Q09 | - |  |  | SI | During the last year how often have you needed a f... |
| Q10 | - |  |  | SI | During the last year how often have you been unabl... |
| Q11 | - |  |  | SI | Have you or has someone else been injured as a res... |
| Q12 | - |  |  | SI | Has a relative, a friend, a doctor or other health... |
| Q13 | - |  |  | SI | 0 -  7: Low |
| Q14 | - |  |  | SI | 8 - 10: Slightly increased |
| Q15 | - |  |  | SI | 11 - 14: Noticeably increased |
| Q16 | - |  |  | SI | 15 - 19: High |
| Q17 | - |  |  | SI | 20 - 40: Very high |
| Q18 | - |  |  | SI | Is it time to make a change? If your risks are ele... |
| Q19 | - |  |  | SI | Take a moment to think about how you could change ... |
| Q20 | - |  |  | SI | Are you alarmed by your test results? Remember tha... |
| Q21 | - |  |  | SI | If you decide to moderate your drinking or quit al... |
| Q22 | - |  |  | SI | Consult an expert – you have a right to know! Espe... |
| Q23 | - |  |  | SI | Find out how alcohol is affecting you and your hea... |
| Q24 | - |  |  | SI | One bottle |
| Q25 | - |  |  | SI | One standard drink: |
| Q26 | - |  |  | SI | (33 cl) of medium beer or cider (max 4.7% vol.) |
| Q27 | - |  |  | SI | One glass |
| Q28 | - |  |  | SI | (12 cl) of table wine (12% vol.) |
| Q29 | - |  |  | SI | One small glass |
| Q30 | - |  |  | SI | (8 cl) of fortified wine (16-22% vol.) |
| Q31 | - |  |  | SI | One restaurant measure |
| Q32 | - |  |  | SI | (4 cl) of spirits (35-40% vol.) |
| Q33 | - |  |  | SI | Examples |
| Q34 | - |  |  | SI | 0.5 l of medium beer cider equals: 1.5	units (max ... |
| Q35 | - |  |  | SI | 0.5 l of strong beer or cider equals: 2 units (5-8... |
| Q36 | - |  |  | SI | 0.75 l bottle of table wine equals: 6 units (12% v... |
| Q37 | - |  |  | SI | 0.5 l bottle of spirits equals: 13 units (35-40% v... |
| Q38 | - |  |  | SI | How much? |
| Q39 | - |  |  | SI | Did you overdo it? |
| Q40 | - |  |  | SI | Work left undone? |
| Q41 | - |  |  | SI | Do you have to jump-start your day? |
| Q42 | - |  |  | SI | Did you feel bad in the morning? |
| Q43 | - |  |  | SI | Blackout? |
| Q44 | - |  |  | SI | Did you hurt yourself or others? |
| Q45 | - |  |  | SI | Has anyone said anything about your drinking? |
| Q46 | - |  |  | SI | Date |
| Q47 | - |  |  | SI | During the last year how often have you had a feel... |
| Q48 | - |  |  | SI | Score |
| Q49 | - |  |  | SI | Is the attendance/admission directly due to alcoho... |
| Q50 | - |  |  | SI | Does patient give consent to answer the assessment... |
| Q51 | - |  |  | SI | Brief advice given, and patient informed of follow... |
| Q52 | - |  |  | SI | Has the patient refused further follow-up from Alc... |
| Q53 | - |  |  | SI | 0 - 7 |
| Q54 | - |  |  | SI | Low |
| Q55 | - |  |  | SI | 8 - 10 |
| Q56 | - |  |  | SI | Slightly increased |
| Q57 | - |  |  | SI | 11 - 14 |
| Q58 | - |  |  | SI | Noticeably increased |
| Q59 | - |  |  | SI | 15 - 19 |
| Q60 | - |  |  | SI | High |
| Q61 | - |  |  | SI | 20 - 40 |
| Q62 | - |  |  | SI | Very high |
| Q63 | - |  |  | SI | Score |
| Q64 | - |  |  | SI | Classification |
| Q65 | - |  |  | SI | Time |
| Q66 | - |  |  | SI | Table with Standards drinks |
| Q67 | - |  |  | SI | Time to make a change |
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