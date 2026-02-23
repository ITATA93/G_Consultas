# questionnaire.QTCEH

> Epilepsy History

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Epilepsy History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | What happens during the seizure (seizure semiology... |
| Q02 | varchar |  |  | SI | (Aura) or warning or unusual feeling at the onset ... |
| Q03 | varchar |  |  | SI | Type of aura |
| Q04 | varchar |  |  | SI | Note |
| Q05 | varchar |  |  | SI | Motor Features |
| Q06 | varchar |  |  | SI | Type of movement |
| Q07 | varchar |  |  | SI | Note |
| Q08 | varchar |  |  | SI | Distribution of movement |
| Q09 | varchar |  |  | SI | Type |
| Q10 | varchar |  |  | SI | Distribution |
| Q11 | varchar |  |  | SI | Level of consciousness during the attack |
| Q12 | varchar |  |  | SI | Is the patient able to talk during attack? |
| Q13 | varchar |  |  | SI | Does the patient display any of the following duri... |
| Q14 | varchar |  |  | SI | Note |
| Q15 | numeric |  |  | SI | Duration of attacks (minutes) |
| Q16 | varchar |  |  | SI | Seizure frequency |
| Q17 | numeric |  |  | SI | How many times |
| Q18 | numeric |  |  | SI | Seizure clusters (per day) |
| Q19 | varchar |  |  | SI | Maximum seizure free period (specify if per days o... |
| Q20 | varchar |  |  | SI | Post ictal symptoms |
| Q21 | varchar |  |  | SI | Note |
| Q22 | varchar |  |  | SI | Event triggering factors |
| Q23 | varchar |  |  | SI | Note |
| Q24 | varchar |  |  | SI | History of previous hospitalization with seizure |
| Q25 | varchar |  |  | SI | History of sustained injuries due to seizure |
| Q26 | varchar |  |  | SI | Is there a diurnal variation of seizure |
| Q27 | varchar |  |  | SI | Previously epilepsy investigations |
| Q28 | date |  |  | SI | Date |
| Q29 | time |  |  | SI | Time |
| Q30 | varchar |  |  | SI | Sensory Features |
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