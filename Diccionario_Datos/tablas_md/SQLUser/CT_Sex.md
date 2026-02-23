# SQLUser.CT_Sex

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Catalogo de **Sexo/Genero**.
Valores: Masculino, Femenino, Indeterminado.
Usado en PA_PatMas.PAPMI_Sex_DR.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSEX_RowId | bigint | PK |  | NO | - |
| CTSEX_Code | varchar |  |  | NO | Sex Code |
| CTSEX_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTSEX_CodeTranslated | varchar |  |  | SI | - |
| CTSEX_CreatedDate | date |  |  | SI | Created Date |
| CTSEX_CreatedTime | time |  |  | SI | Created Time |
| CTSEX_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTSEX_DateFrom | date |  |  | SI | Date From |
| CTSEX_DateTo | date |  |  | SI | Date To |
| CTSEX_Desc | varchar |  |  | NO | Sex Description |
| CTSEX_DescTranslated | varchar |  |  | SI | - |
| CTSEX_Gender | varchar |  |  | SI | Gender |
| CTSEX_GrouperCode | varchar |  |  | SI | Grouper Code |
| CTSEX_HL7Code | varchar |  |  | SI | HL7 Code |
| CTSEX_IconName | varchar |  |  | SI | IconName |
| CTSEX_Owner | varchar |  |  | SI | Owner |
| CTSEX_UpdatedDate | date |  |  | SI | Updated Date |
| CTSEX_UpdatedTime | time |  |  | SI | Updated Time |
| CTSEX_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Please read each statement carefully and then choo... |
| Q04 | - |  |  | SI | 0 = Not at all |
| Q05 | - |  |  | SI | 1 |
| Q06 | - |  |  | SI | 2 = A little |
| Q07 | - |  |  | SI | 3 |
| Q08 | - |  |  | SI | 4 = A lot |
| Q09 | - |  |  | SI | 5 |
| Q10 | - |  |  | SI | 6 = Completely |
| Q11 | - |  |  | SI | 1. I stay in bed for too long even though I had th... |
| Q12 | - |  |  | SI | 2. There were certain things I needed to do that I... |
| Q13 | - |  |  | SI | 3. I am content with the amount and types of thing... |
| Q14 | - |  |  | SI | 4. I engaged in a wide and diverse array of activi... |
| Q15 | - |  |  | SI | 5. I made good decisions about what type of activi... |
| Q16 | - |  |  | SI | 6. I was active, but did not accomplish any of my ... |
| Q17 | - |  |  | SI | 7. I was an active person and accomplished the goa... |
| Q18 | - |  |  | SI | 8. Most of what I did was to escape from or avoid ... |
| Q19 | - |  |  | SI | 9. I did things to avoid feeling sadness or other ... |
| Q20 | - |  |  | SI | 10. I tried not to think about certain things |
| Q21 | - |  |  | SI | 11. I did things even though they were hard becaus... |
| Q22 | - |  |  | SI | 12. I did something that was hard to do but it was... |
| Q23 | - |  |  | SI | 13. I spent a long time thinking over and over abo... |
| Q24 | - |  |  | SI | 14. I kept trying to think of ways to solve a prob... |
| Q25 | - |  |  | SI | 15. I frequently spent time thinking about my past... |
| Q26 | - |  |  | SI | 16. I did not see any of my friends |
| Q27 | - |  |  | SI | 17. I was withdrawn and quiet, even around people ... |
| Q28 | - |  |  | SI | 18. I was not social, even though I had opportunit... |
| Q29 | - |  |  | SI | 19. I pushed people away with my negativity |
| Q30 | - |  |  | SI | 20. I did things to cut myself off from other peop... |
| Q31 | - |  |  | SI | 21. I took time off of work / school simply becaus... |
| Q32 | - |  |  | SI | 22. My work / schoolwork / chores / responsibiliti... |
| Q33 | - |  |  | SI | 23. I structured my day's activities |
| Q34 | - |  |  | SI | 24. I only engaged in activities that would distra... |
| Q35 | - |  |  | SI | 25. I began to feel badly when others around me ex... |
| Q36 | - |  |  | SI | Notes |
| Q37 | - |  |  | SI | Activation subscale |
| Q38 | - |  |  | SI | Avoidance / Rumination subscale |
| Q39 | - |  |  | SI | Work / School Impairment subscale |
| Q40 | - |  |  | SI | Social Impairment subscale |
| Q41 | - |  |  | SI | Total BADS score |
| Q42 | - |  |  | SI | Kanter JW, Mulick PS, Busch AM, Berlin KS, Martell... |
| Q43 | - |  |  | SI | The behavioral activation for depression scale (BA... |
| Q44 | - |  |  | SI | The BADS has also been administered to a clinicall... |
| Q45 | - |  |  | SI | Kanter JW, Rusch LC, Busch AM, & Sedivy SK (2009).... |
| Q46 | - |  |  | SI | Journal of Psychopathology and Behavioral Assessme... |
| Q47 | - |  |  | SI | The scale is designed to be administered weekly to... |
| Q48 | - |  |  | SI | For all subscales, high scores are consistent with... |
| Q49 | - |  |  | SI | For all subscales, high scores are consistent with... |
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