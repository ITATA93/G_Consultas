# SQLUser.PAC_MalignancyGrade

**Schema:** SQLUser
**Columnas:** 98
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MALG_RowId | bigint | PK |  | NO | - |
| MALG_Code | varchar |  |  | NO | Code |
| MALG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MALG_CreatedDate | date |  |  | SI | Created Date |
| MALG_CreatedTime | time |  |  | SI | Created Time |
| MALG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MALG_Desc | varchar |  |  | NO | Description |
| MALG_Owner | varchar |  |  | SI | Owner |
| MALG_UpdatedDate | date |  |  | SI | Updated Date |
| MALG_UpdatedTime | time |  |  | SI | Updated Time |
| MALG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date and time of assessment |
| Q02 | - |  |  | SI | Predictor variable |
| Q03 | - |  |  | SI | Level of engagement 4 (score of 5 or less = low le... |
| Q04 | - |  |  | SI | Interventions involve engaging the person daily in... |
| Q05 | - |  |  | SI | A one-to-one session focused on addressing the spe... |
| Q06 | - |  |  | SI | crisis. |
| Q07 | - |  |  | SI | A family meeting involving appropriate family memb... |
| Q08 | - |  |  | SI | needs to be done (or to happen) to reduce or resol... |
| Q09 | - |  |  | SI | A group session, involving other people in care. T... |
| Q10 | - |  |  | SI | an information focus, providing details about medi... |
| Q11 | - |  |  | SI | Level of engagement 3 (score between 6 and 8 = int... |
| Q12 | - |  |  | SI | Interventions involve providing intermittent level... |
| Q13 | - |  |  | SI | The nurse will talk with the person and discuss wh... |
| Q14 | - |  |  | SI | The nurse should advise the person that someone wi... |
| Q15 | - |  |  | SI | The nurse personally should make direct contact wi... |
| Q16 | - |  |  | SI | The person should be asked if they have any commen... |
| Q17 | - |  |  | SI | Level of engagement 2 (score between 9 and 11 = hi... |
| Q18 | - |  |  | SI | Interventions involve providing regular level of s... |
| Q19 | - |  |  | SI | A healthcare team member will make contact with th... |
| Q20 | - |  |  | SI | assess their situation. |
| Q21 | - |  |  | SI | The nurse will assess for distress and will ask th... |
| Q22 | - |  |  | SI | The nurse should advise the person why the healthc... |
| Q23 | - |  |  | SI | Level of engagement 1 (score 12 or more = very hig... |
| Q24 | - |  |  | SI | Interventions involve providing fullest level of s... |
| Q25 | - |  |  | SI | The person will require continuous access to a nur... |
| Q26 | - |  |  | SI | The nurse should advise the person of the nursing ... |
| Q27 | - |  |  | SI | The nurse should discuss the plan of care for the ... |
| Q28 | - |  |  | SI | Attempts should be made to explain to the person w... |
| Q29 | - |  |  | SI | person's needs. |
| Q30 | - |  |  | SI | Score |
| Q31 | - |  |  | SI | Classification |
| Q32 | - |  |  | SI | <= 5 |
| Q33 | - |  |  | SI | Low level of risk estimated |
| Q34 | - |  |  | SI | 6 - 8 |
| Q35 | - |  |  | SI | Intermediate level of risk |
| Q36 | - |  |  | SI | 9 - 11 |
| Q37 | - |  |  | SI | High level of risk |
| Q38 | - |  |  | SI | >=12 |
| Q39 | - |  |  | SI | Very high level of risk |
| Q40 | - |  |  | SI | <= 5: Low level of risk estimated |
| Q41 | - |  |  | SI | 6 - 8: Intermediate level of risk |
| Q42 | - |  |  | SI | 9 - 11: High level of risk |
| Q43 | - |  |  | SI | >=12: Very high level of risk |
| Q44 | - |  |  | SI | Nurses' Global Assessment of Suicide Risk (NGASR) |
| Q45 | - |  |  | SI | The Nurses' Global Assessment of Suicide Risk (NGA... |
| Q46 | - |  |  | SI | more confident in accurately assessing a patient's... |
| Q47 | - |  |  | SI | Time |
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