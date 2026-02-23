# SQLUser.PAC_DeliveryPlace

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DELPL_RowId | bigint | PK |  | NO | - |
| DELPL_AbortionEdit | varchar |  |  | SI | Abortion Edit  |
| DELPL_Code | varchar |  |  | NO | Code |
| DELPL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DELPL_CreatedDate | date |  |  | SI | Created Date |
| DELPL_CreatedTime | time |  |  | SI | Created Time |
| DELPL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DELPL_DateFrom | date |  |  | SI | DateFrom |
| DELPL_DateTo | date |  |  | SI | DateTo |
| DELPL_Desc | varchar |  |  | NO | Description |
| DELPL_EpisodeType | varchar |  |  | SI | EpisodeType |
| DELPL_NationalCode | varchar |  |  | SI | NationalCode |
| DELPL_Owner | varchar |  |  | SI | Owner |
| DELPL_PregnDelivEdit | varchar |  |  | SI | Pregnancy Delivery Edit |
| DELPL_UpdatedDate | date |  |  | SI | Updated Date |
| DELPL_UpdatedTime | time |  |  | SI | Updated Time |
| DELPL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Thinking about the last 2 weeks tick your response... |
| Q04 | - |  |  | SI | 1- My back pain has spread down my leg(s) at some ... |
| Q05 | - |  |  | SI | 2- I have had pain in the shoulder or neck at some... |
| Q06 | - |  |  | SI | 3- I have only walked short distances because of m... |
| Q07 | - |  |  | SI | 4- In the last 2 weeks, I have dressed more slowly... |
| Q08 | - |  |  | SI | 5- It's not really safe for a person with a condit... |
| Q09 | - |  |  | SI | 6- Worrying thoughts have been going through my mi... |
| Q10 | - |  |  | SI | 7- I feel that my back pain is terrible and it's n... |
| Q11 | - |  |  | SI | 8- In general I have not enjoyed all the things I ... |
| Q12 | - |  |  | SI | 9- Overall, how bothersome has your back pain been... |
| Q13 | - |  |  | SI | Sub score (Q5-9) |
| Q14 | - |  |  | SI | Total score |
| Q15 | - |  |  | SI | Classification |
| Q16 | - |  |  | SI | ≤ 3 |
| Q17 | - |  |  | SI | Low risk |
| Q18 | - |  |  | SI | ≥ 4 |
| Q19 | - |  |  | SI | ≤ 3 |
| Q20 | - |  |  | SI | Medium risk |
| Q21 | - |  |  | SI | ≥ 4 |
| Q22 | - |  |  | SI | ≥ 4 |
| Q23 | - |  |  | SI | High risk |
| Q24 | - |  |  | SI | Sub score (Q5-9) |
| Q25 | - |  |  | SI | The Keele STarT Back Screening Tool (9-item versio... |
| Q26 | - |  |  | SI | Total Score ≤ 3: Low risk |
| Q27 | - |  |  | SI | Total score ≥ 4 and Sub score (Q5-9) ≤ 3: Medium r... |
| Q28 | - |  |  | SI | Total score ≥ 4 and Sub score (Q5-9) ≥ 4: High ris... |
| Q29 | - |  |  | SI | Total score |
| Q30 | - |  |  | SI | designed to screen primary care patients with low ... |
| Q31 | - |  |  | SI | Sub score (Q5-9) calculated |
| Q32 | - |  |  | SI | Sub score (Q5-9) |
| Q33 | - |  |  | SI | Total score |
| Q34 | - |  |  | SI | Total score |
| Q35 | - |  |  | SI | Total score |
| Q36 | - |  |  | SI | Sub score (Q5-9) |
| Q37 | - |  |  | SI | Sub score (Q5-9) |
| Q38 | - |  |  | SI | Classification |
| Q39 | - |  |  | SI | Classification |
| Q40 | - |  |  | SI | Classification |
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