# SQLUser.PAC_FeedOnDischarge

**Schema:** SQLUser
**Columnas:** 103
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FEEDOD_RowId | bigint | PK |  | NO | - |
| FEEDOD_Code | varchar |  |  | NO | Code |
| FEEDOD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FEEDOD_CreatedDate | date |  |  | SI | Created Date |
| FEEDOD_CreatedTime | time |  |  | SI | Created Time |
| FEEDOD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FEEDOD_DateFrom | date |  |  | SI | Date From |
| FEEDOD_DateTo | date |  |  | SI | Date To |
| FEEDOD_Desc | varchar |  |  | NO | Description |
| FEEDOD_NationalCode | varchar |  |  | SI | NationalCode |
| FEEDOD_Owner | varchar |  |  | SI | Owner |
| FEEDOD_SubRegion_DR | bigint |  | FK | SI | Des Ref CTSubRegion |
| FEEDOD_UpdatedDate | date |  |  | SI | Updated Date |
| FEEDOD_UpdatedTime | time |  |  | SI | Updated Time |
| FEEDOD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | History of falling |
| Q02 | - |  |  | SI | Secondary diagnosis |
| Q03 | - |  |  | SI | Ambulatory aid |
| Q04 | - |  |  | SI | IV / Heparin lock |
| Q05 | - |  |  | SI | Gait / Transferring |
| Q06 | - |  |  | SI | Mental status |
| Q07 | - |  |  | SI | History of falling: |
| Q08 | - |  |  | SI | This is scored as 25 if the patient has fallen dur... |
| Q09 | - |  |  | SI | If the patient has not fallen, this is scored 0. |
| Q10 | - |  |  | SI | Note: If a patient falls for the first time, then ... |
| Q11 | - |  |  | SI | Secondary diagnosis: |
| Q12 | - |  |  | SI | This is scored as 15 if more than one medical diag... |
| Q13 | - |  |  | SI | Ambulatory aids: |
| Q14 | - |  |  | SI | This is scored as 0 if the patient walks without a... |
| Q15 | - |  |  | SI | If the patient uses crutches, a cane, or a walker,... |
| Q16 | - |  |  | SI | Intravenous therapy: |
| Q17 | - |  |  | SI | This is scored as 20 if the patient has an intrave... |
| Q18 | - |  |  | SI | Gait: |
| Q19 | - |  |  | SI | A normal gait is characterized by the patient walk... |
| Q20 | - |  |  | SI | This gait scores 0. |
| Q21 | - |  |  | SI | With a weak gait (score as 10), the patient is sto... |
| Q22 | - |  |  | SI | Steps are short and the patient may shuffle. With ... |
| Q23 | - |  |  | SI | (i.e., by using several attempts to rise). |
| Q24 | - |  |  | SI | The patient’s head is down, and he or she watches ... |
| Q25 | - |  |  | SI | Because the patient’s balance is poor, the patient... |
| Q26 | - |  |  | SI | Mental status: |
| Q27 | - |  |  | SI | When using this Scale, mental status is measured b... |
| Q28 | - |  |  | SI | Ask the patient, |
| Q29 | - |  |  | SI | “Are you able to go the bathroom alone or do you n... |
| Q30 | - |  |  | SI | If the patient’s reply judging his or her own abil... |
| Q31 | - |  |  | SI | the patient is rated as “normal” and scored 0. |
| Q32 | - |  |  | SI | If the patient’s response is not consistent with t... |
| Q33 | - |  |  | SI | then the patient is considered to overestimate his... |
| Q34 | - |  |  | SI | Score |
| Q35 | - |  |  | SI | Classification |
| Q36 | - |  |  | SI | 0 - 24 |
| Q37 | - |  |  | SI | Low risk |
| Q38 | - |  |  | SI | 25 - 50 |
| Q39 | - |  |  | SI | Moderate risk |
| Q40 | - |  |  | SI | ≥ 51 |
| Q41 | - |  |  | SI | High risk |
| Q42 | - |  |  | SI | Important Note: |
| Q43 | - |  |  | SI | The Morse Fall Scale should be calibrated for each... |
| Q44 | - |  |  | SI | In other words, risk cut off scores may be differe... |
| Q45 | - |  |  | SI | In addition, scales may be set differently between... |
| Q46 | - |  |  | SI | The Morse Fall Scale (MFS) is a rapid and simple m... |
| Q47 | - |  |  | SI | Date |
| Q48 | - |  |  | SI | Time |
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