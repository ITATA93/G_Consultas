# questionnaire.QTCMFS

> Morse Fall Scale

**Schema:** questionnaire
**Columnas:** 89
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Morse Fall Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | History of falling; immediate or within 3 months |
| Q02 | varchar |  |  | SI | Secondary diagnosis |
| Q03 | varchar |  |  | SI | Ambulatory aid |
| Q04 | varchar |  |  | SI | IV / Heparin lock |
| Q05 | varchar |  |  | SI | Gait / Transferring |
| Q06 | varchar |  |  | SI | Mental status |
| Q07 | varchar |  |  | SI | History of falling: |
| Q08 | varchar |  |  | SI | This is scored as 25 if the patient has fallen dur... |
| Q09 | varchar |  |  | SI | If the patient has not fallen, this is scored 0. |
| Q10 | varchar |  |  | SI | Note: If a patient falls for the first time, then ... |
| Q11 | varchar |  |  | SI | Secondary diagnosis: |
| Q12 | varchar |  |  | SI | This is scored as 15 if more than one medical diag... |
| Q13 | varchar |  |  | SI | Ambulatory aids: |
| Q14 | varchar |  |  | SI | This is scored as 0 if the patient walks without a... |
| Q15 | varchar |  |  | SI | If the patient uses crutches, a cane, or a walker,... |
| Q16 | varchar |  |  | SI | Intravenous therapy: |
| Q17 | varchar |  |  | SI | This is scored as 20 if the patient has an intrave... |
| Q18 | varchar |  |  | SI | Gait: |
| Q19 | varchar |  |  | SI | A normal gait is characterized by the patient walk... |
| Q20 | varchar |  |  | SI | This gait scores 0. |
| Q21 | varchar |  |  | SI | With a weak gait (score as 10), the patient is sto... |
| Q22 | varchar |  |  | SI | Steps are short and the patient may shuffle. With ... |
| Q23 | varchar |  |  | SI | (i.e., by using several attempts to rise). |
| Q24 | varchar |  |  | SI | The patient’s head is down, and he or she watches ... |
| Q25 | varchar |  |  | SI | Because the patient’s balance is poor, the patient... |
| Q26 | varchar |  |  | SI | Mental status: |
| Q27 | varchar |  |  | SI | When using this Scale, mental status is measured b... |
| Q28 | varchar |  |  | SI | Ask the patient, |
| Q29 | varchar |  |  | SI | “Are you able to go the bathroom alone or do you n... |
| Q30 | varchar |  |  | SI | If the patient’s reply judging his or her own abil... |
| Q31 | varchar |  |  | SI | the patient is rated as “normal” and scored 0. |
| Q32 | varchar |  |  | SI | If the patient’s response is not consistent with t... |
| Q33 | varchar |  |  | SI | then the patient is considered to overestimate his... |
| Q34 | varchar |  |  | SI | Score |
| Q35 | varchar |  |  | SI | Classification |
| Q36 | varchar |  |  | SI | 0 - 24 |
| Q37 | varchar |  |  | SI | Low risk |
| Q38 | varchar |  |  | SI | 25 - 50 |
| Q39 | varchar |  |  | SI | Moderate risk |
| Q40 | varchar |  |  | SI | ≥ 51 |
| Q41 | varchar |  |  | SI | High risk |
| Q42 | varchar |  |  | SI | Important Note: |
| Q43 | varchar |  |  | SI | The Morse Fall Scale should be calibrated for each... |
| Q44 | varchar |  |  | SI | In other words, risk cut off scores may be differe... |
| Q45 | varchar |  |  | SI | In addition, scales may be set differently between... |
| Q46 | varchar |  |  | SI | The Morse Fall Scale (MFS) is a rapid and simple m... |
| Q47 | date |  |  | SI | Date |
| Q48 | time |  |  | SI | Time |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*