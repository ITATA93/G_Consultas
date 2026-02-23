# SQLUser.ORC_ConsanguinityBetweenParents

**Schema:** SQLUser
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| COBEPA_RowId | bigint | PK |  | NO | - |
| COBEPA_Code | varchar |  |  | NO | Code |
| COBEPA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| COBEPA_CreatedDate | date |  |  | SI | Created Date |
| COBEPA_CreatedTime | time |  |  | SI | Created Time |
| COBEPA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| COBEPA_DateFrom | date |  |  | SI | Date From |
| COBEPA_DateTo | date |  |  | SI | Date To |
| COBEPA_Desc | varchar |  |  | NO | Description |
| COBEPA_Owner | varchar |  |  | SI | Owner |
| COBEPA_UpdatedDate | date |  |  | SI | Updated Date |
| COBEPA_UpdatedTime | time |  |  | SI | Updated Time |
| COBEPA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | 7. Do other things keep making you think about it? |
| Q11 | - |  |  | SI | 8. Do you try not to think about it? |
| Q12 | - |  |  | SI | If they did not occur during that time please sele... |
| Q13 | - |  |  | SI | Score |
| Q14 | - |  |  | SI | Classification |
| Q15 | - |  |  | SI | 0 - 40 |
| Q16 | - |  |  | SI | Higher scores indicate higher PTSD symptoms |
| Q17 | - |  |  | SI | 0 - 40: Higher scores indicate higher PTSD symptom... |
| Q18 | - |  |  | SI | The Children’s Impact of Event Scale, 8-item (CRIE... |
| Q19 | - |  |  | SI | Intrusion score |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Avoidance score |
| Q3 | - |  |  | SI | Below is a list of comments made by people after s... |
| Q4 | - |  |  | SI | 1. Do you think about it even when you dont mean t... |
| Q5 | - |  |  | SI | 2. Do you try to remove it from your memory? |
| Q6 | - |  |  | SI | 3. Do you have waves of strong feelings about it? |
| Q7 | - |  |  | SI | 4. Do you stay away from reminders of it (e.g. pla... |
| Q8 | - |  |  | SI | 5. Do you try not talk about it? |
| Q9 | - |  |  | SI | 6. Do pictures about it pop into your mind? |
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