# questionnaire.QTCNSHAMD

> Hamilton Depression Rating Scale (HAM-D)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Hamilton Depression Rating Scale (HAM-D)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Depressed mood |
| Q02 | varchar |  |  | SI | Feelings of guilt |
| Q03 | varchar |  |  | SI | Suicide |
| Q04 | varchar |  |  | SI | Insomnia - Initial |
| Q05 | varchar |  |  | SI | Insomnia - Middle |
| Q06 | varchar |  |  | SI | Insomnia - Delayed |
| Q07 | varchar |  |  | SI | Work and interests |
| Q08 | varchar |  |  | SI | Retardation |
| Q09 | varchar |  |  | SI | Agitation |
| Q10 | varchar |  |  | SI | Anxiety - Psychic |
| Q11 | varchar |  |  | SI | Anxiety-Somatic |
| Q12 | varchar |  |  | SI | Somatic symptoms - Gastrointestinal |
| Q13 | varchar |  |  | SI | Somatic symptoms - General |
| Q14 | varchar |  |  | SI | Genital symptoms |
| Q15 | varchar |  |  | SI | Hypochondriasis |
| Q16 | varchar |  |  | SI | Weight loss |
| Q17 | varchar |  |  | SI | Insight |
| Q18 | varchar |  |  | SI | Score 0 - 7: Normal |
| Q19 | varchar |  |  | SI | Score 8 - 13: Mild Depression |
| Q20 | varchar |  |  | SI | Score 14 - 18: Moderate Depression |
| Q21 | varchar |  |  | SI | Score 19 - 22: Severe Depression |
| Q22 | varchar |  |  | SI | Score > 23: Very Severe Depression |
| Q23 | varchar |  |  | SI | The Hamilton Depression Rating Scale (HAM-D) is us... |
| Q24 | varchar |  |  | SI | The standard version of the HAM-D is designed to b... |
| Q25 | varchar |  |  | SI | The scale contains 17 items rated on either a 3- o... |
| Q26 | date |  |  | SI | Date |
| Q27 | time |  |  | SI | Time |
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