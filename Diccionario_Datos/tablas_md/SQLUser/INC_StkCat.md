# SQLUser.INC_StkCat

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCSC_RowId | bigint | PK |  | NO | - |
| INCSC_Code | varchar |  |  | NO | Stock Category Code |
| INCSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCSC_CreatedDate | date |  |  | SI | Created Date |
| INCSC_CreatedTime | time |  |  | SI | Created Time |
| INCSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCSC_Desc | varchar |  |  | NO | Description |
| INCSC_NonReturnable | varchar |  |  | SI | Non Returnable |
| INCSC_Owner | varchar |  |  | SI | Owner |
| INCSC_UpdatedDate | date |  |  | SI | Updated Date |
| INCSC_UpdatedTime | time |  |  | SI | Updated Time |
| INCSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | 1. Select the category that best describes you |
| Q04 | - |  |  | SI | 2. Have you lost some of the symptoms that used to... |
| Q05 | - |  |  | SI | 3. In the past six months how often have you had m... |
| Q06 | - |  |  | SI | (Episodes where you might feel confused, disorient... |
| Q07 | - |  |  | SI | 4. In the past how often have you had severe hypog... |
| Q08 | - |  |  | SI | (Episodes where you were unconscious or had a seiz... |
| Q09 | - |  |  | SI | 5. How often in the last month have you had readin... |
| Q10 | - |  |  | SI | 6. How often in the last month have you had readin... |
| Q11 | - |  |  | SI | Compare patient responses to questions 5 and 6 |
| Q12 | - |  |  | SI | 7. How low does your blood sugar go before you fee... |
| Q13 | - |  |  | SI | 8. To what extent can you tell by your symptoms th... |
| Q14 | - |  |  | SI | The survey assesses hypoglycaemia awareness and is... |
| Q15 | - |  |  | SI | • For people who have been on insulin for many yea... |
| Q16 | - |  |  | SI | • After a severe hypoglycaemic event |
| Q17 | - |  |  | SI | • After a crash |
| Q18 | - |  |  | SI | • A = Awareness |
| Q19 | - |  |  | SI | • R = Reduced awareness |
| Q20 | - |  |  | SI | • U = Unaware |
| Q21 | - |  |  | SI | • Four or more 'R' responses implies reduced hypog... |
| Q22 | - |  |  | SI | • 'U' response (12 or more severe hypoglycaemic ep... |
| Q23 | - |  |  | SI | • For question 5 and 6, one 'R' response is given ... |
| Q24 | - |  |  | SI | Score |
| Q25 | - |  |  | SI | Classification |
| Q26 | - |  |  | SI | 0 - 3 |
| Q27 | - |  |  | SI | Aware |
| Q28 | - |  |  | SI | 4 - 7 |
| Q29 | - |  |  | SI | Reduced awareness |
| Q30 | - |  |  | SI | >= 20 |
| Q31 | - |  |  | SI | Unaware |
| Q32 | - |  |  | SI | The Clarke Hypoglycaemia Awareness Survey comprise... |
| Q33 | - |  |  | SI | It also examines the glycaemic threshold for, and ... |
| Q34 | - |  |  | SI | Scoring |
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